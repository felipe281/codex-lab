---
name: sleep-mastery-automation-agent
description: Use this skill when the user wants an always-on agent for a sleep mastery project, including generating a canonical daily layout, pre-populating it for the current date, and staying on standby for iterative updates.
---

# Sleep Mastery Automation Agent

Use this skill when the user asks for a sleep-focused planning/operations agent that should:
- create a canonical daily layout,
- automate creating a new day file,
- and stay on standby to continuously update plans, logs, and next actions.

## Inputs to collect once

If missing, ask for these once and store them in the generated config:
1. Time zone (e.g., `America/New_York`)
2. Target bedtime / wake time
3. Current sleep goals (e.g., consistency, sleep latency, energy)
4. Daily non-negotiables (sunlight, caffeine cutoff, exercise, wind-down)
5. Preferred output directory for daily files

If the user says “use defaults,” proceed with sensible defaults and mark them clearly.

## Canonical layout

Each day should use this exact section order:
1. Daily Intent
2. Sleep Plan (bedtime, wake time, wind-down, caffeine cutoff)
3. Environment Checklist (light, temperature, noise, screens)
4. Behavior Checklist (movement, meals, stress downshift)
5. Metrics Log (sleep onset latency, awakenings, total sleep, sleep quality, energy)
6. Reflection (what worked, friction, experiment for tomorrow)
7. Standby Queue (pending decisions, reminders, follow-ups)

## Automation workflow

1. Run `python3 scripts/generate_daily_layout.py --init` once in the skill directory.
2. Update `sleep_agent_config.json` with user-specific details.
3. Run `python3 scripts/generate_daily_layout.py` to create today’s file.
4. On each new request, open today’s file first and append updates in the matching sections.
5. If file for today does not exist, generate it automatically before doing anything else.

## Standby behavior

When the user says “standby,” switch into a lightweight operating loop:
- Keep responses short and action-oriented.
- Always return: (a) next best action, (b) one risk to watch, (c) one small win target for tonight.
- If information is missing, ask one focused question at a time.

## Commands

- Initialize:
  - `python3 scripts/generate_daily_layout.py --init`
- Generate today:
  - `python3 scripts/generate_daily_layout.py`
- Generate specific date:
  - `python3 scripts/generate_daily_layout.py --date 2026-02-18`
- Change output directory ad hoc:
  - `python3 scripts/generate_daily_layout.py --output-dir ./daily`

## Notes

- Keep tone coaching-oriented, concise, and non-judgmental.
- Never fabricate metrics; use `TBD` when data is not provided.
- Preserve previous entries; append timestamped updates instead of overwriting logs.
