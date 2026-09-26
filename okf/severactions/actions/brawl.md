---
type: Actions
title: Brawl Actions
description: Non-lethal fist-fight challenge, acceptance, refusal and forfeit actions of the Brawl module.
resource: 'sources/SeverActions/Actions/Brawl'
tags: [actions, skyrimnet, brawl, fists, non-lethal]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Brawl module (FOMOD option "Brawl Actions", recommended) implements ritual fist fights — challenge, accept, decline, forfeit — that end in yield or bleedout, never death. NPCs are routed through DGIntimidateFaction so brawl damage triggers bleedout instead of killing; weapons and spells are stripped for the duration and restored when the fight ends (with a v3.7.2 safety net for fights that end the wrong way). Brawls work against the player AND between any two NPCs (tavern brawls), with a non-pausing PrismaUI overlay for the player-target challenge popup. All execution functions live in SeverActions_Brawl ([/scripts/crime.md](/scripts/crime.md)).

The module ships 5 YAMLs — 4 executable actions plus the cat_brawl category file.

# Member Actions

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| acceptbrawl.yaml | AcceptBrawl | brawl | SeverActions_Brawl.AcceptBrawl_Execute | Answer a challenge or provocation with fists, starting the fight now |
| cat_brawl.yaml | Brawl | brawl | — | Category file grouping the non-lethal fight actions |
| challengebrawl.yaml | ChallengeBrawl | brawl | SeverActions_Brawl.ChallengeBrawl_Execute | Throw down the gauntlet and await the target's answer |
| declinebrawl.yaml | DeclineBrawl | brawl | SeverActions_Brawl.DeclineBrawl_Execute | Refuse a challenge without fighting |
| forfeitbrawl.yaml | ForfeitBrawl | brawl | SeverActions_Brawl.ForfeitBrawl_Execute | Yield and end an ongoing brawl the speaker is losing |

# Mechanics

- Fists only: weapons and spells are stripped for the duration; damage routes to bleedout via DGIntimidateFaction.
- Challenge/accept flows can be driven from dialogue (ChallengeBrawl sets a pending wait state) or from the PrismaUI Actions page; akChallenger may be omitted when a challenge is already pending.
- The brawl state prompt (0161) is composed entirely in C++ via the sever_brawl_state decorator — pending challenge, active fight, and recent-outcome memory contexts ([/prompts/situational.md](/prompts/situational.md)).
- The v3.9.9 overhaul fixed follower sparring (NFF release-and-rejoin), opponents refusing to stay unarmed, and forfeit handling; stripped-spell recovery was added in v3.7.2.

# Citations

[1] `sources/SeverActions/Actions/Brawl/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
[2] `fomod/ModuleConfig.xml` — Brawl Actions description
