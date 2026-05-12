# CLARVUE — Exploratory Forum Analysis

Reddit-based digital trace analysis supporting the design of [CLARVUE](https://seuyoungc.craft.me/clarvue), a cycle-aware planning tool focused on the luteal phase. This repository contains the data pipeline, coded dataset, and notebook used to surface pain points, coping strategies, and unmet needs that informed the product's design.

## What this is

CLARVUE is a planning surface designed around the experience of cycle-driven cognitive load — brain fog, decision fatigue, and the difficulty of holding plans together during the luteal phase and PMDD episodes. To ground the design in lived experience rather than assumption, this repo collects ~500 public posts from r/PMDD, r/pms, and r/Periods around decision-making, planning, and coping, and codes them for themes that map to product opportunities.

This is exploratory hypothesis-generation work — not clinical research, not a substitute for human-subjects studies.

## Method

- **Sampling.** Reddit JSON search across three subreddits (`PMDD`, `pms`, `Periods`) using seven planning- and cognition-related search terms. ~500 posts collected in April 2026.
- **Coding.** Mixed pipeline: TF-IDF + KMeans clustering for thematic structure, VADER for valence, and manual flag columns for `pain_point`, `coping`, `unmet_need`, and `app_signal`.
- **Analysis.** Cluster-level summarization, sentiment by phase-related language, surfacing of "deep read" candidate posts and posts that explicitly request app-style support.

The full pipeline is in [notebooks/analysis.ipynb](notebooks/analysis.ipynb).

## Ethics note

This analysis treats public Reddit posts as digital trace data for exploratory hypothesis generation. Usernames were never collected, and reverse-searchable post URLs and timestamps have been stripped from the published dataset; each row carries only an opaque hashed `post_id`. Quotes shown in any rendered output are paraphrased rather than verbatim. This is not a substitute for clinical or human-subjects research, and no individual user is identified, profiled, or contacted. Raw scraped data with original URLs is kept local and is gitignored.

## Repository structure

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── analysis.ipynb              ← rendered analysis
├── data/
│   ├── raw/                        ← gitignored (URLs intact, local only)
│   └── processed/
│       └── coded_posts.csv         ← anonymized, ready to share
├── scripts/
│   └── scrape_reddit.py            ← scraping pipeline (no credentials needed)
└── outputs/
    └── design_implications.md      ← findings writeup
```

## How to run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

The Reddit JSON endpoint used by `scripts/scrape_reddit.py` requires no API key or OAuth credentials — only a `User-Agent` header.

## Findings

See [outputs/design_implications.md](outputs/design_implications.md) for the full writeup.

## Link back to CLARVUE

- Case study: [https://seuyoungc.craft.me/clarvue](https://seuyoungc.craft.me/clarvue)
- Live MVP: [https://seuyoungc.github.io/clarvue-mvp/](https://seuyoungc.github.io/clarvue-mvp/)