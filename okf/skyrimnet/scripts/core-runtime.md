---
type: Papyrus Script
title: "Core Runtime Scripts"
description: "Main controller, shared library, MinAI bridge, player alias, harness and example integration script."
resource: "sources/SkyrimNet-GamePlugin/Source/Scripts/skynet_MainController.psc"
tags: [skyrimnet, papyrus, scripts]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Core Papyrus runtime scripts: `skynet_MainController` (161 lines) is the controller quest script; `skynet_Library` (907 lines) is the shared library quest; `skynet_MinAIBridge` listens for MinAI mod events and forwards them through SkyrimNet's native API; `skynet_PlayerAlias`, `skynet_Harness` and `skynet_ExampleScript` attach the system to the player and demonstrate integration.

# Compile

```
papyrus.exe -nocache -h headers -i Source/Scripts -output Scripts
```

# Member scripts

All 6 member items assigned to this concept (verified against the manifest):

| Source file | Scriptname | Extends | Lines |
|---|---|---|---|
| `Source/Scripts/skynet_ExampleScript.psc` | `` | — | 7 |
| `Source/Scripts/skynet_Harness.psc` | `skynet_Harness` | — | 34 |
| `Source/Scripts/skynet_Library.psc` | `skynet_Library` | Quest | 907 |
| `Source/Scripts/skynet_MainController.psc` | `` | — | 161 |
| `Source/Scripts/skynet_MinAIBridge.psc` | `skynet_MinAIBridge` | Quest | 161 |
| `Source/Scripts/skynet_PlayerAlias.psc` | `skynet_PlayerAlias` | ReferenceAlias | 7 |

# Related

- Runtime bootstraps through the [main controller quest](/esp/quests.md).
- The controller drives the [dialogue and follow packages](/esp/packages.md).

# Citations

[1] `sources/SkyrimNet-GamePlugin/Source/Scripts/skynet_MainController.psc`
[2] `sources/SkyrimNet-GamePlugin/skynet_Library.psc`
[3] `sources/SkyrimNet-GamePlugin/skynet_MinAIBridge.psc`
[4] `sources/SkyrimNet-GamePlugin/skynet_PlayerAlias.psc`
[5] `sources/SkyrimNet-GamePlugin/skynet_Harness.psc`
[6] `sources/SkyrimNet-GamePlugin/skynet_ExampleScript.psc`

