---
type: Prompt
title: Familiarity Prompts
description: Familiarity, reputation, intimacy stance and consent prompts of the Familiarity module.
resource: 'sources/SeverActions/Prompts/Familiarity'
tags: [prompts, skyrimnet, familiarity, reputation, memory]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Familiarity prompt module (FOMOD option "NPC Familiarity & Reputation", recommended) controls what NPCs know about the player: personal familiarity tiers built from actual dialogue history, name awareness (NPCs only use your name once they have heard it), guild and quest reputation spread by social role, and — when an adult framework is present — a consent-aware intimacy stance. Two character_bio submodules render knowledge into bios; two system prompts are internal assessment calls that write stance/impression state. All four are listed below.

# Member Prompts

| File | Lines | Purpose |
|---|---|---|
| submodules/character_bio/0045_severactions_familiarity.prompt | 276 | What this NPC knows about the player — familiarity tier + interactions + lastSeenDaysAgo plus the LLM-generated per-NPC blurb regenerated on first dialogue and every 100 lines |
| submodules/character_bio/0046_severactions_intimacy_consent.prompt | 58 | How open this NPC is to the player's advances — dialogue- and event-driven stance from sever_intimacy_stance (IntimacyStanceStore) |
| sever_intimacy_assess.prompt | 68 | Internal stance-assessment system deciding how open ONE NPC currently is to intimacy, based only on what actually happened |
| sever_reputation_assess.prompt | 134 | Internal impression-assessment producing a brief inner monologue of how an NPC perceives a person |

# Notes

- The v2.2 rewrite merged the old separate familiarity and reputation prompts into one What-You-Know block; v3.9.13 added the manual blurb update button and stopped showing raw interaction tallies to the LLM.
- Intimate history (encounter counts, consensuality) integrates with SexLab/OStim when installed; nothing explicit is stored.
- Assessment calls are background prompts (sever_background variant) — see [/configs/plugin-wiring.md](/configs/plugin-wiring.md).

# Citations

[1] `sources/SeverActions/Prompts/Familiarity/SKSE/Plugins/SkyrimNet/prompts/**`
