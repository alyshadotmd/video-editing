---
name: post-preview
description: Exact safe zones for 9:16 vertical video and images on Instagram Reels, Stories and Feed, TikTok For You, and Facebook Feed and Reels, measured from real iPhone screenshots. Use when placing text, captions, headlines, stickers, logos or key visuals in a 9:16 (1080x1920) video or static, when checking whether an ad's text will be covered by app buttons, or when someone asks "is this in the safe zone?". Triggers: "safe zone", "will this get covered", "where do I put text on reels", "tiktok safe area", "story safe zone", "9:16 text placement".
---

# Post Preview: 9:16 safe zones

Made by @alysha.md with Runneth. See it visually at https://www.alyshadotmd.com/post-preview

Every number here comes from iPhone screenshots
(1290 x 2796 px = 430 x 932 pt at 3x) of the real apps in October 2026. Positions are
given in **video pixels on a 1080 x 1920 frame**, so you can check a design directly.
Phone-point measurements follow for anyone rebuilding the mockups.

## The one box that's safe everywhere

Keep text, faces and key visuals inside **x 100 to 880, y 290 to 1340**.

- That clears the top bar on every placement, the right-side buttons on Reels and
  TikTok, the bottom name/caption block on Reels and TikTok, and the 4:5 crop on the
  Instagram feed.
- For ads, keep it above **y 1340**: Reels ad buttons start at y 1347, and Story ad
  buttons on videos start around y 1543.

Then check the placement-specific details below when a design runs close to an edge.

## How to check a design

1. Take the frames that matter: the hook, every on-screen headline, every caption
   frame, the end card.
2. Compare each element's box against the covered areas for each placement it will run on.
3. An element is safe when its whole box sits inside the visible area and outside
   every covered area. Report anything that touches a covered area with the
   placement name and the overlap in pixels.
4. Faces and products should stay fully visible too; the app's text sits on top of them.

## Instagram Reels (full screen)

The video fills the 430 x 932 pt screen, so the sides are trimmed.

- **Visible:** x 97 to 983 (about 97 px is cut off each side), full height.
- **Top bar** ("Reels / Friends", camera): down to y ~206.
- **Right buttons** (heart, comment, repost, share, save, menu): x 886 and right, from y ~870 down. On ads they start lower, from y ~1004.
- **Bottom block** (profile photo, name, Follow, caption, "Followed by" line):
  - Organic: from y ~1469.
  - Ads with a button: from y ~1347. The button sits about 51 pt above the profile photo.
- **Progress bar and menu:** from y ~1714 to the bottom.

## Instagram Stories

The video sits in a card from 59 to 823 pt (430 x 764 pt), almost exactly 9:16, so nothing is trimmed.

- **Top:** progress bar and profile row down to y ~129. A Reel shared to a Story adds a
  "Watch full reel" line and the Reel's name, so its top reaches y ~224.
- **Ad button** (one wide pill, centred, 48 pt tall). Where it starts depends on the media:

  | Media | With "Followed by" line | Without |
  |---|---|---|
  | Video | y 1595 | y 1543 |
  | Photo | y 1649 | y 1770 |

- **"Followed by" line:** from y ~1852.
- **Below the card** (Send message box, heart, share or "Ad"): outside the video, so
  it covers nothing.

## Instagram Feed

The feed shows the video at 430 x 692 pt, which is 4:5, so the top and bottom are cut off.

- **Visible:** y 91 to 1829 (about 91 px is cut off top and bottom), full width.
- **Covered:** nothing. The name, likes and caption sit above and below the video, not on it.
- Treat y 91 to 1829 as the feed's frame. A headline above y 91 or below y 1829 is invisible in the feed.

## TikTok For You

The video fills the area above the black menu bar (430 x 848.7 pt), so the sides are trimmed.

- **Visible:** x 54 to 1026 (about 54 px is cut off each side), full height.
- **Top tabs** ("Following", "For You", search): down to y ~228.
- **Right buttons** (profile photo, heart, comment, save, share, sound disc): x 907 and right, from y ~1020 down.
- **Bottom-left block** (name, caption, labels): x 81 to 790. It stacks up from the bottom, so its top depends on the post:
  - Organic, 1-line caption: from y ~1795.
  - Organic, 2-line caption: from y ~1755.
  - Ad with "Ad" label, button bar and 2-line caption: from y ~1597.
- **Ad button bar:** x 81 to 790, y 1812 to 1893.

## Facebook Feed

Facebook crops a 9:16 video differently for ads and organic posts.

- **Ads** (paid partnerships included): shown as **2:3**. Visible y 150 to 1770 (150 px cut off top and bottom), full width.
- **Organic posts:** shown as **4:5**. Visible y 285 to 1635 (285 px cut off top and bottom), full width.
- **On the video:**
  - Mute button, bottom right: x 968 to 1041, about 70 px up from the visible bottom edge.
  - Partnership ads only: an "About this partnership" pill, top right, x 643 to 1042, about 28 to 90 px below the visible top.
- The name, caption, headline strip and button all sit outside the video, so they cover nothing.

## Facebook Reels

The video fills 430 x 854 pt above a black "Add a comment" bar, so the sides are trimmed.

- **Visible:** x 57 to 1023 (about 57 px is cut off each side). The bottom 2 px is covered by the progress bar on organic posts.
- **Top icons** (back, search, more): down to y ~217.
- **Right buttons** (like, comment, share, save, more): x 930 and right.
  - Organic posts start at y ~1196.
  - Ads start at y ~1399.
- **Bottom-left block:**
  - Organic (name, Follow button, caption): from y ~1740.
  - Ads (name, caption, full-width button, "Ad" label): from y ~1540, or ~1498 for a paid partnership with its extra line.
  - Ad button: x 86 to 898, y 1713 to 1806.

## Phone-point measurements (430 x 932 pt screen)

For rebuilding the mockups. A 1080 x 1920 video is scaled to cover each area: Reels
0.4854 pt/px, TikTok 0.4420, Stories and Feed 0.3981.

### Instagram Reels
- Header "Reels" at y 85.
- Rail icons centred at x 399. Menu at y 798.8 for organic or partnership posts, 764.2 for ads, with "Ad" at 805.
  - Organic offsets from the menu: save −69.6, share −142.1, repost −219.8, comment −290, heart −360.6.
  - Ad offsets: share −69, repost −118, comment −190.8, heart −261.9. Ads have no save.
- Bottom block: "Followed by" line 805.5, caption 775, profile photo centre 735 (37.5 pt photo inside a 44 pt story ring at x 38). Name at x 68.5. Follow is centred on the photo.
- Ad buttons, with centres measured up from the photo centre:
  - Small bubble: 31 pt tall, radius 10, centre −49.5.
  - With preview: 46.7 pt tall, 32 pt picture, radius 13, centre −58.3.
  - Big bar: x 16 to 362.7, 47.6 pt tall, radius 10, centre −57.5.
- Progress bar at y 832.

### Instagram Stories
- Background #0C0F14. Card 0 to 430 x 59 to 823, corners 7.7.
- Progress bar y 67, x 8 to 422, 2 pt tall.
- Profile photo 31.3 pt at (12.3, 77.3). Name x 56.7, centred y 93.3, 14.5 pt bold.
- Ad button centred x 215, 48.3 pt tall, corners 11, 26 pt text. Centre y (screen):

  | Media | With "Followed by" | Without |
  |---|---|---|
  | Video | 718.2 | 697.2 |
  | Photo | 739.7 | 787.7 |

- "Followed by" line centred y 804.
- Send message box 16 to 294.3 x 844.3 to 887.7 on ads, or 16 to 329.7 on organic posts.
- Button icons:
  - Link icon: slides up a website.
  - Box with arrow: opens an app.
  - Paper plane: opens a message.

### Instagram Feed
- Video top 61, 430 x 692.
- Header avatar 32 pt at (10.7, 11.7) above the video. Name 15 pt semibold at x 52.3.
- Below the video: action row +24, "Liked by" +58, caption +80, time +101.
- Floating menu 323 x 49 at y 856.
- Caption rule: if it fits in 2 lines, show it all. Otherwise show 1 line, then "... more".

### TikTok For You
- Video area 0 to 848.7. Black menu 848.7 to 932: Home 43, Friends 128.7, + 215, Inbox 301, Profile 387.
- Tabs centred y 80.5, ending at x 361 (For You). Underline y 99.3, 23.3 pt wide. Search 391.7 to 409.7.
- Right rail centred x 399.7:
  - Profile photo 44.7 pt at y 450.7, with a red + (#E94359, 21.7 pt) centred on its bottom edge when not following.
  - Heart 544.3, comment 609.7, save 675.3, share 741.7. Counts sit 24 pt below each icon.
  - Sound disc 795.3 to 834.6.
- Left block x 12.3 to 325.7, stacking up from the bottom:
  - Last label line 831, or 785 when the ad bar shows. Labels 23.5 apart.
  - Last caption line 24 above the first label.
  - Caption lines 17.5 apart, 15 pt.
  - Name 28.5 above the first caption line, or 24 on paid partnership posts. 16.5 pt bold.
- Ad bar x 12.3 to 325.7, y 801 to 836.7, corners 8, 15 pt semibold text.
- Caption rule: organic shows up to 2 lines, then "... more". Ads show 2 lines only if the whole caption fits, otherwise 1 line, then "... more".

### Facebook Feed
- Posts are separated by 2 pt grey lines.
- Post header, measured from the line above it (T):
  - Avatar 40 pt at x 12, top T+12. Partnership posts give the avatar a blue ring.
  - Name 16 pt semibold at x 60.3, centred T+24.3. Partnerships read "a and b".
  - Sub line 13 pt grey, centred T+41: "Ad · 🌐" on ads, or "2h · 🌐" on organic posts.
  - Dots x 356 to 372 and X x 400.7 to 415.3, both centred T+22.
- Caption 15.5 pt, lines centred T+69.7 and T+86.4.
- Video top (V) is T+86 with a 1-line caption, or T+104 with 2 lines.
- Video height: 644.7 pt on ads (2:3), 537.5 pt on organic posts (4:5).
- Below the video, measured from its bottom (B):
  - Ads:
    - Headline strip B to B+48, background #F8F9FB.
    - Headline 15 pt at x 13.3.
    - Button: right edge 12 pt from the screen edge, B+8 to B+40, corners 8, colour #0866FF, 15 pt semibold.
    - Like / Comment / Share row centred B+70. Next divider B+92.
  - Organic: like / comment / share row with counts, centred B+22. Next divider B+44.
- Mute button: 29 pt, centre x 400, centre B−28.
- "About this partnership" pill: right edge 14.7 pt from the screen edge, V+11 to V+36.
- Caption rule: show the first paragraph if it fits in 2 lines, ending in "... See more" when more text follows. Otherwise show 1 line, cut mid-word, then "... See more".

### Facebook Reels
- Video 0 to 854. "Add a comment" bar x 13.3 to 416.7, y 866 to 910, colour #191919, corners 22.
- Top icons centred y 85: back x 18.7 to 28, search x 345 to 367, more x 388.7 to 411.3.
- Rail centred x 402. Each count sits 27 pt below its icon.
  - Organic: like 545.7, comment 618.3, share 690.7 (all with counts), save 764.7, dots 816.
  - Ads: like 635.7 (with count), comment 710, share 768.7, dots 820.
- Avatar 36 pt at x 13, centred on the name row. Name 15.5 pt semibold at x 57.3, followed by the white verified badge and a globe.
- Organic:
  - Outlined Follow button 24 pt tall, about 10 pt after the name.
  - Name 792, caption 829.
  - Progress bar 852 to 853.6.
- Ads:
  - Name 703, caption 740.8.
  - Partnerships add a grey "Paid partnership" line at 718.5 and move the name to 684.3.
  - Button bar x 13 to 374, y 762 to 803.3, see-through white, corners 10.
  - "Ad" pill x 12 to 60, y 820 to 841.3.
- Caption rule: 1 line, then "... more".
