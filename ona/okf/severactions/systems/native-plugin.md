---
type: System
title: Native SKSE Plugin
description: The compiled native C++ layer (SeverActionsNative) owning data, heavy scans and everything performance- or thread-sensitive.
resource: 'sources/SeverActions/00 Core/SKSE/Plugins/SeverActionsNative.dll'
tags: [native, skse, cpp, cosave, decorators, core]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The native plugin is the fourth architecture layer: ~135k lines of C++ (per the README) owning the data, the heavy scans and everything performance- or thread-sensitive, while Papyrus owns quest aliases and packages. State lives in the **SKSE co-save (~40 records)** rather than Papyrus properties, behind a shared store base giving every store the same save/load/revert contract plus an opt-in migration path for schema changes — updates land on existing saves without wiping anything. Since v3.0.1 the DLLs are universal SE/AE/VR binaries compiled against CommonLibVR.

The C++ sources are not in this repository; the shipped artifacts are the compiled DLL, its registration TOML, and three Papyrus-facing stub scripts that expose native functions to the script side.

# Member Files

| File | Kind | Role |
|---|---|---|
| 00 Core/SKSE/Plugins/SeverActionsNative.dll | binary | The compiled native plugin |
| 00 Core/SKSE/Plugins/SeverActionsNative.toml | config | SKSE plugin registration |
| Source/Scripts/SeverActionsNative.psc (+ .pex) | Papyrus stub | Plugin info + string utilities replacing character-by-character Papyrus loops with native implementations |
| Source/Scripts/SeverActionsNativeExt.psc (+ .pex) | Papyrus stub | Exposes HealerPoll and related subsystems |
| Source/Scripts/SeverActionsNativeExt2.psc (+ .pex) | Papyrus stub | Exposes Enterprises labor/economy, hold taxes and camp-takeover functions |

# Registration (SeverActionsNative.toml)

| Key | Value |
|---|---|
| Name | SeverActionsNative |
| Author | Severause |
| Version | 3.9.13 |
| MinimumSKSEVersion | 131 |
| MinimumSkyrimVersion | 353 |
| AddressLibrary | true |

# Native Subsystems Referenced Across the Bundle

Named in headers, prompts and scripts throughout the source:

| Subsystem | Used by |
|---|---|
| GuardFinder | arrest scripts own faction references; guard discovery is native |
| CraftingOrchestrator (kCraftTimeSeconds = 5) | SeverActions_Crafting keeps no timing in Papyrus |
| FurnitureManager | furniture cleanup event consumed by SeverActions_Furniture |
| BrawlManager | queried by the sever_brawl_state decorator behind the brawl prompt |
| TrespassMonitor | suppressed-trespass episodes rendered by the 0176 trespass prompt |
| CellCatchup | follower catch-up configuration synced from FollowerManager |
| HealerPoll | ~1s combat tick, priority chain player > self > ally, cooldowns + magicka + healChance, dispatches SeverActionsNative_HealerCast |
| TravelSpeed enum | mirrored as constants in SeverActions_Travel |
| OutfitDataStore | outfit presets, rename (case-insensitive), fuzzy name matching, lock enforcement |
| EmploymentRegistry | seeded by labor_curation.json |
| DataGatherer | reads settings via quest references passed by SeverActions_PrismaUI |
| IntimacyStanceStore | written by the intimacy assessment prompt, read via sever_intimacy_stance |
| Native_IsCellOwner | ownership gate in SeverActions_Property |

# Decorators (native, called from Jinja prompts)

sever_truce, sever_camp, sever_war_band, camp_challenge_pending, sever_brawl_state, custom_bio_blocks, retainer_status, enterprises_summary, npc_employer, npc_workforce, hold_tax_rate, is_tax_collector, is_guard_or_authority, debt_context, sever_intimacy_stance. All return "" for uninvolved actors so prompts cost nothing outside their situations.

# Notes

- SkyrimNet decorators must register AFTER SkyrimNet finishes standing up its own systems — registering earlier deadlocked VR startup (v3.0.1 fix).
- A VR-incompatible fast-travel event sink is guarded; the fast-travel event does not exist on VR.
- Kidnap, truce and captive state all persist through these co-save stores ([/actions/kidnap.md](/actions/kidnap.md), [/actions/combat.md](/actions/combat.md)).

# Citations

[1] `sources/SeverActions/00 Core/SKSE/Plugins/SeverActionsNative.dll` and `.toml`
[2] `sources/SeverActions/00 Core/Source/Scripts/SeverActionsNative{,Ext,Ext2}.psc`
[3] `sources/SeverActions/README.md` — Under the hood
