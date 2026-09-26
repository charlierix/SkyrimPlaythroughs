---
type: Actions
title: Combat Actions
description: Lethal attack, ceasefire, yield and outlaw-standoff actions of the Combat module.
resource: 'sources/SeverActions/Actions/Combat'
tags: [actions, skyrimnet, combat, outlaws, truce]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Combat module (FOMOD option "Combat Actions", recommended) covers real fights — attack, stand down, surrender — plus the v3.9 outlaw-standoff verbs that give a pacified camp's challenger a verdict in dialogue. Execution functions live in SeverActions_Combat; the truce layer itself is native and its history sits in [/references/version-history.md](/references/version-history.md) (v3.9.0/v3.9.2).

The module ships 6 YAMLs — 5 executable actions plus the cat_combat category file.

# Member Actions

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| attacktarget.yaml | AttackTarget | combat | SeverActions_Combat.AttackTarget_Execute | Attack with weapons and start a real fight — lethal intent |
| cat_combat.yaml | Combat | combat | — | Category file grouping attack, surrender and ceasefire actions |
| ceasefighting.yaml | CeaseFighting | combat | SeverActions_Combat.CeaseFire_Execute | Call a truce in an ongoing fight; both combatants stand down |
| letthempass.yaml | LetThemPass | — | SeverActions_Combat.LetThemPass_Execute | The challenger is satisfied with the player's answer and waves them through the camp for this visit |
| runthemoff.yaml | RunThemOff | — | SeverActions_Combat.RunThemOff_Execute | Reject the stranger's answer and attack; the whole camp joins the fight |
| yield.yaml | Yield | combat | SeverActions_Combat.Yield_Execute | Surrender a losing real fight and hope for mercy |

# Eligibility Notes

- AttackTarget vs ChallengeBrawl: lethal intent vs non-lethal fists. The v2.1.7 aggression side effects were reverted in v2.5 and self-healed in v2.9.5.
- LetThemPass / RunThemOff fire only for the one outlaw who walked over to question the player (camp_challenge_pending) — see the camp challenge prompt [/prompts/core.md](/prompts/core.md).
- The AIO flee-suppression interplay (SeverActions_AttackFaction / SeverActions_TargetFaction added during AttackTarget) lives in SeverActions_Combat and the AI Overhaul patch ([/patches/ai-overhaul.md](/patches/ai-overhaul.md)).

# Citations

[1] `sources/SeverActions/Actions/Combat/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
