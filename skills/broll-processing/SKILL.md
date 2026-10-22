---
name: broll-processing
description: |
  Turn raw b-roll footage into a tagged, searchable library of short clips. Watch each b-roll video once, tag every useful moment with timestamps, pick the moments worth keeping (the editor picks, or the AI picks on its own if the editor says so), cut only those picks with a 1-second buffer, and learn the editor's taste from their reasons. Use when someone uploads b-roll, asks to tag, bank or label b-roll, or asks to find a kind of shot ("find me unboxing b-roll").
  Triggers: "process my b-roll", "tag this b-roll", "bank this b-roll", "b-roll library", "find me unboxing b-roll", "do we have b-roll of", "label my b-roll"
---

# B-roll processing

The goal: every b-roll video gets watched once, the best moments get picked, and only those clips are kept. Each kept clip is cut with a 1-second buffer and tagged by what's in it, so any shot can be found later without rewatching footage.

This skill is built for **Claude** (Claude Code, or the Claude app with code tools turned on) and **Runneth**. It needs three things:

- **A way to see the video:** in Runneth, a video model watches it. Claude can't watch video, so it reads still frames instead: small contact sheets of 2 frames a second to find moments (`ffmpeg -i IN.mp4 -vf fps=2,scale=160:-2,tile=10x6 sheet_%02d.jpg`), full-size frames to judge them (`ffmpeg -ss <time> -i IN.mov -frames:v 1 frame.jpg`), plus the audio transcript when one is available. If there's no way to transcribe, work from the frames alone.
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

1. Save each b-roll video untouched and full length, with a plain name: `broll-<n>-<what-it-is>.<ext>` (for example `broll-4-unboxing.mov`). Note which project and brand it belongs to, and the shoot date.
2. Check its length and orientation.
3. Make a light working copy for watching and picking. With ffmpeg:
   `ffmpeg -i IN.mov -vf scale=540:960 -c:v libx264 -preset veryfast -crf 25 -g 15 -pix_fmt yuv420p -c:a aac -b:a 96k -movflags +faststart OUT.mp4`
   (the short keyframe gap makes it scrub smoothly; swap 540:960 for 960:540 on landscape footage).

## Step 2: Tag it

1. Watch the working copy and write a working map that covers every stretch of the video, with no gaps: time range, tags from the library's tag list, and one plain sentence of what happens. Unusable stretches stay in the map too, with a short note on why (out of focus, checking the frame), so it's clear they were looked at. The map is only for finding the picks; it's deleted with the working copies, and only kept clips get saved tags.
2. Check what an AI viewer can't know: whose footage it is, whether the product on screen is really the brand's product (a coffee in the shot is just coffee), and anything that looks off. Use the small contact sheets to find moments, then look at full-size frames before calling any moment usable. Small frames hide a soft product and where the creator's eyes are.
3. A great idea that came out unusable becomes a reshoot note.
4. Write one plain line naming the point of each video (what it was filmed to show), worked out from the footage alone. Step 3 always keeps the moment that shows it, if it's usable.
5. Say whether each video is **lifestyle** (no product in it, reusable for any brand) or **product** footage.

## Step 3: Pick the moments

**If the editor wants a pitch first:**

1. Give the editor the working copies and a short list of the strongest moments from your working map as a starting point.
2. The editor marks each moment they want to keep: start time, end time, and **why** they picked it. Any format works (a picker app, a spreadsheet, a notes doc, timestamps in a message), as long as every pick has a start, an end and a reason.
3. The reasons matter as much as the times. They're how this skill learns the editor's taste (Step 4, item 6).

**If the editor said just get to work:**

1. Pick the moments yourself, using "What makes a moment worth keeping" in order. Always keep the video's point (rule 4) and bank the evergreen shots (rule 9).
2. When the same action happens more than once, keep the cleanest take.
3. Write a start, an end and a one-line reason for every pick.
4. Check each pick on full-size frames before cutting: the product is sharp, the creator's eyes are on the product or the camera, and the times are right (AI times are close, not exact). Drop any pick that fails.

## Step 4: Cut the picks and save them

1. Cut each pick at full quality from the original file, with **1 second of extra footage before and after** the pick times, clamped to the start and end of the video. Name each clip `<shoot-date>-v<video>-<pick>-<what-happens>.mp4` (for example `2026-10-22-v4-4-unbox-tear-top.mp4`). The date keeps names from clashing, since every shoot for a brand lands in the same folder and video numbers restart each shoot. With ffmpeg, a high-quality cut is `-c:v libx264 -crf 16`. If a clip is too big to move where it needs to go, raise the crf a little (18) rather than shortening it.
2. A pick with no length (start equals end) is a note, not a clip. It goes in the shoot file's reshoot notes (for example "out of focus, reshoot").
3. Store the clips in the brand's b-roll folder, the one place all of that brand's b-roll lives across projects.
4. Write the shoot file, one per shoot, at `shoots/<shoot-date>-<brand>.md` in the library folder (template: `templates/shoot-file.md`): each video's point, then every kept clip with its file name, pick time, tags, what happens, and why it was picked. The editor's reasons go in word for word; reasons the AI wrote are marked "(AI)". End it with reshoot notes and the shots this brand is still missing.
5. Add each clip under its tags in the library index's "Find by tag" table. The first time, start the index from `templates/b-roll-library-index.md`. Then delete the original full videos and every working copy. Only the picked clips are kept.
6. Learn from the reasons: turn each of the **editor's** reasons into a general rule and merge it into "What makes a moment worth keeping" below (or into the b-roll selection skill when it's about where a clip goes in a video). Keep the list short: rewrite and combine rules instead of piling on new ones. Only the editor's reasons change the rules; reasons marked "(AI)" stay as they are.
7. If the editor rejects a kept clip later, delete it, take it out of the shoot file and the index, and turn their reason into a rule.

## Finding b-roll later

When someone asks for a kind of shot ("unboxing for this brand", "me looking tired"), look it up in the library index's "Find by tag" table and hand back the matching clips. A bare tag (`pet`) matches every detail under it (`pet:cat`, `pet:dog`). Lifestyle clips count for any brand; product clips belong to their own brand.

## What makes a moment worth keeping

These rules came from a real editor's picks and reasons on a UGC product shoot. Apply them in order, then replace them with your own editor's rules as their reasons come in.

1. **Movement.** The best moment in a shot is where something changes: a head turn, a hand gesture, a new expression, a pet walking in. A shot where nothing moves reads like a photo. A still shot is only kept as a short accent (a clean product close-up); tag it `static`.
2. **A face that acts out the feeling.** A sigh, a yawn, head in hands, a big smile. The expression shows the line's feeling on its own.
3. **Eyes in the scene.** The clip starts and ends while the creator is looking at what they're doing. Start after any glance at the camera or off to the side. If they hold the product up but look somewhere else, they're checking the frame, not doing a take. It reads as weird on screen, so skip it.
4. **The video's point is always picked.** Every b-roll video was filmed to show something, and the moment that shows it most clearly is always a keeper. Read the point from the footage itself: what most of the video is spent on, or what the creator sets up and then shows. The point can be anything: a product pouring smoothly, a competitor's powder clumping, a messy "before", a pet doing something funny. Showing the product working is one kind of point, not the rule. If the moment that shows the point isn't usable (blurry, out of frame), it becomes the first reshoot note instead.
5. **Real life in the frame.** Pets, small funny moments (tossing an empty packet) and other unplanned details make b-roll feel real and give viewers something to look at.
6. **The natural, flattering version.** When the creator does the same action twice, the one that looks natural and like a real person wins (a yawn with a hand over the mouth).
7. **Sharp focus.** A shot counts when the product and the face are in focus. Judge focus on a full-size frame, never a contact sheet. If the product is never sharp anywhere in the shot, the whole shot is out. A great idea that came out blurry becomes a reshoot note.
8. **The whole product.** Show the full package, and flip it to show the back. Turning it adds movement and introduces the product, and the back carries details like ingredients.
9. **Evergreen shots, every time.** Bank these from every product shoot, even when the current video won't use them: unboxing (tear, look inside, pull one out), product in use (open, pour, mix, sip), pointing at the ingredients, creator smiling with the product, clean product close-up, holding the product. Any good close-up is worth banking too (a glass held up to the lens, hands mixing); tag it `closeup:<what>` so it can be used as a short accent.
10. **Short is fine.** A clean 2-second slice is a usable clip.

## Rules for every tag

- Every kept clip has a start, an end, tags, a plain description and a reason.
- Tags describe only what can be seen in the clip, so anyone tagging the same clip would pick the same tags without knowing the brand or the script. What a clip *means* for a video (a "before" shot, a pain point) is decided later, in the b-roll selection skill.
- Add the detail after the colon (`tag:<what>`) whenever it's visible and someone might search for it.
- Times come from the original file's timeline. The shoot file records the pick times; the clip itself starts 1 second earlier.
- AI-generated times are close, not exact. Check them on full-size frames before cutting.
