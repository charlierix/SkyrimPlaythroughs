# character types — playthrough shapes the machinery supports

[← docs](./_overview.md)

The Ohne machinery — virtual entities, identity links, knowledge scoping, seeded memories, SeverActions tuning — is a kit, not a single playthrough. This doc catalogs shapes it can express, what each needs, and what is verified vs ⚠. Nothing here needs new SkyrimNet code: every ingredient is a declarative surface (dashboard config, knowledge entries, prompt overrides). The shapes are for **other playthroughs** — the current one stays one mind, five bodies.

## the shape kit — what varies

| ingredient | surface | the knob |
| --- | --- | --- |
| a bodiless character | dashboard VirtualEntities, `conversationMode` | `private` (only the player hears it) vs `public` (the world can address it) |
| self-model | `always_inject: true` knowledge, condition `decnpc(actorUUID).isVirtual` | what the entity believes it is |
| witnessing a life | identity link `is_virtual: true` | `sees_their_memories`: true = it watches your life; false = it feels you out |
| power over a body | link `dominance` | `host_led` whisper · `entity_led` it takes the reins · `contested` the mouth changes hands |
| possession framing | link `host_unaware` | the body never knew — its own branch in 7050 |
| voice | a profile for the entity (`speech_style`, `aspirations`) | register, humor, vocabulary |
| material | seeded memories (`RegisterPersistentEvent…`) | what it has to draw on |
| audience scoping | NPC groups + `is_in_npc_group` conditions | who gets which entries |

## voice-in-head characters

The Ohne drift (failure mode 7) was the capability announcing itself: a registered virtual with world presence and no self-model invented a body. The fix designed for Ohne — private mode, an always-inject self-model rule, never grouped, no profile, memory hygiene — **is** the "better prompting"; turned deliberately, it becomes a character type: a voice in the player's head, felt not seen.

| ingredient | Ohne's value → the inner-voice value |
| --- | --- |
| `conversationMode` | `private` — only the player hears it (verified semantics) |
| self-model rule | "no body, the folds speak for me" → "you are a voice in {{ playerName }}'s head; you have no body; you are felt, not seen" |
| link to the player | folds use `shared_virtual`, `sees_their_memories: false` → the voice wants `is_virtual: true`, `sees_their_memories: true`: it watches your life and comments |
| memories | Ohne carries none by design → the voice needs them as material (⚠ deliberate seeding onto a virtual — one live check; the drifted Ohne did accumulate them, deletable on the Memories page) |
| profile | none for Ohne → `speech_style` + `aspirations` give the voice its register |
| dominance | n/a on shared_virtual → `host_led` = whisper beneath · `entity_led` = sometimes it takes the reins · `contested` = the mouth changes hands |

### named candidates

| shape | build |
| --- | --- |
| **angel / devil pair** | two private virtuals with opposing self-models; per-entity scoping via one group per entity + `is_in_npc_group` conditions ⚠ multiple private virtuals at once is unverified |
| **lore master** | semantic knowledge entries as its domain (higher importance, topic tags); `host_led` whisper; `sees_their_memories: true` so commentary tracks your deeds |
| **standup comic** | seeded memories of your exploits as material; heckling register in its profile voice |
| **conscience** | `host_led`; self-model = "you know what you promised"; seeded memories of oaths and debts |

### what would be needed (all declarative)

1. register the virtual(s), private, in the dashboard VirtualEntities config
2. author the self-model standing rule — `always_inject: true`, condition `decnpc(actorUUID).isVirtual`
3. one identity link voice ↔ player with `is_virtual: true` + witnessing/dominance as designed
4. seed the voice's memories; give it a profile voice
5. ⚠ live checks: multiple private virtuals rendering at once · deliberate memory seeding onto virtuals · how bodied↔virtual bond branches render in 7050 · whether `is_present` makes sense for a bodiless side

The Ohne cleanup ladder ([frozen knowledge manual](<../output entries/knowledge/_manual_knowledge.md>)) doubles as drift recovery for any inner voice.

## other shapes

| type | what changes | notes |
| --- | --- | --- |
| **one mind, N bodies** (current) | built — [`output package/`](<../output package/README.md>) | shared_virtual bonds, `sees_their_memories: false`, group-scoped fold facts |
| **possession** | a bodied↔bodied link with `host_unaware: true`, or `dominance: entity_led` so the rider takes the reins; `suppress_host_persona` stands the body's sections down | a ridden vessel, a taken follower |
| **classic party** | no identity links at all — stock bios, cold SeverActions defaults | the baseline; a package ships fewer artifacts |
| **a public oddity** | virtual with `conversationMode: public` — a ghost, a shrine voice the world can address | needs its own knowledge conditions (not group-scoped) ⚠ how locals treat a public virtual is untested |
| **world flavor** | knowledge packs only — faction lore, region rumors; no virtuals, no links | the cheapest package for a different campaign |

## packaging tie-in

Each shape is one package instance of the same machinery ([recipe](./prompt-set-package.md)): a `pack.json` character block plus re-parameterized runtime entries. An inner-voice package differs from Ohne's in `runtime/identity/register.md` (mode, count), the standing-rule entries, the link parameters, and whether memories are seeded — `plugin/prompts/` may not change at all.

## open items ⚠

1. deliberate memory seeding onto virtual entities — the surface exists (drifted Ohne accumulated memories); one proof needed
2. multiple private virtuals active simultaneously — one live test
3. bodied ↔ virtual bond rendering — the 7050 branch never checks `is_virtual`; one smoke test
4. public virtuals in NPC conversation — one live test before building on it

## related

[identity links](./identity-links.md) · [helper agents](./helper-agents.md) · [what goes where](./what-goes-where.md) · [the packaging proposal](./prompt-set-package.md) · [multi-playthroughs](./multi-playthroughs.md)
