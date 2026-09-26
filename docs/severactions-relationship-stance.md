# severactions relationship stance — decided and wired

The question parked in [attribution](../writeups/attribution.md): SeverActions' relationship machinery vs the mind's absolute trust. **Decided:** keep SeverActions installed; prewarm warm floors; override the Follower module's three fold-facing prompts. The player wanted a lite reputation requirement — scores start warm, climb while play stays in the mind's style, erode only on sustained counter-style play. The pressure lands on the player; the fiction stays one mind. Suspicion toward locals stays fully available (the Familiarity module keeps it).

## what the source says (verified)

| module | mechanism | fold exposure |
| --- | --- | --- |
| Familiarity (FOMOD "NPC Familiarity & Reputation") | familiarity tiers stranger→familiar, name awareness, reputation blurbs; wariness prose in tier branches | **none — `0045_severactions_familiarity.prompt` hard-gates `{% if not is_follower(actorUUID) ... %}`; locals only by code**. Keep installed. |
| Follower module bio (`0175_severactions_follower.prompt`) | player blurb (or cold "still forming your impressions" fallback), companion opinions, **Companion Behavior Guidelines** ("refuse orders you distrust", "threaten to leave") | the commander frame — contradicts [the-hinge](../writeups/the-hinge.md); overridden fold-gated |
| `sever_relationship_assess.prompt` (background) | companion→player rapport/trust/loyalty ±15, mood ±20; the blurb is what the fold "sees" of its own feelings | the lite-reputation engine |
| `sever_relationship_interfollower.prompt` (background) | fold↔fold affinity (start 0) / respect (start 30); "conflicting values erode both" | the fold↔fold spiral vector — overridden: linked folds omitted from pairs |

## state stores and prewarm (verified signatures)

| call | script | notes |
| --- | --- | --- |
| `Native_SetRapport / SetTrust / SetLoyalty / SetMood(Actor, Float)` | SeverActionsNativeExt.psc | backing keys `SeverFollower_Rapport/Trust/Loyalty/Mood`, SKSE cosave |
| `Native_SetPlayerBlurb(Actor, String)` | SeverActionsNativeExt.psc | rendered by 0175 via `sever_player_blurb` |
| `Native_SetPairRelationship(Actor, Actor, Float, Float, String)` | SeverActionsNative.psc | directed pair store; clamps affinity ±100, respect 0–100 |
| opinion-string rebuild | FollowerManager.psc | `RebuildAllCompanionOpinions` runs on every load and at recruit |

Defaults for contrast: rapport 0, trust 25, loyalty 50, mood 50; pair affinity 0, respect 30. Prewarm floors: 70/70/70 (mood untouched) and 70/50 per pair — set in the per-recruit batch at [prewarm](<../output entries/prewarm/_manual_prewarm.md>).

## the overrides (full replacement texts)

| file | base | change |
| --- | --- | --- |
| [follower-0175](<../output entries/prompts/follower-0175.md>) | `submodules/character_bio/0175_severactions_follower.prompt` | fold-gated on `get_linked_identities`: mind-frame fallbacks + behavior guidelines; non-fold followers keep stock text |
| [relationship-assess](<../output entries/prompts/relationship-assess.md>) | `sever_relationship_assess.prompt` | fold-context line + fold rules: causal reads, single-misstep floors, sticky highs, mind-voiced blurb |
| [interfollower-assess](<../output entries/prompts/interfollower-assess.md>) | `sever_relationship_interfollower.prompt` | identity-linked folds omitted from pairs — bonds authored, never eroded, no blurb |

All three ship into `overlay/prompts/` at the same path (saves > overlay > plugins). Base text carried verbatim; deltas are brace-verified against the sources.

## reconciliation with attribution

The fiction keeps its one line — the mind does not withhold from itself, and no fold ever suspects a fold. What stays dynamic is the mind's warmth responding to how its own hand is carried: the assessment machinery measures the player-fold's conduct, and the fold-side floor (70s, never eroding between folds) keeps the framework from ever writing doubt into the one.

## live-verify at first setup

1. console callability of the Global natives (syntax + registration) — one round-trip test: set, then read back
2. `get_linked_identities` inside 0175's and the assessments' render contexts — validation panel
3. assessment cadence (MCM) once scores are observable in play
