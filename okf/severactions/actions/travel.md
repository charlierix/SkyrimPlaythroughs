---
type: Actions
title: Travel Actions
description: Departure, pace and cancellation actions of the Travel module.
resource: 'sources/SeverActions/Actions/Travel'
tags: [actions, skyrimnet, travel, off-screen]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Travel module (FOMOD option "Travel Actions", recommended) lets an NPC leave right now for a named destination: the trip is simulated off-screen across unloaded cells, with adjustable pace and a non-pausing confirmation popup for the player-facing variant. All execution functions live in SeverActions_Travel ([/scripts/magic-travel.md](/scripts/magic-travel.md)); speed constants mirror the native TravelSpeed enum, and the stuck-detector falls back to distance checks on VR.

The module ships 3 YAMLs, all executable (no category file).

# Member Actions

| File | Action | Script.Function | Purpose |
|---|---|---|---|---|
| canceltravel.yaml | CancelTravel | SeverActions_Travel.CancelTravel | Call off a trip decided in this conversation; the speaker stays where they are |
| changetravelspeed.yaml | ChangeTravelSpeed | SeverActions_Travel.SetTravelSpeedNatural | Change pace during a trip already underway — urgent news, scenic stretch, dangerous road |
| traveltoplace.yaml | TravelToPlace | SeverActions_Travel.TravelToPlace | Leave right now, on foot, for a destination — only when the trip is firmly decided |

# Eligibility Notes

- TravelToPlace never fires merely because a place was mentioned, remembered, or wondered about — that lesson is the v3.9.13 release theme (followers no longer march off on musings; excluded by default with a Followers-Can-Travel toggle).
- The v3.7.1 overhaul added the wait-vs-errand parameter (greet-on-arrival vs free time) and conversational destination resolution.
- Off-screen simulation and destination data (road network) relate to [/systems/native-plugin.md](/systems/native-plugin.md) and [/configs/data-store.md](/configs/data-store.md).

# Citations

[1] `sources/SeverActions/Actions/Travel/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
