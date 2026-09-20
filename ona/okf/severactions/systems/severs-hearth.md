---
type: System
title: "Sever's Hearth (bundled)"
description: Bundled camping mini-mod with its own ESP, native plugin, script, camp actions and camp prompt.
resource: 'sources/SeverActions/99 Sever''s Hearth'
tags: [hearth, camping, bundled, native, skse]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

**Sever's Hearth** is a self-contained camping mini-mod bundled with SeverActions (README module table: 3 actions — establish camp, break camp, travel back to it). It ships its own ESP, its own native SKSE plugin (universal SE/AE/VR like the main one), one quest script, a seq file, four SkyrimNet action YAMLs and one camp-context prompt. All 11 files are listed below.

# Member Files

| File | Purpose |
|---|---|
| 00 Core/SeversHearth.esp | The mini-mod plugin (47,432 bytes) |
| 00 Core/SKSE/Plugins/SeversHearthNative.dll | Compiled native plugin |
| 00 Core/SKSE/Plugins/SeversHearthNative.toml | Plugin registration |
| 00 Core/Source/Scripts/SeversHearth_Camp.psc | Camp quest script source |
| 00 Core/Scripts/SeversHearth_Camp.pex | Compiled camp script |
| 00 Core/seq/SeversHearth.seq | Scene/sequencer file |
| Actions/Camp/SKSE/Plugins/SkyrimNet/config/actions/EstablishCamp.yaml | Pitch a new camp — fire ring, bedroll, gear from the Camp Kit |
| Actions/Camp/SKSE/Plugins/SkyrimNet/config/actions/BreakCamp.yaml | Snuff the fire, pack tent and bedroll, stow gear |
| Actions/Camp/SKSE/Plugins/SkyrimNet/config/actions/GoToCamp.yaml | Walk back to the player's established camp |
| Actions/Camp/SKSE/Plugins/SkyrimNet/config/actions/cat_camp.yaml | Camping category file (action + 3 executable verbs) |
| Prompts/Camp/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0185_seversHearth_camp_context.prompt | Appends the camp summary to tracked followers' dialogue context while a camp is active |

# Registration (SeversHearthNative.toml)

| Key | Value |
|---|---|
| Name | SeversHearthNative |
| Author | Severause |
| Version | 0.1.0 |
| MinimumSKSEVersion | 131 |
| MinimumSkyrimVersion | 353 |
| AddressLibrary | true |

# Notable Behaviour

- SeversHearth_Camp wires follower sandboxing via a user-provided Package record applied with PapyrusUtil's ActorUtil (sandbox-around-actor pattern).
- The cat_camp description tells the AI to prefer the camping category over generic travel whenever the destination is the camp.
- The camp prompt (0185) renders nothing unless a camp is active and the actor is a tracked follower.
- Ships on VR too — both native plugins were multi-targeted in v3.0.1 ([/references/version-history.md](/references/version-history.md)).

# Citations

[1] `sources/SeverActions/99 Sever's Hearth/**`
