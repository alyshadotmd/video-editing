# Setup guide

You don't need to know anything technical to use these skills. The AI sets up its own tools.

## Using Runneth

Nothing to set up. Add the skill folders to your skills and start editing.

## Using Claude Code

1. **Get Claude Code.** Download it from [claude.com/claude-code](https://claude.com/claude-code) and sign in.
2. **Add the skills.** Download this repo (green **Code** button, then **Download ZIP**), unzip it, and tell Claude Code: "Add the skills in this folder to my skills." Keep the setup skill in there; it's the one that gets the tools ready.
3. **Let it set up its tools.** The first time you ask for an edit, Claude checks for a few free tools it needs: one that cuts video and one that turns speech into text. If any are missing, it asks: "Want me to set them up?" Say yes.
4. **Click Install if a box pops up.** On some Macs a box appears asking to install developer tools. Click **Install** and tell Claude when it's done.
5. **That's it.** Setup takes a few minutes, happens once, and doesn't change anything else on your computer.

## If something goes wrong

Tell Claude: "The video tools didn't install. Try again and tell me what you need from me." It will walk you through it one step at a time.

What it installs, if you're curious:

- **ffmpeg:** cuts clips, pulls the sound out of a video, and grabs still frames.
- **Python:** runs the small check that makes sure no word got chopped.
- **faster-whisper:** writes down every word you say, with the time you said it.
