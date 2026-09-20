[← identity-links — recruit manual](_manual_identity-links-recruit.md) · full trace: [docs/identity-links](../../docs/identity-links.md)

# bonds — the 20 directed bonds, in recruitment waves

Five bodies, each bonded to the other four: 20 directed links, rendered by `submodules/character_bio/7050_identity_links.prompt` — each fold's bio renders its own four. Created wave by wave as folds are recruited: recruitment *k* adds the new fold's bond to the player-fold and to every earlier fold, in both directions.

## fixed values (every link)

| field | value |
| --- | --- |
| `shared_virtual` | `Ohne` — the mind both bodies belong to. Register the virtual entity under that name at first setup; if the surface wants a uuid, it derives from the registration name (`GetVirtualNPCUUID("Ohne")`) and stays stable across sessions |
| `sees_their_memories` | `false` — gaps are the texture; retelling closes them ([message-flow](../../writeups/message-flow.md)) |
| `is_present` | runtime — `true` whenever both folds share a scene; both mouths may speak |
| `custom_framing` | not offered on the shared_virtual branch — its framing text is fixed; if it fights the voice set, override `7050_identity_links.prompt` itself ([prompts](../prompts/_manual_prompts.md)) |

## names and uuids

- `to name` — filled with the locked roster: player-fold = Ingrid, fold1 = Miya, fold2 = Neala, fold3 = Ornella, fold4 = Svetlana. Names are enough everywhere except the next field.
- `to uuid` — the one field that needs a real ID: nothing resolves a link by name. Fetch each body's UUID at recruit time — `GetEntityUUID(Actor)` or read it off the dashboard — and paste it in.
- `player-fold`, `fold1`–`fold4` labels are recruit order.

## wave 1 — Miya recruited (+2)

| # | from (bio that renders the bond) | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 1 | player-fold | fold1 | Miya | {uuid} |
| 2 | fold1 | player-fold | Ingrid | {uuid} |

## wave 2 — Neala recruited (+4)

| # | from | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 3 | player-fold | fold2 | Neala | {uuid} |
| 4 | fold2 | player-fold | Ingrid | {uuid} |
| 5 | fold1 | fold2 | Neala | {uuid} |
| 6 | fold2 | fold1 | Miya | {uuid} |

## wave 3 — Ornella recruited (+6)

| # | from | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 7 | player-fold | fold3 | Ornella | {uuid} |
| 8 | fold3 | player-fold | Ingrid | {uuid} |
| 9 | fold1 | fold3 | Ornella | {uuid} |
| 10 | fold3 | fold1 | Miya | {uuid} |
| 11 | fold2 | fold3 | Ornella | {uuid} |
| 12 | fold3 | fold2 | Neala | {uuid} |

## wave 4 — Svetlana recruited (+8, party complete)

| # | from | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 13 | player-fold | fold4 | Svetlana | {uuid} |
| 14 | fold4 | player-fold | Ingrid | {uuid} |
| 15 | fold1 | fold4 | Svetlana | {uuid} |
| 16 | fold4 | fold1 | Miya | {uuid} |
| 17 | fold2 | fold4 | Svetlana | {uuid} |
| 18 | fold4 | fold2 | Neala | {uuid} |
| 19 | fold3 | fold4 | Ornella | {uuid} |
| 20 | fold4 | fold3 | Ornella | {uuid} |

2 + 4 + 6 + 8 = 20. Each wave doubles as the per-recruitment checklist: at recruitment *k*, create wave *k*'s links before leaving town.

## creation — dashboard only (chat assistant verifies)

1. dashboard → Settings → NPCs → Identity Links (localhost:8080) — the only creation surface; the chat assistant has no creation tool and no MCP branch ([setup manual](./_manual_identity-links-setup.md) holds the smoke test)
2. after each wave, ask the chat assistant to read the new bonds back via `get_linked_identities` — confirm the "One Soul, Two Bodies" framing renders
3. if the UI can't express a bond or the framing misrenders: override `submodules/character_bio/7050_identity_links.prompt` with the bonds hard-coded (see [prompts](../prompts/_manual_prompts.md))
