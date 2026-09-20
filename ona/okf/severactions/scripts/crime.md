---
type: Script
title: "Crime & Combat Scripts"
description: Bounty ledger, arrest dispatch, judgment, player confrontation, combat wiring, brawl and yield Papyrus scripts.
resource: 'sources/SeverActions/00 Core/Source/Scripts'
tags: [scripts, papyrus, arrest, bounty, crime, combat, brawl]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Seven scripts implement the crime-and-combat engine side: the bounty ledger, the arrest/dispatch/escort machinery, the judgment phase, the player-bounty confrontation state machine, real-combat wiring, the brawl system and the yield alias. Each ships as `.psc` plus compiled `.pex`. Guard discovery itself is native (GuardFinder). Surfaces: [/actions/arrest.md](/actions/arrest.md), [/actions/combat.md](/actions/combat.md), [/actions/brawl.md](/actions/brawl.md); state prompts: [/prompts/arrest.md](/prompts/arrest.md).

# Member Files

| Script (.psc) | Compiled (.pex) | Role |
|---|---|---|
| SeverActions_Arrest.psc | SeverActions_Arrest.pex | Arrest, dispatch, escort and pleas; faction properties filled in CK; vanilla crime factions |
| SeverActions_ArrestBounty.psc | SeverActions_ArrestBounty.pex | The bounty ledger; bounty-pay confirm popup bridge |
| SeverActions_ArrestJudgment.psc | SeverActions_ArrestJudgment.pex | Judgment phase state and lifecycle (OrderJailed / OrderRelease) |
| SeverActions_ArrestPlayer.psc | SeverActions_ArrestPlayer.pex | Player-bounty confrontation and persuasion FSM (ArrestPlayer, Accept/RejectPersuasion) |
| SeverActions_Brawl.psc | SeverActions_Brawl.pex | Fist-fight system: challenge wait states, weapon/spell stripping, forfeit handling |
| SeverActions_Combat.psc | SeverActions_Combat.pex | AttackTarget / CeaseFire / Yield execution; combat faction wiring |
| SeverActions_YieldAlias.psc | SeverActions_YieldAlias.pex | Alias wiring for the yield flow |

# Notable Behaviour

- **Guard factions are owned by native GuardFinder** (`Native/src/GuardFinder.h`); the Papyrus side keeps references and lifecycle only.
- **SeverActions_Combat** adds SeverActions_AttackFaction / SeverActions_TargetFaction to actors during AttackTarget so the AI Overhaul flee-suppression patch can suppress flee packages for NPCs in forced combat; they are removed when combat ends via RestoreOriginalValues. The vanilla follower faction is kept for reference only; the SkyrimNet follower faction is optional.
- **SeverActions_Brawl** keeps transient state for the player-target popup loop and a PrismaUI-overlay defer-retry: when a challenge is triggered from a PrismaUI menu, that menu still holds focus for a beat after closing, so the overlay open is suppressed and retried a few times (PrismaUI_OpenBrawlPrompt) rather than dropping to the SkyMessage box.
- **SeverActions_ArrestBounty** registers the bounty-pay confirm popup choice (PrismaUIBountyPromptBridge) on the load path — not OnInit — so existing saves also get the listener.
- **SeverActions_ArrestPlayer** owns the confrontation + persuasion FSM that the 0276 prompt and Accept/RejectPersuasion actions drive.
- The v2.1.7 confidence/aggression changes made here during PrepareForCombat were reverted in v2.5 and self-healed for old saves in v2.9.5 — see [/references/version-history.md](/references/version-history.md).

# Citations

[1] `sources/SeverActions/00 Core/Source/Scripts/SeverActions_{Arrest,ArrestBounty,ArrestJudgment,ArrestPlayer,Brawl,Combat,YieldAlias}.psc`
[2] `sources/SeverActions/00 Core/Scripts/SeverActions_{Arrest,ArrestBounty,ArrestJudgment,ArrestPlayer,Brawl,Combat,YieldAlias}.pex`
