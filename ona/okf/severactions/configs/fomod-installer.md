---
type: Config
title: FOMOD Installer
description: Module selection installer definition (ModuleConfig.xml) and package metadata (info.xml).
resource: 'sources/SeverActions/fomod'
tags: [config, fomod, installer, modules]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Two XML files define the FOMOD installer that mod managers present. `ModuleConfig.xml` (633 lines) installs the required `00 Core` folder and offers four install steps of optional modules; `info.xml` carries name, author, version, description and Nexus groups. 2 files are listed below.

# Member Files

| File | Purpose |
|---|---|
| fomod/ModuleConfig.xml | Installer: required files + 4 install steps (633 lines) |
| fomod/info.xml | Name, author, version 3.9.13, long description with credits; groups Gameplay, SkyrimNet |

# Install Steps (ModuleConfig.xml)

## Page 1 — Action Modules (SelectAny)

| Plugin | Type | Installs |
|---|---|---|
| Basic Actions | Recommended | Actions/Basic |
| Travel Actions | Recommended | Actions/Travel |
| Combat Actions | Recommended | Actions/Combat |
| Brawl Actions | Recommended | Actions/Brawl |
| Outfit Actions | Recommended | Actions/Outfit |
| Furniture Actions | Recommended | Actions/Furniture |
| Follower Actions | Recommended | Actions/Follower |
| Economy Actions | Optional | Actions/Economy + Prompts/Economy-Core |
| Enterprises Actions | Optional | Actions/Enterprises |
| Crafting Actions | Optional | Actions/Crafting + Prompts/Crafting |
| Arrest Actions | Optional | Actions/Arrest |
| Kidnap and Captive Actions | Optional | Actions/Kidnap |

## Page 2 — Prompt Modules / Context Awareness

| Plugin | Type | Installs |
|---|---|---|
| Core Awareness Prompts | Recommended | Prompts/Core + Prompts/Enterprises |
| NPC Familiarity & Reputation | Recommended | Prompts/Familiarity |
| Combat Awareness Prompt | Recommended | Prompts/Combat |
| Brawl Awareness Prompt | Recommended | Prompts/Brawl |
| Follower Companion Prompts | Recommended | Prompts/Follower |
| Group Meeting Awareness | Recommended | Prompts/GroupMeeting |
| Survival Prompt | Optional | Prompts/Survival |
| Arrest/Crime Prompts | Optional | Prompts/Arrest |
| Merchant Prompt — Show Anywhere | Optional (SelectAtMostOne) | Prompts/Economy-Anywhere |
| Merchant Prompt — Location Restricted | Optional (SelectAtMostOne) | Prompts/Economy-LocationOnly |

The merchant group is mutually exclusive with none; debt context is bundled with Economy Actions regardless of the choice.

## Page 3 — Compatibility Patches (SelectAny)

| Plugin | Installs |
|---|---|
| AI Overhaul Flee Patch | Patches/AI Overhaul — see [/patches/ai-overhaul.md](/patches/ai-overhaul.md) |
| Daegon Kaekiri Outfit Patch | Patches/Daegon Kaekiri — see [/patches/daegon-kaekiri.md](/patches/daegon-kaekiri.md) |

## Page 4 — Adult Content (Optional)

| Group | Type | Plugins |
|---|---|---|
| Arousal Actions | SelectAtMostOne | OSL Aroused (Actions/Adult-OSLAroused) or SL Aroused (Actions/Adult-SLOAroused) |
| Arousal Prompts | SelectAtMostOne | OSL Aroused (Prompts/Adult-OSLAroused) or SL Aroused (Prompts/Adult-SLOAroused) |
| Fertility Content | SelectAny | Fertility Status Prompt (Prompts/Adult-Fertility) |

# Notes

- Prompt modules are separate from action modules by design; the FOMOD couples a few (Economy+debt prompt, Crafting+commission prompt, Core+Enterprises prompts).
- The info.xml description is a v1.0-era text ("58 actions, 25 context prompts"); the shipped content has since grown to 125 action YAMLs and 77 prompt templates — the README and inventory counts are authoritative.

# Citations

[1] `sources/SeverActions/fomod/ModuleConfig.xml`
[2] `sources/SeverActions/fomod/info.xml`
