# writeups — overview

Seed docs for the playthrough. Two layers, one rule: one concept per file, cross-reference by pointer instead of restating.

- **The lore spine** — motivation, origin, the-five, the-hinge, names. What Ohne is, and why it is here.
- **The voice set** — failure-modes, speech-quality, topics, attribution, message-flow, cover-story. How Ohne speaks, and what the prompts must design against.

This folder is design guidance, not the prompts themselves. It directs the skyrimnet prompt-rewrite pass (bios, world definitions, behavior prompts) and the writing of pre-generated memories. By play time the essence of these docs is the default: skyrim people talk like skyrim people, Ohne talks like Ohne.

## doc map

| doc | question it answers |
| --- | --- |
| motivation.md | why be here at all — explore and grow, not finish |
| origin.md | where we came from — Ona, the reaching, the split into five |
| the-five.md | what we are — one mind, five folds; the hum; reaching |
| the-hinge.md | the one inequality — the world leans on the player-fold |
| names.md | Ona and Ohne — the origin and the mind |
| failure-modes.md | what to design against — the latch patterns |
| speech-quality.md | what the voice sounds like — qualities, registers, group talk |
| topics.md | what they talk about, and what they don't |
| attribution.md | how events get read — the negativity filter and the trust baseline |
| message-flow.md | how words move — group talk, memory seeding, gist retelling |
| cover-story.md | what locals are told — one line, kept boring |

## for the later pass

- skyrimnet's default prompts get overwritten category by category, with these docs as the source of truth for both lanes (locals and Ohne).
- pre-generated memories obey attribution.md — memories fossilize into opinions.
- memory seeding primitives: message-flow.md.
- SeverActions' relationship machinery: decided — Familiarity stays (locals-only by code, useful suspicion toward locals); the Follower module gets fold-gated overrides plus warm prewarm floors, and a lite reputation requirement on the player ([stance doc](../docs/severactions-relationship-stance.md), attribution.md).
- the cover story for locals: cover-story.md — one line, kept boring; bios and world definitions build on it.
