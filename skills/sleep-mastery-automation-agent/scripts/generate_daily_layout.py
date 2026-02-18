#!/usr/bin/env python3
"""Generate canonical daily layouts for the Sleep Mastery Automation Agent."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

DEFAULT_CONFIG = {
    "timezone": "UTC",
    "target_bedtime": "22:30",
    "target_wake_time": "06:30",
    "sleep_goals": [
        "Improve sleep consistency",
        "Reduce sleep onset latency",
        "Increase morning energy",
    ],
    "non_negotiables": [
        "10+ minutes morning sunlight",
        "No caffeine after 14:00",
        "Light movement during the day",
        "30-minute wind-down routine",
    ],
    "output_dir": "./daily",
    "project_name": "Sleep Mastery",
}

CANONICAL_TEMPLATE = """# {project_name} — {date}\n\n## Daily Intent\n- Main focus: TBD\n- Why it matters today: TBD\n\n## Sleep Plan\n- Target bedtime: {target_bedtime}\n- Target wake time: {target_wake_time}\n- Wind-down start: TBD\n- Caffeine cutoff: TBD\n\n## Environment Checklist\n- [ ] Bedroom cool and comfortable\n- [ ] Light exposure reduced 90 minutes before bed\n- [ ] Noise strategy ready (earplugs / white noise / other)\n- [ ] Screens minimized before bed\n\n## Behavior Checklist\n- [ ] Morning sunlight completed\n- [ ] Movement completed\n- [ ] Meals timed to support sleep\n- [ ] Stress downshift completed\n\n## Metrics Log\n- Sleep onset latency (min): TBD\n- Night awakenings (#): TBD\n- Total sleep duration: TBD\n- Sleep quality (1-10): TBD\n- Morning energy (1-10): TBD\n\n## Reflection\n- What worked: TBD\n- Friction encountered: TBD\n- Experiment for tomorrow: TBD\n\n## Standby Queue\n- Next best action: TBD\n- Risk to watch: TBD\n- Tonight small win target: TBD\n\n---\nGenerated automatically by sleep-mastery-automation-agent.\nTimezone: {timezone}\nGoals: {sleep_goals}\nNon-negotiables: {non_negotiables}\n"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate sleep mastery daily layout")
    parser.add_argument("--init", action="store_true", help="Create default config file")
    parser.add_argument("--date", help="Date in YYYY-MM-DD (defaults to today)")
    parser.add_argument("--output-dir", help="Override output dir from config")
    parser.add_argument(
        "--config",
        default="sleep_agent_config.json",
        help="Path to config file (default: sleep_agent_config.json)",
    )
    return parser.parse_args()


def write_default_config(config_path: Path) -> None:
    config_path.write_text(json.dumps(DEFAULT_CONFIG, indent=2) + "\n", encoding="utf-8")


def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        raise FileNotFoundError(
            f"Missing config at {config_path}. Run with --init first to create defaults."
        )
    return json.loads(config_path.read_text(encoding="utf-8"))


def resolve_date(date_input: str | None) -> dt.date:
    if not date_input:
        return dt.date.today()
    return dt.datetime.strptime(date_input, "%Y-%m-%d").date()


def ensure_daily_file(config: dict, target_date: dt.date, output_dir_override: str | None) -> Path:
    output_dir = Path(output_dir_override or config.get("output_dir") or "./daily")
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / f"{target_date.isoformat()}.md"
    if file_path.exists():
        return file_path

    content = CANONICAL_TEMPLATE.format(
        project_name=config.get("project_name", "Sleep Mastery"),
        date=target_date.isoformat(),
        target_bedtime=config.get("target_bedtime", "TBD"),
        target_wake_time=config.get("target_wake_time", "TBD"),
        timezone=config.get("timezone", "UTC"),
        sleep_goals=", ".join(config.get("sleep_goals", [])) or "TBD",
        non_negotiables=", ".join(config.get("non_negotiables", [])) or "TBD",
    )
    file_path.write_text(content, encoding="utf-8")
    return file_path


def main() -> None:
    args = parse_args()
    config_path = Path(args.config)

    if args.init:
        if config_path.exists():
            print(f"Config already exists at {config_path}")
        else:
            write_default_config(config_path)
            print(f"Initialized config: {config_path}")
        return

    config = load_config(config_path)
    target_date = resolve_date(args.date)
    file_path = ensure_daily_file(config, target_date, args.output_dir)
    print(f"Ready: {file_path}")


if __name__ == "__main__":
    main()
