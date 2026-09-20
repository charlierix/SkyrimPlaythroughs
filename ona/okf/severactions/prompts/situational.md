---
type: Prompt
title: Situational Prompts
description: Single-prompt modules covering brawl state, combat state, crafting commissions, group meetings and survival needs.
resource: 'sources/SeverActions/Prompts/Survival'
tags: [prompts, skyrimnet, combat, brawl, crafting, survival, group]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Five prompt modules ship exactly one template each, covering distinct situations: brawl awareness (composed entirely in C++ via the sever_brawl_state decorator), combat awareness, the workshop-commission capability for smiths, group-meeting participant awareness, and survival needs. Each pairs with the matching action module. All five templates are listed below.

# Member Prompts

| Module | File | Lines | Purpose |
|---|---|---|---|
| Brawl | 0161_severactions_brawl.prompt | 15 | Fist-fight state context; ALL composition happens in the C++ sever_brawl_state decorator (SkyrimNetBridge.h) querying BrawlManager |
| Combat | 0160_severactions_combat.prompt | 110 | Combat state context for NPC dialogue — lets NPCs respond appropriately during fights |
| Crafting | submodules/system_head/0152_crafting_commission.prompt | 26 | Deferred workshop commissions; GATED to JobBlacksmithFaction so only smiths see it; capability intro always shown to smiths |
| GroupMeeting | submodules/system_head/0260_severactions_engaged_participants.prompt | 84 | Gives an engaged party member the names of the rest of the active party so multi-companion conversations read naturally; SkyrimNet-native decorators only |
| Survival | 0170_severactions_survival.prompt | 43 | Hunger, cold/warmth and fatigue status for followers and nearby NPCs |

# Notes

- The brawl prompt is the purest example of the thin-template pattern: the Jinja file is 15 lines because the native decorator does the composition — see [/systems/native-plugin.md](/systems/native-plugin.md).
- The commission prompt pairs with CommissionItem/CollectCommission in [/actions/crafting.md](/actions/crafting.md); the survival prompt pairs with the survival script ([/scripts/companions.md](/scripts/companions.md)).

# Citations

[1] `sources/SeverActions/Prompts/Brawl/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0161_severactions_brawl.prompt`
[2] `sources/SeverActions/Prompts/Combat/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0160_severactions_combat.prompt`
[3] `sources/SeverActions/Prompts/Crafting/SKSE/Plugins/SkyrimNet/prompts/submodules/system_head/0152_crafting_commission.prompt`
[4] `sources/SeverActions/Prompts/GroupMeeting/SKSE/Plugins/SkyrimNet/prompts/submodules/system_head/0260_severactions_engaged_participants.prompt`
[5] `sources/SeverActions/Prompts/Survival/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0170_severactions_survival.prompt`
