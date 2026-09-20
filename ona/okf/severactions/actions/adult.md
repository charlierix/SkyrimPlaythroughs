---
type: Actions
title: Adult Arousal Actions
description: Optional arousal-adjustment actions bridging OSL Aroused and SexLab Aroused.
resource: 'sources/SeverActions/Actions/Adult-OSLAroused'
tags: [actions, skyrimnet, adult, arousal, osl, sexlab]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The optional Adult module ships two FOMOD variants — one per arousal framework. Each ships exactly one action with the same narrative intent ("the speaker's blood runs hotter or cooler in the moment — a flirtation, a cold bucket of water, a glance held a beat too long, a chastening word from a priest"), differing only in the bridge script. The matching context prompts live in [/prompts/adult.md](/prompts/adult.md).

The two variants ship 2 YAMLs total, one each, both enabled.

# Member Actions

| File | Module | Action | Script.Function | Purpose |
|---|---|---|---|---|
| modifyarousal.yaml | Adult-OSLAroused | ModifyArousal | SeverActions_Arousal.ModifyArousal_Execute | Push arousal up or down via the OSL Aroused bridge |
| modifyarousalslo.yaml | Adult-SLOAroused | ModifyArousalSLO | SeverActions_SLOArousal.ModifyArousal_Execute | Push arousal up or down via the SexLab Aroused bridge |

# Notes

- Only one variant should be installed, matching the arousal framework in the load order; both write through the bridge scripts documented in [/scripts/magic-travel.md](/scripts/magic-travel.md).
- The SLO variant adjusts the exposure component directly (UpdateActorExposure) rather than treating total arousal as the exposure value.
- Both modules are optional FOMOD picks; without an arousal framework installed they do nothing.

# Citations

[1] `sources/SeverActions/Actions/Adult-OSLAroused/SKSE/Plugins/SkyrimNet/config/actions/modifyarousal.yaml`
[2] `sources/SeverActions/Actions/Adult-SLOAroused/SKSE/Plugins/SkyrimNet/config/actions/modifyarousalslo.yaml`
