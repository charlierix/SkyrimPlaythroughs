---
type: Prompt Template
title: "Shared Prompt Components"
description: "Reusable fragments: agent tools base, four character-bio variants, three event-history variants, memory access, quest dialogue action and five scene-context components."
resource: "sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/components"
tags: [skyrimnet, prompts, inja]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Reusable Inja fragments included by the top-level templates: the agent tools base (role/context blocks plus available-tools listing), four character-bio render variants, three event-history verbosity variants, memory access, quest dialogue action, and the five-piece scene-context family.

# Member files

All 15 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `plugins/skyrimnet/base/prompts/components/agent_tools_base.prompt` | 5.9KB | 129 |  |
| `plugins/skyrimnet/base/prompts/components/character_bio_dialogue_target.prompt` | 707.0B | 19 | {# This prompt is used when the actor is the target in a dialogue. #} |
| `plugins/skyrimnet/base/prompts/components/character_bio_full.prompt` | 558.0B | 26 | Bio |
| `plugins/skyrimnet/base/prompts/components/character_bio_interject_inline.prompt` | 43.0B | 1 |  |
| `plugins/skyrimnet/base/prompts/components/character_bio_short_inline.prompt` | 33.0B | 1 |  |
| `plugins/skyrimnet/base/prompts/components/context/component_npc_state_summary.prompt` | 5.2KB | 65 | {# Get nearby NPCs once and store the result #} |
| `plugins/skyrimnet/base/prompts/components/context/component_recent_events.prompt` | 716.0B | 15 | {# Get nearby NPCs once and store the result #} |
| `plugins/skyrimnet/base/prompts/components/context/scene_context.prompt` | 3.9KB | 72 |  |
| `plugins/skyrimnet/base/prompts/components/context/scene_context_full.prompt` | 475.0B | 26 |  |
| `plugins/skyrimnet/base/prompts/components/context/scene_context_target_selection.prompt` | 161.0B | 9 |  |
| `plugins/skyrimnet/base/prompts/components/event_history.prompt` | 9.0KB | 114 | {# Use events context variable if set by C++, otherwise fetch via decorator #} |
| `plugins/skyrimnet/base/prompts/components/event_history_compact.prompt` | 8.5KB | 98 | {# Use events context variable if set by C++, otherwise fetch via decorator #} |
| `plugins/skyrimnet/base/prompts/components/event_history_verbose.prompt` | 5.9KB | 73 | {# Use events context variable if set by C++, otherwise fetch via decorator #} |
| `plugins/skyrimnet/base/prompts/components/memory_access.prompt` | 633.0B | 17 | NPC Memories |
| `plugins/skyrimnet/base/prompts/components/quest_dialogue_action.prompt` | 3.2KB | 39 | {% if feature_enabled("quest_actions") %} |

# Related

- Inline bio variants complement the numbered [character bio submodule](/prompts/components/character-bio.md).

# Citations

[1] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/components`

