---
name: edit-video
description: >-
  Run a full short-form video edit from raw footage to finished video by running the other video editing skills in order: setup, sorting the footage, the a-roll cut, b-roll processing, b-roll placement, framing, headline and captions, then a final check of what each step produced. Built for Claude Code and Runneth. Use when someone asks to "edit this video", "edit my footage", "make an ad from these", or hands over raw footage and wants a finished edit.
---

# Edit video

The goal: raw footage in, finished video out, with every step done in order and nothing skipped. This skill doesn't edit anything itself. It runs the other skills, in this order, and checks each one left behind what it should.

This skill is built for **Claude Code** and **Runneth**.

## Step 1: Setup

In Claude Code, run the **video-editing-setup** skill first. In Runneth, skip this.

In Runneth with the **edit-studio** skill installed, run it next, every time: it finds this video's project or makes a new one (its folder with the info document, script, version log, raw footage, b-roll picks, drafts and final, plus its card in the content studio). Every step below saves into that folder.

## Step 2: Sort the footage

Go through every file and decide what it is:

- **A-roll:** someone talking to the camera, saying the script (one recording or several).
- **B-roll:** everything else: product shots, hands, lifestyle moments, reactions.
- **Already in a b-roll library:** clips that are already tagged and saved.

When a file could be either, ask about that file. Say how you sorted everything in one short list.

## Step 3: Ask how they want to work

Ask this before any editing starts:

"Do you want to check in at each step (the takes, the b-roll picks, the b-roll plan, the framing plan, the headline options, the caption style), or should I run straight through and show you the finished video?"

- **Check in at each step:** each skill below asks its own questions when its turn comes, so the caption style gets asked when it's time for captions.
- **Run straight through:** ask the caption questions from the **captions** skill right now, one at a time (one word at a time or a few words, and if a few words, whether the word being said lights up and in which colour), so the run never stalls halfway. Then use the strongest headline option, pitch nothing, and only stop for a real problem (a missing file, a word you can't make out). Each skill below skips its own opening question and uses these answers.

## Step 4: Run the skills in order

1. **aroll-processing**, on the a-roll: the rough cut. The talking head is the video, so it comes first, and the locked script makes the b-roll easier to judge.
2. **broll-processing**, on any raw b-roll. Its clips, shoot file and library index are saved before b-roll selection starts. With no raw b-roll, skip it.
3. **broll-selection**, placing b-roll from the library onto the cut.
4. **framing**, on the cut with b-roll.
5. **headline**.
6. **captions**.

Each skill runs its own checks before the next one starts. When one fails a check it can't fix, stop and say what's wrong in plain words.

## Step 5: Final check and handover

Run every check from framing, headline and captions once more on the finished video, plus two that problems slip past: the a-roll word-gap check (transcribe the finished video; no gap over about 0.3s between words) and the b-roll segment check (every segment between edges, talking head or b-roll, is at least about 0.3s; no stray frames). Then hand it over with a short list of what each step left behind:

1. **A-roll processing:** the takes file and the cut list.
2. **B-roll processing:** the clips saved to the library, the shoot file, and the updated library index.
3. **B-roll selection:** the b-roll plan and the still-to-film list.
4. **Framing:** the framing plan.
5. **Headline:** the headline used, and the other two options.
6. **Captions:** the captions file.
7. **The finished video.**

A step with nothing to list was skipped: go back and run it before handing over. The one exception is b-roll processing when there was no raw b-roll; list it as "no raw b-roll this time".
