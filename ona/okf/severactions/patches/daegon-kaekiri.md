---
type: Patch
title: Daegon Kaekiri Patch
description: Script-only compatibility patch letting SeverActions manage Daegon Kaekiri's outfit against her mod's enforcement system.
resource: 'sources/SeverActions/Patches/Daegon Kaekiri'
tags: [patch, papyrus, outfit, daegon-kaekiri, followers]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Daegon Kaekiri (by Kukielle, Nexus 112097) ships a custom outfit enforcement system that forcibly re-equips her default outfit on every load and blocks unequips with `preventRemoval=True` — silently defeating SeverActions' Undress/Equip/Preset actions. This optional FOMOD patch ("Daegon Kaekiri Outfit Patch") replaces two of her scripts so the enforcement hooks back off when she is a tracked SeverActions follower. Pure Papyrus script override — no ESP, no new master. All 10 shipped files are listed below.

# Member Files

| File | Purpose |
|---|---|
| README.md | Patch documentation (root cause, fix, install, verification) |
| Scripts/k101PlayerAliasLoaderScript.pex | Replaced compiled script — Initialize() no longer re-equips the default outfit when Daegon is a SeverActions follower |
| Scripts/k101DaegonQuestAliasScript.pex | Replaced compiled script — OnItemRemoved/OnObjectUnequipped no longer force-restore outfit pieces |
| Source/Scripts/k101DaegonQuestAliasScript.psc | Modified source — carries the IsSeverActionsFollower() check and change notes |
| Source/Scripts/k101PlayerAliasLoaderScript.psc | Modified source — same runtime check on the player alias Initialize path |
| Source/Scripts/k101DaegonController.psc | Decompiled dependency, included to satisfy the compiler (unmodified) |
| Source/Scripts/k101DaegonCustomOutfitContainerScript.psc | Decompiled dependency (unmodified) |
| Source/Scripts/k101DaeHugScript.psc | Decompiled dependency (unmodified) |
| Source/Scripts/k101DaegonUtilityScript.psc | Decompiled dependency (unmodified) |
| Source/Scripts/ww42hugfollowerscript.psc | Compile-time stub for the "I'm Glad You're Here" hook — never deploy its .pex |

# Root Cause (per README)

| Script | Hook | Behaviour |
|---|---|---|
| k101PlayerAliasLoaderScript::Initialize() | OnPlayerLoadGame + OnInit | Calls EquipCustomOutfit() on every load — re-applies default clothes |
| k101DaegonQuestAliasScript::OnItemRemoved | Piece removed | Adds it back and re-equips with preventRemoval=True + notification |
| k101DaegonQuestAliasScript::OnObjectUnequipped | Piece unequipped | Re-equips immediately with preventRemoval=True |

The `preventRemoval=True` flag silently defeats UnequipItem — the engine holds the lock.

# Fix

Both replaced scripts call a helper `IsSeverActionsFollower()` that resolves **SeverActions_FollowerFaction (FormID 0x000EB708 in SeverActions.esp)** at runtime via `Game.GetFormFromFile(...)`:

- SeverActions not installed → lookup returns None, original behaviour unchanged.
- Daegon not a tracked SeverActions follower → same; her custom outfit system keeps working.
- Daegon tracked as a SeverActions follower → the three enforcement hooks back off and SeverActions owns her outfit.

No new master is required.

# Known Limitation — Brawls

The patch does NOT cleanly fix brawls against Daegon: her outfit enforcement re-equips her dagger faster than SeverActions can strip it, through a script path not yet understood. SeverActions instead auto-detects the re-equip war after 3 attempts and whitelists her dagger for that brawl — she fights with her dagger, but the brawl still resolves through DGIntimidateFaction bleedout routing ([/actions/brawl.md](/actions/brawl.md)).

# Installation & Verification

- Install AFTER Daegon Kaekiri (higher MO2 priority); file priority resolves the override, not plugin load order.
- In-game check: Undress strips all armor; save+reload keeps her undressed; no "part of Dae's custom outfit" notifications while SeverActions manipulates her equipment.
- Uninstall by deleting the two replaced `.pex` files — the originals take over on next load.

# Related

- Outfit machinery being unblocked: [/scripts/outfit.md](/scripts/outfit.md), [/actions/outfit.md](/actions/outfit.md)

# Citations

[1] `sources/SeverActions/Patches/Daegon Kaekiri/README.md`
[2] `sources/SeverActions/Patches/Daegon Kaekiri/**`
