# skyrim_ona — Ohne, one mind in five bodies

A Skyrim playthrough built on [SkyrimNet](sources/SkyrimNet-GamePlugin) — LLM-driven NPC conversation, memory and bios — plus [SeverActions](sources/SeverActions), its companion/action framework. One continuous mind divided itself into five folds to enter Skyrim: the player character and four recruited followers. This repository holds the design, the play-time artifact pack, and the injection manual that wires it all in.

## what the playthrough focuses on

- **One mind, five bodies** — the five are not a party of friends; they are folds of one awareness. Identity links render "one soul, N bodies", group conversation is the default scene, and a thought becomes the mind's by being said aloud.
- **Explore and grow, not finish** — quests are stories the world is telling, loot is ours without score-keeping, and uncertainty is the point of the door. Nothing here is the center of the story.
- **Ideas as the default register** — ruins, magic, customs and the bodies' own experiments are the conversation; events are doorways into ideas; people are observed, never scored.
- **Trust as structure** — inside the mind, suspicion has nowhere to land: events read as mechanisms, not malice. The pack actively counterworks the frameworks' built-in wariness.
- **A lite reputation requirement on the player** — relationship scores start warm, climb while the player plays in the mind's style, and erode only on sustained counter-style play ([stance doc](docs/severactions-relationship-stance.md)). Suspicion toward locals stays fully in play.
- **Two speech lanes, both defined** — Skyrim people talk like Skyrim people; Ohne talks like Ohne.

## glossary — terms coined in the writeups

| term | meaning |
| --- | --- |
| **Ona** | the origin — the place-that-was(-not-a-place) where the mind was whole; remembered as a feeling, not a location |
| **Ohne** | the mind — who the five are, here and now; also the name registered as the identity linking the bodies |
| **fold** | one body of the mind — not a person, a way of being the same one thing |
| **player-fold** | the fold the world leans on: quests, doors and oaths answer to the player character. Not a rank — the world's shape |
| **follower-fold** | one of the four folds recruited after the player-fold |
| **the five** | the whole mind in play: player-fold + four follower-folds |
| **the hum** | the constant feeling of being one — presence only: no words, no power, not a Shout; nearness deepens it, distance thins it, nothing silences it |
| **the crossing** | the split and fall into Skyrim — meant to be equal; the world gripped one fold |
| **the hinge** | that one inequality: the world leans on the player-fold while the five stay exactly equal inside the mind |
| **reaching** | the act that started everything — and, in play, the channels between folds: words, touch, aimed thought |
| **gist retelling** | how a fold repeats what another fold said — the sense of it, never a recording |
| **cover story** | "we're old friends, traveling around Skyrim" — the entire disclosure to locals; one-line answers, kept boring |
| **Omla** | the reserve village name for the cover story — volunteered only under pressure, then never changed |
| **lite reputation requirement** | the SeverActions tuning — warm floors, sticky highs, pressure on the player |

Mod-side terms (identity links, overlay layer, prewarm floors) are defined where they are used — see [docs/](docs/_overview.md) and the injection manual.

## what you do in SkyrimNet

Everything injectable lives in [`output entries/`](<output entries/_manual.md>) — and **[`output entries/_manual.md`](<output entries/_manual.md>) is the step-by-step injection manual**. The short version:

| when | what |
| --- | --- |
| first setup | paste the prompt overrides into the dashboard's prompt editor (overlay layer) · create the `ohne` NPC group + world-knowledge entries · register the virtual entity "Ohne" and verify the identity-link surface · inject the three shared memories into the player character |
| per recruitment ×4 | merge the fold profile over the follower's bio · inject four memories (three shared + one recruitment memory) · bond the new fold to every earlier fold · add it to the group · run the prewarm console batch (relationship floors) |

All follower/player names are tokens (`{player}`, `{fold1}`–`{fold4}`) filled at injection — the five bodies are chosen at play time, so the pack ships shareable. Core lore names (Ohne, Ona, Omla) are fixed. Surfaces that could not be verified from source are flagged ⚠ in the manuals, each with a live-verify list.

## repository map

| folder | what it is |
| --- | --- |
| [`writeups/`](writeups/_overview.md) | design source of truth — the lore spine and the voice set |
| [`docs/`](docs/_overview.md) | how the design maps onto SkyrimNet surfaces (identity links, overlay placement, SeverActions stance) |
| [`output entries/`](<output entries/_manual.md>) | the play-time artifact pack + injection manual |
| `okf/` | knowledge bundles for SkyrimNet and SeverActions — reference |
| `sources/` | vendored source snapshots of both mods, used to verify every prompt contract — reference only, not needed to play |

## requirements & status

- Skyrim (targeted at VR play) with **SkyrimNet** and **SeverActions** installed — the Follower module and "NPC Familiarity & Reputation" both enabled
- the SkyrimNet dashboard (`localhost:8080`) for injections, and an LLM configured for the model agents
- status: theory complete, play-testing pending — the manuals flag every unverified surface with ⚠
