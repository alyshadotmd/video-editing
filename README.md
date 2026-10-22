# video-editing

Skills for editing short-form video with AI, built for Claude Code and Runneth. Each skill is a plain markdown file with steps and rules.

Made by [Alysha](https://github.com/alyshadotmd) while building her own AI video editing stack.

## The skills

| Skill | What it does |
|---|---|
| [`video-editing-setup`](skills/video-editing-setup/SKILL.md) | Sets up the free tools the other skills need, for Claude Code. The person says yes once and Claude installs everything, with no typing. Runneth doesn't need it. |
| [`aroll-processing`](skills/aroll-processing/SKILL.md) | Turns raw talking-head footage into a tight rough cut. Drop in one long recording or several recordings of the same script, and it finds every take, picks the best piece of each line (from any recording), and cuts it so no word is chopped and no pause is left. Shows you the picks first, or just does the edit. |
| [`broll-processing`](skills/broll-processing/SKILL.md) | Turns raw b-roll into a tagged library of short clips. AI watches and tags every moment, you pick the keepers and say why, and only your picks get cut and saved. Your reasons become rules, so it learns your taste. |
| [`broll-selection`](skills/broll-selection/SKILL.md) | Plans b-roll for a first cut, line by line: which lines need b-roll, which clip from your library fits, and what you still need to film. Places the clips after you approve. |

Start with a-roll processing for the rough cut. The b-roll pair works together: processing builds the library, selection places clips on the cut.

## How to use them

1. **Claude Code:** copy the skill folders into your skills folder, always including `video-editing-setup`. The first time you edit, it sets up the tools (see the [setup guide](SETUP.md)).
2. **Runneth:** add the skill folder to your skills. Every tool is already installed.
3. **Set up your library:** the templates live inside the skill that fills them in ([`broll-processing/templates/`](skills/broll-processing/templates/)). Copy them into a folder for your b-roll. Each skill folder carries its own templates. In Claude Code, the editing skills also rely on `video-editing-setup` for their tools.

## What you need

Nothing technical. In Claude Code, the skills set up their own free tools the first time you use them: you just say yes. See the [setup guide](SETUP.md) for the few clicks involved.

In Runneth, a video model watches the footage. Claude can't watch video, so the skills have it read still frames and the transcript instead.

## Make it yours

The keeper rules in each skill ("what makes a take the keeper", "what makes a moment worth keeping") come from one editor's real picks. Every time you swap a take or pick a clip, say why. The skills turn those reasons into rules, so over time they pick the way you do.
