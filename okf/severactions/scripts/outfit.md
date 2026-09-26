---
type: Script
title: Outfit Scripts
description: Outfit actions, alias re-equip wiring and slot-system logging scripts.
resource: 'sources/SeverActions/00 Core/Source/Scripts'
tags: [scripts, papyrus, outfits, presets, slots]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Three scripts back the Outfit module: the action executor (registered via YAML), the alias that re-applies outfits on load/cell/enable events, and the slot-system helper with dual-destination logging. Persistence itself lives in the native outfit store — the v3.0 rebuild on a native cosave — while these scripts handle equip/unequip timing and animation events. Actions surface: [/actions/outfit.md](/actions/outfit.md).

# Member Files

| Script (.psc) | Compiled (.pex) | Role |
|---|---|---|
| SeverActions_Outfit.psc | SeverActions_Outfit.pex | Outfit management actions — dress/undress/equip/unequip/presets/situations; compatible with Immersive Equipping Animations |
| SeverActions_OutfitAlias.psc | SeverActions_OutfitAlias.pex | Events trigger re-equip on NPC load, cell change and enable; also holds the 60-second-cooldown bleedout recovery that restores half of base health |
| SeverActions_OutfitSlot.psc | SeverActions_OutfitSlot.pex | Slot-system singleton; logging helper writes to BOTH Papyrus.0.log and SeverActionsNative.log so traces appear even with Papyrus logging disabled |

# Notable Behaviour

- Outfit-excluded actors are skipped entirely (the per-follower outfit bypass toggle from v2.0.7).
- The alias restores a bleeding-out follower to half of base health once per cooldown — enough to stand up without trivializing combat.
- The re-equip infinite-loop guard (per-actor re-entry protection from v2.0.7) lives on the alias/event path; manual locks correctly suppress DefaultOutfit (v2.0.6).
- Preset persistence, rename and fuzzy matching are native (OutfitDataStore) — see [/systems/native-plugin.md](/systems/native-plugin.md).

# Citations

[1] `sources/SeverActions/00 Core/Source/Scripts/SeverActions_{Outfit,OutfitAlias,OutfitSlot}.psc`
[2] `sources/SeverActions/00 Core/Scripts/SeverActions_{Outfit,OutfitAlias,OutfitSlot}.pex`
