# multiple playthroughs — what's shared and what's per character

[← docs](./_overview.md)

The question: if we inject prompt changes for this playthrough, do they apply to every SkyrimNet playthrough on the install? Short answer, verified against the beta25 migration doc: **prompt changes yes, play-time state no** — and the built-in isolation mechanism is a per-character **external plugin**, not a cloned mod setup.

## the content-library layers

Every prompt file resolves through four layers, highest priority first:

| layer | holds | scope |
| --- | --- | --- |
| `saves/` | per-playthrough character bios (`prompts/_saves/**`) | one playthrough |
| `overlay/` | the player's dashboard edits | the install |
| `library/` + `external/` | installed + mod-shipped plugins, in the player's chosen order | while enabled |
| shipped defaults | the base plugin | always on |

Facts that drive everything else ([MIGRATING_TO_BETA25](../sources/SkyrimNet-GamePlugin/docs/modding/MIGRATING_TO_BETA25.md)):

- there is **no per-playthrough prompt layer** — `saves/` holds only per-playthrough bios, and `prompts/_saves/**` is explicitly "not allowed in a plugin"
- a file override replaces the whole file; the highest-priority layer that has the file provides it
- two plugins providing the same file resolve by priority — the dashboard shows which one wins, per file
- dashboard edits land in `overlay/` — install-global. Hand-editing prompts per character through the editor is the wrong tool; use plugin layers instead

## what is per save anyway

The play-time state is natively per playthrough — no work needed:

| state | scope |
| --- | --- |
| memories | per NPC, per save |
| profile rows and generated/dynamic bios | per save (regenerated) |
| identity bonds | per save |
| NPC-group **membership** | per save (group *names* may ship with a pack) |
| SeverActions relationship stores | per save (SKSE cosave) |
| knowledge packs (`.sknpack`) | **Persistent badge** — projected into every save while the plugin is enabled; per-entry toggles and per-playthrough edits stay save-local |

So only the **prompt templates** (and any shipped knowledge pack) are shared — exactly the part a prompt set packages.

## the isolation pattern — one plugin per character

| step | what |
| --- | --- |
| 1 | ship one character's prompt set as one small external plugin: `Data/SKSE/Plugins/SkyrimNet/external/{author}.{slug}/` with `manifest.json` + `prompts/` |
| 2 | give each character's copy its own manifest id (`{author}.{character}-promptset`), strict semver |
| 3 | the character's MO2 profile enables only its prompt-set mod → its layer sits above defaults for that playthrough only |
| 4 | removing the mod removes the layer; disabling keeps its settings until it returns |

Two sets enabled at once still resolve safely by priority — the dashboard shows the winner per file — but the clean pattern is **one set enabled per profile**.

### what not to do

| don't | why |
| --- | --- |
| clone the whole MO2 instance/folder per character | nothing requires it — the plugin layer isolates the only global part (prompts) |
| ship content into `library/` | a folder there SkyrimNet did not install is ignored |
| rely on `saves/` for prompts | per-playthrough bios only; prompt sets cannot ride that layer |
| put per-save content in a plugin | rejected — per-playthrough bios and generated bios are not allowed; per-save state never ships |

## per playthrough vs automatically clean

**Redo per playthrough** — the prep + joiner phases from the [prompt-set proposal](./prompt-set-package.md):

- fill tokens (`{player}`, body names) from the character's `pack.json`
- register the mind's virtual entity and verify the bond surface ⚠ (whether the registration itself persists across saves needs one live check — treat it as per-playthrough until proven otherwise)
- seed the shared memories; per recruitment, the joiner phase runs per follower
- group membership — names ship with the pack, membership is re-created per playthrough

**Starts clean with no work:** memories, profile rows, bonds, group membership, relationship stores.

## recipe — a new character

1. copy the prompt-set package; edit `pack.json`'s character block, the memory texts, and the character-voiced prompts — machinery untouched; ship under its own id ([new character](./prompt-set-package.md))
2. MO2: new profile for the character; enable the base mods **+ that character's prompt-set mod**
3. run the prep phase once before recruiting (task graph in the proposal)
4. play — each follower recruitment runs the joiner phase; all injected state lands in that save only

## open items

1. MO2-profile enable/disable cycle with an external layer — one live pass to confirm clean removal ⚠
2. two prompt-set plugins enabled at once — confirm the dashboard's per-file winner display ⚠
3. virtual entity registration persistence across saves — verify live ⚠

## related

[the packaging proposal](./prompt-set-package.md) · [package layout](./prompt-set/package-layout.md) · [task graph](./prompt-set/task-graph.md) · [beta25 migration](../sources/SkyrimNet-GamePlugin/docs/modding/MIGRATING_TO_BETA25.md) · [what goes where](./what-goes-where.md)