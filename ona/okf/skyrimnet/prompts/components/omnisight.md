---
type: Prompt Template
title: "Omnisight Description Prompts"
description: "Perception templates describing actors, items, locations, scenes, furniture, book pages and defaults, plus per-type base submodules."
resource: "sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts"
tags: [skyrimnet, prompts, inja]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

OmniSight perception prompts asking a vision model to describe actors, items, locations, scenes, furniture, book pages and a default case, each paired with its per-type `submodules/omnisight_*` base section.

# Member files

All 13 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `plugins/skyrimnet/base/prompts/omnisight/describe_actor.prompt` | 6.1KB | 86 | [user] |
| `plugins/skyrimnet/base/prompts/omnisight/describe_book_page.prompt` | 271.0B | 3 | Analyze this screenshot of a from the game Skyrim. The title is "" (editor ID: {{ book_ed |
| `plugins/skyrimnet/base/prompts/omnisight/describe_default.prompt` | 1.4KB | 26 | [user] |
| `plugins/skyrimnet/base/prompts/omnisight/describe_furniture.prompt` | 1.4KB | 26 | [user] |
| `plugins/skyrimnet/base/prompts/omnisight/describe_item.prompt` | 6.3KB | 77 | [user] |
| `plugins/skyrimnet/base/prompts/omnisight/describe_location.prompt` | 3.7KB | 51 |  |
| `plugins/skyrimnet/base/prompts/omnisight/describe_scene.prompt` | 5.3KB | 82 |  |
| `plugins/skyrimnet/base/prompts/submodules/omnisight_actor/0000_base.prompt` | 110.0B | 2 | {# Omnisight Actor Submodule - Mods can add numbered .prompt files here to extend actor capture context #} |
| `plugins/skyrimnet/base/prompts/submodules/omnisight_default/0000_base.prompt` | 114.0B | 2 | {# Omnisight Default Submodule - Mods can add numbered .prompt files here to extend default capture context #} |
| `plugins/skyrimnet/base/prompts/submodules/omnisight_furniture/0000_base.prompt` | 118.0B | 2 | {# Omnisight Furniture Submodule - Mods can add numbered .prompt files here to extend furniture capture context #} |
| `plugins/skyrimnet/base/prompts/submodules/omnisight_item/0000_base.prompt` | 108.0B | 2 | {# Omnisight Item Submodule - Mods can add numbered .prompt files here to extend item capture context #} |
| `plugins/skyrimnet/base/prompts/submodules/omnisight_location/0000_base.prompt` | 116.0B | 2 | {# Omnisight Location Submodule - Mods can add numbered .prompt files here to extend location capture context #} |
| `plugins/skyrimnet/base/prompts/submodules/omnisight_scene/0000_base.prompt` | 110.0B | 2 | {# Omnisight Scene Submodule - Mods can add numbered .prompt files here to extend scene capture context #} |

# Citations

[1] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts`

