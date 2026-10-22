---
name: headline
description: >-
  Write and place the hook headline on a vertical (9:16) talking-head video: the short line of on-screen text a viewer reads in the first seconds. Writes a few options that add to what's being said, lets the editor pick, then places it above the head in a clean box style for the whole hook. Built for Claude Code and Runneth. Use after framing, when someone asks for a hook headline, text hook, title on the video or on-screen hook.
---

# Headline

The goal: in the first second, the viewer reads one short line that tells them what this is about and makes them need to hear the rest.

This is step 4 of the editing order: a-roll cut, b-roll, framing, **headline**, captions. It runs on the framed video, before captions, so captions can stay out of its way.

This skill is built for **Claude Code** and **Runneth**.

## Before you start: the tools

In Runneth, everything is already installed: skip this section.

In Claude Code, this skill needs the free video tools the **video-editing-setup** skill installs. Check quietly that `~/.video-editing-tools/bin/ffmpeg -version` runs. If it does, use the tools in `~/.video-editing-tools/bin` (`ffmpeg`, `ffprobe`, `python`) wherever this skill says `ffmpeg`, `ffprobe` or `python3`, and carry on. If it doesn't, follow the video-editing-setup skill first, then come back here.

**The font:** Figtree SemiBold, the only font this skill uses. It's a free Google font. Check quietly whether it's on the computer or in a fonts folder next to the project. If it isn't, ask: "This uses Figtree, a free Google font. Want me to download it for you?" On yes, download the Figtree SemiBold file from Google Fonts (fonts.google.com/specimen/Figtree) into a fonts folder next to the project, and carry on. This check applies in Runneth too.

## What it needs

- The framed video and its words with timings.
- Who the video is for and what they already know (problem, the kind of fix, or this product), if the editor has said.

## Step 1: Find the hook

The hook runs from the first clip through the end of the first complete thought. When that's unclear, it's the first clip. The headline stays on screen for exactly that stretch.

## Step 2: Write three completely different options

Write three headlines that are completely different from each other, and let the editor pick. Each one takes a different angle and does a different job from the list below, so the editor is choosing between three real directions, never three wordings of the same idea. Each one:

1. **10 words or fewer, aiming for 3 to 8,** and always fits on one or two lines.
2. **Sounds like the person in the video typed it over their own post** in five seconds: casual, plain words, the way they'd text. A headline that could be a YouTube title or a blog header gets rewritten.
3. **Says something different from the first spoken line.** The text and the voice work together; the text never just repeats the voice.
4. **Leaves something hanging:** an unanswered question, an unexplained claim, something unsaid.
5. **Does one of three jobs:**
   - **Names what the voice leaves vague** (what's being tried or talked about).
   - **Calls out the viewer,** worded the way they'd say it ("if your brain won't shut up at night").
   - **Makes a claim the video has to back up,** in first person.
6. **Matches what the viewer already knows.** A video opening on the problem gets a headline about the problem, with no product name. The product name goes in only when the video opens on the product or an offer.

Give each option a few words on which job it does. Wait for the pick, unless the editor said to just go ahead: then use the strongest one and say which.

## Step 3: The look

The default style, **box headline**:

- **Figtree SemiBold, about 66px, in sentence case: the first letter is always a capital,** on a solid rounded box per line (about 18px corners). The two lines' boxes overlap slightly so they read as one shape.
- **White box with black text.**
- **One line if it fits** between x 60 and 1020, otherwise two. When it won't fit in two lines at full size, rewrite it shorter; the size stays the same.
- It can end with one emoji the person would actually use.

## Step 4: Where it sits

1. **Above the head, centred,** with its top around y 260 in a 1080x1920 video, inside the safe area.
2. **The face stays fully visible.** When the head sits too high for the headline to fit above it, move the headline to the clearest open space inside the safe area and keep it off the eyes and mouth.
3. **It appears on the first frame of the hook and leaves on the frame the hook ends,** with a hard cut on and off. When the hook ends on a cut, it leaves on that cut.

## Step 5: Build and burn

1. Draw the headline as a transparent PNG at full size with Python (Pillow) and the font file, measuring the real text to size each box: even space above the tallest letter and below the lowest one, sides about 1.5 times that.
2. Lay it over the video for the hook's exact frames in one pass (x264, slow, crf 14 to 18), sound copied untouched.

## Step 6: Check before anyone sees it

1. A frame at the start, middle and end of the hook: the headline sits inside the safe area, the face is fully visible, and the text is sharp.
2. The frame just before the hook ends still has it, and the frame after doesn't.
3. It's one or two lines, 10 words or fewer, and starts with a capital letter.

## Step 7: Learn from the editor

When the editor changes the wording, the look or the timing, ask why (unless they said). Write the reason as a rule in "Headline rules from the editor" below, worded as what should be true. Reasons you came up with yourself are marked "(AI)" and never change the rules.

## Headline rules from the editor

(Empty to start. Add each rule the editor gives.)
