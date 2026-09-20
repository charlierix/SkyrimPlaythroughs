---
type: Actions
title: Crafting Actions
description: Forge, alchemy, cookpot and deferred-commission actions of the Crafting module.
resource: 'sources/SeverActions/Actions/Crafting'
tags: [actions, skyrimnet, crafting, smithing, cooking, commissions]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Crafting module (FOMOD option "Crafting Actions", optional; installs together with the Crafting prompt) has NPCs walk to a workstation and work it: smithing and smelting at the forge, potions at an alchemy lab, meals at a cookpot or spit — with the finished piece handed to whoever asked. Smiths can also take deferred commissions that mature over a few in-game days, collected later with the remaining payment. All execution functions live in SeverActions_Crafting; timing constants live in the native CraftingOrchestrator (kCraftTimeSeconds = 5).

The module ships 6 YAMLs — 5 executable actions plus the cat_crafting category file.

# Member Actions

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| brewpotion.yaml | BrewPotion | crafting | SeverActions_Crafting.BrewPotion_Internal | Brew a potion at an alchemy lab and hand the finished bottle to someone |
| cat_crafting.yaml | Crafting | crafting | — | Category file grouping forge, lab, cookpot and commission actions |
| collectcommission.yaml | CollectCommission | crafting | SeverActions_Crafting.CollectCommission_Internal | Hand over a finished workshop commission the player has come back to collect, with the remaining payment |
| commissionitem.yaml | CommissionItem | crafting | SeverActions_Crafting.CommissionItem_Internal | Take a deferred order — ready in a few days, usually naming a timeframe and a deposit |
| cookmeal.yaml | CookMeal | crafting | SeverActions_Crafting.CookMeal_Internal | Cook food at a cookpot or spit and serve it to someone |
| craftitem.yaml | CraftItem | crafting | SeverActions_Crafting.CraftItem_Internal | Work the forge — hammer, tongs, quench — and hand over the finished piece on the spot |

# Eligibility Notes

- On-the-spot work is CraftItem / BrewPotion / CookMeal; deferred orders are CommissionItem then CollectCommission — the pairs are explicitly cross-guarded in their descriptions.
- CollectCommission only fires when the workshop-commissions context lists the order as finished — see the Crafting prompt [/prompts/situational.md](/prompts/situational.md).
- Crafting delivery and loot transfer scripts: [/scripts/economy-crafting.md](/scripts/economy-crafting.md).

# Citations

[1] `sources/SeverActions/Actions/Crafting/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
