[← prompts manual](_manual_prompts.md) · [message-flow](../../writeups/message-flow.md)

# extra-instructions — full replacement for `submodules/user_final_instructions/0700_extra_instructions.prompt`

Overlay override: paste as `submodules/user_final_instructions/0700_extra_instructions.prompt`. The base text is carried verbatim; the group-talk sentence is added after it. Ungated on purpose — it is true for locals and folds alike: what is said aloud is heard by the near, and party knowledge spreads. This is the message-flow prompt footprint's whole remainder; nothing else prompts for group talk.

````text
{% if not is_narration_enabled() %}
No narration or asterisks—{% if render_mode == "thoughts" %}pure internal thought only{% else %}spoken words only{% endif %}.
{% endif %}

What you say aloud, everyone nearby hears. And among close companions, what is known to one is soon known to the rest — news does not stay put in a party that shares its days.
````
