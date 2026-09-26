---
type: Script
title: "Core & UI Scripts"
description: Startup, settings, hotkeys, property gate and UI-bridge Papyrus scripts of SeverActions.
resource: 'sources/SeverActions/00 Core/Source/Scripts'
tags: [scripts, papyrus, init, mcm, hotkeys, prismaui, wheel-menu, property]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Six scripts own startup and the interface surface: initialization ordering, the shared property store with the ownership gate, MCM settings, configurable hotkeys, the PrismaUI bridge and the radial wheel menu. Each ships as source `.psc` under `00 Core/Source/Scripts/` and compiled `.pex` under `00 Core/Scripts/`. All 12 files are listed below.

# Member Files

| Script (.psc) | Compiled (.pex) | Role |
|---|---|---|
| SeverActions_Init.psc | SeverActions_Init.pex | Initialization: delays so all quest scripts run their OnInit first; heals the v2.1.7 aggression corruption |
| SeverActions_Property.psc | SeverActions_Property.pex | Property ownership actions; the ownership gate lives here (issue #12) because eligibility decorators cannot see the dynamic propertyName parameter |
| SeverActions_MCM.psc | SeverActions_MCM.pex | MCM settings mirroring properties in other scripts (currency, dialogue animation, etc.); passes settings to the native DLL |
| SeverActions_Hotkeys.psc | SeverActions_Hotkeys.pex | MCM-configured hotkeys; includes the two-step use-furniture state (pick NPC, then furniture target) |
| SeverActions_PrismaUI.psc | SeverActions_PrismaUI.pex | PrismaUI lifecycle bridge; passes quest references to C++ so the DataGatherer reads settings without going through Papyrus |
| SeverActions_WheelMenu.psc | SeverActions_WheelMenu.pex | Radial wheel menu; option indices match wheel positions; hotkey configurable via MCM |

# Notable Behaviour

- The ownership gate in SeverActions_Property uses `Native_IsCellOwner`, accepting either a direct NPC owner or membership in the cell's faction owner (covering Hulda/Bannered Mare via BanneredMareInnFaction); an empty cleanName falls back to the actor's current cell.
- The v2.1.7 aggression corruption heal in Init is the same self-heal documented for v2.9.5 — a defensive cleanup for old saves.
- Hotkeys' furniture flow pairs with the Furniture actions ([/actions/furniture.md](/actions/furniture.md)); the wheel menu opens the action wheel whose entries map onto the action modules.

# Dependencies

- PrismaUI bridge talks to the compiled views in [/systems/prismaui-interface.md](/systems/prismaui-interface.md).
- Settings recorded by MCM are read natively via the passed quest references — [/systems/native-plugin.md](/systems/native-plugin.md).
- TransferOwnership eligibility: [/actions/basic.md](/actions/basic.md).

# Citations

[1] `sources/SeverActions/00 Core/Source/Scripts/SeverActions_{Init,Property,MCM,Hotkeys,PrismaUI,WheelMenu}.psc`
[2] `sources/SeverActions/00 Core/Scripts/SeverActions_{Init,Property,MCM,Hotkeys,PrismaUI,WheelMenu}.pex`
