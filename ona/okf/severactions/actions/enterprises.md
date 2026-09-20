---
type: Actions
title: Enterprises Actions
description: Hiring, wages, loans, hold taxes and outlaw-camp management actions of the Enterprises module.
resource: 'sources/SeverActions/Actions/Enterprises'
tags: [actions, skyrimnet, enterprises, employment, loans, taxes, camps]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Enterprises module (FOMOD option "Enterprises Actions", optional) is the off-screen economy: any NPC can be hired to run a venture — a mine, a shop or trade stall, an alchemy bench, a farm, a fencing operation, a mercenary contract — and hold stewards channel every retainer's weekly take into a vault the player collects from. Wages, raises and terms are negotiable; loans flow both ways; the Imperial Fiscal Levy's Final Audit presses back-taxes; and outlaw camps can swear to the player, muster for war, or be released. Nearly every execution function lives in SeverActions_Currency; the two hired-thug verbs live in SeverActions_Travel.

The module ships 27 YAMLs — 26 executable actions plus the `cat_employment` category file.

# Member Actions

## Hiring and service

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| cat_employment.yaml | Employment | employment | — | Category file grouping all employment and camp actions |
| hireretainer.yaml | HireRetainer | employment | SeverActions_Currency.HireRetainer | The speaker agrees to work for the player running an off-screen venture |
| hiresteward.yaml | HireSteward | employment | SeverActions_Currency.HireSteward | Appoint an existing retainer as STEWARD of the player's hold |
| dismissretainer.yaml | DismissRetainer | employment | SeverActions_Currency.DismissRetainer | End a retainer's service; they stop producing and go back to normal life |
| dismisssteward.yaml | DismissSteward | employment | SeverActions_Currency.DismissSteward | Relieve a steward; the hold vault hands itself back automatically |

## Collections, wages and terms

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| collectfromretainer.yaml | CollectFromRetainer | employment | SeverActions_Currency.CollectFromRetainer | Take the earnings a retainer has been holding since last collection |
| collectfromsteward.yaml | CollectFromSteward | employment | SeverActions_Currency.CollectFromSteward | Collect the hold's whole takings from the steward's vault in one handover |
| payarrears.yaml | PayArrears | employment | SeverActions_Currency.PayArrears | Pay the back-wages the player owes a retainer |
| grantretainerraise.yaml | GrantRetainerRaise | employment | SeverActions_Currency.GrantRetainerRaise | Agree to pay a retainer better; actually changes the wage or split |
| negotiateterms.yaml | NegotiateTerms | employment | SeverActions_Currency.NegotiateTerms | Haggle — split the difference on a raise or a share |

## Grievances

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| reassureretainer.yaml | ReassureRetainer | employment | SeverActions_Currency.ReassureRetainer | Sincerely hear out and genuinely address a retainer's grievance face to face |
| brushoffretainer.yaml | BrushOffRetainer | employment | SeverActions_Currency.BrushOffRetainer | Dismiss, mock or threaten the retainer's grievance to their face |

## Loans

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| grantloan.yaml | GrantLoan | employment | SeverActions_Currency.GrantLoan | Lend a retainer the coin they asked for — real money leaves the player's purse |
| refuseloan.yaml | RefuseLoan | employment | SeverActions_Currency.RefuseLoan | Turn down a retainer's loan request |
| forgiveloan.yaml | ForgiveLoan | employment | SeverActions_Currency.ForgiveLoan | Write off what a retainer still owes |

## Hold taxes and the Final Audit

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| collectauthorizedtaxes.yaml | CollectAuthorizedTaxes | — | SeverActions_Currency.CollectAuthorizedTaxes | A Treasury collector accepts the back-taxes payment the player agreed to in dialogue |
| granttaxrelief.yaml | GrantTaxRelief | — | SeverActions_Currency.GrantTaxRelief | A jarl genuinely persuaded in person eases the hold's enterprise taxes |
| raiseholdtaxes.yaml | RaiseHoldTaxes | — | SeverActions_Currency.RaiseHoldTaxes | A jarl angered or unimpressed raises the hold's enterprise taxes |
| pressthedemand.yaml | PressTheDemand | — | SeverActions_Currency.PressTheDemand | The Treasury detail escalates after the player refuses the Final Audit's demand |

## Outlaw camps

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| swearcamptoplayer.yaml | SwearCampToPlayer | employment | SeverActions_Currency.SwearCampToPlayer | A camp leader agrees that their whole camp will serve the player |
| recruitleaderlesscamp.yaml | RecruitLeaderlessCamp | employment | SeverActions_Currency.RecruitLeaderlessCamp | One voice of a leaderless camp personally throws in with the player |
| releasecampfromservice.yaml | ReleaseCampFromService | employment | SeverActions_Currency.ReleaseCampFromService | Cut a sworn camp loose entirely; they keep their ground |
| renouncecampoath.yaml | RenounceCampOath | employment | SeverActions_Currency.RenounceCampOath | The oath breaks after betrayal; the camp returns to ordinary outlaws |
| mustercamp.yaml | MusterCamp | employment | SeverActions_Currency.MusterCamp | Rally the whole sworn camp to the player's side right now |
| sendcamphome.yaml | SendCampHome | employment | SeverActions_Currency.SendCampHome | Dismiss a mustered war band back to the camp |

## Hired thugs

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| thugattack.yaml | ThugAttack | employment | SeverActions_Travel.ThugAttack_Execute | The ambush pack turns to violence after a refused settlement or drawn weapon |
| thugstanddown.yaml | ThugStandDown | employment | SeverActions_Travel.ThugStandDown_Execute | The thugs back off after being paid off, intimidated or talked down |

# Related

- Retainer, steward, camp and treasury state prompts: [/prompts/enterprises.md](/prompts/enterprises.md)
- Weekly settlements, wages and arrears flow through the Currency script: [/scripts/economy-crafting.md](/scripts/economy-crafting.md)
- Shared debt and payment machinery with the Economy module: [/actions/economy.md](/actions/economy.md)

# Citations

[1] `sources/SeverActions/Actions/Enterprises/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
