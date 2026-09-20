# failure modes

Latch patterns to design against — some seen in play, some caught at the drafting stage. Every new prompt or memory gets checked against these.

## 1. the phrase latch (seen in game)
Last playthrough: the LLM latched onto a phrase and repeated it ("say it to me plain" became a refrain). Repeated lines are the most visible voice failure.
Rule: prompts describe qualities, never lines to recite. Example sentences are shape-only, rare, and never quotable slogans. If a prompt contains a string an NPC could literally say, assume it will be said forever.

## 2. the don'ts trap (drafting failure, caught before play)
The first voice.md was drafted as mostly prohibitions. It was rejected before any playthrough — but the trap is general and worth naming: any short, salient list gets re-read on every call and becomes the whitelist of safe content, regardless of polarity. Don'ts, examples, both.
Rule: build the voice from positive qualities and open-ended directions. A surviving prohibition is few, general, and paired with a positive alternative (speech-quality.md).

## 3. the thu'um latch (drafting failure)
The hum was drafted next to Skyrim's Voice lore, and the model reached for thu'um to explain it.
Rule: anything adjacent to an existing Skyrim mechanic gets an explicit fence in the seed docs. Already fenced in the-five.md: the hum is presence-only, not a Shout, nothing can silence it or speak through it.

## 4. the robot failure (drafting failure)
The old voice.md treated "remove Skyrim flavor" as "shorten everything," and its examples read as simple-minded bots.
Rule: the center of the sentence moves — to observation, analysis, curiosity — and length is free. Elaboration is a mind at play (speech-quality.md).

## 5. the negativity spiral (seen in game)
Previous playthroughs: followers filtered events as aimed at themselves; suspicion accumulated within the team and toward the player ("you're holding out on me"). One misread becomes a stored opinion that later prompts read back as fact.
Rule: attribution.md's causal-neutral framing applies to pre-generated memories first, live conversation second — storage is what makes the filter dangerous. Trust inside Ohne is absolute, and the frameworks' own reputation machinery (SeverActions' Familiarity & Reputation module) initially pushes the other way — handled in attribution.md.

## 6. dialect drift (mitigated by the overwrite pass)
skyrimnet's stock prompts pull speech toward fantasy register — archaisms, oath-cadence, role performance. This is an overwrite problem, not a description problem: the stock defaults get replaced category by category, with both lanes defined — skyrim people talk like skyrim people, Ohne talks like Ohne. The residual risk is only a lane left undefined: if Ohne's register is not given a full positive description, the model falls back into the lane that is.