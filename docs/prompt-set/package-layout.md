# prompt set — package layout

[← proposal](../prompt-set-package.md)

One folder per character, split by SkyrimNet's delivery rules: what a plugin may carry ships; per-save runtime state is executed by the importer agent.

## tree

```
{author}.{character}-promptset/
    pack.json                  identity + character block + token registry + phase pointers
    tasks/
        prep.json              phase 1 — once per playthrough
        joiner.json            phase 2 — per follower, repeatable
    plugin/                    → ships as external/{author}.{slug}/
        manifest.json          beta25 schema (folder name = id, strict semver)
        prompts/               full-replacement overrides, base text + our additions
    runtime/                   → importer agent's material, never ships
        knowledge/             the six entries — roster-bearing ones update per joiner; a sknpack for the stable ones is an open ⚠
        profiles/
            mind.md            the mind-owned bio blocks
            body-template.md   body-side fill-ins + the ten-block paste skeleton
        memories/
            shared-1..3.md     the shared pool
            joiner.md          the joiner memory template (live party list filled in)
        identity/
            register.md        virtual entity registration spec
            bonds.md           bond rule (fields + directions), not a fixed 20-row table
        prewarm/
            floors.md          floor values + console-line templates
        run-log.md             per-playthrough execution log (created by the agent)
```

Generalization vs the current writeup: `bonds.md` (20 fixed rows) and `recruitment/recruit-1..4.md` become **rules + one template** — the joiner phase computes bonds and memory text from live party state.

## pack.json

```json
{
  "pack_id": "ona.ohne-promptset",
  "schema": 1,
  "min_skyrimnet_version": "0.25.0",
  "character": {
    "mind_name": "Ohne",
    "mind_mode": "private",
    "lore_names": ["Ohne", "Ona", "Omla"],
    "party_group": "ohne",
    "party_cap": 4,
    "player_is_member": true
  },
  "tokens": {
    "{player}":    { "fill": "prep",    "source": "user" },
    "{joiner}":    { "fill": "joiner",  "source": "live body name" },
    "{party}":     { "fill": "joiner",  "source": "live member names, recruit order" },
    "{uuid}":      { "fill": "joiner",  "source": "dashboard or GetEntityUUID(Actor)" },
    "{mind_name}": { "fill": "package", "source": "character.mind_name" }
  },
  "phases": ["tasks/prep.json", "tasks/joiner.json"]
}
```

Token hygiene, carried over from the manual and now machine-checkable: a token left unfilled reaches the game verbatim — every step producing game-facing text must pass a fill check (no `{` tokens left) before submission.

## ships vs runs

| current output-entries artifact | package slot | delivery |
| --- | --- | --- |
| `prompts/*.md` (6 files) | `plugin/prompts/…` | ships — same paths as base, full replacements |
| `knowledge/*.md` (6 entries + group) | `runtime/knowledge/` — executed, not shipped | the roster entry updates per joiner; a sknpack for the stable ones stays an open ⚠ |
| `profiles/mind.md` + `body-template.md` | `runtime/profiles/` | runtime |
| `memories/shared/*.md` | `runtime/memories/` | runtime |
| `memories/recruitment/recruit-N.md` | `runtime/memories/joiner.md` (template) | runtime |
| `identity-links/bonds.md` | `runtime/identity/bonds.md` (rule) | runtime |
| `prewarm/_manual_prewarm.md` | `runtime/prewarm/floors.md` | runtime |
| `_manual.md` order of operations | `tasks/prep.json` + `tasks/joiner.json` | runtime — machine-readable |

## beta25 constraints the plugin half obeys

- folder name = manifest `id`; `version` strict semver, bumped on any content change
- extensions exactly `.prompt` / `.yaml` / `.sknpack`; no non-ASCII names
- only the four content folders — no `prompts/_saves/**`, no generated bios (`characters/dynamic/**`, `*.dynamic.prompt`)
- `external/` is never written by SkyrimNet; player edits land in their overlay

Contract: [MIGRATING_TO_BETA25](../../../sources/SkyrimNet-GamePlugin/docs/modding/MIGRATING_TO_BETA25.md).
