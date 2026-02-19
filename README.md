# Sleep Mastery (Mobile-First)

A simple web-based **voice-friendly daily sleep log** designed for mobile use.

- Pure HTML/CSS/JavaScript
- No external APIs
- Local data storage with `localStorage`
- Auto-calculations, flags, daily summary, weekly trends, and bottleneck detection

## Features

### Daily log fields
- Wake Anchor (target)
- Actual Wake Time
- Lights Out Time
- Estimated Sleep Onset Time
- Sleep Latency (auto)
- Estimated Total Sleep (auto)
- Wake Quality (0–10)
- Post-Wake Activation (0–10)
- Post-Wake Lay Downtime (minutes)
- Last Caffeine (time + amount)
- Last Stimulant (compound + mg + time)
- Sleep Medication (compound + mg + time)
- Melatonin (mg + time)
- Screens Last Hour (Y/N)
- Night Interruptions (count)
- Light Exposure within 30 min of wake (Y/N + minutes)

### Auto-calculations and flagging
On submit, the app calculates:
- Anchor deviation
- Sleep latency
- Total sleep duration
- Sleep efficiency estimate

And flags:
- Late stimulant usage
- Late caffeine usage
- Large anchor deviation (>60 min)
- Second sleep risk (wake delay >20 min)

### Reports
- Daily summary report (for the saved day)
- Weekly trend summary (latest 7 logs)
- Primary Bottleneck detection (ranked top 3 issues)

## Project structure

```text
/
├── index.html
├── README.md
├── logs/
├── metrics/
├── reports/
└── experiments/
```

> The folders are included so you can later export snapshots or generated artifacts if needed.

## Run locally

### Option 1: Open directly
Open `index.html` in your browser.

### Option 2: Use a local server (recommended)
From the repository root:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Deploy on GitHub Pages

1. Push this repository to GitHub.
2. In GitHub, open **Settings → Pages**.
3. Under **Build and deployment**, set:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` (or your default branch), folder `/ (root)`
4. Save, then wait for GitHub Pages to publish.
5. Visit the generated Pages URL.

Because this is a static site, no build step is required.
