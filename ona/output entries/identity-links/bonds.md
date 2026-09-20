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

- `to name` — a `{foldN}` / `{player}` token, filled at injection with the body's name. Names are enough everywhere except the next field.
- `to uuid` — the one field that needs a real ID: nothing resolves a link by name. Fetch each body's UUID at recruit time — `GetEntityUUID(Actor)` or read it off the dashboard — and paste it in.
- `player-fold`, `fold1`–`fold4` labels are recruit order.

## wave 1 — first fold recruited (+2)

| # | from (bio that renders the bond) | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 1 | player-fold | fold1 | {fold1} | {uuid} |
| 2 | fold1 | player-fold | {player} | {uuid} |

## wave 2 — second fold recruited (+4)

| # | from | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 3 | player-fold | fold2 | {fold2} | {uuid} |
| 4 | fold2 | player-fold | {player} | {uuid} |
| 5 | fold1 | fold2 | {fold2} | {uuid} |
| 6 | fold2 | fold1 | {fold1} | {uuid} |

## wave 3 — third fold recruited (+6)

| # | from | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 7 | player-fold | fold3 | {fold3} | {uuid} |
| 8 | fold3 | player-fold | {player} | {uuid} |
| 9 | fold1 | fold3 | {fold3} | {uuid} |
| 10 | fold3 | fold1 | {fold1} | {uuid} |
| 11 | fold2 | fold3 | {fold3} | {uuid} |
| 12 | fold3 | fold2 | {fold2} | {uuid} |

## wave 4 — fourth fold recruited (+8, party complete)

| # | from | to | to name | to uuid |
| --- | --- | --- | --- | --- |
| 13 | player-fold | fold4 | {fold4} | {uuid} |
| 14 | fold4 | player-fold | {player} | {uuid} |
| 15 | fold1 | fold4 | {fold4} | {uuid} |
| 16 | fold4 | fold1 | {fold1} | {uuid} |
| 17 | fold2 | fold4 | {fold4} | {uuid} |
| 18 | fold4 | fold2 | {fold2} | {uuid} |
| 19 | fold3 | fold4 | {fold3} | {uuid} |
| 20 | fold4 | fold3 | {fold3} | {uuid} |

2 + 4 + 6 + 8 = 20. Each wave doubles as the per-recruitment checklist: at recruitment *k*, create wave *k*'s links before leaving town.

## creation ⚠ verify live

1. dashboard → VirtualEntities config (localhost:8080) — find link/bond creation
2. or ask the chat assistant which identity tools it carries (MCP, port 8889, is a possibility)
3. if neither exists: override `submodules/character_bio/7050_identity_links.prompt` with the bonds hard-coded (see [prompts](../prompts/_manual_prompts.md))
