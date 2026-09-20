---
type: Script
title: Companion Scripts
description: Follow pool, follower lifecycle manager, survival needs and eating-animation Papyrus scripts.
resource: 'sources/SeverActions/00 Core/Source/Scripts'
tags: [scripts, papyrus, followers, companions, survival, follow]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Four scripts implement the companion framework's engine side: the follow alias pool, the follower lifecycle manager behind the companion actions, the survival needs system (hunger, cold, fatigue), and an optional eating-animation helper. Each ships as `.psc` plus compiled `.pex`. The LLM side of the same framework is documented in [/prompts/follower.md](/prompts/follower.md); the actions in [/actions/follower.md](/actions/follower.md).

# Member Files

| Script (.psc) | Compiled (.pex) | Role |
|---|---|---|
| SeverActions_Follow.psc | SeverActions_Follow.pex | Casual follow verbs and follow distance; rides the follow quest alias pool |
| SeverActions_FollowerManager.psc | SeverActions_FollowerManager.pex | Companion lifecycle: register/wait/resume/dismiss/leave, homes, combat styles; executes most Follower-module actions |
| SeverActions_Survival.psc | SeverActions_Survival.pex | Hunger, cold and fatigue tracking; settings adjustable via MCM |
| SeverActions_EatingAnimations.psc | SeverActions_EatingAnimations.pex | Helper playing eating animations from TaberuAnimation.esp (Eating Animations and Sounds); optional, gracefully skips if absent |

# Notable Behaviour

- SeverActions_Follow implements the **200-alias follow pool (FLWD v18)**: one mechanism replaces the legacy 21-slot + PO3-override-overflow dual system — every follower rides an alias in SeverActions_FollowQuest whose CK packages (Close above V2) re-apply NATIVELY on cell load, closing the documented hole where PO3 overrides dropped on 3D unload.
- FollowerManager syncs **healer combat-style configuration** (per-target/per-healer cooldowns, magicka gating, healChance) and **cell-catchup configuration** to the native HealerPoll and CellCatchup subsystems — see [/systems/native-plugin.md](/systems/native-plugin.md).
- Survival warmth degrades gracefully on VR, falling back to armor-record warmth where the SE/AE engine API is unavailable (v3.0.1).
- EatingAnimations checks keywords distributed at runtime by Keyword Item Distributor (KID); the mod is an optional dependency.
- FollowerLeaves (companion quits for good) and the kidnap verbs execute here via FollowerManager — [/actions/kidnap.md](/actions/kidnap.md).

# Citations

[1] `sources/SeverActions/00 Core/Source/Scripts/SeverActions_{Follow,FollowerManager,Survival,EatingAnimations}.psc`
[2] `sources/SeverActions/00 Core/Scripts/SeverActions_{Follow,FollowerManager,Survival,EatingAnimations}.pex`
