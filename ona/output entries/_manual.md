[← surface research — docs](../docs/_overview.md)
[← design source of truth — writeups](../writeups/_overview.md)

# output entries — the play-time injection manual

Files here are written to match what SkyrimNet expects, then injected one at a time at play time through the dashboard (`localhost:8080`) — hand a file to the right helper agent and let it inject, or paste directly into the page editor. No bulk import anywhere.

## ⚠ runtime fill — the tokens in these files

**The five bodies are chosen at play time, not in this pack.** Wherever an artifact needs a body's or the player's name, it carries a token — fill it at injection. A token left unfilled reaches the game verbatim, so treat the fill as part of every injection step below.

Before playing the game, it would be a good idea to nail down what the player's name will be, and the names of the four followers, what order you will recruit them (use a burner playthrough to figure all that out).  Then have your ai framework replace all the placeholder tokens with those concrete names.  It will make the skyrimnet injection process much smoother

| token | fill with | when |
| --- | --- | --- |
| `{player}` | the player character's name | first setup |
| `{fold1}` … `{fold4}` | the four follower bodies' names, in recruit order | at each recruitment |
| `{name}` | the body whose profile is being merged | at each recruitment |
| `{uuid}` | the body's real UUID — dashboard or `GetEntityUUID(Actor)` | at each recruitment (identity-links only) |

Core lore names — **Ohne**, **Ona**, **Omla** — are fixed in the pack and are never substituted.

# order of operations

**first setup — before recruiting**

1. inject the prompt overrides ([prompts](./prompts/_manual_prompts.md))
2. create the NPC group + knowledge entries, and put the player-fold in the group ([knowledge](./knowledge/_manual_knowledge.md))
3. register the virtual entity Ohne + verify the identity-link creation surface live — no bonds yet, those happen per recruitment ([identity-links — setup](./identity-links/_manual_identity-links-setup.md))
4. inject the 3 shared memories into the player-fold ([memories — setup](./memories/_manual_memories-setup.md))

**per recruitment — repeat ×4**

1. recruit, look at the follower, pause
2. inject the fold profile into the body's profile ([profiles](./profiles/_manual_profiles.md))
3. inject memories: the 3 shared + this fold's recruitment memory ([memories — recruit](./memories/_manual_memories-recruit.md))
4. bond the new fold to every earlier fold ([identity-links — recruit](./identity-links/_manual_identity-links-recruit.md))
5. add the fold to the NPC group (knowledge conditions key off it)
6. prewarm the relationship floors — rapport/trust/loyalty + player blurb + fold pairs, both directions ([prewarm](./prewarm/_manual_prewarm.md))

Unverified surfaces are marked ⚠ — confirm live at first setup.

# map

| folder | artifact | skyrimnet surface | agent | when |
| --- | --- | --- | --- | --- |
| [profiles/](./profiles/_manual_profiles.md) | fold profiles for the five bodies | Profiles page | chat assistant / page editor | per recruitment |
| [memories/](./memories/_manual_memories-setup.md) ([recruit](./memories/_manual_memories-recruit.md)) | 3 shared memories + 1 recruitment memory per fold | Memories page (full CRUD, verified) | chat assistant / page editor | shared → player-fold at first setup, pools per recruitment |
| [knowledge/](./knowledge/_manual_knowledge.md) | NPC group + cover story + fold-shared facts | World Knowledge page | knowledge builder | first setup |
| [prompts/](./prompts/_manual_prompts.md) | diary override, group-talk sentence, memory bias, SeverActions relationship overrides | prompt editor (overlay layer) | prompt helper | first setup |
| [identity-links/](./identity-links/_manual_identity-links-setup.md) ([recruit](./identity-links/_manual_identity-links-recruit.md)) | the 20 directed fold bonds | VirtualEntities config ⚠ verify live | chat assistant / manual | register Ohne at first setup, bonds per recruitment |
| [prewarm/](./prewarm/_manual_prewarm.md) | relationship floors per recruitment — native SeverActions calls | Follower-module stores (rapport/trust/loyalty, player blurb, pair affinity/respect) ⚠ console verify | chat assistant / console | per recruitment |

Design source of truth: [writeups](../writeups/_overview.md) · surface research: [docs](../docs/_overview.md)
