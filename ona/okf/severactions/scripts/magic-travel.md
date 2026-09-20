---
type: Script
title: "Magic, Travel & Bridge Scripts"
description: Spell casting and teaching, off-screen travel, furniture use and optional-framework bridge Papyrus scripts.
resource: 'sources/SeverActions/00 Core/Source/Scripts'
tags: [scripts, papyrus, spells, shouts, travel, furniture, arousal, fertility]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Eight scripts cover the remaining engine surfaces: animated spellcasting and its alias dispatcher, spell/shout teaching, off-screen travel, furniture use, and three optional-framework bridges (OSL Aroused, SexLab Aroused, Fertility Mode Reloaded). Each ships as `.psc` plus compiled `.pex`. Related actions: [/actions/basic.md](/actions/basic.md) (cast/learn/teach), [/actions/travel.md](/actions/travel.md), [/actions/furniture.md](/actions/furniture.md), [/actions/adult.md](/actions/adult.md).

# Member Files

| Script (.psc) | Compiled (.pex) | Role |
|---|---|---|
| SeverActions_SpellCast.psc | SeverActions_SpellCast.pex | Animated NPC spellcasting (v2.9): charge and release with proper animation, heals-to-full auto-repeat for restoration |
| SeverActions_SpellCastAlias.psc | SeverActions_SpellCastAlias.pex | ESP-filled properties and per-cast runtime state; the dispatcher calls in after ForceRefTo |
| SeverActions_SpellTeach.psc | SeverActions_SpellTeach.pex | TeachSpell / LearnSpell / TeachShout; fade-to-black effect, failure system settings, visual FX |
| SeverActions_Travel.psc | SeverActions_Travel.pex | TravelToPlace / ChangeTravelSpeed / CancelTravel and the hired-thug standoff verbs (ThugAttack, ThugStandDown from the Enterprises module) |
| SeverActions_Furniture.psc | SeverActions_Furniture.pex | Furniture use; registers for the native cleanup event from FurnitureManager on game load |
| SeverActions_Arousal.psc | SeverActions_Arousal.pex | OSL Aroused bridge; also provides the get_arousal_state decorator returning arousal JSON for prompts |
| SeverActions_SLOArousal.psc | SeverActions_SLOArousal.pex | SexLab Aroused bridge; decorators global for template access |
| SeverActions_FertilityMode_Bridge.psc | SeverActions_FertilityMode_Bridge.pex | Bridges Fertility Mode Reloaded data to SkyrimNet via native decorators |

# Notable Behaviour

- **Travel speed constants mirror the native TravelSpeed enum**; the stuck-detector skipped the SE-only IsPathing refinement on VR (v3.9.13 fix), falling back to distance-based checks.
- **The SLO bridge adjusts the exposure component directly** via UpdateActorExposure — SetActorExposure(GetActorArousal + amount) would wrongly treat total arousal as the exposure value.
- **The Fertility Mode bridge uses a hybrid native approach**: Papyrus reads FM's arrays and pushes them into a native cache for O(1) lookups; a real-time deadline after a None TrackedActors read prevents FM's benign per-read log line from repeating every 3 seconds while FM is idle. Quest scripts never receive OnPlayerLoadGame, so no such handler exists. Requires the FM Reloaded source files (_JSW_BB_Storage.psc, _JSW_BB_Utility.psc) to compile.
- The Arousal decorator checks whether OSLAroused is loaded before reading values and derives a textual arousal description.

# Citations

[1] `sources/SeverActions/00 Core/Source/Scripts/SeverActions_{SpellCast,SpellCastAlias,SpellTeach,Travel,Furniture,Arousal,SLOArousal,FertilityMode_Bridge}.psc`
[2] `sources/SeverActions/00 Core/Scripts/` matching `.pex` files
