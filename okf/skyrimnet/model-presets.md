---
type: Configuration
title: "Model Presets"
description: "OpenRouter preset YAMLs (budget/balanced/premium), recommended-models list and the dashboard manifest that enumerates them."
resource: "sources/SkyrimNet-GamePlugin/model-presets/index.yaml"
tags: [skyrimnet, project, llm]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The dashboard fetches `model-presets/index.yaml` once (cached ~10 minutes) to enumerate the built-in presets and the recommended-models file; dropping a new YAML into `presets/` and registering it in the index requires no code change. Shipped presets configure OpenRouter budget/balanced/premium model rotations.

# Built-in presets

| Preset id | Name | Provider | File |
|---|---|---|---|
| `openrouter-budget` | Budget | openrouter | `presets/openrouter-budget.yaml` |
| `openrouter-default` | Balanced | openrouter | `presets/openrouter-default.yaml` |
| `openrouter-performance` | Premium | openrouter | `presets/openrouter-performance.yaml` |

`recommended-models.yaml` drives the dashboard ModelPicker's Recommended section; each entry carries an `id` (provider model id) plus optional sampling fields: `temperature`, `max_tokens`, `top_p`, `top_k`, `frequency_penalty`, `presence_penalty`. A bare-string form applies no overrides.

# Member files

All 5 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `model-presets/index.yaml` | 682.0B | 21 | SkyrimNet model-presets manifest. The dashboard fetches this once |
| `model-presets/presets/openrouter-budget.yaml` | 2.8KB | 74 | Budget preset — Gemma-3 27B for the cheap bulk variants, Qwen 235B |
| `model-presets/presets/openrouter-default.yaml` | 2.8KB | 74 | Default preset — mirrors the in-code TextModelConfig defaults. |
| `model-presets/presets/openrouter-performance.yaml` | 3.0KB | 77 | Performance preset — Sonnet 4.6 for dialogue/profiles/diary/action/ |
| `model-presets/recommended-models.yaml` | 4.3KB | 172 | Recommended models surfaced in the dashboard's ModelPicker |

# Related

- Presets configure the model roles described in [Model Agents & Usage](/docs/model-agents.md).

# Citations

[1] `sources/SkyrimNet-GamePlugin/model-presets/index.yaml`
[2] `sources/SkyrimNet-GamePlugin/model-presets/presets/openrouter-budget.yaml`
[3] `sources/SkyrimNet-GamePlugin/model-presets/presets/openrouter-default.yaml`
[4] `sources/SkyrimNet-GamePlugin/model-presets/presets/openrouter-performance.yaml`
[5] `sources/SkyrimNet-GamePlugin/model-presets/recommended-models.yaml`

