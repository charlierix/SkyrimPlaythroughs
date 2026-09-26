---
type: Overview
title: "SkyrimNet Project Overview"
description: "Single SKSE plugin that turns Skyrim NPCs into LLM-driven conversationalists with memory, opinions and autonomous behavior (README)."
resource: "sources/SkyrimNet-GamePlugin/README.md"
tags: [skyrimnet, project]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

SkyrimNet turns every Skyrim NPC into a real conversationalist: NPCs hold their own opinions, remember what happened to them, react to their surroundings, and decide what to do next, all voiced through the TTS engine of your choice and powered by your choice of large language model. It is the only project of its kind that runs as a single native SKSE plugin — no WSL, no Python launcher, no background server window. Install the mod, launch the game, open `localhost:8080`, and you are talking to NPCs in minutes.

# Why it is built this way

- **Speed** — game state is read straight from memory; TTS starts on the first sentence while the model writes the second; action eligibility is pre-warmed during transcription.
- **Stability** — game data is touched only through guarded patterns (reference-counted wrappers, validity checks, strict lock ordering); heavy work runs on worker threads so a slow LLM can never freeze the game.
- **Setup** — first launch generates working defaults; a guided web wizard collects API keys.
- **Performance** — the game thread is never blocked on network, database or TTS work.
- **Extensibility** — Papyrus API and public C++ DLL API; Inja templating with 100+ built-in decorators; YAML-defined actions can call Papyrus quest functions.

# Feature highlights

- Context-aware streaming conversations; 3,000+ pre-written NPC bios; continuous scene mode; realistic perception (whisper mode).
- Private per-NPC vector memory with importance and decay; diaries; condition-scoped world knowledge; knowledge packs (`.sknpack`); NPC groups.
- Eight TTS engines (Piper default, PocketTTS, XTTS, ElevenLabs, Inworld, Zonos, Chatterbox, Kokoro) with live cloning on several; per-NPC voice effects; local Whisper STT.
- PrismaUI in-game chat overlay: `@` targeting with Tab autocomplete, whisper `^` / group `&` modifiers, slash commands (`/think`, `/transform`, `/silent`, `/monologue`, `/compose`, `/playsong`, `/summon`, `/npcthink`, `/telepathy`), inline edit/delete, audience strip.
- OmniSight vision descriptions; YAML triggers; AI-composed bard songs via Suno; NPC thoughts and telepathy perk channel.
- Web dashboard (~30 pages) at `localhost:8080`; MCP server on port 8889 exposing 44+ tools; VastAI cloud-GPU provisioning.

# Repository map

| Directory | Purpose |
|---|---|
| `spriggit/SkyrimNet/` | Spriggit-serialized ESP source (version controlled) |
| `plugins/skyrimnet/base/` | `skyrimnet.base` content library (manifest, prompts, bios, translation CSVs) |
| `Source/Scripts/` | Papyrus script sources (`.psc`) |
| `headers/` | Vanilla Skyrim Papyrus headers for compilation |
| `interface/` | MCM/UI templates (DDS icons) |
| `SKSE/Plugins/SkyrimNet/` | Runtime assets, in-game docs, chat UI |
| `docs/` | Modder documentation |
| `model-presets/` | Dashboard model presets |
| `utilities/` | Bio partition / serialization tooling |
| `.github/` | CI workflows and issue templates |

# Member files

All 1 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `README.md` | 24.9KB | 298 | SkyrimNet |

# Related

- SkyrimNet ships its default prompts as the always-enabled [skyrimnet.base bundle](/base-plugin.md).
- Different model roles are documented under [Model Agents & Usage](/docs/model-agents.md).
- This bundle was generated from the repository `sources/SkyrimNet-GamePlugin`; each top-level directory (`characters/`, `docs/`, `esp/`, `prompts/`, `reference/`, `runtime/`, `scripts/`, `tools/`) has its own index.

# Citations

[1] `sources/SkyrimNet-GamePlugin/README.md`

