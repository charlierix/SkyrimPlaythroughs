---
type: Prompt
title: Economy Prompts
description: Debt and merchant context prompts in the three scoping variants of the Economy prompt modules.
resource: 'sources/SeverActions/Prompts/Economy-Core'
tags: [prompts, skyrimnet, economy, debt, merchants]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Economy prompts ship as three separate FOMOD variants that scope merchant awareness differently — Economy-Core (system-level debt context), Economy-Anywhere (merchant stock shown anywhere), and Economy-LocationOnly (merchant stock only at the shop). Together they let the AI know about outstanding debts and what a merchant actually has in stock. All three templates are listed below.

# Member Prompts

| Module | File | Lines | Purpose |
|---|---|---|---|
| Economy-Core | submodules/system_head/0150_debt_context.prompt | 11 | Financial Obligations block via the debt_context decorator — rendered only when the NPC is involved in a debt |
| Economy-Anywhere | submodules/character_bio/0075_severactions_merchant.prompt | 35 | Merchant stock awareness for any non-player actor, gated by render_mode including action (buy/sell/vendor drill-downs) |
| Economy-LocationOnly | submodules/character_bio/0080_severactions_merchantloc.prompt | 151 | Location-scoped variant of the merchant prompt with fuller stock and vendor logic |

# Notes

- Both merchant variants exclude the player and check the SexLab-animating faction to avoid awkward overrides during animations.
- Debt actions live in [/actions/economy.md](/actions/economy.md); the ledger script is [/scripts/economy-crafting.md](/scripts/economy-crafting.md).
- The FOMOD Economy Actions plugin installs Actions/Economy together with Prompts/Economy-Core.

# Citations

[1] `sources/SeverActions/Prompts/Economy-Core/SKSE/Plugins/SkyrimNet/prompts/submodules/system_head/0150_debt_context.prompt`
[2] `sources/SeverActions/Prompts/Economy-Anywhere/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0075_severactions_merchant.prompt`
[3] `sources/SeverActions/Prompts/Economy-LocationOnly/SKSE/Plugins/SkyrimNet/prompts/submodules/character_bio/0080_severactions_merchantloc.prompt`
