---
type: Actions
title: "Kidnap & Captives Actions"
description: Abduction, restraint, ransom and interrogation actions of the Kidnap module.
resource: 'sources/SeverActions/Actions/Kidnap'
tags: [actions, skyrimnet, kidnap, captivity, ransom, dark-roleplay]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Kidnap module (FOMOD option "Kidnap and Captive Actions", optional; dark roleplay content split out from Follower Actions so it can be opted into separately) lets companions seize, hold, move, ransom and interrogate NPCs, with real crime consequences when a grab goes witnessed. Every execution function lives in SeverActions_FollowerManager, sharing apparatus with the follower and arrest systems. The README notes kidnap is opt-in while restrain ships on.

The module ships 9 YAMLs, all executable (no category file).

# Member Actions

| File | Action | Script.Function | Purpose |
|---|---|---|---|---|
| demandransom.yaml | DemandRansom | SeverActions_FollowerManager.DemandRansom | Send a ransom demand to the captive's home hold; the answer returns by courier — payment scaled by the captive's standing, or refusal and searchers |
| interrogatecaptive.yaml | InterrogateCaptive | SeverActions_FollowerManager.InterrogateCaptive | Press a held captive for secrets; resolve cracks and their own knowledge becomes fair game in conversation |
| kidnapnpc.yaml | KidnapNPC | SeverActions_FollowerManager.KidnapNPC | Quietly abduct a named NPC to a named destination — bound and hooded, tied on arrival |
| leashcaptive.yaml | LeashCaptive | SeverActions_FollowerManager.LeashCaptiveByName | Bring a held, bound captive along — hands stay tied, they walk behind you |
| movecaptive.yaml | MoveCaptive | SeverActions_FollowerManager.MoveCaptive | Untie, march to a new location, bind again there |
| releasecaptive.yaml | ReleaseCaptive | SeverActions_FollowerManager.ReleaseCaptive | Cut bonds and end the captivity for good |
| restrainnpc.yaml | RestrainNPC | SeverActions_FollowerManager.RestrainNPC | Bind someone's hands and hold them standing — the lighter in-the-open variant, no crime |
| unleashcaptive.yaml | UnleashCaptive | SeverActions_FollowerManager.UnleashCaptiveByName | Stop leading a leashed captive and hold them where they stand |
| untiecaptive.yaml | UntieCaptive | SeverActions_FollowerManager.UntieCaptive | Loosen bonds without freeing — hood and ties off, watched but mobile |

# Eligibility Notes

- KidnapNPC requires an explicit player order naming both target and destination; jailed prisoners, active arrests, the player's followers and children are off-limits as targets.
- Captives are people, not props: a held NPC knows they are bound and narrates from inside the hood; an unwatched unbound captive escapes far more easily.
- Captive state (binding, holding, ransom status) lives in the native co-save stores — see [/systems/native-plugin.md](/systems/native-plugin.md).
- Situation awareness for victim and kidnapper comes from the kidnap prompt in the Follower module: [/prompts/follower.md](/prompts/follower.md).

# Citations

[1] `sources/SeverActions/Actions/Kidnap/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
[2] `fomod/ModuleConfig.xml` — Kidnap and Captive Actions description
