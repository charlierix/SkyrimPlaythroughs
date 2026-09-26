---
type: Prompt
title: Enterprises Prompts
description: Retainer, steward, camp, treasury and Imperial Fiscal Levy character prompts of the Enterprises module.
resource: 'sources/SeverActions/Prompts/Enterprises'
tags: [prompts, skyrimnet, enterprises, employment, taxes, npcs]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Enterprises prompt module (FOMOD option "Core Awareness Prompts", installed together with Prompts/Core) is the biggest prompt group: 23 templates across three kinds. Seven character_bio submodules inject the player's retainer roster, individual employment state, grievances and hearings, the NPC labor market, hold taxes and the Final Audit. One system prompt (sever_retainer_worklife) generates each retainer's weekly off-screen work diary. Fifteen character bios define the Imperial Fiscal Levy — the Treasury's twelve-soldier military commission and its command — as SkyrimNet original_prompts.

# Member Prompts

## Retainer and enterprise state (character_bio submodules)

| File | Lines | Purpose |
|---|---|---|
| 0168_severactions_retainer.prompt | 57 | Surfaces an NPC's employment as one of the player's retainers — job, pay, mood — via retainer_status ("" for non-retainers) |
| 0169_severactions_enterprises_summary.prompt | 13 | The player's roster summary, rendered on the PLAYER's own bio so NPCs can reference how the businesses are doing |
| 0169_severactions_retainer_hearing.prompt | 31 | A retainer's grievance about working for the player and the hearing flow when the player sent word to talk it out — mirrors the arrest persuasion block |
| 0171_severactions_npc_employment.prompt | 20 | The NPC labor market: this NPC's own employer (npc_employer) or the workforce they employ (npc_workforce) |
| 0172_severactions_hold_taxes.prompt | 11 | Hold enterprise tax rate via hold_tax_rate |
| 0173_severactions_final_audit.prompt | 33 | The Final Audit context — is this actor one of the Treasury collectors (is_tax_collector) |
| 0174_severactions_final_audit_court.prompt | 26 | Final Audit court context — collector plus authority flags for guards and jarls |

Note: two files share the 0169 sequence number; both are listed explicitly above.

## System prompt

| File | Lines | Purpose |
|---|---|---|
| sever_retainer_worklife.prompt | 191 | System prompt helping a retainer write a condensed first-person weekly work journal (3-5 sentences) about the venture they run for the player; honors the user-configured world setting/tone submodule |

## Imperial Fiscal Levy character bios (original_prompts/characters/)

Each file defines SkyrimNet `{% block %}` fields — summary, interject_summary, background, personality — for one named soldier of the Levy.

| File | Character | Role / post |
|---|---|---|
| general_cassius_vero_c09.prompt | General Cassius Vero | Commander of the Levy and the Final Audit; Bravil canal-quarter origin |
| legate_livia_aquillia_c0a.prompt | Legate Livia Aquillia | The Audit's mind — counting-house storm-mage, second to the General |
| legate_drusilla_metella_c0b.prompt | Legate Drusilla Metella | The Audit's silence — pulled from a Bravil canal the night a crooked collector burned her family out |
| optio_sabina_prisca_c20.prompt | Optio Sabina Prisca | Senior NCO; Chorrol road-warden's daughter; fairness as procedure |
| decanus_aranwe_fidelis_c22.prompt | Decanus Aranwe Fidelis | Front rank, Whiterun; the one Altmer, carries a shield, believes in the writ |
| decanus_numerius_silo_c2a.prompt | Decanus Numerius Silo | Legion sapper, Morthal; Colovian bridge-wright family |
| decanus_postumus_varro_c24.prompt | Decanus Postumus Varro | Front rank, Solitude; born on the Nibenese roads after his father died on them |
| decanus_aemilia_ruso_c26.prompt | Decanus Aemilia Ruso | Shield of the Markarth pair; Skingrad stonemason's daughter |
| decanus_torvald_falco_c28.prompt | Decanus Torvald Falco | Falkreath patrol; Bruma-born Nord first posted north |
| battlemage_ancel_vaugier_c21.prompt | Battlemage Ancel Vaugier | Frost-caster, Whiterun daylight patrol; Wayrest contracts-and-no-hands family |
| battlemage_nadir_sarran_c23.prompt | Battlemage Nadir Sarran | Whiterun patrol physician; Sentinel Forebear surgery family |
| battlemage_tullia_bassa_c25.prompt | Battlemage Tullia Bassa | Solitude patrol; Legion paymaster's clerk turned caster |
| battlemage_decimus_curio_c27.prompt | Battlemage Decimus Curio | Markarth pair caster; Imperial City street conjuror |
| battlemage_junia_merula_c29.prompt | Battlemage Junia Merula | Strongest raw caster in the detail, least interested in it; Gold Coast anchorage upbringing |
| battlemage_herennia_nepos_c2b.prompt | Battlemage Herennia Nepos | The detail's correspondent and Morthal caster; Cheydinhal chapel scriptorium |

# Related

- The hiring, wages and camp actions these prompts give state to: [/actions/enterprises.md](/actions/enterprises.md)
- Hold stewards and collections flow through Currency: [/scripts/economy-crafting.md](/scripts/economy-crafting.md)

# Citations

[1] `sources/SeverActions/Prompts/Enterprises/SKSE/Plugins/SkyrimNet/prompts/**`
[2] `sources/SeverActions/Prompts/Enterprises/SKSE/Plugins/SkyrimNet/original_prompts/characters/*.prompt`
