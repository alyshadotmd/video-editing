---
name: framing
description: >-
  Frame and zoom a vertical (9:16) talking-head cut: line the person up in every clip so their eyes sit in the safe area and the middle third of the width, with anything they're showing in frame, then pick the lines that earn a slow push-in or a punch-in and plan every other clip around them. Built for Claude Code and Runneth. Use after the a-roll cut and b-roll are in place, when someone asks to frame, re-centre, zoom, punch in or add motion to a video.
---

# Framing

The goal: every clip looks lined up, and zooms land only where the words earn them, so the emphasis feels chosen instead of random.

This is step 3 of the editing order: a-roll cut, b-roll, **framing**, headline, captions. It runs on the finished cut, before any text goes on.

This skill is built for **Claude Code** and **Runneth**.

## Before you start: the tools

In Runneth, everything is already installed: skip this section.

In Claude Code, this skill needs the free video tools the **video-editing-setup** skill installs. Check quietly that `~/.video-editing-tools/bin/ffmpeg -version` runs. If it does, use the tools in `~/.video-editing-tools/bin` (`ffmpeg`, `ffprobe`, `python`) wherever this skill says `ffmpeg`, `ffprobe` or `python3`, and carry on. If it doesn't, follow the video-editing-setup skill first, then come back here.

## What it needs

- The cut (one video file) and its clip list: where every clip starts and ends in the cut, and which clips are talking head versus b-roll, screen recording or green screen.
- The words with timings (the a-roll transcript, or transcribe the cut).

## Step 0: Ask one question first

Ask exactly this: "Do you want to see my framing plan first, or should I just go ahead and frame it?"

## Step 1: Line the person up, one position for the whole video

Every talking-head clip gets a "normal" framing before any zoom is planned, and clips filmed the same way share one normal framing, so the person stays in the same spot from clip to clip and the video flows.

1. **Group the clips by how they were filmed.** Clips from the same recording, or filmed with the same camera position, are one group. A clip only gets its own group when it was filmed with clearly different framing (camera moved, different spot, different distance).
2. **Find where the eyes usually sit in each group.** Grab one frame from the middle of each clip and draw a grid on it (`ffmpeg -ss T -i cut.mp4 -frames:v 1 -vf "drawgrid=w=iw/10:h=ih/10:t=2:c=red@0.6" grid.jpg`). Note the eye position in every clip, then take the middle value across the group. Small leans in single clips don't move it.
3. **Set one normal framing per group from that position:**
   - **The eyes sit inside the safe area:** The safe zones come from the **post-preview** skill: keep everything inside **x 100 to 880, y 290 to 1340** on a 1080x1920 frame (the one box that's safe on Reels, Stories, Feed, TikTok and Facebook). Check post-preview for a placement's exact covered areas when something runs close to an edge.
   - **The eyes land in the middle third of the width** (x 360 to 720 in a 1080-wide video). Anywhere inside it looks natural, so a group whose eyes already sit there keeps 1.0x and no shift.
   - **The whole subject stays in frame:** the person plus anything they're holding up, pointing at or showing. People often lean to one side to make room for a product next to their face; that's the shot working, so keep it as filmed.
   - **Shift only when the eyes sit outside the middle third,** and only as far as it takes to bring them inside it, with the smallest zoom that allows it (shifting sideways by `d` pixels needs a zoom of at least `1 + 2d/1080`, staying at about 1.1x or less). A shift that would cut off what they're holding or showing doesn't happen.
4. **Every clip in a group uses that group's framing,** the same zoom and the same shift. When there are several groups, their normals look as alike as the footage allows (eyes at the same height and centred).
5. B-roll, screen recordings, green screen and footage of someone pointing at or showing something stay as they are.

## Step 2: Check the line-up before any zooms

Zooms are planned only once every clip's normal framing is right.

1. Apply each group's normal framing and grab frames at the start, middle and end of every talking-head clip, with the safe area drawn on.
2. The eyes sit inside the safe area in every frame, and clips from the same group put the person in the same spot.
3. When a frame fails, adjust that group's framing (still at about 1.1x or less) and check again. Only then move on.

## Step 3: Pick the moments that earn emphasis

Read what's being said and shown in every clip. Decide which lines earn a zoom, then plan everything else around them.

- **Slow push-in:** for a line that builds (a story, a reveal, a feeling). Only on clips about 8 seconds or longer. Eased, so it starts and ends smoothly.
- **Punch-in:** a jump straight to a closer framing on the cut, for a line that should hit (a punchline, a claim, a turn in the story).
- **Normal:** everything else. Two or more normal clips in a row is fine.
- **The closest zoom in the video goes on its most important line,** so that line stands out most.
- Every zoom is measured from the clip's normal framing, and never goes past **1.3x** of the original footage.
- **Every zoom grows around the eyes,** so the eyes stay in the same spot on screen at every zoom level, normal included. The face gets bigger, but it never slides down toward the captions or off to one side. When a zoom would crop off what they're holding or showing, it goes smaller, or the clip stays normal.

## Step 4: Plan the clips around the picks

1. **After a slow push-in,** the next clip goes the same or closer than where the push ended, or back to normal. Never a step back that lands in between. Example: slow push-in, same-or-closer punch-in, then normal.
2. **Hold one framing while the person walks through steps or a list,** across every cut in that run.
3. **Clips under about 1 second keep the framing of the clip next to them.** A change that quick reads as a twitch.
4. **Every framing lasts at least about 2 seconds.**
5. **A framing change that goes with a graphic lands on the same frame as the graphic.** Changes that don't go together sit at least 0.5 seconds apart.
6. Framing changes land exactly on cuts; only a slow push-in moves during a clip.

## Step 5: Show the plan (only if they asked to see it first)

One line per clip: clip number, time in the cut, the words, the framing (normal, punch-in to 1.15x, slow push 1.05x to 1.15x), and a short reason for every zoom ("punchline", "the reveal"). Wait for their OK or changes.

## Step 6: Render

- Each clip: crop, then scale back to 1080x1920. The crop is placed so the group's eye point lands at the same screen spot as in its normal framing (Steps 1 and 2): for zoom `z` and eye point `(ex, ey)` in the original, the crop's top-left is `ex - sx/z`, `ey - sy/z`, where `(sx, sy)` is where the eyes sit on screen in the normal framing. A slow push eases `z` across the clip, using the same formula on every frame.
- Render from the original-quality cut in one pass (x264, slow, crf 14 to 18), audio copied untouched.

## Step 7: Check before anyone sees it

1. **Measure the eyes in the finished video, every half second** (a face detector, or a grid frame read by eye). For every talking-head clip:
   - The eyes sit inside the safe area.
   - The eyes sit at the same screen spot in every clip of a group, zoomed or not (within about 30px), inside the middle third of the width, with anything they're holding or showing fully in frame.
   - **The real zoom stays at 1.3x or less.** Compare the distance between the eyes to the same distance in the original footage; the ratio is the zoom actually on screen.
2. The tightest frame in the video looks sharp, not soft.
3. When any check fails, fix the plan or the crop and render again before anyone sees it.
3. No framing lasts under about 2 seconds, and the video's length matches the cut.

## Step 8: Learn from the editor

When the editor changes a zoom, ask why (unless they said). Write the reason as a rule in "Framing rules from the editor" below, worded as what should be true. Reasons you came up with yourself are marked "(AI)" and never change the rules.

## Framing rules from the editor

(Empty to start. Add each rule the editor gives.)
