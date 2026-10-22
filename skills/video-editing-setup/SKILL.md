---
name: video-editing-setup
description: >-
  Set up the free tools the video editing skills need (ffmpeg, Python, numpy, faster-whisper) on the person's computer, with no typing and no technical words on their side. Built for Claude Code; Runneth already has every tool. Use the first time someone uses a video editing skill, when another video editing skill finds a tool missing, or when someone asks to set up their video editing tools.
---

# Video editing setup

The goal: the person says yes once, and every tool the video editing skills use is ready. They never type a command, see an error message, or need to know what these tools are.

In **Runneth**, everything is already installed: tell the person they're all set and stop.

## What gets set up

| Tool | What it does (plain words) |
|---|---|
| ffmpeg and ffprobe | Cut video, pull the sound out, grab still frames, measure length |
| Python 3 | Runs the small scripts, like the check that no word got chopped |
| numpy | Does the math on the sound |
| Pillow | Draws text boxes, like the hook headline |
| faster-whisper | Writes down every spoken word with the time it was said |

Everything except Python goes into one private tool folder, `~/.video-editing-tools`, so nothing else on the computer changes. When `~/.video-editing-tools/bin` exists, the editing skills use the tools inside it.

## Step 1: Check quietly

Run these and note which ones fail:

- `python3 --version`
- `~/.video-editing-tools/bin/python -c "import numpy, PIL, faster_whisper"`
- `~/.video-editing-tools/bin/ffmpeg -version` and `~/.video-editing-tools/bin/ffprobe -version`

If everything works, tell the person in one line that their video tools are ready, then hand back to the skill that sent you here.

## Step 2: Ask once, in plain words

For example: "Before I can edit, I need to add a few free tools to your computer: one that cuts video and one that turns speech into text. It takes a few minutes and doesn't change anything else. Want me to set them up?"

Wait for yes.

## Step 3: Install everything yourself, in this order

1. **Python, if it's missing.**
   - Mac: run `python3` once. macOS shows a pop-up offering to install its developer tools. Tell the person: "A box popped up on your screen. Click Install, then tell me when it's done." Wait for them.
   - Windows: run `winget install Python.Python.3.12`.
2. **The private tool folder:** `python3 -m venv ~/.video-editing-tools`. On Windows, the folder uses `Scripts` instead of `bin` everywhere below.
3. **The add-ons:** `~/.video-editing-tools/bin/pip install numpy pillow faster-whisper static-ffmpeg`.
4. **ffmpeg and ffprobe**, with no password needed:
   - Run `~/.video-editing-tools/bin/static_ffmpeg_paths`. The first run downloads ffmpeg, then prints two lines, `FFMPEG=<path>` and `FFPROBE=<path>`.
   - Link both into the tool folder: `ln -sf <printed ffmpeg path> ~/.video-editing-tools/bin/ffmpeg` and `ln -sf <printed ffprobe path> ~/.video-editing-tools/bin/ffprobe`. On Windows, copy the two files there instead.
5. **The speech model:** run `~/.video-editing-tools/bin/python -c "from faster_whisper import WhisperModel; WhisperModel('base')"` once. This downloads the model, about 150 MB, so the first edit doesn't stall.

Tell the person in one short line what's happening while the downloads run ("Downloading the tools now, this takes a few minutes").

## Step 4: Check again and finish

Run the Step 1 checks again. When they pass, tell the person in one line that their video tools are ready, then hand back to the skill that sent you here.

## If something won't install

- Try once more. A dropped download is the usual cause.
- Still failing: tell the person in plain words what didn't work and what you need from them (for example, "Your computer needs an update before I can add the speech tool"). Never paste an error message at them.
- Ask one thing at a time and wait for their answer.
