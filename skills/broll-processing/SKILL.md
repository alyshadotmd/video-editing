---
name: broll-processing
description: |
  Turn raw b-roll footage into a tagged, searchable library of short clips. Watch each b-roll video once, tag every useful moment with timestamps, pick the moments worth keeping (the editor picks, or the AI picks on its own if the editor says so), cut only those picks with a 1-second buffer, and learn the editor's taste from their reasons. Use when someone uploads b-roll, asks to tag, bank or label b-roll, or asks to find a kind of shot ("find me unboxing b-roll").
  Triggers: "process my b-roll", "tag this b-roll", "bank this b-roll", "b-roll library", "find me unboxing b-roll", "do we have b-roll of", "label my b-roll"
---

# B-roll processing

The goal: every b-roll video gets watched once, the best moments get picked, and only those clips are kept. Each kept clip is cut with a 1-second buffer and tagged by what's in it, so any shot can be found later without rewatching footage.

This skill works with any AI tool or agent. It needs three things, and any version of each works:

- **A way to watch video:** any video-understanding model, or a person scrubbing through.
- **A way to cut video:** ffmpeg, or any video editor.
- **A b-roll library folder:** a place for clips plus two kinds of text files (an index and one file per shoot). Templates are in the `templates/` folder next to this file.

Talk to the editor in plain everyday words, one idea at a time.

## Step 0: Ask one question first

Before doing anything else, ask the editor exactly this, as one question with two options:

> "Do you want me to pitch you the timestamps first, or just get to work?"

- **Pitch me first** → follow every step below, including Step 3 (the editor picks).
- **Just get to work** → run every step start to finish without stopping. In Step 3, pick the moments yourself using "What makes a moment worth keeping". Don't ask for approval, project names or anything else along the way; leave unknowns as `_not given_` in the shoot file and mention them once at the end.

Skip the question if the editor already said which one in their message ("just do it", "don't ask me", "pitch me the picks"). If no one is there to answer, treat it as "just get to work".

## Step 1: Keep the full video until the picks are cut

1. Save each b-roll video untouched and full length, with a plain name: `broll-<n>-<what-it-is>.<ext>` (for example `broll-4-unboxing.mov`). Note which project and brand it belongs to.
2. Check its length and orientation.
3. Make a light working copy for watching and picking. With ffmpeg:
   `ffmpeg -i IN.mov -vf scale=540:960 -c:v libx264 -preset veryfast -crf 25 -g 15 -pix_fmt yuv420p -c:a aac -b:a 96k -movflags +faststart OUT.mp4`
   (the short keyframe gap makes it scrub smoothly; swap 540:960 for 960:540 on landscape footage).

## Step 2: Tag it

1. Watch the working copy and write a timeline that covers the whole video with no gaps: time range, tags from the library's tag list, and one plain sentence of what happens. This timeline is a working draft for picking; only the kept clips get saved.
2. Check what an AI viewer can't know: whose footage it is, whether the product on screen is really the brand's product (a coffee in the shot is just coffee), and anything that looks off. Look at the key moments up close (stills or a contact sheet).
3. Only usable moments get tagged and considered: in focus, in frame, clean. A great idea that came out unusable becomes a reshoot note instead.
4. Say whether each video is **lifestyle** (no product in it, reusable for any brand) or **product** footage.

## Step 3: Pick the moments

**If the editor wants a pitch first:**

1. Give the editor the working copies and a short list of the strongest moments from your timeline as a starting point.
2. The editor marks each moment they want to keep: start time, end time, and **why** they picked it. Any format works (a picker app, a spreadsheet, a notes doc, timestamps in a message), as long as every pick has a start, an end and a reason.
3. The reasons matter as much as the times. They're how this skill learns the editor's taste (Step 4, item 6).

**If the editor said just get to work:**

1. Pick the moments yourself, using "What makes a moment worth keeping" in order. Always bank the evergreen shots (rule 9).
2. When the same action happens more than once, keep the cleanest take.
3. Write a start, an end and a one-line reason for every pick.
4. Check each pick up close before cutting (AI times are close, not exact).

## Step 4: Cut the picks and save them

1. Cut each pick at full quality from the original file, with **1 second of extra footage before and after** the pick times, clamped to the start and end of the video. Name each clip `v<video>-<pick>-<what-happens>.mp4` (for example `v4-4-unbox-tear-top.mp4`). With ffmpeg, a high-quality cut is `-c:v libx264 -crf 16`. If a clip is too big to move where it needs to go, raise the crf a little (18) rather than shortening it.
2. A pick with no length (start equals end) is a note, not a clip. It goes in the shoot file's reshoot notes (for example "out of focus, reshoot").
3. Store the clips in the brand's b-roll folder, the one place all of that brand's b-roll lives across projects.
4. Write the shoot file, one per shoot (template: `templates/shoot-file.md`): every kept clip with its file name, pick time, tags, what happens, and why it was picked. The editor's reasons go in word for word; reasons the AI wrote are marked "(AI)". End it with reshoot notes and the shots this brand is still missing.
5. Add each clip under its tags in the library index's "Find by tag" table. The first time, start the index from `templates/b-roll-library-index.md`. Then delete the original full videos and every working copy. Only the picked clips are kept.
6. Learn from the reasons: turn each of the **editor's** reasons into a general rule and merge it into "What makes a moment worth keeping" below (or into the b-roll selection skill when it's about where a clip goes in a video). Keep the list short: rewrite and combine rules instead of piling on new ones. Only the editor's reasons change the rules; reasons marked "(AI)" stay as they are.

## Finding b-roll later

When someone asks for a kind of shot ("unboxing for this brand", "me looking tired"), look it up in the library index's "Find by tag" table and hand back the matching clips. Lifestyle clips count for any brand; product clips belong to their own brand.

## What makes a moment worth keeping

These rules came from a real editor's picks and reasons on a UGC product shoot. Apply them in order, then replace them with your own editor's rules as their reasons come in.

1. **Movement.** The best moment in a shot is where something changes: a head turn, a hand gesture, a new expression, a pet walking in. A shot where nothing moves reads like a photo.
2. **A face that acts out the feeling.** A sigh, a yawn, head in hands, a big smile. The expression shows the line's feeling on its own.
3. **Eyes in the scene.** The clip starts and ends while the creator is looking at what they're doing. Start after any glance at the camera or off to the side.
4. **The product looks like it works.** Keep moments where the product behaves the way it should: it opens, pours and mixes evenly.
5. **Real life in the frame.** Pets, small funny moments (tossing an empty packet) and other unplanned details make b-roll feel real and give viewers something to look at.
6. **The natural, flattering version.** When the creator does the same action twice, the one that looks natural and like a real person wins (a yawn with a hand over the mouth).
7. **Sharp focus.** A shot counts when the product and the face are in focus. A great idea that came out blurry becomes a reshoot note.
8. **The whole product.** Show the full package, and flip it to show the back. Turning it adds movement and introduces the product, and the back carries details like ingredients.
9. **Evergreen shots, every time.** Bank these from every product shoot, even when the current video won't use them: unboxing (tear, look inside, pull one out), product in use (open, pour, mix, sip), pointing at the ingredients, creator smiling with the product, clean product close-up, holding the product. Any good close-up is worth banking too (a glass held up to the lens, hands mixing); tag it `closeup:<what>` so it can be used as a short accent.
10. **Short is fine.** A clean 2-second slice is a usable clip.

## Rules for every tag

- Every kept clip has a start, an end, tags, a plain description and a reason.
- Tags describe only what can be seen in the clip, so anyone tagging the same clip would pick the same tags without knowing the brand or the script. What a clip *means* for a video (a "before" shot, a pain point) is decided later, in the b-roll selection skill.
- Times come from the original file's timeline. The shoot file records the pick times; the clip itself starts 1 second earlier.
- AI-generated times are close, not exact. Check up close before cutting.
