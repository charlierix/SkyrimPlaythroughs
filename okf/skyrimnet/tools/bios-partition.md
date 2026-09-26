---
type: Utility
title: "Bio Partition Tool"
description: "Historical one-time tool that split 3,098 bios into skyrimnet.base and per-mod hub packs; ships audit reports and hand-attribute overrides."
resource: "sources/SkyrimNet-GamePlugin/utilities/bios"
tags: [skyrimnet, tooling]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Historical, one-time bio partition tool: it split the pre-restructure `original_prompts/characters/` (3,098 bios) into the bios kept in `skyrimnet.base` and per-source-mod `skyrimnet.bios-{mod}` hub packs (Core `ai_docs/CONTENT_STORE_DESIGN.md`, ruling 26). The paths it targeted no longer exist — run it against commit `3700301` or earlier. Its audit trail lives in `report/`; `overrides.csv` records hand attributions.

# Member files

All 8 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `utilities/bios/README.md` | 2.3KB | 42 | Bio partition tool |
| `utilities/bios/generate_legacy_fingerprints.py` | 2.7KB | 71 | !/usr/bin/env python3 |
| `utilities/bios/overrides.csv` | 13.8KB | 88 | bioKey,target,note |
| `utilities/bios/partition_bios.py` | 12.3KB | 286 | !/usr/bin/env python3 |
| `utilities/bios/report/assignment.csv` | 92.0KB | 3099 | bioKey,targets |
| `utilities/bios/report/multi-claim.csv` | 6.0KB | 59 | bioKey,claimants,shippedIn |
| `utilities/bios/report/packs.csv` | 8.0KB | 216 | slug,bioCount,pluginFiles |
| `utilities/bios/report/unattributed.txt` | 1.8KB | 80 | adilya_generic |

# Citations

[1] `sources/SkyrimNet-GamePlugin/utilities/bios`

