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

## Step 0: Make sure the b-roll is in the library

This skill places clips from a tagged b-roll library. Before planning, check that every b-roll file for this video is in the library, with a shoot file. Any raw b-roll that isn't gets run through the **broll-processing** skill first, then come back here.

## Step 1: Read the first cut

1. Get the cut's timeline: every spoken line with its start and end time in the cut. A transcript with word timings works best.
2. Read what's known about the project: the script and the brand's shoot files in the b-roll library (each kept clip with its tags and why it was picked).

## Step 2: Decide what each line needs

For each line, write what's said and the kind of shot that shows it, in the library's tags. This is where a clip gets its meaning: the same yawn can be the "before" in one video and a relatable moment in another. Rules, in order:

0. **Plan the whole video before placing anything.** Don't fill lines in order. First go through the strongest shots and give each one the line it fits most literally, then fill the remaining lines with what's left. A shot spent early on a loose fit can't be used later where it fits exactly (reading in bed belongs on "bring it to bed with me while I read my book", not on an earlier "nighttime routine" line).
1. **Show the line literally.** Literal means a viewer with the sound off would get the line from the shot alone. An action that's only nearby doesn't count: fluffing a pillow is a task, not "unwind and relax". "This just got delivered" gets the full unopened package; "the ingredients" gets someone pointing at the ingredients; "trying to get through the day" gets a tired face, a sigh or a yawn.
2. **Match the product to the moment.** A delivery means the full package; a nighttime routine means the product in use. Use the form the viewer would expect at that point in the story.
3. **Use the best 1 to 2 seconds of a long clip.** Pick the slice with the most action: the main motion the clip was filmed for (pulling the blanket up), never the fussing before or after it. Close-ups work as short accents.
4. **Chain related clips into a mini story, in the order it happens in real life.** Each step follows the one before it: unboxing goes the sealed package first, then tear the top off, show inside, pull one out. Using the product goes open, pour, mix, sip. Working on the couch goes into lying down for a nap. Short slices of one action placed back to back (half a second of ripping the bag, half a second of opening it, half a second of pulling a packet out) make a strong mini story.
5. **The happy creator with the product goes near the end.** Use it by the call to action, or on any line that isn't visual on its own.
6. **A clip means what its whole shoot shows.** Read the shoot file's point and the full clip before using a slice of it. Working on the couch and then napping there is someone getting through a tired day; it shows daytime tiredness, so it fits a "getting through the day" line and never a "lying in bed at night" line.
7. **Never repeat a moment.** Two clips cut from the same original b-roll video can't both go in one edit when they show the same moment, meaning the same or similar tags (two tired-at-the-counter shots, two yawns, two sips). Clips from the same video that show different things (opening, mixing, a close-up of the glass) are fine to use separately. When a video has two similar moments, put the stronger one on the line it fits best and find something else for the other line, or leave that line on the person talking. Back-to-back slices of one action forming a mini story (rule 4) count as a single use.
   **Stack a video instead of scattering it.** Aim for no more than two separate spots per b-roll video in one edit. When a video has several good moments, stack the related ones into one mini story at the line that fits (getting into bed with the cat, then reading with the drink) rather than spreading them across the video, which feels repetitive. Close-up product shots (anything tagged `closeup:`, like stirring the glass right up to the lens) are the exception: they stand alone as accents and don't count toward a video's two spots.
8. **A line with no clip that truly fits stays on the person talking.** A close-enough clip that shows something different is worse than no b-roll. Add the missing shot to the still-to-film list only when it would clearly help the video.

## Step 3: Pull the clips

1. For each line, find matching clips in the library's "Find by tag" table. Library clips carry 1 second of buffer on both sides, so trim into the actual pick.
2. Lifestyle clips (no product in them) can come from any brand's shoot. Product clips come from this brand only.
3. When nothing in the library fits, the line goes on the "still to film" list with a one-line description of the shot.

## Step 4: Show the editor the plan

Show a short table: line number, what's said, the b-roll (shoot, clip, exact seconds), and why. Then the still-to-film list. The editor approves, swaps or cuts. Clips get placed once the editor says go.

## Step 5: Place it

1. Trim each approved slice from its clip.
2. Lay it over the cut at its line, with the speaker's audio running underneath unchanged. Cut the b-roll in and out on cut points or in the gaps between words.
3. **Work in frame numbers, not seconds.** Convert every a-roll cut and every b-roll edge to a whole frame number (time x frame rate, rounded) before placing anything, and turn slices on and off by frame number. Times like 28.867s at 30fps fall between frames and leave a stray frame showing.
4. **Stacked b-roll butts together frame for frame.** When two b-roll slices sit next to each other, the second starts on the exact frame number the first ends on, so no frame of the person talking slips through between them.
5. **B-roll near a cut snaps to the cut.** When a b-roll edge lands within about 0.3s (9 frames at 30fps) of an a-roll cut, move that edge onto the cut's frame. A slice that starts on a line's first word starts on that line's cut instead, so the talking head never flashes for a few frames before the b-roll.
6. Re-check the edit after placing: audio length matches video length, every b-roll slice lines up with its line, and captions (if any) still read cleanly over the new footage.
7. **No segment under about 0.3 seconds.** Build one list of every edge in the finished video, a-roll cuts and b-roll edges together, in frame numbers. Every segment between two edges, talking head or b-roll, is at least 9 frames at 30fps. A shorter one is a flash and fails. Scene detection alone misses these, because two takes of the same person look alike, so check the list, then grab the frames on both sides of every edge to confirm. Measure where the a-roll cuts really land (the frame with the biggest picture change near each planned cut) rather than trusting times converted from seconds.
8. Turn the editor's feedback on the placement into general rules in Step 2 above. Rewrite and combine rules instead of piling on new ones.
