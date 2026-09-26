---
type: Actions
title: Arrest Actions
description: Bounty tracking, arrest, cross-cell dispatch, escort pleas and judgment actions of the Arrest module.
resource: 'sources/SeverActions/Actions/Arrest'
tags: [actions, skyrimnet, arrest, bounty, guards, jail, crime]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Arrest module (FOMOD option "Arrest Actions", optional) implements the working crime system: guards log bounties, arrest suspects, dispatch across cells with off-screen escort, investigate homes for evidence, confront the player over an existing bounty, and pass judgment on delivered prisoners. Execution functions are split across SeverActions_ArrestBounty (the ledger), SeverActions_Arrest (arrest, dispatch, escort), SeverActions_ArrestPlayer (player confrontation) and SeverActions_ArrestJudgment (judgment phase).

The module ships 15 YAMLs — 14 executable actions plus the `cat_arrest` category file.

# Member Actions

## Bounty ledger

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| cat_arrest.yaml | Arrest | arrest | — | Category file grouping all law-enforcement actions |
| addbountytoplayer.yaml | AddBountyToPlayer | arrest | SeverActions_ArrestBounty.AddBountyToPlayer_Internal | Log a witnessed crime against the player in this hold — the precondition for ArrestPlayer |
| paynpcbountytoguard.yaml | PayNpcBountyToGuard | arrest | SeverActions_ArrestBounty.PayNpcBountyToGuard_Internal | The player pays a guard to clear another person's tracked bounty |

## Arrest and dispatch

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| arrestnpc.yaml | ArrestNPC | arrest | SeverActions_Arrest.ArrestNPC_Internal | Cuff and march a present suspect off to the cells |
| dispatchguardtoarrest.yaml | DispatchGuardToArrest | arrest | SeverActions_Arrest.DispatchGuardToArrest_Execute | Send a guard across the hold to track down a named suspect and bring them in |
| dispatchguardtohome.yaml | DispatchGuardToHome | arrest | SeverActions_Arrest.DispatchGuardToHome_Execute | Send a guard to search a suspect's home containers for evidence |

## Escort and pleas

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| appealduringescort.yaml | AppealDuringEscort | arrest | SeverActions_Arrest.AppealDuringEscort_Internal | A prisoner being escorted makes a last plea — innocence, bribe, mercy |
| acceptescortplea.yaml | AcceptEscortPlea | arrest | SeverActions_Arrest.AcceptEscortPlea_Internal | The escorting guard genuinely accepts the plea; cuffs come off and the hold bounty is wiped |
| rejectescortplea.yaml | RejectEscortPlea | arrest | SeverActions_Arrest.RejectEscortPlea_Internal | The guard is not having any of it; the march to the cells resumes |

## Player confrontation

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| arrestplayer.yaml | ArrestPlayer | arrest | SeverActions_ArrestPlayer.ArrestPlayer_Internal | Confront the player over an existing bounty; light bounties settle on the spot, over 300g they can submit, resist, bribe or talk |
| acceptpersuasion.yaml | AcceptPersuasion | arrest | SeverActions_ArrestPlayer.AcceptPersuasion_Internal | The guard is genuinely convinced during a bounty confrontation and waves the player on |
| rejectpersuasion.yaml | RejectPersuasion | arrest | SeverActions_ArrestPlayer.RejectPersuasion_Internal | The argument fails; the confrontation moves to submit-or-resist |

## Judgment and release

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| orderjailed.yaml | OrderJailed | arrest | SeverActions_ArrestJudgment.OrderJailed_Execute | A jarl or magistrate finds against a prisoner standing judgment after a dispatch |
| orderrelease.yaml | OrderRelease | arrest | SeverActions_ArrestJudgment.OrderRelease_Execute | The charges are found thin and the prisoner walks |
| freefromjail.yaml | FreeFromJail | arrest | SeverActions_Arrest.FreeNPC_Internal | Release an NPC already sitting in a hold's cell — sentence served, pardon, or favor |

# Flow Notes

- AddBountyToPlayer must fire first; ArrestPlayer only works once a bounty exists on the books.
- DispatchGuardToArrest routes the suspect to judgment (OrderJailed / OrderRelease); FreeFromJail is for an NPC already serving in a cell.
- Escort pleas (AppealDuringEscort answered by Accept/RejectEscortPlea) can end an escort with the hold bounty wiped.
- PayNpcBountyToGuard is a legal bounty settlement — deliberately distinct from the Economy module's CollectPayment, which is for merchant tabs.

# Related

- Bounty ledger, judgment and player-arrest scripts: [/scripts/crime.md](/scripts/crime.md)
- Bounty, warrant and jail status prompts: [/prompts/arrest.md](/prompts/arrest.md)

# Citations

[1] `sources/SeverActions/Actions/Arrest/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
