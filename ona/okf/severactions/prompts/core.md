---
type: Prompt
title: Core Prompts
description: Core context-injection templates covering state, spells, gold, inventory, surroundings, reading, truce and camp context, trespass, bio blocks and embedded actions.
resource: 'sources/SeverActions/Prompts/Core'
tags: [prompts, skyrimnet, jinja, character-bio, context, core]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Core prompt module (FOMOD option "Core Awareness Prompts", recommended, installed together with the Enterprises prompts) is the largest awareness surface: it tells the AI what the speaker and the player carry, know, and see, and renders the outlaw truce/camp layer that makes conversation with outlaws possible. Fifteen files live under `Prompts/Core/SKSE/Plugins/SkyrimNet/prompts/`; two more core-level templates ship under `00 Core/SKSE/Plugins/SkyrimNet/prompts/` (bio blocks and trespass). All are Jinja templates rendered into SkyrimNet's prompt stack; character_bio submodules must keep their render_mode gate within the first 5 lines (SkyrimNet's PromptEngine validator).

17 templates total; every one is listed below.

# Member Prompts

## Module tree — system-level prompts

| File | Lines | Purpose |
|---|---|---|
| sever_letter_writer.prompt | 40 | System prompt ghost-writing a single hand-written in-world letter (courier letters feature); renders the setting submodule and outputs ONLY a JSON object |

## Module tree — character_bio submodules

| File | Lines | Purpose |
|---|---|---|
| submodules/character_bio/0012_severactions_action_header.prompt | 22 | Renders "## {{ me.name }}'s Current State" (gender, race, …) in action render mode |
| submodules/character_bio/0035_severactions_knownspells.prompt | 47 | Known-spell list via get_spell_list, first-person render |
| submodules/character_bio/0085_severactions_gold.prompt | 7 | "## Gold" — the actor's carried gold |
| submodules/character_bio/0095_severactions_inventory.prompt | 20 | Actor inventory and worn equipment via get_inventory / get_worn_equipment |
| submodules/character_bio/0096_severactions_player_inventory.prompt | 77 | Player inventory for NPC eyes — categorized, top 15 per type, nameless items filtered |
| submodules/character_bio/0180_severactions_nearbyref.prompt | 69 | Nearby objects, flora and furniture for full/static render modes |
| submodules/character_bio/0181_severactions_nearbyref_action.prompt | 82 | Sibling of 0180 for action render mode |
| submodules/character_bio/0185_severactions_gossip.prompt | 20 | Local gossip — what has been happening around town |
| submodules/character_bio/0186_severactions_truce.prompt | 81 | Outlaw truce context via sever_truce; returns "" for everyone else so it costs nothing normally |
| submodules/character_bio/0187_severactions_camp.prompt | 44 | Camp leadership context via sever_camp — who leads this outlaw's camp and what that means for how they talk; leader-dead line conditional on actual state |
| submodules/character_bio/0188_severactions_war_band.prompt | 18 | The armed company at the player's back, shown to BYSTANDERS only via sever_war_band |
| submodules/character_bio/0189_severactions_camp_challenge.prompt | 25 | Shown ONLY to the one outlaw who walked over to question the player (camp_challenge_pending = "1" for exactly that actor) |
| submodules/character_bio/0280_severactions_readbook.prompt | 65 | Book-reading mode; per-actor title/text live in StorageUtil via papyrus_util, keeping book text out of the cosave |

## Module tree — user_final_instructions submodules

| File | Lines | Purpose |
|---|---|---|
| submodules/user_final_instructions/0750_embedded_actions.prompt | 19 | When actions are embedded in dialogue, lists eligible actions and mandates the output format: dialogue FIRST, then one action on a separate line |

## Core-level (00 Core/SKSE/Plugins/SkyrimNet/prompts/)

| File | Lines | Purpose |
|---|---|---|
| submodules/character_bio/0040_severactions_bio_blocks.prompt | 15 | Renders the custom_bio_blocks decorator — every user-authored Bio Blocks library block applied to this character as "### Title" sections (issue #425) |
| submodules/character_bio/0176_severactions_trespass.prompt | 14 | Injected while this actor has a live suppressed-trespass episode (native TrespassMonitor denied the vanilla warn-follow package and recorded them instead) — the v3.7.1 LLM-driven trespass flow |

# Conventions

- Decorators return "" for uninvolved actors, so most templates render nothing and cost no tokens outside their situations.
- The render_mode gate MUST stay on line 1 (before comments) — SkyrimNet scans only the first 5 lines of a character_bio submodule and requires both the literal 'render_mode' and a '{% if' there.
- Bio Blocks starter library data: [/configs/data-store.md](/configs/data-store.md). Trespass monitoring is native: [/systems/native-plugin.md](/systems/native-plugin.md).

# Citations

[1] `sources/SeverActions/Prompts/Core/SKSE/Plugins/SkyrimNet/prompts/**`
[2] `sources/SeverActions/00 Core/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0040_severactions_bio_blocks.prompt`
[3] `sources/SeverActions/00 Core/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0176_severactions_trespass.prompt`
