# video-editing

Skills for editing short-form video with AI, built for Claude (Claude Code, or the Claude app with code tools turned on) and Runneth. Each skill is a plain markdown file with steps and rules.

Made by [Alysha](https://github.com/alyshadotmd) while building her own AI video editing stack.

## The skills

| Skill | What it does |
|---|---|
| [`broll-processing`](skills/broll-processing/SKILL.md) | Turns raw b-roll into a tagged library of short clips. AI watches and tags every moment, you pick the keepers and say why, and only your picks get cut and saved. Your reasons become rules, so it learns your taste. |
| [`broll-selection`](skills/broll-selection/SKILL.md) | Plans b-roll for a first cut, line by line: which lines need b-roll, which clip from your library fits, and what you still need to film. Places the clips after you approve. |

They work as a pair: processing builds the library, selection uses it.

## How to use them

1. **Claude Code:** copy a skill folder into your skills folder.
2. **The Claude app:** add the skill folder as a skill (code tools need to be on so it can run ffmpeg).
3. **Runneth:** add the skill folder to your skills.
4. **Set up your library:** the templates live inside the skill that fills them in ([`broll-processing/templates/`](skills/broll-processing/templates/)). Copy them into a folder for your b-roll. Each skill folder works on its own, templates included.

## What you need

- An AI that can watch video (or you, scrubbing through) to tag moments.
- [ffmpeg](https://ffmpeg.org) or any video editor to cut clips.
- A folder for your b-roll library: clips plus a few markdown files.

## Make it yours

The "what makes a moment worth keeping" rules come from one editor's real picks on a UGC product shoot. Every time you pick a clip, write down why. The skill turns those reasons into rules, so over time it picks the way you do.
