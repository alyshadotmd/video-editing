---
name: captions
description: >-
  Add burned-in captions to a vertical (9:16) talking-head video: exact word timings, one word at a time or short chunks broken by meaning, white outlined Figtree Bold with an optional highlighted word, placed in the safe area clear of the face and the hook headline. Built for Claude Code and Runneth. Use after framing and the headline, when someone asks for captions, subtitles or on-screen words.
---

# Captions

The goal: captions a viewer reads without effort. Each one is a short, complete piece of meaning, timed to the exact word, sitting in the same spot all video.

This is step 5 of the editing order: a-roll cut, b-roll, framing, headline, **captions**. It runs on the framed video, after the headline, so captions can stay out of the headline's way.

This skill is built for **Claude Code** and **Runneth**.

## Before you start: the tools

In Runneth, everything is already installed: skip this section.

In Claude Code, this skill needs the free video tools the **video-editing-setup** skill installs. Check quietly that `~/.video-editing-tools/bin/ffmpeg -version` runs. If it does, use the tools in `~/.video-editing-tools/bin` (`ffmpeg`, `ffprobe`, `python`) wherever this skill says `ffmpeg`, `ffprobe` or `python3`, and carry on. If it doesn't, follow the video-editing-setup skill first, then come back here.

**The font:** Figtree Bold, the only font this skill uses. It's a free Google font. Check quietly whether it's on the computer or in a fonts folder next to the project. If it isn't, ask: "This uses Figtree, a free Google font. Want me to download it for you?" On yes, download the Figtree Bold file from Google Fonts (fonts.google.com/specimen/Figtree) into a fonts folder next to the project, and carry on. This check applies in Runneth too.

## What it needs

- The video, framed and with the headline on (or its timing).
- The script, if there is one, so names and product words are spelled right.
- When the headline is on screen and where it sits.

## Step 0: Ask about the style first

Ask these one at a time, waiting for each answer:

1. "Do you want captions one word at a time, or a few words at a time?"
2. Only for a few words at a time: "Do you want the word being said to light up in a different colour?"
3. Only if yes: "Which colour?" Offer bright yellow (#FFFF3A) as the default, or their brand colour.

## Step 1: Get every word with its time

1. Transcribe the video's own sound with word timings (faster-whisper `base`, `word_timestamps=True`, `vad_filter=False`). The timings must come from this exact video, because every cut moves them.
2. Use the script's spelling for names, brands and product words, and keep the transcript's timing.
3. Every spoken word gets a caption. Nothing that wasn't said gets one.

## Step 2: Split into chunks by meaning (a few words at a time only)

1. **Usually 1 to 3 words a chunk, up to about 5** when that keeps a phrase whole and it still fits the width.
2. **Keep together:** a noun with its describing words ("a sleep drink"), names ("Claude skill"), a verb with its little words ("go to bed"), and short complete thoughts ("but that's how I felt").
3. **Each chunk ends on a word that carries meaning.** Little words (the, a, of, to, and, because, that, I) start the next chunk instead.
4. Each chunk shows from its first word until the next chunk starts, so the screen never flashes empty mid-sentence.
5. Read the whole list once like a viewer and fix any break that reads awkwardly.

## Step 3: The look

Every caption uses **Figtree Bold**, white, with a black outline. No box, no shadow, no pop-in or bounce: captions just appear. Mostly lowercase, with I, names and brands capitalised, and no full stops or commas at the end.

- **One word at a time:** about 140px with a 6px outline, one word on screen at a time. Each word stays until the next one starts. A long word shrinks to fit about 720px wide. Skip the chunking in Step 2.
- **A few words at a time:** about 60px with a 3px outline, using the chunks from Step 2.
  - **With the word lighting up:** the word being said changes to the chosen colour inside the chunk, karaoke style.
  - **Without:** the whole chunk stays white.

## Step 4: Where they sit

1. **Centred, at chest height,** about y 1260 to 1305 in a 1080x1920 video: below the chin, above the app's caption and buttons.
2. **Inside the safe area:** every letter within x 180 to 900 and above y 1340. Measure each chunk's width; a chunk too wide gets split.
3. **Clear of the headline.** While the headline is on screen, captions sit below it with a clear gap; when the headline sits low, captions move down within the safe area rather than overlapping it.
4. **The same spot all video,** so the eye always knows where to look.

## Step 5: Build and burn

1. Write the captions as an ASS subtitle file. With the word lighting up, use one event per word so the colour moves with the speech. Letter spacing goes in an inline `\fsp` tag.
2. Point the renderer at a fonts folder holding only the Figtree Bold file, so the right weight is used: `ass=captions.ass:fontsdir=fonts`.
3. Burn in one pass from the full-quality video (x264, slow, crf 14 to 18), sound copied untouched.

## Step 6: Check before anyone sees it

1. **Every word, once, on time:** compare the caption list to the transcript word for word.
2. **A frame from every chunk that's widest or sits near the headline:** inside the safe area, nothing cut off, nothing overlapping the headline or the face.
3. **With the word lighting up, the colour lands on the word being said,** checked at a few points through the video.

## Step 7: Learn from the editor

When the editor changes a split, a word or the look, ask why (unless they said). Write the reason as a rule in "Caption rules from the editor" below, worded as what should be true. Reasons you came up with yourself are marked "(AI)" and never change the rules.

## Caption rules from the editor

(Empty to start. Add each rule the editor gives.)
