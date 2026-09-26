# prompt set — the task graph

[← proposal](../prompt-set-package.md) · [layout](./package-layout.md) · [importer brief](./importer-agent.md)

The machine-readable half: what the importer agent does, in order, against which surface, with which tokens and which read-back. Two phases: `prep` (once per playthrough) and `joiner` (per follower, repeatable).

## step object

```json
{
  "id": "joiner.bond",
  "title": "bond the joiner to every existing member",
  "surface": "dashboard",
  "helper": "chat-assistant",
  "page": "Identity Links",
  "input": "runtime/identity/bonds.md",
  "tokens": ["{joiner}", "{party}", "{uuid}"],
  "repeat": "per member, both directions",
  "verify": { "tool": "assistant", "call": "get_linked_identities", "expect": "shared_virtual={mind_name} on both actors" },
  "on_fail": "hard-code bonds into a 7050_identity_links.prompt override (decided at packaging)"
}
```

| field | meaning |
| --- | --- |
| `surface` | `dashboard` (page editor / config), `assistant` (chat assistant — verify-only), `console` (SKSE/Papyrus fallback), `agent` (the importer itself) |
| `helper` | optional — which in-game helper receives the instruction (`prompt-helper`, `knowledge-builder`, `chat-assistant`); the step carries the exact instruction text so nothing is improvised |
| `verify` | every step carries one; a step without its read-back is not done |
| `on_fail` | the declared fallback — chosen at packaging time |
| `repeat` | how the step fans out over live state |

## prep — once per playthrough

| # | id | surface | action | verify |
| --- | --- | --- | --- | --- |
| 1 | `prep.plugin` | dashboard | plugin layer active, External badge, no skipped files | page read |
| 2 | `prep.tokens` | agent | fill `{player}` + character tokens; fill-check all `runtime/` texts | grep for `{` tokens |
| 3 | `prep.group` | dashboard | group + knowledge entries present with the pack ⚠ | World Knowledge: 6 entries, Persistent badge |
| 4 | `prep.player-in-group` | dashboard | put the player-fold in `{party_group}` | page read |
| 5 | `prep.register-mind` | dashboard | register `{mind_name}`, mode private, enable | assistant `get_virtual_npc_list` → mode private |
| 6 | `prep.bond-smoke` | dashboard | throwaway bond → read-back → remove | assistant `get_linked_identities`, both actors |
| 7 | `prep.shared-memories` | dashboard | inject shared 1–3 into the player-fold | Memories page read-back ×3 |

## joiner — per follower (repeat)

| # | id | surface | action | verify |
| --- | --- | --- | --- | --- |
| 1 | `joiner.resolve` | agent | pause; body name + `{uuid}` | — |
| 2 | `joiner.profile` | dashboard | ten-block profile: mind blocks + body template; create if missing | blocks present in order; DynamicBio guard set |
| 3 | `joiner.memories` | dashboard | shared 1–3 + `joiner.md` filled with `{party}` | Memories read-back ×4 |
| 4 | `joiner.bond` | dashboard | bonds to player-fold + every existing member, both directions | `get_linked_identities` |
| 5 | `joiner.group` | dashboard | add to `{party_group}` | page read |
| 6 | `joiner.prewarm` | console ⚠ | floors: rapport/trust/loyalty + player blurb; pair blocks both directions | `Native_GetRapport` reads back 70 |
| 7 | `joiner.log` | agent | append run-log: step ids + read-back results | — |

## dynamic rules

- **fan-out from live state** — `repeat: per member` reads the current party (dashboard pages, assistant reads); joins at 2, 4 or 9 followers all run the same graph
- **party cap** — `character.party_cap` is optional; the joiner phase keeps working past it unless the pack says stop
- **idempotency** — check-before-create everywhere: profile exists? memory present? bond already there? A re-run patches or skips, never duplicates
- **resumability** — a joiner run may abort mid-way; the run log marks what landed and the next run resumes from it. Ordering constraints are only where stated (bonds after `prep.register-mind`)

Step lists condense the [output-entries manual](<../../output entries/_manual.md>); the per-step detail (form fields, console lines, exact texts) stays in those manuals — the package references, it does not restate.
