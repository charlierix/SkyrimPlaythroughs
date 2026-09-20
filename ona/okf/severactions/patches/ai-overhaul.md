---
type: Patch
title: AI Overhaul Patch
description: Compatibility ESP patching AI Overhaul's flee packages for followers and forced combat.
resource: 'sources/SeverActions/Patches/AI Overhaul'
tags: [patch, ai-overhaul, combat, compatibility]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

AI Overhaul gives most civilian NPCs flee packages that trigger during any nearby combat, which makes recruited civilian followers run instead of fight and lets AttackTarget targets flee instead of fighting back. This optional FOMOD patch ("AI Overhaul Flee Patch") adds conditions to **all 7 AIO flee packages** so forced-combat participants hold their ground. 1 file is listed below.

# Member Files

| File | Purpose |
|---|---|
| AIO-SeverActions-Patch.esp | Conditions all 7 AI Overhaul flee packages |

# Behaviour

- **SeverActions followers are fully exempt** — they never flee.
- **NPCs in forced combat (AttackTarget) are exempt while fighting** — this interlocks with the SeverActions_AttackFaction / SeverActions_TargetFaction factions that SeverActions_Combat adds to attacker and target during AttackTarget and removes via RestoreOriginalValues when combat ends ([/scripts/crime.md](/scripts/crime.md)).
- All other NPCs keep their normal flee behaviour.
- Requires AI Overhaul SSE (any version); optional FOMOD pick installing at priority 2.

# History

- v2.5 rebuilt this patch against the user's actual AI Overhaul ESP after the first version was generated against a different AIO variant and carried two "ghost" override records — see [/references/version-history.md](/references/version-history.md).
- The v2.5 cowering regression hunt also reverted the 2.1.7 confidence/aggression changes made in PrepareForCombat, keeping only the faction add/remove logic this patch consumes.

# Citations

[1] `sources/SeverActions/Patches/AI Overhaul/AIO-SeverActions-Patch.esp`
[2] `fomod/ModuleConfig.xml` — AI Overhaul Flee Patch description
