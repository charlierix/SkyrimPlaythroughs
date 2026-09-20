---
type: Actions
title: Outfit Actions
description: Equip, unequip, outfit presets and situation outfits of the Outfit module, plus the misplaced worn-equipment prompt.
resource: 'sources/SeverActions/Actions/Outfit'
tags: [actions, skyrimnet, outfit, equipment, presets]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Outfit module (FOMOD option "Outfit Actions", recommended) covers clothing and gear: putting on and taking off named items, dressing and undressing, saving the current look as a named preset, re-applying presets, and standing situation rules that automatically switch outfits for town, adventure, home or sleep. All execution functions live in SeverActions_Outfit; persistence runs through the native outfit store.

The module ships 9 YAMLs — 8 executable actions plus the cat_outfit category file — and, unusually, also contains one misplaced prompt template inside its action tree.

# Member Actions

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| applyoutfitpreset.yaml | ApplyOutfitPreset | outfit | SeverActions_Outfit.ApplyOutfitPreset_Execute | Change into an outfit previously saved with SaveOutfitPreset |
| cat_outfit.yaml | Outfit | outfit | — | Category file grouping all clothing and gear actions |
| clearsituationoutfit.yaml | ClearSituationOutfit | outfit | SeverActions_Outfit.ClearSituationPreset_Execute | Drop the standing outfit rule for one situation |
| equipitems.yaml | EquipArmor | outfit | SeverActions_Outfit.EquipMultipleItems_Execute | Put on one or more named items from inventory (any gear, not just armor) |
| getdressed.yaml | GetDressed | outfit | SeverActions_Outfit.Dress_Execute | Put back on the clothes and armor removed earlier |
| saveoutfitpreset.yaml | SaveOutfitPreset | outfit | SeverActions_Outfit.SaveOutfitPreset_Execute | Save the current look under a short name for later recall |
| setsituationoutfit.yaml | SetSituationOutfit | outfit | SeverActions_Outfit.SetSituationPreset_Execute | Automatically change into a saved outfit whenever a situation begins |
| undress.yaml | Undress | outfit | SeverActions_Outfit.Undress_Execute | Take off all equipped armor and clothing |
| unequipitems.yaml | UnequipArmor | outfit | SeverActions_Outfit.UnequipMultipleItems_Execute | Take off specific worn pieces by name |

# Misplaced Prompt

| File | Content |
|---|---|
| SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0410_equipment.prompt | Jinja render of the speaker's worn equipment ("### Worn Equipment"), gated by render_mode including full/thoughts/transform/equipment/action. It sits inside the Outfit action tree rather than under Prompts/; SkyrimNet still picks it up by path convention. Accounted for in this concept because it ships here. |

# Related

- Presets, slots and situation switching mechanics: [/scripts/outfit.md](/scripts/outfit.md)
- Follower outfit context prompt (0415, in the Follower module): [/prompts/follower.md](/prompts/follower.md)

# Citations

[1] `sources/SeverActions/Actions/Outfit/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
[2] `sources/SeverActions/Actions/Outfit/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0410_equipment.prompt`
