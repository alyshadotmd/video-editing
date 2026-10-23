---
name: aroll-processing
description: |
  Turn raw talking-head footage full of repeated takes (one long recording, or several recordings of the same script) into a tight rough cut. Find every take of every line, judge each take on its words, sound and picture, pick the keeper for each line, and either show the editor the picks first or go straight to the cut. The cut is checked so no word is chopped and no pause is left in before anyone sees it. Built for Claude Code and Runneth. Use when someone uploads raw talking-head footage and asks to find the takes, pick the best ones, make a cut list or rough cut it.
  Triggers: "process my a-roll", "find my takes", "pick the best takes", "rough cut this", "cut list", "edit my talking head", "which take is best"
---

# A-roll processing

The goal: one long recording, or several recordings of the same script, goes in, and a tight rough cut comes out, built from the best take of every line. Speech runs straight into speech, every word is whole, and the cut sounds like one clean take, on the first try.

This skill is built for **Claude Code** and **Runneth**. It needs:

- **ffmpeg** to measure the audio, grab still frames and cut the video.
- **Word timings for everything said:** a speech-to-text tool that gives the time of each word (Whisper, faster-whisper, whisper.cpp).
- **A way to judge the picture:** see "How to judge a take" below.
- **The check script** in `scripts/cut_check.py` (python3 with numpy and ffmpeg).

Talk to the editor in plain everyday words, one idea at a time.

## Before you start: the tools

In Runneth, everything is already installed: skip this section.

In Claude Code, this skill needs the free video tools the **video-editing-setup** skill installs. Check quietly that `~/.video-editing-tools/bin/ffmpeg -version` runs. If it does, use the tools in `~/.video-editing-tools/bin` (`ffmpeg`, `ffprobe`, `python`) wherever this skill says `ffmpeg`, `ffprobe` or `python3`, and carry on. If it doesn't, follow the video-editing-setup skill first, then come back here.

## Step 0: Two quick checks before any work

1. **The file is the one the editor meant.** If they said it's a refilm or a new clip and it's the same length or setting as an earlier one, ask in one line before starting.
2. **Ask exactly this, as one question with two options:**

   > "Do you want me to show you the takes I'd keep first, or just go ahead and do the edit?"

   - **Show me first** → follow every step below, and stop at Step 4 for the editor's OK.
   - **Just do the edit** → run every step start to finish without stopping. Mention anything you weren't sure about once, at the end.

   Skip the question if the editor already said which one ("just cut it", "show me the takes first"). If no one is there to answer, treat it as "just do the edit".

## Step 1: Get the words

1. Check each recording's length, orientation and frame rate (`ffprobe`). When there are several recordings, give each a plain label (Video A, Video B, Video C) and run every step below on all of them.
2. Pull the audio out of each recording: `ffmpeg -i IN.mov -vn -ac 1 -ar 16000 audio.wav`.
3. Mark every stretch of speech: `ffmpeg -i audio.wav -af silencedetect=n=-35dB:d=0.3 -f null -`. The stretches between silences are the speech islands. Every word lives inside one, and they're more exact than any transcript time.
4. Transcribe with word timings. With faster-whisper: model `base`, `word_timestamps=True`, `condition_on_previous_text=False`, and an `initial_prompt` listing names and brand words likely in the video. Bigger English-only models quietly clean up restarts, which hides the false starts this skill needs to see.
5. Transcripts drift or skip in long stretches. Every speech island needs words. When one has none, or words seem missing between silences, transcribe just that stretch again: start the window about 1 second before the island, end it about 1 second after, and turn off any speech filter (`vad_filter=False`).
6. Short re-transcribed windows can invent words at the end that weren't said ("Thank you very much", "Thanks for watching"). Keep only words that fall inside the island and fit the line; words stacked at the same timestamp are invented.
7. Fix clear mishears of names and brand words. If there's a script, use it as the map of lines; if not, the transcript is the map.

## Step 2: Group the takes

1. Split the footage into lines (one sentence or idea each) and group every attempt at the same line, across every recording. Several recordings of one script are one pool of takes: line 1 gets every take of line 1 from Video A, B and C side by side, and each take is labeled with its recording ("Video B, take 3"). Attempts usually start with the same few words.
2. A take runs from the start of one attempt to the end of its last word, before the next attempt starts.
3. Mark each take as **complete** (says the whole line) or a **false start** (stops partway).
4. Every phrase inside a line counts as its own piece. A line can be built from the best pieces of different takes (the first sentence from take 4, the second from take 2), including clean pieces of false starts.

## Step 3: Judge every take

Every take of every line gets judged, including lines said only once. The best version of each phrase wins, whatever take or order it came in. Build each line from those best pieces when the joint between them is clean (see rule 7 below). Use "What makes a take the keeper" below, and write one row per take in the takes file (template: `templates/takes.md`): line, take, time, what you saw, keep or not, and a short reason.

### How to judge a take

What to judge stays the same in both. How to see it depends on the tool:

- **In Runneth** (or any setup that can send video to a model that watches it, like Gemini), have that model watch every recording and judge every repeated line on "What makes a take the keeper", plus tone, emphasis, joke timing and hesitations. Keep your own picks out of what you send it, so the two reads stay independent. Where it picks a different take than you, its pick goes in. Always take the times from the transcript and speech islands, never from the video model: its timestamps drift and it sometimes skips lines.
- **In Claude**, which can't watch video, judge from three things it can check on its own:
  1. **The words** (transcript): the whole line, no stumbles, no filler, no restart in the middle.
  2. **The sound** (`astats` on each take): steady volume, no clipping, no bumps or bursts of noise.
  3. **The picture** (still frames): one sheet per repeated line with every take stacked, 2 frames a second: `ffmpeg -nostdin -ss START -t LENGTH -i IN.mov -vf fps=2,scale=160:-2,tile=10xN take.jpg`, one per take, stacked into one image. Look at the sheets for everything in "What makes a take the keeper".
- **Screen recordings with a voice:** judge the wording, the voice, and whether the pointing or clicking matches what's being said.

## Step 4: Show the picks (only if the editor asked to see them first)

1. Show the cut list: one numbered line per kept piece, `start-end` and the exact words kept. Mark close calls with "(close call: take 2 is just as clean)" on that line, so the editor knows where to look; clear picks get no note. Add one short line at the end only if something blocks the edit (a word you can't make out).
2. The editor approves, swaps a take ("use take 2 for line 4") or cuts a line. Their changes stand, even if a video model later disagrees. When they swap, ask why in one short question if they didn't say. Their reason is how the skill learns (Step 7).

## Step 5: Build the cut

The cut is really tight: speech runs straight into speech everywhere, inside kept takes too. Thinking pauses and breaths between phrases get cut. The only held moment is about 0.5s on the last frame.

1. **Edges come from the speech islands**, not the transcript. Each kept piece starts at its island's first sound and ends at its last. Breaths, lip smacks and handling noise before the first word can poke above -30dB and get stitched into the island, so a piece starts at the onset of its first word (where the level jumps up to speech, usually -25dB or louder), not at the first blip. Any stretch of breath or noise at the start or end of a piece gets cut. Ends work the other way: a line often trails off quietly ("asleep at night" said softly), so a piece ends after its last word even when that word is quieter than the rest. Check the last word of every line is in the cut's transcript.
2. **Pauses inside a kept take** get found with a more sensitive pass, `silencedetect=n=-30dB:d=0.2`, and every one of 0.25s or more is cut out. Restarts and repeated words inside a take get cut too, keeping only the clean final phrasing.
3. **Pad each piece about 0.05s on each side.** More leaves a pause; less chops a word.
   Then snap every edge to a whole frame (start rounds down to the frame before, end rounds up to the frame after). Edges between frames make the join duplicate or drop frames, which moves every later cut by a frame or two and lets stray frames through when b-roll is placed on the cuts.
4. **Pieces shorter than about 0.3s are almost always leftovers** (a stray syllable). Drop them unless they hold a whole word.
5. Add a 20ms audio fade at every joint and join everything in one re-encode from a working copy. The original file stays untouched.
6. Save the list of pieces (`[[start, end], ...]` in seconds) as `clips.json`; the check script reads it.

## Step 6: Check the cut before the editor sees it

Every version the editor sees has passed every check on that exact file. A check that wasn't run counts as a fail.

1. **Run the check script:** `python3 scripts/cut_check.py --voice audio.wav --clips clips.json --out CUT.mp4`. It checks three things and prints `RESULT PASS` or `FAIL`:
   - **Endings:** the last 50ms of every piece is below speech level (-30dB). If it isn't, a word got cut off: move that end later to where the level drops.
   - **Starts:** the 30ms before every piece's start is quiet, so no piece starts in the middle of a word.
   - **Gaps:** no pause of 0.25s or more anywhere in the cut except the final hold.
   With several recordings, run it once per recording: that recording's audio as `--voice` and only its pieces in `clips.json`, each time with the same cut as `--out`.
   If the sound comes from a different file than the picture (a separate mic), also cut the camera's own audio with the same trims and pass it as `--camlock`, so the script checks sync too (every 3 seconds within 40ms).
2. **Every word, whole, once:** transcribe the cut with word timings and compare it to the cut list word for word. A half word at a joint means that edge is too tight. A repeated word or phrase at a joint means a leftover restart.
   **No dead air between words:** in that transcript, no gap between one word ending and the next starting is longer than about 0.3s (except the final hold). The gap check in the script only finds quiet pauses; a pause full of breathing is loud enough to pass it, so this word-gap check is what catches it. Trim the piece to its first word and run every check again.
3. **Each joint, one by one:** for every cut, name the last word before it and the first word after it, and confirm both are fully said. Transcribe a 2-second window around each joint to check (a general "any problems?" lets a chopped word slip through). In Runneth, also have the video model watch the cut as a picky first-time viewer and list problems with times: clipped or stray words, glitches, frozen frames, jarring jumps.
4. **Length:** the cut's length matches the cut list total.

Fix everything that fails, cut again and rerun every check.

## Step 7: Learn from the editor

Every time the editor swaps a take, changes an edge or says why one take is better, turn that reason into a general rule and merge it into "What makes a take the keeper" below (or into Step 5 when it's about how tight the cut is). Keep the list short: rewrite and combine rules instead of piling on new ones. Only the editor's reasons change the rules.

## What makes a take the keeper

These rules came from one editor's real picks on her own talking-head videos. Apply them in order, then replace them with your own editor's rules as their reasons come in.

1. **The whole line, said cleanly.** A take with a stumble or a missing word loses to a clean one, however good it looks.
2. **Nothing covering the face.** A hand or mic in front of the mouth rules a take out.
3. **Energy.** Gestures, movement and an animated delivery beat a still, flat read.
4. **The happiest face.** A real smile and bright eyes win between two clean takes.
5. **The face fits the line.** Wide eyes on a punchline, a real smile on a happy line.
6. **Natural, even pace.** Not rushed, no long pauses.
7. **Best pieces, joined cleanly.** The best take wins whichever recording it's in, and a line made from parts of two takes beats one whole take when each part is the better version. The joint is clean when the speaker's head and hands sit in about the same place on both sides (check the frame before and after), or when the joint gets covered later by b-roll. A switch between recordings also needs the same look on both sides (hair, light, framing, product in hand); when the look changes, the switch lands between lines and gets covered by b-roll or a zoom change.
8. **Shorter when it lands harder.** Cut a line down to its strongest part when the rest repeats what's already been said or slows the video down ("until I ran out" instead of "I didn't realize how much it was helping until I ran out").
9. **Close calls stay close calls.** When two takes are equally clean and the frames show no real difference, pick one and mark it as a close call. Still frames can't show tone, so don't pretend one is clearly better.

## Rules for every cut

- Every word in the cut comes from the audio. Words you can't make out are marked as unclear, never guessed.
- Times come from the original recording's timeline, and every piece in the cut list names its recording.
- AI times are close, not exact. Every edge gets set from the speech islands and checked in the audio.
