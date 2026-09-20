---
type: System
title: PrismaUI Web Interface
description: Bundled PrismaUI web views — the config dashboard, diary, letter and non-pausing prompt overlays, plus the item-context SWF.
resource: 'sources/SeverActions/00 Core/PrismaUI'
tags: [ui, prismaui, dashboard, overlays, web]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

SeverActions ships its in-game interface as pre-built PrismaUI web views: a full configuration dashboard plus focused overlay views for confirmations, the follower diary, courier letters and arrest/brawl/retainer/travel prompts. The views are compiled Vite bundles (hashed asset filenames); a shared `client-Der9nqag.js` runtime ships 4 times (main, Diary, Letter, Prompt views). The Papyrus bridge is SeverActions_PrismaUI ([/scripts/core-system.md](/scripts/core-system.md)); the MCM is the fallback surface for VR and non-PrismaUI setups. 31 files are listed below.

# Member Files

## Main dashboard — PrismaUI/views/SeverActions/ (14 files)

| File | Purpose |
|---|---|
| index.html | Entry page; title "SeverActions Config"; loads main-BBoYcSml.js, preloads client-Der9nqag.js and main-DwXf0qPX.css |
| skyrim-map.png | Parchment Skyrim atlas base (Caro Tuts paper map) for the World page |
| assets/client-Der9nqag.js | Shared Vite client runtime |
| assets/main-BBoYcSml.js | Main application bundle |
| assets/main-DwXf0qPX.css | Main stylesheet |
| sigils/dawnstar.png | Hold sigil marker |
| sigils/falkreath.png | Hold sigil marker |
| sigils/markarth.png | Hold sigil marker |
| sigils/morthal.png | Hold sigil marker |
| sigils/riften.png | Hold sigil marker |
| sigils/solitude.png | Hold sigil marker |
| sigils/whiterun.png | Hold sigil marker |
| sigils/windhelm.png | Hold sigil marker |
| sigils/winterhold.png | Hold sigil marker |

## Diary view — SeverActionsDiary/ (4 files)

| File | Purpose |
|---|---|
| index.html | Follower diary reader |
| assets/client-Der9nqag.js | Shared client runtime |
| assets/diary-C5m9arau.js | Diary view bundle |
| assets/diary-C6-cjn6R.css | Diary stylesheet |

## Letter view — SeverActionsLetter/ (4 files)

| File | Purpose |
|---|---|
| index.html | Letter reader (courier letters feature) |
| assets/client-Der9nqag.js | Shared client runtime |
| assets/letter-7CqVZlV0.js | Letter view bundle |
| assets/letter-DtHbtKH6.css | Letter stylesheet |

## Prompt view — SeverActionsPrompt/ (4 files)

| File | Purpose |
|---|---|
| index.html | Generic confirmation prompt overlay |
| assets/client-Der9nqag.js | Shared client runtime |
| assets/prompt-DzO-U9tV.js | Prompt view bundle |
| assets/prompt-BofJ1Axu.css | Prompt stylesheet |

## Single-file overlay views (4 files)

| File | Purpose |
|---|---|
| SeverActionsArrestPrompt/index.html | Non-pausing arrest/bounty confirmation popup |
| SeverActionsBrawlPrompt/index.html | Non-pausing brawl challenge popup |
| SeverActionsRetainerPrompt/index.html | Retainer hearing/arrangement popup |
| SeverActionsTravelPrompt/index.html | Non-pausing travel confirmation popup |

## Item context — Interface/ (1 file)

| File | Purpose |
|---|---|
| severitemcontext.swf | Scaleform item-context menu |

# Pages (per README and changelog)

Dashboard (Portal Tiles frontispiece), Companions, Inventory, World (parchment map with hold sigil markers, per-hold drawer: bounty, properties, travel, debts), Outfits (roster + mannequin preview), Survival (Camp shell, Party Vitals, Rations/Warmth/Risk), Enterprises, Stats/Spells, Settings. The v3.0 "Hearth Ledger" visual identity (parchment + brass + dark surface) and the v3.8.0 true-fullscreen with auto-proportional density apply to these views.

# Citations

[1] `sources/SeverActions/00 Core/PrismaUI/views/**`
[2] `sources/SeverActions/00 Core/Interface/severitemcontext.swf`
