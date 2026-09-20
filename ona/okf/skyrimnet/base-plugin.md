---
type: Plugin Manifest
title: "skyrimnet.base Plugin Bundle"
description: "Manifest of the always-enabled base prompt bundle v0.24.0 that sits at the bottom of the priority order."
resource: "sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/manifest.json"
tags: [skyrimnet, project]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The `skyrimnet.base` content-library plugin is the always-enabled bottom layer of the SkyrimNet prompt-priority order: every other content layer resolves above it. It ships the default prompt templates, shared components, translation CSVs, and the pre-written character bios; third-party-mod bios live as separate `skyrimnet.bios-{mod}` hub packs on the plugin hub.

# Manifest

| Field | Value |
|---|---|
| `id` | `skyrimnet.base` |
| `type` | `bundle` |
| `title` | SkyrimNet Base |
| `tagline` | The default prompts SkyrimNet ships with. |
| `description` | Shipped default content; always enabled, always bottom of the priority order. |
| `author` | `skyrimnet` |
| `version` | 0.24.0 |
| `min_skyrimnet_version` | 0.24.0 |

# Member files

All 1 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `plugins/skyrimnet/base/manifest.json` | 413.0B | 10 | { |

# Related

- The bundle core ships the [dialogue templates](/prompts/templates/dialogue.md).
- Bios are assembled by the shared [character bio module](/prompts/components/character-bio.md).

# Citations

[1] `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/manifest.json`

