---
type: Runtime Asset
title: "In-Game Chat Web UI"
description: "Browser chat interface served by the plugin (JS/HTML/CSS) on localhost:8080."
resource: "sources/SkyrimNet-GamePlugin/SKSE/Plugins/SkyrimNet/chat"
tags: [skyrimnet, runtime, assets]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Browser chat interface served by the plugin: `index.html` plus `styles.css` and five JS modules (`theme`, `messages`, `audience`, `input`, `app`) loaded in dependency order. It renders the PrismaUI chat panel with persistent history, a nearby-NPC audience strip, whisper/mode badges and @-target autocomplete.

# Member files

All 7 member items assigned to this concept (verified against the manifest):

| Source file | Size | Lines | Summary |
|---|---|---|---|
| `SKSE/Plugins/SkyrimNet/chat/app.js` | 1.3KB | 48 | window.updateMessages = function(json) { |
| `SKSE/Plugins/SkyrimNet/chat/audience.js` | 2.6KB | 80 | let audienceData = { actors: [], whisperMode: false, whisperRadius: 0 }; |
| `SKSE/Plugins/SkyrimNet/chat/index.html` | 1.5KB | 47 | <!DOCTYPE html> |
| `SKSE/Plugins/SkyrimNet/chat/input.js` | 5.1KB | 178 | const MODE_PREFIXES = { |
| `SKSE/Plugins/SkyrimNet/chat/messages.js` | 4.3KB | 142 | let messages = []; |
| `SKSE/Plugins/SkyrimNet/chat/styles.css` | 7.3KB | 378 | /* Chat overlay styles using CSS custom properties for theming */ |
| `SKSE/Plugins/SkyrimNet/chat/theme.js` | 2.0KB | 72 | const THEMES = { |

# Citations

[1] `sources/SkyrimNet-GamePlugin/SKSE/Plugins/SkyrimNet/chat`

