[← back to the output-entries manual](../_manual.md)

# identity links — bonding at recruitment

> ⚠ **runtime fill needed** — [bonds.md](./bonds.md) takes `{fold1}`…`{fold4}` / `{player}` for the name columns **and one real `{uuid}` per row**, fetched live at recruit time (dashboard or `GetEntityUUID(Actor)`). Nothing in this folder can be pre-filled before the bodies exist.

The prerequisite is already taken care of at this point: the virtual entity Ohne is registered and the link-creation surface is verified — initial setup handled it (see [identity links — setup](./_manual_identity-links-setup.md)).

## per recruitment — bond the new fold

When a fold is recruited, create its rows from [bonds.md](./bonds.md): links to the player-fold and to every earlier fold, each bond in both directions. Each row needs the other body's real `{uuid}` — dashboard or `GetEntityUUID(Actor)` at recruit time.

Per-link values:

| field | value |
| --- | --- |
| `shared_virtual` | Ohne — the mind both bodies belong to |
| `sees_their_memories` | false — gaps are the texture; retelling closes them ([message-flow](../../writeups/message-flow.md)) |
| `is_present` | runtime — both mouths may speak when the party shares a scene |
| `name`, `uuid` | the other fold |

The shared_virtual framing text is fixed — `custom_framing` is not offered on that branch. If it ever fights the voice set, the fallback is overriding `7050_identity_links.prompt` itself (see [prompts](../prompts/_manual_prompts.md)).

Bonding per recruitment means every fold arrives already bonded to the minds it came from; doing all 20 at once after the party is complete also works if the surface makes it easier.

## files (next pass)

- `bonds.md` — all 20 directed links in one table
