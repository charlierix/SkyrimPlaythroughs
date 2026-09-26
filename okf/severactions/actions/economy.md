---
type: Actions
title: Economy Actions
description: Gold, trade, debt and extortion actions of the Economy module.
resource: 'sources/SeverActions/Actions/Economy'
tags: [actions, skyrimnet, economy, gold, debt, trade]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Economy module (FOMOD option "Economy Actions", optional) covers gold and debt: atomic item-for-gold trades, gifts and tips, extortion, and a full debt system with one-off tabs, recurring charges (rent, wages, dues), credit limits, due dates, and repayment or forgiveness. Execution functions split between SeverActions_Currency (coin in hand) and SeverActions_Debt (the ledger). The FOMOD description notes the debt system auto-grows from item gifts and reports severely overdue debts to guards.

The module ships 12 YAMLs — 11 executable actions plus the `cat_economy` category file.

# Member Actions

## Coin in hand (SeverActions_Currency)

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| cat_economy.yaml | Economy | economy | — | Category file grouping all gold, trade and debt actions |
| buyitem.yaml | BuyItem | economy | SeverActions_Currency.BuyItem_Execute | Coin one way, goods the other, settled in the same breath |
| sellitem.yaml | SellItem | economy | SeverActions_Currency.SellItem_Execute | Goods one way, coin the other — not for finished commissions |
| givegold.yaml | GiveGold | economy | SeverActions_Currency.GiveGold_Execute | Coin moves from the speaker to someone else — gift, tip, fee, reward, refund |
| collectpayment.yaml | CollectPayment | economy | SeverActions_Currency.CollectPayment_Execute | Take gold owed TO the speaker; automatically reduces open debts |
| extortgold.yaml | ExtortGold | economy | SeverActions_Currency.ExtortGold_Execute | Squeeze coin out of someone through threat or intimidation |
| repaydebt.yaml | RepayDebt | economy | SeverActions_Currency.RepayDebt_Execute | The speaker pays back some or all of a debt THEY owe |

## The ledger (SeverActions_Debt)

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| createdebt.yaml | CreateDebt | economy | SeverActions_Debt.CreateDebt_Execute | Open a one-off tab with optional due dates and credit limits |
| createrecurringdebt.yaml | CreateRecurringDebt | economy | SeverActions_Debt.CreateRecurringDebt_Execute | Strike an ongoing arrangement where coin changes hands on a schedule |
| addtodebt.yaml | AddToDebt | economy | SeverActions_Debt.AddToDebt_Execute | Add charges to a tab that already exists |
| reducedebt.yaml | ReduceDebt | economy | SeverActions_Debt.ReduceDebt_Execute | Reduce a tab by agreed amount with no gold changing hands |
| forgivedebt.yaml | ForgiveDebt | economy | SeverActions_Debt.ForgiveDebt_Execute | Cancel every debt the other person owes — all tabs at once |

# Eligibility Notes

- CollectPayment only ever moves gold TO the speaker; the speaker paying is GiveGold or BuyItem. Guard bounty payments deliberately route through PayNpcBountyToGuard instead ([/actions/arrest.md](/actions/arrest.md)).
- ForgiveDebt is a deliberate act of mercy or giving up — payments settle their own debts automatically.
- RepayDebt with amount 0 (or omitted) pays everything owed; it can never exceed the debt.

# Related

- Currency and Debt scripts own these ledgers: [/scripts/economy-crafting.md](/scripts/economy-crafting.md)
- Shared wage and settlement machinery with Enterprises: [/actions/enterprises.md](/actions/enterprises.md)
- Debt and merchant context prompts: [/prompts/economy.md](/prompts/economy.md)

# Citations

[1] `sources/SeverActions/Actions/Economy/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
