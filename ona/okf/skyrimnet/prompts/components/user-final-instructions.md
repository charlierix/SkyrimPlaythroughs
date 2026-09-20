---
type: Prompt Template
title: "User Final Instructions Submodule"
description: "Ten sections appended before each response (environmental awareness, telepathy reception, combat status, response format, audio tags, embedded actions, narration, state changes)."
resource: "sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/submodules/user_final_instructions"
tags: [skyrimnet, prompts, inja]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Ten numbered sections appended before every response: environmental awareness, telepathy reception, combat status, response format, audio tags, extra instructions, quest dialogue, embedded actions, direct narration and recent state changes.

# Member files

All 10 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0150_environmental_awareness.prompt` | 106.0B | 3 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" %} |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0160_telepathy_reception.prompt` | 883.0B | 11 | {% if triggeringEvent and triggeringEvent.type == "dialogue_player_telepathy" and exists("npc") and existsIn(npc, "UUID" |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0200_combat_status.prompt` | 4.1KB | 49 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" %} |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0500_response_format.prompt` | 14.3KB | 114 | Response Format |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0650_audio_tags.prompt` | 7.0KB | 118 | {% set actor_tags_enabled = is_audio_tags_enabled(npc.UUID) %} |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0700_extra_instructions.prompt` | 179.0B | 3 | {% if not is_narration_enabled() %} |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0740_quest_dialogue.prompt` | 801.0B | 15 | {% if feature_enabled("quest_actions") %} |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0750_embedded_actions.prompt` | 1.6KB | 23 | {% if embed_actions_in_dialogue and eligible_actions and length(eligible_actions) > 0 %} |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/0800_direct_narration.prompt` | 238.0B | 3 | {% if triggeringEvent and triggeringEvent.type == "direct_narration" %} |
| `plugins/skyrimnet/base/prompts/submodules/user_final_instructions/8000_recent_state_changes.prompt` | 4.1KB | 124 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" %} |

# Citations

[1] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/submodules/user_final_instructions`

