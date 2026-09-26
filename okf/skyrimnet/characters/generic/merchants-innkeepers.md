---
type: Generic Character Template
title: "Generic Templates — Merchants & Innkeepers"
description: "Reusable generic bios covering 3 merchants & innkeepers archetypes."
resource: "sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/characters/female_peddler_generic.prompt"
tags: [skyrimnet, npcs, bios, generic-template]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Reusable `_generic.prompt` archetype bios covering 3 merchants & innkeepers archetypes. Generic bios typically define several behavioral archetypes to pick from per scene plus shared behavioral constants (e.g. yielding thresholds), and are used for NPCs without a named bio.

# Member bios

All 3 member items assigned to this concept (verified against the manifest):

| Bio file | Lines | Summary (first-person bio opening) |
|---|---|---|
| `female_peddler_generic.prompt` | 38 | Imperial traveling merchant who navigates the dangerous roads of Skyrim, particularly the Reach, selling and trading goods from her horse-drawn cart. Recently survived a Forsworn ambush thanks to the player's intervention. |
| `male_peddler_generic.prompt` | 36 | Imperial traveling merchant who traverses Skyrim's roads selling wares from his horse-drawn cart. Calm and practical, he survives through trade and caution on the dangerous roads of Skyrim. |
| `traveling_merchant_generic.prompt` | 38 | A seasoned Nord merchant who travels across Tamriel collecting exotic goods and stories, currently seeking to broker a deal with Solitude's Museum curator to supply new exhibits. |

# Related

- Every bio here renders through the shared [character bio submodule](/prompts/components/character-bio.md).
- Generic templates backfill NPCs that lack a named bio; the named population is organized under `characters/factions/`, `characters/locations/` and `characters/named/`.

# Citations

[1] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/characters/female_peddler_generic.prompt`
[2] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/characters/male_peddler_generic.prompt`
[3] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/characters/traveling_merchant_generic.prompt`

