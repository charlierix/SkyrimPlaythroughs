---
type: Prompt
title: Arrest Prompts
description: Bounty, jail, persuasion, judgment, dispatch and escort state prompts of the Arrest module.
resource: 'sources/SeverActions/Prompts/Arrest'
tags: [prompts, skyrimnet, arrest, bounty, jail, dispatch]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Arrest prompt module (FOMOD option "Arrest Prompts") gives guards, prisoners and authorities their legal state. A base template (0275) covers normal-mode bounty awareness for any guard; the four 0276-0279 templates were extracted from it in the prompt-split refactor and handle the four active arrest flows — persuasion, judgment, cross-cell dispatch, and same-cell arrest in progress. One template (0165) adds jail-time awareness for imprisoned NPCs. All six are listed below.

# Member Prompts

| File | Lines | Purpose |
|---|---|---|
| 0165_severactions_jailed.prompt | 43 | Imprisonment awareness for jailed NPCs |
| 0275_severactions_bounty.prompt | 118 | Normal-mode bounty + debt awareness for any guard; fires only when no global active-arrest state exists |
| 0276_severactions_persuasion_active.prompt | 52 | Active bounty-persuasion confrontation; fires only on the confronting guard |
| 0277_severactions_judgment_active.prompt | 137 | Active judgment hold (Phase 6) with three sub-cases: presiding sender, dispatch guard, accused prisoner |
| 0278_severactions_dispatch_active.prompt | 173 | Active cross-cell dispatch (phases 1-5) for the dispatch guard and the prisoner during escort |
| 0279_severactions_arrest_in_progress.prompt | 126 | Same-cell arrest in progress — ArrestState 1=approach, 2=cuffing, 3=escort, 4=escort plea |

# Notes

- State semantics are documented in template comments: DispatchPhase (cross-cell) is distinct from ArrestState 1..4 (same-cell).
- These prompts pair with the arrest actions ([/actions/arrest.md](/actions/arrest.md)) and the crime scripts ([/scripts/crime.md](/scripts/crime.md)).
- Several were extracted from 0275 during the prompt-split refactor; each keeps the render_mode gate on line 1.

# Citations

[1] `sources/SeverActions/Prompts/Arrest/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/*.prompt`
