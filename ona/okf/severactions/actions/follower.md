---
type: Actions
title: Follower Actions
description: Companion recruitment, waiting, dismissal, homes and combat-style actions of the Follower module.
resource: 'sources/SeverActions/Actions/Follower'
tags: [actions, skyrimnet, followers, companions, relationship]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Follower module (FOMOD option "Follower Actions", recommended) is the companion framework surface: making an NPC a registered companion, waiting and resuming, parting ways, assigning a home, tuning combat style and follow distance, and the rare relationship-driven outcome. Nearly everything executes in SeverActions_FollowerManager, with follow distance in SeverActions_Follow. Recruitment makes the NPC a proper Skyrim teammate and integrates with NFF/EFF when installed; relationship drift itself is not an action here — it is assessed by LLM background prompts.

The module ships 9 YAMLs, all executable (no category file).

# Member Actions

| File | Action | Script.Function | Enabled | Purpose |
|---|---|---|---|---|
| adjustrelationship.yaml | AdjustRelationship | SeverActions_FollowerManager.AdjustRelationship | false | Feelings shift after a meaningful moment together — shipped disabled; relationship is assessed by background prompts instead |
| assignhome.yaml | AssignHome | SeverActions_FollowerManager.AssignHome | true | Assign the follower a home — where they head back when dismissed |
| companionfollow.yaml | CompanionFollow | SeverActions_FollowerManager.CompanionFollow | true | A waiting companion shoulders their pack and falls back in step |
| companionwait.yaml | CompanionWait | SeverActions_FollowerManager.CompanionWait | true | Wait here until the player returns, wandering nearby on their own business |
| dismissfollower.yaml | DismissFollower | SeverActions_FollowerManager.DismissCompanion | true | Part ways amicably — they head home and can be re-recruited later |
| followerleaves.yaml | FollowerLeaves | SeverActions_FollowerManager.FollowerLeaves | true | The companion quits for good after severe, sustained mistreatment (extremely rare) |
| setcombatstyle.yaml | SetCombatStyle | SeverActions_FollowerManager.SetCombatStyle | true | How to fight from now on — hold the front, hang back at range, or keep allies healed |
| setcompanion.yaml | SetCompanion | SeverActions_FollowerManager.RegisterFollower | true | Agree to travel with the player as a registered companion — first sign-up or re-recruit |
| setfollowdistance.yaml | SetFollowDistance | SeverActions_Follow.SetFollowDistance | true | Trail closely ("close") or with comfortable travelling room ("normal") |

# Eligibility Notes

- SetCompanion (registration), CompanionFollow (resume after wait) and StartFollowing (casual follow, Basic module) are distinct verbs; DismissFollower is a parting, CompanionWait is not a farewell, FollowerLeaves only fires on collapsed relationships.
- When NFF owns the follower, recruit/dismiss/wait/resume route through NFF's own controller (v3.9.9) — see [/references/project-overview.md](/references/project-overview.md).
- The manager behind these verbs is documented in [/scripts/companions.md](/scripts/companions.md); companion-state prompts in [/prompts/follower.md](/prompts/follower.md).

# Citations

[1] `sources/SeverActions/Actions/Follower/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
