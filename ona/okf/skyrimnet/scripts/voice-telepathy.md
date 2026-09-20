---
type: Papyrus Script
title: "Voice Input & Telepathy Scripts"
description: "Magic-effect scripts for the four voice-input modes, wheel menu, telepathy eavesdrop/listen-in and the text-entry overlay."
resource: "sources/SkyrimNet-GamePlugin/Source/Scripts/skynet_VoiceInput{Direct,Normal,Thought,Transform}.psc"
tags: [skyrimnet, papyrus, scripts]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Input-channel scripts: four `skynet_VoiceInput*` ActiveMagicEffect scripts (Direct, Normal, Thought, Transform — text input modes are handled via prefixes in the PrismaUI chat), `skynet_WheelMenu` (the function called from the DLL for the input wheel), telepathy `Eavesdrop`/`ListenIn` powers, and the `uitextentrymenu` text-entry overlay.

# Member scripts

All 8 member items assigned to this concept (verified against the manifest):

| Source file | Scriptname | Extends | Lines |
|---|---|---|---|
| `Source/Scripts/skynet_TelepathyEavesdrop.psc` | `skynet_TelepathyEavesdrop` | ActiveMagicEffect | 12 |
| `Source/Scripts/skynet_TelepathyListenIn.psc` | `skynet_TelepathyListenIn` | ActiveMagicEffect | 16 |
| `Source/Scripts/skynet_VoiceInputDirect.psc` | `skynet_VoiceInputDirect` | ActiveMagicEffect | 14 |
| `Source/Scripts/skynet_VoiceInputNormal.psc` | `skynet_VoiceInputNormal` | ActiveMagicEffect | 14 |
| `Source/Scripts/skynet_VoiceInputThought.psc` | `skynet_VoiceInputThought` | ActiveMagicEffect | 14 |
| `Source/Scripts/skynet_VoiceInputTransform.psc` | `skynet_VoiceInputTransform` | ActiveMagicEffect | 14 |
| `Source/Scripts/skynet_WheelMenu.psc` | `skynet_WheelMenu` | ActiveMagicEffect | 181 |
| `Source/Scripts/uitextentrymenu.psc` | `UITextEntryMenu` | UIMenuBase | 141 |

# Related

- Voice scripts are attached by the [voice input spells](/esp/spells.md).

# Citations

[1] `sources/SkyrimNet-GamePlugin/Source/Scripts/skynet_VoiceInput{Direct,Normal,Thought,Transform}.psc`
[2] `sources/SkyrimNet-GamePlugin/skynet_WheelMenu.psc`
[3] `sources/SkyrimNet-GamePlugin/skynet_Telepathy{Eavesdrop,ListenIn}.psc`
[4] `sources/SkyrimNet-GamePlugin/uitextentrymenu.psc`

