[← profiles manual](_manual_profiles.md)

# body-template — the per-body fill-ins and the paste-ready skeleton

Two jobs at recruit time: fill the body-side slots from the body's own base profile (vanilla bodies ship pre-built bios; mod bodies get auto-generated — if neither exists yet, write plain body-side text yourself and keep it boring), and feed the skeleton below into the [profiles manual](./_manual_profiles.md) flow: mind text over body base, section by section.

## per-block rules (bio-file order)

| # | block | fill with |
| --- | --- | --- |
| 1 | summary | [mind](./mind.md) summary, with `{name}` → {BODY NAME} |
| 2 | interject_summary | [mind](./mind.md) interject_summary, with `{name}` → {BODY NAME} |
| 3 | background | the background line below |
| 4 | personality | [mind](./mind.md) personality, unchanged |
| 5 | appearance | the body's base text, unchanged |
| 6 | aspirations | [mind](./mind.md) core + the experiment line below |
| 7 | relationships | the body's base text, unchanged |
| 8 | occupation | the body's base text, unchanged |
| 9 | skills | the body's base text, unchanged |
| 10 | speech_style | [mind](./mind.md) speech_style, unchanged |

{BODY NAME} — the body's name as SkyrimNet knows it; roster: Miya, Neala, Ornella, Svetlana (recruit order).

## the experiment line

Each fold runs its body's own experiment; append to the aspirations core:

- This body's experiment: {what this body is for — e.g. what hunger is like, what a sword arm learns, what startle does to thinking, what carrying weight teaches}

## the background line

One boring line, body-side only, nothing fold-side. Shape: "{BODY NAME} came from {place}, worked as {trade} before taking to the road."

## the paste-ready skeleton

Create-and-fill in one paste ([profiles manual — step 1](_manual_profiles.md)): swap `{name}` inside the mind text for the body's name, replace every `[...]` slot, keep the `{% block %}` markers exactly.

```
{% block summary %}[mind summary — `{name}` swapped for the body's name]{% endblock %}

{% block interject_summary %}[mind interject_summary — `{name}` swapped for the body's name]{% endblock %}

{% block background %}{BODY NAME} came from {place}, worked as {trade} before taking to the road.{% endblock %}

{% block personality %}[mind personality, verbatim]{% endblock %}

{% block appearance %}[the body's base appearance text]{% endblock %}

{% block aspirations %}[mind core bullets + the experiment line]{% endblock %}

{% block relationships %}[the body's base relationships text]{% endblock %}

{% block occupation %}[the body's base occupation text]{% endblock %}

{% block skills %}[the body's base skills text]{% endblock %}

{% block speech_style %}[mind speech_style, verbatim]{% endblock %}
```

## merge checklist (recruit time)

- speech_style and interject_summary survived the merge
- background is one boring line with nothing fold-side in it
- appearance, occupation, relationships, skills untouched
- DynamicBio checked — Advanced Configuration → DynamicBio: make sure its rewrite set does not cover the fold-owned sections (summary, personality, speech_style, interject_summary), or the fold voice gets washed out
