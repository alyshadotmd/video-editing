# B-roll library

Every b-roll video gets tagged here once, so any shot can be found later by what's in it ("grab unboxing b-roll") without rewatching footage. The `broll-processing` skill fills this in; the `broll-selection` skill searches it.

- `shoots/<date>-<brand>.md`: one file per shoot, listing every kept clip with its tags, what happens and why it was picked.
- Only the picked moments are kept, cut with 1 second of buffer on each side. The original full videos are deleted once the picks are cut.
- Lifestyle clips (no product in them) are reusable for any brand. Product clips belong to their brand.

## Tags

Tags describe only what you can see in the clip. Anyone tagging the same clip would pick the same tags, without knowing the brand or the script. Tag what stands out in the clip, not every detail: a tag earns its place when someone would search for that shot. Start with these and add your own the same way.

| Tag | Means |
|---|---|
| movement | Something moves: head turn, hand gesture, posture change |
| expression:<what> | A visible face or body action: yawn, sigh, smile, laugh, frown, head-in-hands |
| pet | An animal in the shot (say if it moves) |
| sleeping | Lying down, napping, asleep |
| unboxing | Opening, ripping, showing what's inside, pulling one out |
| packaging-full | The whole package clearly in view |
| closeup:<what> | Something fills most of the frame, close to the lens: closeup:product, closeup:glass, closeup:hands |
| packaging-back | Back label or ingredients |
| pointing | Pointing at something on the product |
| product-in-hand | Holding the product |
| product-in-use | Drinking, eating, taking, applying, mixing, pouring |
| happy-with-product | Creator smiling with the product |
| static | Little or no movement (reads like a photo) |
| setting:<where> | Where it happens: setting:kitchen, setting:bedroom, setting:car, setting:desk, setting:outside |
| hands-only | Only hands in the shot, no face |
| selfie | Someone taking a selfie, alone or with something (the product, a pet, a friend) |
| asmr:<sound> | A clear real sound worth hearing: asmr:pour, asmr:crinkle, asmr:fizz, asmr:can-open |
| time:<when> / weather:<what> | Only when it's central to the clip: time:night, time:sunrise, weather:rain, weather:snow, weather:sunny |

## Find by tag

Each row lists every kept clip with that tag, and the shoot file it's in. Example:

| Tag | Clips |
|---|---|
| unboxing | `v4-4-unbox-tear-top` (shoots/<date>-<brand>.md) |
