[← back to the output-entries manual](../_manual.md)

# knowledge — the group + world knowledge entries

> ⚠ **runtime fill needed** — [fold-facts-party.md](./fold-facts-party.md) takes `{fold1}`…`{fold4}` (follower names in recruit order); fill as the party grows. The group name `ohne` and the lore names (Ohne, Ona, Omla) ship fixed — never substitute them.

Two things to set up here, in order — both at first setup. The group comes first: the entries' conditions check group membership, so nothing works until it exists.

## step 1 — create the NPC group `ohne`

| field | value |
| --- | --- |
| name | `ohne` |
| description | `player + 4 followers` |

Two routes — the AI agent is easiest, since the exact name/id matters:

- ask the dashboard chat assistant to create the NPC group with the values above
- or by hand: Settings (bottom left) → NPCS → NPC Groups

Groups are defined in the web UI and referenced from knowledge conditions (verified in the README). Then put the player-fold in the group, and add each follower fold **as recruited** — membership is what scopes the entries below: the fold-facts reach folds only, the cover story reaches everyone else.

## step 2 — add player to npc group

ask the ai agent to put the player into the group

## step 3 — create the four knowledge entries

One file = one entry, ready to hand over or paste. Each file maps 1:1 onto the **World Knowledge** entry form — the file's `## fields` fills the form, its `## content` is the text. Hand the file to the knowledge-builder agent, or paste it in the page editor yourself. Create all four at first setup.

| file | display name | holds | condition |
| --- | --- | --- | --- |
| [cover-story.md](./cover-story.md) | Ohne cover story | what locals are told — the travelers' cover | `not is_in_npc_group(actorUUID, "ohne")` |
| [fold-facts-party.md](./fold-facts-party.md) | Ohne — the five folds | the roster + the hinge + no ownership — the group's baseline fact | `is_in_npc_group(actorUUID, "ohne")` |
| [fold-facts-voice.md](./fold-facts-voice.md) | Ohne — how the mind talks | the mind's register — ideas first, gist retelling | `is_in_npc_group(actorUUID, "ohne")` |
| [fold-facts-cover.md](./fold-facts-cover.md) | Ohne — the story for locals | the one-line answers, for folds running the cover on locals | `is_in_npc_group(actorUUID, "ohne")` |

All four are semantic entries (`always_inject: false`) — they surface when the condition matches, per [message-flow](../../writeups/message-flow.md). The cover story is the locals-only entry; the three fold-facts are group-only.

## example knowledge-builder prompt

> Create a world knowledge entry. Content: {text — may use `{{ playerName }}` and decorators}. Display name: "Ohne cover story". Condition: `not is_in_npc_group(actorUUID, "ohne")`. always_inject: false. importance: 0.7. tags: {natural-language labels}.

## notes

- Keep `{{ playerName }}` double-braced — SkyrimNet renders it in-game; do not replace it by hand.
- Rule of thumb for any entry you add yourself: omitting it in an unrelated conversation would break the NPC → `always_inject: true`; otherwise semantic (default). Field reference: [helper-agents](../../docs/helper-agents.md).
