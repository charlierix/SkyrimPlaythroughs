---
type: Actions
title: Furniture Actions
description: Sitting, lying and getting up from furniture of the Furniture module.
resource: 'sources/SeverActions/Actions/Furniture'
tags: [actions, skyrimnet, furniture, sit, sleep]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Furniture module (FOMOD option "Furniture Actions", recommended) lets NPCs use the world's furniture — chairs, benches, beds, shrines and crafting stations — with automatic cleanup handled by the native FurnitureManager. Both actions execute in SeverActions_Furniture ([/scripts/companions.md](/scripts/companions.md)); the FormID is picked from the nearby-objects list injected by the prompts.

The module ships 2 YAMLs, both executable (no category file).

# Member Actions

| File | Action | Script.Function | Purpose |
|---|---|---|---|---|
| sitorlaydown.yaml | SitOrLayDown | SeverActions_Furniture.UseFurniture_Execute | Settle onto furniture — chair, bench, bed or shrine — when they say they want to sit, rest, sleep or pray |
| stopusingfurniture.yaml | StopUsingFurniture | SeverActions_Furniture.StopUsingFurniture_Execute | Get up from furniture they are using — push back from the chair, roll off the bed |

# Eligibility Notes

- Both are cross-guarded: SitOrLayDown refuses if already using furniture, StopUsingFurniture only when currently sitting, lying or kneeling.
- Hotkey-driven furniture use (two-step pick NPC then pick furniture) lives in SeverActions_Hotkeys — [/scripts/core-system.md](/scripts/core-system.md).

# Citations

[1] `sources/SeverActions/Actions/Furniture/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
