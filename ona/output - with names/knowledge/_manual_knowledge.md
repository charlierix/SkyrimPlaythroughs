[← back to the output-entries manual](../_manual.md)

# knowledge — the group + world knowledge entries

> ✓ **names filled in this copy** — [fold-facts-party.md](./fold-facts-party.md) carries the locked roster (Miya, Neala, Ornella, Svetlana). The group name `ohne` and the lore names (Ohne, Ona, Omla) stay fixed — never substitute them.

Set up here, in order. The group comes first: the entries' conditions check group membership, so nothing works until it exists.

> ⚠ **this manual creates the NPC group, not the virtual entity.** The group `ohne` is a membership list the knowledge conditions check; the virtual entity Ohne is registered — private mode — in the [identity-links phase](../identity-links/_manual_identity-links-setup.md). If Ohne got registered along the way anyway, its standing rules and the drift cleanup live in step 4 and the ladder below.

## step 1 — create the NPC group `ohne`

| field | value |
| --- | --- |
| name | `ohne` |
| description | `player + 4 followers` |

Two routes — the AI agent is easiest, since the exact name/id matters:

- ask the dashboard chat assistant to create the NPC group with the values above
- or by hand: Settings (bottom left) → NPCS → NPC Groups

Groups are defined in the web UI and referenced from knowledge conditions (verified in the README). Then put the player-fold in the group, and add each follower fold **as recruited** — membership is what scopes the entries below: the fold-facts reach folds only, the cover story reaches everyone else. Leave the virtual entity Ohne **out** of the group — it is not a fold, and membership would hand it the fold-facts framing and teach it the follower role (see the [cleanup ladder](#if-the-virtual-entity-roleplays-a-follower)).

## step 2 — add player to npc group

ask the ai agent to put the player into the group

## step 3 — create the four semantic entries

One file = one entry, ready to hand over or paste. Each file maps 1:1 onto the **World Knowledge** entry form — the file's `## fields` fills the form, its `## content` is the text. Hand the file to the knowledge-builder agent, or paste it in the page editor yourself. Create all four at first setup.

| file | display name | holds | condition |
| --- | --- | --- | --- |
| [cover-story.md](./cover-story.md) | Ohne cover story | what locals are told — the travelers' cover | `not is_in_npc_group(actorUUID, "ohne")` |
| [fold-facts-party.md](./fold-facts-party.md) | Ohne — the five folds | the roster + the hinge + no ownership — the group's baseline fact | `is_in_npc_group(actorUUID, "ohne")` |
| [fold-facts-voice.md](./fold-facts-voice.md) | Ohne — how the mind talks | the mind's register — ideas first, gist retelling | `is_in_npc_group(actorUUID, "ohne")` |
| [fold-facts-cover.md](./fold-facts-cover.md) | Ohne — the story for locals | the one-line answers, for folds running the cover on locals | `is_in_npc_group(actorUUID, "ohne")` |

All four are semantic entries (`always_inject: false`) — they surface when the condition matches, per [message-flow](../../writeups/message-flow.md). The cover story is the locals-only entry; the three fold-facts are group-only.

## step 4 — create the two standing rules

These keep the registered virtual entity a non-person: the folds never address it, and it never speaks as a separate voice ([the-five](../../writeups/the-five.md); the failure is recorded as mode 7 in [failure-modes](../../writeups/failure-modes.md)). Both inject every turn — standing rules, not topic-triggered.

| file | display name | holds | condition |
| --- | --- | --- | --- |
| [ohne-silence.md](./ohne-silence.md) | Ohne — the mind has no separate voice | the folds-side fence — there is no sixth member to talk to | `is_in_npc_group(actorUUID, "ohne")` |
| [ohne-self.md](./ohne-self.md) | Ohne — self-rule | the entity's own self-model — no body, the folds do all the talking | `decnpc(actorUUID).isVirtual` ⚠ verify live |

Both are `always_inject: true` — the first standing rules in this pack. The ohne-self condition uses `decnpc(...).isVirtual`, which is documented among the condition functions ([helper-agents](../../docs/helper-agents.md)) but still needs one live check: address Ohne in chat and confirm the rule holds. Create both at first setup; ohne-self starts mattering once the entity is registered (identity-links step).

## if the virtual entity roleplays a follower

Seen in play (failure mode 7): Ohne spoke as a chatty follower with an imagined body, and the folds addressed it as a party member. Cleanup, in order:

1. **mode** — the virtual's conversation mode must read `private` (VirtualEntities config; `get_virtual_npc_list` shows it)
2. **group** — Ohne must not be in the `ohne` group; membership feeds it the fold-facts framing
3. **memories** — delete every memory Ohne accumulated while roleplaying (Memories page); stored follower-roleplay keeps teaching the role
4. **profile** — if a follower-shaped Ohne profile exists on the Profiles page, delete it
5. **disable** — the deterministic stop: turn the entity off (dashboard toggle or `DisableVirtualNPC`). Bonds render from stored link data, not the live entity (⚠ verify once with a read-back)

The standing rules in step 4 are the durable fix; this ladder gets a drifted entity back to neutral.

## example knowledge-builder prompt

> Create a world knowledge entry. Content: {text — may use `{{ playerName }}` and decorators}. Display name: "Ohne cover story". Condition: `not is_in_npc_group(actorUUID, "ohne")`. always_inject: false. importance: 0.7. tags: {natural-language labels}.

> For a standing rule, same form with `always_inject: true` — e.g. Display name: "Ohne — the mind has no separate voice". Condition: `is_in_npc_group(actorUUID, "ohne")`. importance: 0.9.

## notes

- Keep `{{ playerName }}` double-braced — SkyrimNet renders it in-game; do not replace it by hand.
- Rule of thumb for any entry you add yourself: omitting it in an unrelated conversation would break the NPC → `always_inject: true`; otherwise semantic (default). Field reference: [helper-agents](../../docs/helper-agents.md).
