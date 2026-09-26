---
type: ESP Record — Package
title: "ESP Packages"
description: "Nine package records (with templates) driving NPC dialogue, player dialogue, follow and talk-to-player behavior."
resource: "sources/SkyrimNet-GamePlugin/spriggit/SkyrimNet/Packages"
tags: [skyrimnet, esp, records]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

Nine package records (with their templates) driving NPC dialogue, player dialogue, follow and talk-to-player behavior. Example: `SkyrimNet_NPCDialoguePackage` (000004) is owned by the `skynet_MainController` quest (000802), extends template 000005, and targets the `SkyrimNet_DialogueTargetKeyword` linked reference (000002).

# Member records

All 9 member items assigned to this concept (verified against the manifest):

| Record file | FormKey | EditorID |
|---|---|---|
| `SkyrimNet_FollowPlayerPackage - 000E8E_SkyrimNet.esp.json` | `000E8E:SkyrimNet.esp` | SkyrimNet_FollowPlayerPackage |
| `SkyrimNet_FollowPlayerPackageTemplate - 000E8D_SkyrimNet.esp.json` | `000E8D:SkyrimNet.esp` | SkyrimNet_FollowPlayerPackageTemplate |
| `SkyrimNet_NPCDialoguePackage - 000004_SkyrimNet.esp.json` | `000004:SkyrimNet.esp` | SkyrimNet_NPCDialoguePackage |
| `SkyrimNet_NPCDialoguePackageTemplate - 000005_SkyrimNet.esp.json` | `000005:SkyrimNet.esp` | SkyrimNet_NPCDialoguePackageTemplate |
| `SkyrimNet_PlayerDialoguePackage - 000003_SkyrimNet.esp.json` | `000003:SkyrimNet.esp` | SkyrimNet_PlayerDialoguePackage |
| `SkyrimNet_PlayerDialoguePackageTemplate - 000001_SkyrimNet.esp.json` | `000001:SkyrimNet.esp` | SkyrimNet_PlayerDialoguePackageTemplate |
| `SkyrimNet_PlayerFollowPackage - 000008_SkyrimNet.esp.json` | `000008:SkyrimNet.esp` | SkyrimNet_PlayerFollowPackage |
| `SkyrimNet_PlayerFollowPackageTemplate - 000007_SkyrimNet.esp.json` | `000007:SkyrimNet.esp` | SkyrimNet_PlayerFollowPackageTemplate |
| `SkyrimNet_TalkToPlayerPackage - 000E9D_SkyrimNet.esp.json` | `000E9D:SkyrimNet.esp` | SkyrimNet_TalkToPlayerPackage |

# Related

- Packages select the [dialogue templates](/prompts/templates/dialogue.md).

# Citations

[1] `sources/SkyrimNet-GamePlugin/spriggit/SkyrimNet/Packages`

