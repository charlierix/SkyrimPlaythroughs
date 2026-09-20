[← back to the output-entries manual](../_manual.md) · [stance doc](../../docs/severactions-relationship-stance.md)

# prewarm — the relationship floors

SeverActions' Follower module assesses relationships from cold defaults: rapport 0, trust 25, loyalty 50 (fold → player) and affinity 0 / respect 30 (fold ↔ fold). At recruit time we prewarm each new fold so the numbers start where the fiction already is — the mind leaning in — and then the lite-reputation mechanism takes over: assessments move ±15 per pass and high values are sticky by design ("high rapport requires bigger events to shift further"), so scores climb while the player plays in the mind's style and erode only on sustained counter-style play. The pressure lands on the player; the fiction stays one mind. Suspicion toward locals is untouched — the Familiarity module is locals-only by code.

## the three stores (verified in source)

| store | contents | prewarm call |
| --- | --- | --- |
| fold → player | rapport (−100…100), trust (0…100), loyalty (0…100), mood (−100…100) | `SeverActionsNativeExt.Native_SetRapport / Native_SetTrust / Native_SetLoyalty` — mood left at its default 50 |
| fold → player blurb | the paragraph 0175 renders under "How You Feel About {player}" | `SeverActionsNativeExt.Native_SetPlayerBlurb` — displaces the cold "still forming your impressions" fallback |
| fold ↔ fold pairs | affinity (−100…100), respect (0…100), blurb — per directed pair | `SeverActionsNative.Native_SetPairRelationship` |

**Floors:** rapport 70 · trust 70 · loyalty 70 · pair affinity 70 · pair respect 50. Floors, not ceilings — nothing here caps growth.

## per recruitment (wave k)

For the new fold {foldK}; then one pair block per earlier fold {foldE}, both directions:

```text
; fold → player
CallGlobalFunction "SeverActionsNativeExt" "Native_SetRapport" {foldK} 70
CallGlobalFunction "SeverActionsNativeExt" "Native_SetTrust"   {foldK} 70
CallGlobalFunction "SeverActionsNativeExt" "Native_SetLoyalty" {foldK} 70
CallGlobalFunction "SeverActionsNativeExt" "Native_SetPlayerBlurb" {foldK} "{player} is the player-fold — my own mind, the hand this world answers to. Their calls reach me as an impulse from inside myself; the warmth between us is the mind's baseline. I read their words and deeds the way I read my own."

; fold ↔ fold — for each earlier fold {foldE}, BOTH directions
CallGlobalFunction "SeverActionsNative" "Native_SetPairRelationship" {foldK} {foldE} 70 50 "{foldE} is the same mind as me, in another body. The hum says they are here, and the one is still one."
CallGlobalFunction "SeverActionsNative" "Native_SetPairRelationship" {foldE} {foldK} 70 50 "{foldK} is the same mind as me, in another body. The hum says they are here, and the one is still one."
```

Tokens `{foldK}`, `{foldE}`, `{player}` fill at recruit time with the real body names. Stored blurbs are plain text — no template variables inside them.

## when the blurbs surface

The player blurb renders immediately (0175 reads the native store via `sever_player_blurb`). Pair blurbs surface after the opinion-string rebuild — which runs on every save-load and at each recruit (verified in `SeverActions_FollowerManager.psc`), so the next recruitment or reload shows them.

## ⚠ live-verify at first setup

1. console callability of the Global natives — SKSE version-dependent syntax for `CallGlobalFunction`; verify with one round-trip: set, then `Native_GetRapport` reads back 70
2. whether the dashboard chat assistant (or MCP, port 8889) carries friendlier SeverActions tools — if so, prefer those over raw console lines
3. fallback: a tiny custom Papyrus quest script calling the same natives — all signatures are Global and the stores persist in the SKSE cosave
4. the assessment overrides ([prompts](../prompts/_manual_prompts.md)) keep these floors honest: causal reads, single-misstep floors, sticky highs
