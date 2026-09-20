---
type: Config
title: "Plugin Registration & Distribution"
description: Main ESP, SkyrimNet plugin manifest with LLM variants, SPID custom-AI distribution and localization strings.
resource: 'sources/SeverActions/00 Core/SeverActions.esp'
tags: [config, esp, skyrimnet, spid, localization]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Four files wire SeverActions into the game and into SkyrimNet: the compiled plugin, the SkyrimNet plugin manifest that also declares LLM variant routing, the SPID distribution file for custom-AI follower detection, and the localization strings. 4 files are listed below.

# Member Files

| File | Size | Purpose |
|---|---|---|
| 00 Core/SeverActions.esp | 434,207 B | Main plugin: quest aliases, packages, follow templates, 400 slot×preset outfit triplets (v2.9), Levy soldier records; dropped Dawnguard/Dragonborn masters in v3.1.1 |
| SKSE/Plugins/SkyrimNet/config/plugins/SeverActions/manifest.yaml | — | SkyrimNet plugin registration |
| 00 Core/SeverActions_CustomAI_DISTR.ini | — | SPID distribution of the custom-AI follower keyword |
| 00 Core/Interface/Translations/SeverActions_english.txt | 522 B | UI strings (UTF-16) |

# SkyrimNet manifest (manifest.yaml)

- `plugin:` name SeverActions, version "3.0", description "SkyrimNet companion / outfit / arrest / cast-spell action pack", icon 🌊.
- **LLM variants:** one named variant `sever_background` — a config bucket routing background prompts (relationship assessment, banter, off-screen life, quest awareness, reputation, inter-follower opinions) to a cheaper model than the dialogue tier.
- **Schema fields** (all optional, category "LLM Overrides", empty/0 = inherit the base OpenRouter config): API Endpoint (`llm.endpoint`), API Key (`llm.api_key`), Model Name (`llm.model_name`), Temperature (`llm.temperature`, 0-2), Max Tokens (`llm.max_tokens`, 0-4096), Request Timeout seconds (`llm.timeout`, 0-120).
- Zero behavior change for users who do not touch these settings.

# Custom-AI distribution (SeverActions_CustomAI_DISTR.ini)

- Distributes the `SeverActions_CustomAIFollower` keyword (FormID `0x13C78B~SeverActions.esp`) to followers with their own custom AI systems, putting SeverActions into **tracking-only mode** for them: relationship assessments, gossip, diary reading and PrismaUI visibility work, but AI packages, follow behaviour and outfit management are never overridden.
- **SPID is optional since 3.5.1**: the mod also parses this file natively and matches followers by NAME or EditorID, so entries work without SPID (and cover renamed forks). With SPID present, both mechanisms run.
- **Plugin-qualified names (3.9.7+)** for collision-prone common names: `Keyword = 0x13C78B~SeverActions.esp|NPCName@Plugin.esp|NPCEditorID` — the native matcher flags the name only when the NPC's defining plugin matches. Qualified entries are native-only (SPID ignores them).
- **Shipped entries (14):** Inigo, Lucien Flavius, Auri, Sofia, Vilja, Kaidan, Kaidan (KRCE revoiced), Recorder, M'rissi, Remiel, Xelzaz, Nebarra, Gore, Katana — each with Nexus link and EditorID in a comment; the FormID must match xEdit's AddCustomAIKeyword.pas output (0x000D70 note).

# Localization (SeverActions_english.txt)

UTF-16 key/value pairs: `$Rapport`, `$Trust`, `$Loyalty`, `$Crime`, and the nine hold names (`$Whiterun`, `$The Rift`, `$Haafingar`, `$Eastmarch`, `$The Reach`, `$Falkreath`, `$The Pale`, `$Hjaalmarch`, `$Winterhold`).

# Citations

[1] `sources/SeverActions/00 Core/SeverActions.esp`
[2] `sources/SeverActions/00 Core/SKSE/Plugins/SkyrimNet/config/plugins/SeverActions/manifest.yaml`
[3] `sources/SeverActions/00 Core/SeverActions_CustomAI_DISTR.ini`
[4] `sources/SeverActions/00 Core/Interface/Translations/SeverActions_english.txt`
