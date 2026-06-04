# CLARVUE — Exploratory Forum Analysis

Reddit-based digital trace analysis supporting the design of [CLARVUE](https://seuyoungc.craft.me/clarvue), a cycle-aware planning tool focused on the luteal phase. This repository contains the data pipeline, coded dataset, and notebook used to surface pain points, coping strategies, and unmet needs that informed the product's design.

This is exploratory hypothesis-generation work — not clinical research, not a substitute for human-subjects studies.

**Research question:**
> How do people with PMS/PMDD describe their biggest recurring luteal-phase problems, what coping strategies do they already use, and what kinds of help feel usable rather than burdensome?

---

## Method

- **Sampling** 
    - Reddit JSON search across three subreddits (`PMDD`, `pms`, `Periods`) using seven planning- and cognition-related search terms. ~500 posts collected in April 2026.
- **Coding** 
    - Mixed pipeline: TF-IDF + KMeans clustering for thematic structure, VADER for valence, and manual flag columns for `pain_point`, `coping`, `unmet_need`, and `app_signal`.
- **Analysis** 
    - Cluster-level summarization, sentiment by phase-related language, surfacing of "deep read" candidate posts and posts that explicitly request app-style support.

The full pipeline is in [notebooks/analysis.ipynb](notebooks/analysis.ipynb).

---

## Findings

Seven patterns emerged from the analysis. Findings 1, 2, and 4 were selected to test in the MVP based on their directness as product surfaces. The full set with extended implications is in [outputs/design_implications.md](outputs/design_implications.md).

### 1. ★ The briefing must answer "what do I do" — not "what phase am I in" *(tested in MVP)*

Every competing app stops at the label. Users describe opening Flo and seeing "Day 24. Luteal phase," and reading that as the app stating the obvious instead of helping. They want the action already taken — the meal already decided, the schedule already adjusted — and phase information as secondary context, not the headline.

> *"The app just being like 'Day 24. Luteal phase.' Yeah, obviously. I am literally the one on the couch."* — r/PMDD

**Design implication.** The briefing surface must lead with a decided, executable action. Phase information is metadata, not the lede.

### 2. ★ Cognition is the design target, not mood *(tested in MVP)*

Brain fog and executive dysfunction are described as worse than emotional symptoms — because they can't be hidden. Users say they can mask anxiety or low mood; they can't fake clear thinking. The community already has a theoretical frame for this: **spoon theory** — the idea that a person has a finite number of "spoons" of mental and physical energy per day.

> *"I can at least try to hide my emotional symptoms. But I can't fake being able to think clearly."* — r/PMDD

**Design implication.** Copy and interactions should frame the product as a cognitive offload — not a soothing or wellness tone. The unit of design is the spoon, not the mood.

### 3. The partner signal is a sleeper feature with massive demand

The highest-scoring post in the app-signal dataset (842 upvotes) was about a user who built physical flip cards in Canva so her partner could see what cycle phase she was in. That post outscores everything else by a wide margin, indicating a deep unmet need: a simple, non-clinical way to signal "today is rough" to a partner without explaining PMDD from scratch every month.

**Design implication.** Partner-facing status communication is a validated unmet need. The form factor (app, physical object, ambient) is open; the demand is clear.

### 4. ★ Food is the first system that breaks *(tested in MVP)*

Meals collapse first during luteal. Users describe cravings spiraling, ordering takeout out of desperation, or skipping food entirely because they can't plan. The meal-decision intervention point is the highest-friction, lowest-effort fix: the meal doesn't need to be elaborate, it needs to be *decided* without the user having to think.

**Design implication.** A meal-decision feature is the right first product surface — high pain, low cognitive cost to deliver, immediately verifiable.

### 5. Calendar blocking is validated DIY behavior

Multiple users already schedule their luteal phase in Google Calendar, set reminders, and pre-decline social plans. They are automating the cognitive work of "should I commit to this thing two weeks from now" — by hand, with sticky notes and calendar reminders.

> *"I broke down my tasks. And you know what? It worked. I got through the day."* — r/PMDD

**Design implication.** A calendar-coordination feature doesn't need to be sold or explained. The product framing is "this saves you the work you're already doing," not "this introduces a new behavior."

### 6. "Don't make decisions in luteal" is a community mantra

Two posts in the dataset use that exact phrase, both with 600+ upvotes, in different subreddits. The community has already articulated the value proposition in their own words — this is unusual. Most products have to construct their own value-prop language.

**Design implication.** Product copy should reference this framing not as a borrowed slogan, but as evidence of alignment with the community's own vocabulary.

### 7. The dead zone is the highest-stakes failure case

Users who forget they're in luteal and make impulsive decisions — quitting jobs, ending relationships, spiraling — represent the most dangerous pattern in the data. Multiple posts contain the line "I looked at my calendar and realized." The window where attention to phase fades is when the worst decisions get made.

**Design implication.** A dead-zone alert is not a retention feature; it is a safety feature. Any design in this space needs an answer for it, even if intentionally minimal.

---

## Ethics note

This analysis treats public Reddit posts as digital trace data for exploratory hypothesis generation. Usernames were never collected, and reverse-searchable post URLs and timestamps have been stripped from the published dataset; each row carries only an opaque hashed `post_id`. Quotes shown in any rendered output are paraphrased rather than verbatim. This is not a substitute for clinical or human-subjects research, and no individual user is identified, profiled, or contacted. Raw scraped data with original URLs is kept local and is gitignored.

---

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
    └── design_implications.md      ← full design implications writeup
```

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

The Reddit JSON endpoint used by `scripts/scrape_reddit.py` requires no API key or OAuth credentials — only a `User-Agent` header.

---

## Links

- Case study: [seuyoungc.craft.me/clarvue](https://seuyoungc.craft.me/clarvue)
- Live MVP: [seuyoungc.github.io/clarvue-mvp](https://seuyoungc.github.io/clarvue-mvp/)
