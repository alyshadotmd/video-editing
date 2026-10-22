"""Cut check: run on EVERY version of a cut before the editor sees it. Prints PASS/FAIL.
Needs python3, numpy and ffmpeg.

usage: python3 cut_check.py --voice VOICE.wav --clips clips.json --out CUT.mp4 [--camlock camlock.wav]

clips.json: [[start,end],...] in VOICE timeline seconds (the audio actually used).
--camlock: the camera's own audio, cut with the exact same trims as the picture INSIDE THE SAME concat
           as the picture (concat=n:v=1:a=2). Needed whenever sound and picture come from different files.

Checks:
 1. Edges: the 50ms just inside each clip END is below speech level (-30 dB) -> no word cut off.
    Clip STARTS are checked over the 30ms before the start (the word onset itself is fine).
 2. Sync: delivered audio vs camlock, every 3s window within +-40ms.
 3. Gaps: no silence of 0.25s+ inside the cut (only the final hold).
"""
import argparse,json,subprocess,numpy as np,wave,tempfile,os
ap=argparse.ArgumentParser();ap.add_argument('--voice');ap.add_argument('--clips');ap.add_argument('--out');ap.add_argument('--camlock')
A=ap.parse_args(); S=json.load(open(A.clips)); fail=0
def pcm(f,ss=None,t=None,sr=16000):
  cmd=['ffmpeg','-v','error']+(['-ss',str(ss)] if ss is not None else [])+(['-t',str(t)] if t else [])+['-i',f,'-ac','1','-ar',str(sr),'-f','s16le','-']
  return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,dtype=np.int16).astype(float)
def db(x): return 20*np.log10(np.sqrt((x**2).mean())/32768+1e-9) if len(x) else -99
print('1. EDGES')
for i,(a,b) in enumerate(S):
  pre=db(pcm(A.voice,max(0,a-0.03),0.03)); end=db(pcm(A.voice,b-0.05,0.05)); f=[]
  if i>0 and pre>-30: f.append('START cuts into a word')
  if end>-30: f.append('END cuts off a word')
  fail+=len(f); print(f'  clip {i+1} {a:.2f}-{b:.2f}: before start {pre:.0f} dB, last 50ms {end:.0f} dB', '  <-- '+', '.join(f) if f else '')
if A.camlock:
  print('2. SYNC')
  def env(x): x=np.abs(x); return np.convolve(x,np.ones(40)/40,'same')[::8]
  c,o=env(pcm(A.camlock,sr=8000)),env(pcm(A.out,sr=8000)); n=min(len(c),len(o)); c,o=c[:n]-c[:n].mean(),o[:n]-o[:n].mean(); w=3000; worst=0
  for s in range(0,n-w,w):
    r=np.correlate(np.pad(o[s:s+w],2000),c[s:s+w],'valid'); L=int(np.argmax(r))-2000; worst=max(worst,abs(L))
    if abs(L)>40: fail+=1; print(f'  {s/1000:.1f}s: audio {L:+d} ms off picture  <--')
  print(f'  worst {worst} ms')
print('3. GAPS')
r=subprocess.run(['ffmpeg','-nostats','-i',A.out,'-af','silencedetect=n=-30dB:d=0.25','-f','null','-'],capture_output=True,text=True).stderr
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',A.out],capture_output=True,text=True).stdout)
for l in r.splitlines():
  if 'silence_start' in l:
    t=float(l.split('silence_start:')[1])
    if t<dur-0.8: fail+=1; print(f'  gap at {t:.2f}s  <--')
print('RESULT', 'PASS' if not fail else f'FAIL ({fail})')
