---
type: Trigger
title: Pregnancy Trigger
description: SkyrimNet trigger YAML that fires the Abort Pregnancy narration when the spell is applied.
resource: 'sources/SeverActions/Triggers/Adult/SKSE/Plugins/SkyrimNet/config/triggers/Abort Pregnancy.yaml'
tags: [trigger, skyrimnet, adult, fertility]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

This is the bundle's only SkyrimNet **trigger** (distinct from action YAMLs): it fires a narration event when a spell effect is applied, rather than declaring an action the AI may choose. It supports the Fertility Mode integration's pregnancy endings. 1 file is listed below.

# Member Files

| File | Purpose |
|---|---|
| Triggers/Adult/SKSE/Plugins/SkyrimNet/config/triggers/Abort Pregnancy.yaml | Fires when the Abort Pregnancy spell is cast on a target, ending the pregnancy — with or without the target's consent |

# Definition

| Field | Value |
|---|---|
| name | "Abort Pregnancy" |
| eventCriteria.eventType | active_effect |
| schemaConditions | effect equals "Abort Pregnancy" (case-insensitive); action equals "applied" |
| response.type | direct_narration |
| response.content | "{{ player.name }} casts a spell on {{ event_json.target }}, ending the pregnancy." |
| audience | target |
| enabled | true |
| probability | 1 |
| cooldownSeconds | 30 |
| priority | 1 |

# Related

- The Fertility status prompt that makes NPCs aware of fertility/pregnancy state: [/prompts/adult.md](/prompts/adult.md)
- The Fertility Mode bridge script feeding the data: [/scripts/magic-travel.md](/scripts/magic-travel.md)

# Citations

[1] `sources/SeverActions/Triggers/Adult/SKSE/Plugins/SkyrimNet/config/triggers/Abort Pregnancy.yaml`
