---
type: Reference
title: Version History
description: All 39 releases of SeverActions from v0.88 to v3.9.13 with their themes and headline changes.
resource: "sources/SeverActions/CHANGELOG.md"
tags: [changelog, history, releases]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The changelog lists **39 versions**, newest first, with narrative release notes. No calendar dates are given; the current version is **3.9.13** (also recorded in `fomod/info.xml` and `SeverActionsNative.toml`).

# Release History

| Version | Theme | Headline changes |
|---|---|---|
| v3.9.13 | Settling In | Followers excluded from travel action by default (+toggle); dressing saves auto-named outfit presets; home outfits switch in any player house; NFF-follower relax fix; familiarity blurb update button + fixes; wheel-menu key closes menu; VR travel crash fix (IsPathing); outfit auto-switch frame-spreading; situation-switch fixes; "home" = inside the house; Bio Blocks MCM page + 78-block starter library |
| v3.9.11 | The quartermaster's ledger | Fix new-game/autosave crash from a wrong flag on the Levy's hidden deployment-room cell |
| v3.9.10 | Housekeeping | Clear Home (Target) hotkey; ambient director keeps townsfolk trading locally; xEdit false positives on the Levy soldiers cleared |
| v3.9.9 | Whose follower is this? | NFF-routed recruit/dismiss/wait/resume; camp registration fixes; LightFoot trap immunity; steward walk-arounds; template-shout teaching fix; beef-stew bow swap removed; brawl overhaul; Bio Blocks library page; live retainer locations; roster cap raised to 500 |
| v3.9.2 | The camp asks your business | Pacified-camp door challenge; the verdict belongs to the outlaw (LetThemPass / RunThemOff); boss-chest plunder turns the camp; break propagation by roster; three new Outlaws settings |
| v3.9.0 | Outlaws, industry, and the Voice | Outlaw truce layer default-on, runtime-only and fully recorded/reversible; camp swearing, mustering and morale; the Voice; biggest release since Enterprises |
| v3.8.0 | Fullscreen UI, per-retainer schedules, alias overhaul | PrismaUI true fullscreen with auto-proportional density; per-retainer work hours incl. 24h bodyguard duty for any NPC; follow alias overhaul |
| v3.7.3 | Custom-AI follower fix | Custom-AI followers no longer stuck on home/play packages mid-follow |
| v3.7.2 | Pay off NPC bounties | PayNpcBountyToGuard from UI and dialogue; brawl spell-recovery safety net |
| v3.7.1 | Custom bios, LLM trespass, travel overhaul | Per-companion custom bio blocks; LLM-driven trespass replacing scripted threat-stalking; travel wait-vs-errand parameter and phrasing resolution |
| v3.5.0 | Abduction & restraint, morale with teeth | Kidnap/restraint systems, per-offender NPC bounties, ransom negotiation, interrogation, escape and consequences; stability pass |
| v3.1.1 | Follower reliability, clearer arrangements | Recruiting working NPCs follows; Vassalage→Indentured, Sworn→Retained with valence colours; Dawnguard/Dragonborn masters dropped |
| v3.1.0 | Enterprises | Retainers running off-screen ventures; Employed/Partnership/Tribute arrangements; arrears→desertion; fences with heat and jail; courier letters; player-placed camp |
| v3.0.7 | Mannequin fidelity | Skin subsurface/specular, SKEE overlays, makeup tint, warpaint; transparent-viewport fallback; outfit-menu crash fix; camp reliability |
| v3.0.5 | Outfits, followers, arrest, survival fixes | Mannequin crash pass; ghost presets cleaned; stronger follower catch-up with track-only toggle; arrest-eligibility fix |
| v3.0.1 | Skyrim VR support | Universal SE/AE/VR DLLs (CommonLibVR); VR startup deadlock and main-menu crash fixes; outfit EditorID fallback; survival warmth fallback |
| v3.0 | Hearth Ledger, native cosave, arrest overhaul, brawl | Six-page UI rebuild; outfit subsystem rebuilt on a native cosave store; full arrest pipeline; fist-fight brawl system |
| v2.9.9 | SkyrimNet Bio Audit Tier 1 | 55 priority character bios de-primed (speech_style priming, summary spoilers) |
| v2.9.5 | Cross-cell follower teleport | Catch-up teleport across doors/cell boundaries; v2.1.7 aggression self-heal; outfit fixes (blacklist, rename, slot orphan cleanup, fuzzy matching) |
| v2.9 | Outfit slot system | 50 followers × 8 preset bays (400 slot×preset triplets in the ESP); animated CastSpell; Daegon Kaekiri compat patch |
| v2.7.0 | Cowering fix & prompt cleanup | Cowering mitigations; familiarity dedup; prompt-stack simplification; PrismaUI survival CSS; FOMOD target-selectors fix |
| v2.5 | Cowering regression hunt | AIO patch rebuilt against the real ESP; follow template repairs; 2.1.7 confidence/aggression revert; ESP persistent-flag and orphan-record cleanup |
| v2.2 | NPC knowledge rewrite | Single What-You-Know block combining familiarity tiers and role-based reputation |
| v2.0.7 | Outfit exclusion & lock fixes | Per-follower outfit bypass toggle; re-equip loop guard; stale-lock and unbound-native fixes; survival template fix |
| v2.0.6 | Manual-lock & sandbox fixes | DefaultOutfit suppression scoping; auto-sandbox deadlock fix; direct-address dialogue rule |
| v2.0.5 | Outfit builder & follower QoL | Inventory-only builder mode; optimistic equip UI; follower soft reset; teleport behind player; global teleport cooldown |
| v2.0 | Quest awareness | Firsthand/secondhand/unaware tiers; objective-driven LLM narratives; permanent SkyrimNet memories |
| v1.95 | Banter & dialogue | Follower banter; anti-fixation and topic passthrough; PrismaUI pause; relationship blurb; injection-mode toggle |
| v1.9 | Conditional knowledge | KnowledgeStore with cosave; World page revamp (bounties, debts, knowledge) |
| v1.8 | Property & followers | Property ownership system; two-mode follower refactor; off-screen life; essential toggle; NFF-safe recruitment |
| v1.6 | Inventory & actions | Inventory manager with transfer/equip/destroy; vanilla recruitment routing; actions page overhaul |
| v1.1 | Custom AI | Custom AI detection; PrismaUI improvements |
| v1.0 | Dashboard & homes | PrismaUI config dashboard; home system; inter-follower relationships |
| v0.99 | Foundations | Loot transfer; self-healing follow; speaker selector; relationship assessment; group conversation rewrite |
| v0.98 | Debt | Debt system; outfit lock; anti-duplicate actions |
| v0.95 | Outfits & hotkeys | Outfit persistence; consolidated wait; hotkeys; wheel menu; EFF support |
| v0.91 | Framework | Follower framework; outfit manager overhaul; yield monitor |
| v0.90 | Reading & dispatch | Book reading; guard dispatch overhaul; NND integration |
| v0.88 | Initial release | First public version |

# Notes

- Release arcs worth knowing: the outfit saga (v0.95 lock → v2.9 slots → v3.0 native cosave), the v3.0 arrest/brawl overhaul, Enterprises (v3.1.0), abduction (v3.5.0), and the v3.9.x outlaw-truce line.
- Some versions contain detailed root-cause hunts (v2.5 cowering, v2.0.7 re-equip loop, v3.9.13 VR travel) — useful precedent for engine-interaction debugging.

# Citations

[1] `sources/SeverActions/CHANGELOG.md`
