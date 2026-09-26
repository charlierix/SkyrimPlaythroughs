---
type: Prompt Template
title: "Character Bio Submodule"
description: "Eighteen numbered sections composing the shared character bio block (header, summary, background, personality, appearance, skills, relationships, memories, speech style)."
resource: "sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/submodules/character_bio"
tags: [skyrimnet, prompts, inja]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The 18 numbered sections composing the shared character bio block: header, physical activity, summary, world knowledge, background, personality, interject summary, aspirations, appearance, equipment, skills, relationships, party quests, occupation, memories & progression, identity links, memories, and speech style. Render modes (`full`, `thoughts`, `transform`, `dialogue_target`, `short_inline`, `bio_summary`) control which sections appear, and `suppress_host_persona` switches to an entity-led presentation of the host body.

# Member files

All 18 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0010_header.prompt` | 3.7KB | 84 | {# Handle the header based on render mode #} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0050_physical_activity.prompt` | 1.9KB | 34 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" or render_mode == "dialogue_targe |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0100_summary.prompt` | 1.2KB | 15 | {% if suppress_host_persona and (render_mode == "full" or render_mode == "thoughts" or render_mode == "transform") %} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0130_world_knowledge.prompt` | 364.0B | 11 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" %} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0200_background.prompt` | 626.0B | 9 | {# Suppressed in the self-bio when a linked entity fully wears this body (entity_led): the |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0300_personality.prompt` | 695.0B | 10 | {# suppress_host_persona: when a linked virtual entity fully wears this body (entity_led), |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0310_interject_summary.prompt` | 707.0B | 9 | {# Suppressed in the full bio for a body fully worn by a linked entity (entity_led). The |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0320_aspirations.prompt` | 534.0B | 8 | {# Suppressed for a body fully worn by a linked entity (entity_led); the "bio_aspirations" |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0400_appearance.prompt` | 563.0B | 10 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" or render_mode == "dialogue_targe |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0410_equipment.prompt` | 4.8KB | 69 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" or render_mode == "equipment" %} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0500_skills.prompt` | 313.0B | 6 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" or render_mode == "bio_skills" %} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0600_relationships.prompt` | 1.6KB | 26 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" or render_mode == "bio_relationsh |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0610_party_quests.prompt` | 1.9KB | 44 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" %} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/0700_occupation.prompt` | 728.0B | 13 | {# At entity_led the body's trade is still useful (the entity has to keep up appearances in |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/7000_memories_and_progression.prompt` | 361.0B | 6 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" or render_mode == "bio_long_term_ |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/7050_identity_links.prompt` | 24.5KB | 239 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" %} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/7100_memories.prompt` | 1.9KB | 25 | {% if render_mode == "full" or render_mode == "thoughts" or render_mode == "transform" %} |
| `plugins/skyrimnet/base/prompts/submodules/character_bio/9990_speech_style.prompt` | 9.5KB | 132 | {# Suppressed when a linked entity fully wears this body (entity_led): the host's manner of |

# Citations

[1] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/submodules/character_bio`

