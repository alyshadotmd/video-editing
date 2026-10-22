# B-roll library

Every b-roll video gets tagged here once, so any shot can be found later by what's in it ("grab unboxing b-roll") without rewatching footage. The `broll-processing` skill fills this in; the `broll-selection` skill searches it.

- `shoots/<shoot-date>-<brand>.md`: one file per shoot, listing every kept clip with its tags, what happens and why it was picked.
- Clips are named `<shoot-date>-v<video>-<pick>-<what-happens>.mp4`, so clips from different shoots never clash.
- Only the picked moments are kept, cut with 1 second of buffer on each side. The original full videos are deleted once the picks are cut.
- Lifestyle clips (no product in them) are reusable for any brand. Product clips belong to their brand.

## Tags

Tags describe only what you can see in the clip. Anyone tagging the same clip would pick the same tags, without knowing the brand or the script. Tag what stands out in the clip, not every detail: a tag earns its place when someone would search for that shot. Start with these and add your own the same way.

Every tag takes a detail after a colon, `tag:<what>`, saying what exactly is in the shot (`pet:cat`, `sleeping:couch`). Add the detail whenever it's visible and someone might search for it; leave it off when there's nothing specific to say. Searching a tag on its own (`pet`) finds every detail under it.

| Tag | Means | Example details |
|---|---|---|
| movement:<what> | Something moves | movement:head-turn, movement:posture-change, movement:hand-gesture |
| expression:<what> | A visible face or body action | expression:yawn, expression:sigh, expression:laugh, expression:head-in-hands |
| pet:<what> | An animal in the shot | pet:cat, pet:dog, pet:cat-walks-in |
| sleeping:<where> | Lying down, napping, asleep | sleeping:bed, sleeping:couch |
| unboxing:<what> | Opening a delivery or package | unboxing:box, unboxing:bag, unboxing:pull-one-out |
| packaging:<view> | The package clearly in view | packaging:front, packaging:back, packaging:ingredients |
| closeup:<what> | Something fills most of the frame, close to the lens | closeup:product, closeup:glass, closeup:hands |
| pointing:<at-what> | Pointing at something | pointing:ingredients, pointing:screen, pointing:label |
| product-in-hand:<how> | Holding the product | product-in-hand:next-to-face, product-in-hand:flip |
| product-in-use:<action> | Using the product | product-in-use:pour, product-in-use:mix, product-in-use:sip, product-in-use:apply |
| happy-with-product | Creator smiling with the product | |
| static | Little or no movement (reads like a photo); only kept as a short accent | |
| setting:<where> | Where it happens | setting:kitchen, setting:bedroom, setting:car, setting:desk, setting:outside |
| hands-only:<doing-what> | Only hands in the shot, no face | hands-only:mixing, hands-only:typing |
| selfie:<with-what> | Someone taking a selfie | selfie:product, selfie:pet, selfie:friend |
| asmr:<sound> | A clear real sound worth hearing | asmr:pour, asmr:crinkle, asmr:fizz, asmr:can-open |
| time:<when> / weather:<what> | Only when it's central to the clip | time:night, time:sunrise, weather:rain, weather:snow |

## Find by tag

Each row lists every kept clip with that tag, and the shoot file it's in. Example:

| Tag | Clips |
|---|---|
| unboxing:box | `<shoot-date>-v4-4-unbox-tear-top` (shoots/<shoot-date>-<brand>.md) |
