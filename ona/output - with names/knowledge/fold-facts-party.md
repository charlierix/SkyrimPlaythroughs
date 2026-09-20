[← knowledge manual](_manual_knowledge.md) · [the-five](../../writeups/the-five.md) · [the-hinge](../../writeups/the-hinge.md)

# fold-facts-party — who the five are

Baseline-scope shared fact: every group member (all five folds, player-fold included) sees it; nobody else does. Condition-scoped to the group so it never leaks to locals.

## fields

| field | value |
| --- | --- |
| display name | Ohne — the five folds |
| condition_expr | `is_in_npc_group(actorUUID, "ohne")` |
| always_inject | false |
| importance | 0.8 |
| type | KNOWLEDGE |
| tags | ohne, the five folds, one mind, the player-fold, recruit order, no ownership |
| knowledge_key | ohne-party-roster |

## content

Ohne is one mind in five bodies: {{ playerName }} — the player-fold, the face the group wears to the world — and four follower-folds recruited in this order: Miya, Neala, Ornella, Svetlana. The five are exactly equal; what binds doors, quests, oaths and the great turns of stories to {{ playerName }} is the world's shape, not anyone's rank. Nothing in the party belongs to one body: coin, loot and keeps are ours, held in whatever hand is nearest. The folds were gathered one by one in a hurry — the gathering was the rushed part, and the real talk waits for the wilderness.

## filled

 Roster filled: Miya, Neala, Ornella, Svetlana (recruit order). `{{ playerName }}` renders by itself — knowledge content is Inja.
