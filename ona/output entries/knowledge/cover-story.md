[← knowledge manual](_manual_knowledge.md) · [cover-story](../../writeups/cover-story.md)

# cover-story — what locals are told

For every non-fold NPC. Prerequisite: the NPC group must exist first (create it in the dashboard); each recruited fold — and the player-fold at first setup — goes into it, which is exactly what removes this entry from the folds' own prompts.

## fields

| field | value |
| --- | --- |
| display name | Ohne cover story |
| condition_expr | `not is_in_npc_group(actorUUID, "ohne")` |
| always_inject | false |
| importance | 0.7 |
| type | KNOWLEDGE |
| tags | old friends, travelers, wandering Skyrim, cover story, the group of companions |
| knowledge_key | ohne-cover-story |

## content

The travelers who go together — {{ playerName }} and their companions — are old friends from a village somewhere north of here. They wander Skyrim to see the country: that is why they stare at ruins and ask pointed questions. They carry weapons for the roads, and they are headed wherever they feel like. Pressed on where exactly they are from, one of them may mention a small village called Omla — few have ever heard of it.

