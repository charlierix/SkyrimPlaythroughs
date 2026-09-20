---
type: Prompt
title: Adult Prompts
description: Arousal and fertility context prompts for the three optional adult integrations.
resource: 'sources/SeverActions/Prompts/Adult-OSLAroused'
tags: [prompts, skyrimnet, adult, arousal, fertility, osl, sexlab]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The optional Adult prompts ship as three separate FOMOD variants, one per framework integration — OSL Aroused, SexLab Aroused (SLO), and Fertility Mode Reloaded. Each injects the framework's live state into character_bio so the AI knows about arousal or pregnancy rather than inventing it. They pair with the arousal actions in [/actions/adult.md](/actions/adult.md). All three templates are listed below.

# Member Prompts

| Module | File | Lines | Purpose |
|---|---|---|---|
| Adult-OSLAroused | submodules/character_bio/0150_severactions_oslarousal.prompt | 102 | OSL arousal state in the actor's bio; render_mode gate documented as MUST stay on line 1 |
| Adult-SLOAroused | submodules/character_bio/0155_severactions_sloarousal.prompt | 95 | SexLab Aroused state in the actor's bio; same first-5-lines gate note |
| Adult-Fertility | submodules/character_bio/0250_severactions_fertility.prompt | 113 | Fertility Mode Reloaded integration; carries a TONE CONTRACT comment from a field report fixing over-narration |

# Notes

- The OSL/SLO templates both document the SkyrimNet PromptEngine constraint in comments: only the FIRST 5 LINES of a character_bio submodule are scanned, requiring both the literal 'render_mode' and a '{% if' there.
- The fertility prompt is gated to render only in relevant render modes (full/thoughts/transform/dialogue_target/target).
- The paired Abort Pregnancy SkyrimNet trigger is documented in [/configs/pregnancy-trigger.md](/configs/pregnancy-trigger.md).
- None of these do anything without the corresponding framework installed; all three are optional FOMOD picks.

# Citations

[1] `sources/SeverActions/Prompts/Adult-OSLAroused/.../0150_severactions_oslarousal.prompt`
[2] `sources/SeverActions/Prompts/Adult-SLOAroused/.../0155_severactions_sloarousal.prompt`
[3] `sources/SeverActions/Prompts/Adult-Fertility/.../0250_severactions_fertility.prompt`
