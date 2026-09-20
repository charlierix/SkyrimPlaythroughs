---
type: Prompt Template
title: "System Head Prompts"
description: "Numbered system-head sections (instructions, setting, format rules, actor bios, telepathy awareness, scene context, omnisight, speech style) plus roleplay guidelines."
resource: "sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/submodules"
tags: [skyrimnet, prompts, inja]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The numbered `system_head` sections assembled into every main prompt — instructions, setting, format rules, actor bios, telepathy awareness, scene context, omnisight, speech style — plus the `roleplay_guidelines` submodule.

# Member files

All 9 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `plugins/skyrimnet/base/prompts/submodules/guidelines/0500_roleplay_guidelines.prompt` | 567.0B | 9 | Roleplay |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0010_instructions.prompt` | 963.0B | 15 | Task |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0010_setting.prompt` | 336.0B | 3 | {# This file controls the "Setting". You should describe how your particular world of Skyrim plays, and any other settin |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0020_format_rules.prompt` | 1.5KB | 29 |  |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0100_actor_bios.prompt` | 214.0B | 4 |  |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0150_telepathy_awareness.prompt` | 917.0B | 9 | {% if exists("npc") and existsIn(npc, "UUID") and has_perk(npc.UUID, "SkyrimNet_TelepathyCanonicalPerk") %} |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0200_scene_context.prompt` | 156.0B | 5 | {% if responseTarget %} |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0250_omnisight.prompt` | 776.0B | 12 | {% if has_current_scene_description() and is_scene_newer_than_location() %} |
| `plugins/skyrimnet/base/prompts/submodules/system_head/0400_speech_style_bio.prompt` | 1.1KB | 13 | {% if render_mode == "full" or render_mode == "transform" %} |

# Related

- System head embeds [omnisight perception context](/prompts/components/omnisight.md).
- System head composes the [final user instructions](/prompts/components/user-final-instructions.md).

# Citations

[1] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/submodules`

