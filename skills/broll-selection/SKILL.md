---
name: broll-selection
description: |
  Plan and place b-roll on a video from its first cut: go through the cut line by line, decide which lines get b-roll and what kind of shot, pull the best matching moments from a tagged b-roll library, list what still needs filming, and place the b-roll once the editor approves. Use after a first cut exists and someone wants b-roll added, asks what b-roll a video needs, or asks for a b-roll shot list.
  Triggers: "add b-roll", "what b-roll do I need", "b-roll plan", "place the b-roll", "b-roll for this cut", "what should I film for b-roll", "shot list for this edit"
---

# B-roll selection

The goal: the right b-roll on the right line, chosen the way the editor would choose it. B-roll does two jobs: it adds context to what's being said, and it keeps people watching.

This skill is built for **Claude Code** and **Runneth**. It reads from a tagged b-roll library: a folder of short clips plus an index with a "Find by tag" table (each tag, then the clips that have it). The `broll-processing` skill builds one, and any folder of clips with tags works too. Placing the clips needs ffmpeg or any video editor.

Talk to the editor in plain everyday words, one idea at a time.

## Before you start: the tools

In Runneth, everything is already installed: skip this section.

In Claude Code, this skill needs the free video tools the **video-editing-setup** skill installs. Check quietly that `~/.video-editing-tools/bin/ffmpeg -version` runs. If it does, use the tools in `~/.video-editing-tools/bin` (`ffmpeg`, `ffprobe`, `python`) wherever this skill says `ffmpeg`, `ffprobe` or `python3`, and carry on. If it doesn't, follow the video-editing-setup skill first, then come back here.

## Step 1: Read the first cut

1. Get the cut's timeline: every spoken line with its start and end time in the cut. A transcript with word timings works best.
2. Read what's known about the project: the script and the brand's shoot files in the b-roll library (each kept clip with its tags and why it was picked).

## Step 2: Decide what each line needs

For each line, write what's said and the kind of shot that shows it, in the library's tags. This is where a clip gets its meaning: the same yawn can be the "before" in one video and a relatable moment in another. Rules, in order:

1. **Show the line literally.** "This just got delivered" gets the full unopened package; "the ingredients" gets someone pointing at the ingredients; "trying to get through the day" gets a tired face, a sigh or a yawn.
2. **Match the product to the moment.** A delivery means the full package; a nighttime routine means the product in use. Use the form the viewer would expect at that point in the story.
3. **Use the best 1 to 2 seconds of a long clip.** Pick the slice with the most action. Close-ups work as short accents.
4. **Chain related clips into a mini story.** Unboxing goes tear the top off, show inside, pull one out. Using the product goes open, pour, mix, sip. Working on the couch goes into lying down for a nap.
5. **The happy creator with the product goes near the end.** Use it by the call to action, or on any line that isn't visual on its own.

## Step 3: Pull the clips

1. For each line, find matching clips in the library's "Find by tag" table. Library clips carry 1 second of buffer on both sides, so trim into the actual pick.
2. Lifestyle clips (no product in them) can come from any brand's shoot. Product clips come from this brand only.
3. When nothing in the library fits, the line goes on the "still to film" list with a one-line description of the shot.

## Step 4: Show the editor the plan

Show a short table: line number, what's said, the b-roll (shoot, clip, exact seconds), and why. Then the still-to-film list. The editor approves, swaps or cuts. Clips get placed once the editor says go.

## Step 5: Place it

1. Trim each approved slice from its clip.
2. Lay it over the cut at its line, with the speaker's audio running underneath unchanged. Cut the b-roll in and out on cut points or in the gaps between words.
3. Re-check the edit after placing: audio length matches video length, every b-roll slice lines up with its line, and captions (if any) still read cleanly over the new footage.
4. Turn the editor's feedback on the placement into general rules in Step 2 above. Rewrite and combine rules instead of piling on new ones.
