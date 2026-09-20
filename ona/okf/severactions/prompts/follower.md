---
type: Prompt
title: Follower Prompts
description: Companion framework prompts — banter, ambient actions, off-screen life, relationships, quest awareness and companion bio context.
resource: 'sources/SeverActions/Prompts/Follower'
tags: [prompts, skyrimnet, followers, companions, banter, off-screen-life]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Follower prompt module (FOMOD option "Follower Prompts") is the LLM side of the companion framework: eight system-level prompts run as background LLM jobs (routed through the sever_background variant) — banter direction, ambient action direction, off-screen life simulation, relationship and quest assessments — while six character_bio submodules inject companion state, kidnap situations, conversation discipline and outfit context into dialogue. All 14 templates are listed below.

# Member Prompts

## System-level (background LLM calls)

| File | Lines | Purpose |
|---|---|---|
| sever_follower_banter.prompt | 199 | Banter director deciding whether two companions should spontaneously talk, and who speaks to whom |
| sever_ambient_banter.prompt | 204 | Ambient banter director for two nearby NON-follower NPCs (already filtered for combat/hostility/follower status) |
| sever_ambient_action_director.prompt | 93 | Decides whether ONE nearby non-follower NPC should spontaneously DO something right now |
| sever_action_adjudicator.prompt | 34 | Adjudicates whether an NPC's just-announced plan should actually proceed based on the short conversation it started |
| sever_offscreen_life.prompt | 285 | Internal life simulation for a dismissed companion living at their assigned home while the player is away |
| sever_quest_awareness.prompt | 64 | Writes a brief quest-awareness note for a companion; the New Objective field is a game mechanic, never quoted as spoken text |
| sever_relationship_assess.prompt | 126 | Analyzes recent events and outputs a JSON object for how a companion's feelings should change |
| sever_relationship_interfollower.prompt | 164 | Inter-companion assessment — how companions feel about EACH OTHER from recent interactions |

## character_bio submodules

| File | Lines | Purpose |
|---|---|---|
| 0175_severactions_follower.prompt | 95 | Follower framework — relationship, role and behavioral context |
| 0176_severactions_offscreen_life.prompt | 32 | What a dismissed follower did while the player was away |
| 0177_severactions_quest_awareness.prompt | 14 | What this follower knows about the player's quests |
| 0178_severactions_kidnap.prompt | 12 | Kidnap situation awareness for victim (seized/hooded) or kidnapper (on the job); empty for uninvolved actors |
| 0179_severactions_conversation_discipline.prompt | 25 | Group-conversation discipline fixing mis-addressing and speaker-ambiguity in multi-companion scenes |
| 0415_outfit_context.prompt | 13 | What the follower is wearing and their situation presets |

# Notes

- Background prompts (banter, off-screen life, relationship, quest awareness) route through the `sever_background` LLM variant declared in the SkyrimNet plugin manifest, so users can run them on a cheaper model than dialogue — see [/configs/plugin-wiring.md](/configs/plugin-wiring.md).
- Off-screen life summaries become memories the dismissed follower can tell you about when re-recruited (v1.8/2.0 lineage; the companion framework is documented in [/scripts/companions.md](/scripts/companions.md)).
- Companion actions themselves: [/actions/follower.md](/actions/follower.md).

# Citations

[1] `sources/SeverActions/Prompts/Follower/SKSE/Plugins/SkyrimNet/prompts/**`
