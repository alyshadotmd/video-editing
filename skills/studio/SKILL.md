---
name: studio
description: >-
  Keep every edited video in one Runneth app, the video studio, where the person watches each version, leaves notes at exact moments and approves the one they like. The first edit creates the app; every edit after that drops its new version in. Runneth only. Use every time a video edit produces something the person should watch (a first cut, a draft, a fix, a final), and when someone asks for "the studio", "my videos", or where to review an edit.
---

# Studio

The goal: one place where every video the person edits lives, version by version. They open it, watch the newest cut, pause where something should change, type a note, and paste their notes back into the chat. Runneth makes the changes and the next version shows up in the same place.

This skill is built for **Runneth** only. It needs the `app` command, which only Runneth has.

## How it fits the editing order

Every time any video editing skill renders a video the person should watch, it goes into the studio as the next version before the video is handed over. That covers the a-roll rough cut, each round of fixes, the version with b-roll, the version with the headline and captions, and the final. **edit-video** does this at its handover, and each skill does it when run on its own.

## The first edit: create the studio

Do this only when `/agent/apps/video-studio` doesn't exist yet. Run these from this skill's folder:

1. Create the app:
   ```bash
   app create video-studio --icon film-slate --colors "#111827,#9CA3AF"
   ```
2. Put the studio page in it:
   ```bash
   python3 scripts/studio.py install
   ```
3. Run `app check video-studio`. It should say no violations.

The studio needs a sign-in to open, so only people with access to this Runneth workspace can see the videos. Keep it that way unless the person asks for a public link.

Tell the person once, in one short line, that their edits now live in their video studio and every future version will land there too.

## Every edit: add the new version

1. Add the video:
   ```bash
   python3 scripts/studio.py add --project "<video title>" --video "<path to the rendered video>" --label "<what changed>"
   ```
   - **Project:** the video's title, written exactly the same way for every version of the same video. A new title makes a new project.
   - **Label:** a few plain words about this version, like "First cut", "Tighter hook", "B-roll added" or "Captions and headline".
   - The script copies the video in as the next version number, makes a poster frame, and prints the version number. Earlier versions always stay, so the person can compare.
2. Get the studio's link from `app list` (the `url` for `video-studio`), add `#/<project slug>?v=<version>` from the script's output, and hand it over with the app link. The project slug is in the script's output too.
3. Say in one line what changed in this version.

## When the person sends notes back

The **Copy my notes** button copies their notes like this:

```
Notes on "My video", version 2:
- 0:03.4: cut the pause before "so"
- Whole video: captions a bit bigger
```

Each time is the moment in that version. Work through every note, render the new video, and add it as the next version with a label that says what changed. Then tell them which notes are done, in the same order they wrote them.

**Approve this version** copies `Approved "My video", version 3.` When that comes in, that version is the one they want: finish the remaining steps on it, or call it done if it's the final.

## What the studio shows

- **Home:** every video, newest first.
- **A video:** the version buttons (V1, V2, ...), the player, a timeline with a dot for each note, a box to leave a note at the paused moment or on the whole video, and their notes listed by time.

Notes and approvals are saved in the person's browser, so they stay put between visits on the same computer until they copy them back.

## Keep it plain

The studio uses Runneth's own look. It shows only the videos and the notes: every version a person watches goes in, and the page stays exactly as the install made it unless the person asks for a change.
