---
type: Script
title: "Economy & Crafting Scripts"
description: Currency, debt ledger, crafting delivery and loot-transfer Papyrus scripts.
resource: 'sources/SeverActions/00 Core/Source/Scripts'
tags: [scripts, papyrus, currency, debt, crafting, loot, enterprises]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Four scripts carry the coin, the ledgers and the physical handovers: Currency executes both the Economy trades and most Enterprises verbs (hiring, collections, wages, loans, taxes, camps), Debt owns the tab ledger, Crafting delivers work at stations, and Loot moves items between packs and tracks book reading. Each ships as `.psc` plus compiled `.pex`. Action surfaces: [/actions/economy.md](/actions/economy.md), [/actions/enterprises.md](/actions/enterprises.md), [/actions/crafting.md](/actions/crafting.md), [/actions/basic.md](/actions/basic.md).

# Member Files

| Script (.psc) | Compiled (.pex) | Role |
|---|---|---|
| SeverActions_Currency.psc | SeverActions_Currency.pex | Coin in hand: BuyItem, SellItem, GiveGold, CollectPayment, ExtortGold, RepayDebt — plus the Enterprises verbs (hire/dismiss, collections, wages, loans, taxes, camps) |
| SeverActions_Debt.psc | SeverActions_Debt.pex | The debt ledger: CreateDebt, CreateRecurringDebt, AddToDebt, ReduceDebt, ForgiveDebt |
| SeverActions_Crafting.psc | SeverActions_Crafting.pex | Walk-to-station crafting delivery: CraftItem, BrewPotion, CookMeal, CommissionItem, CollectCommission |
| SeverActions_Loot.psc | SeverActions_Loot.pex | Item transfers and book reading: give/take/bring/pickup, loot/search, ReadBook/StopReading, UseItem |

# Notable Behaviour

- **Conjured Gold** (NPCs giving gold they do not have) ships OFF as of dev141 — a recorded user decision: with retainers, camps, stewards and the NPC labor economy all minting real coin, defaulting the money printer on no longer made sense. Existing saves keep whatever the player chose; the default only governs new games.
- **SeverActions_Crafting** keeps no timing in Papyrus: CRAFT_TIME, INTERACTION_DISTANCE and arrival timeouts live as constants inside the native CraftingOrchestrator.h (kCraftTimeSeconds = 5) — see [/systems/native-plugin.md](/systems/native-plugin.md).
- **SeverActions_Loot** stores active book-reading state (title + text) in per-actor StorageUtil, read by the prompts via papyrus_util — storing them as quest properties bloated the cosave on every save because book text can run tens of KB.
- The debt system features credit limits, due dates, recurring charges, auto-growth from item gifts and automatic guard reporting for severely overdue debts (FOMOD description).

# Citations

[1] `sources/SeverActions/00 Core/Source/Scripts/SeverActions_{Currency,Debt,Crafting,Loot}.psc`
[2] `sources/SeverActions/00 Core/Scripts/SeverActions_{Currency,Debt,Crafting,Loot}.pex`
