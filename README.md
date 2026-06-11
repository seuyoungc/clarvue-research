# 🔬 CLARVUE — Exploratory Forum Analysis

*Digital trace analysis of **~500 public Reddit posts** on PMS/PMDD, supporting the design of [CLARVUE](https://seuyoungc.craft.me/clarvue).*

---

## ⚡ TL;DR

> **The central finding:** luteal-phase disruption is primarily a **cognitive load problem, not a mood problem** — and existing apps don't address it.

~500 public posts from **r/PMDD**, **r/PMS**, and **r/Periods** were collected and analyzed through a mixed computational + manual pipeline (**TF-IDF** → **K-Means** → **VADER** → manual coding). Three findings shaped the CLARVUE MVP directly.

> ⚠️ This is **exploratory hypothesis-generation** work — *not* clinical research.

---

## 📌 What This Is

CLARVUE began with a personal observation: **every luteal phase, healthy habits would collapse**, not from lack of willpower, but from **brain fog and decision fatigue** at the exact moment capacity was lowest.

The pattern felt testable. Before designing anything, I wanted to check whether it held up across a wider sample of people describing the same window. This repository contains the **full data pipeline, coded dataset, and analysis notebook** used to do that.

### 🌐 Why Reddit

Public PMS/PMDD communities are where people describe their lived experience **in their own language, at scale**, without the framing effects of a structured interview. 

The goal wasn't to validate effect sizes — it was to **surface how people describe the problem in their own words** before building anything.
| Strengths:                       | Known Limitations:            |
| ------------------------------- | --------------------------- |
| Natural language, unprompted    | Self-selection bias         |
| Large scale, low cost           | Public-posting bias         |
| Lived experience, in-the-moment | No demographic ground truth |

---

## 🔎 Hypothesis & Research Question

The work started from a single hypothesis drawn from personal experience:

> **The planning collapse around the luteal phase is best understood as a cognitive load problem, not a mood problem.**

If true, this implies effective interventions should **reduce decision burden** — not surface emotional data or prompt reflection.

To test it against lived experience, I pursued a more specific research question:

> **How do people with PMS/PMDD describe their biggest recurring luteal-phase problems, what coping strategies do they already use, and what kinds of help feel *usable* rather than *burdensome*?**

---

## 🧪 Method

**~500 public posts** collected from r/PMDD, r/PMS, and r/Periods using **seven planning- and cognition-related search terms** — chosen to pull posts about cognitive load specifically, not general symptom discussion:

`decision` · `brain fog` · `meal` · `schedule` · `cope` · `can't function` · `luteal`

The pipeline was deliberately **mixed-methods**:


| Stage                     | Technique                                                                       | What it produced                                      |
| ------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Quantitative**          | TF-IDF · K-Means (elbow-plot *k*) · PCA · VADER sentiment                       | Cluster structure + sentiment per topic               |
| **Manual coding**         | Schema-driven, word-boundary matching, iterative keyword refinement             | `pain_point` · `coping` · `unmet_need` · `app_signal` |
| **Qualitative deep-read** | Close read of high-engagement (score > 50) & high-distress (VADER < −0.5) posts | Paraphrased quotes + app-mention analysis             |


**Pipeline details**

- **Quantitative pass** — TF-IDF vectorization; K-Means with manual cluster naming after reading top terms + sample posts; PCA scatter for separation diagnostics; VADER scoring across topics and clusters.
- **Manual coding pass** — Coding schema defined *before* collection. Token & bigram frequency surfaced vocabulary the original keyword lists missed (e.g. "brain fog," "birth control").
- **Qualitative deep-read** — Separate close read of *every* post mentioning an app, tracker, calendar, or logging tool.

> 🔒 Posts were treated as **digital trace data** — usernames were never collected; URLs and timestamps were stripped from the published dataset; all quotes are paraphrased.

Full pipeline: `[notebooks/analysis.ipynb](notebooks/analysis.ipynb)`  ·  Scraper: `[scripts/scrape_reddit.py](scripts/scrape_reddit.py)`

---

## 🏆 Findings

Seven patterns emerged. Three (findings 1, 2, and 4) were selected to test in the MVP, based on their directness as product surfaces.

For all seven findings and full design implications → [`outputs/design_implications.md`](outputs/design_implications.md)

### ⭐ 1. The briefing must answer *"what do I do"* — not *"what phase am I in"*
Every competing app stops at the label; users read "Day 24. Luteal phase" as stating the obvious. They want the action already taken — and notably, no poster names a current app as having actually helped.

### ⭐ 2. Cognition is the design target, not mood
Brain fog and executive dysfunction are described as worse than emotional symptoms — because they can't be hidden. The community already runs on **spoon theory**; the unmet need is having the triage done *for* them.

### 3. The partner signal is a sleeper feature with massive demand
The single highest-scoring app-signal post (842 upvotes) was a user's DIY Canva flip cards so her partner could see her phase — a validated, non-clinical "today is rough" signal with no product to fill it.

### ⭐ 4. Food is the first system that breaks
Meals collapse first during luteal — cravings spiral, planning fails, desperation takeout. The cleanest match of high pain to low-cost intervention: the meal doesn't need to be elaborate, it needs to be *decided*.

### 5. Calendar blocking is validated DIY behavior
Users already block their luteal phase in Google Calendar and pre-decline plans by hand. The behavior isn't new — it's a fragile, manual version of something worth automating.

### 6. "Don't make decisions in luteal" is a community mantra
Two posts use that exact phrase, both 600+ upvotes. The community has already written the value proposition — the framing can be reflected, not invented.

### 7. The dead zone is the highest-stakes failure case
Impulsive, irreversible decisions ("I looked at my calendar and realized") cluster in the silent window between cycles. A dead-zone alert is a safety feature, not a retention one.

---

## ⚖️ Limits & Ethics

This is exploratory digital trace analysis on public posts — **not a clinical study** and not a substitute for human-subjects research.


| Concern                       | Detail                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sample bias**               | Reddit PMDD/PMS users are self-selected, often posting mid-distress. Silent sufferers are absent. Loudest ≠ most representative.                              |
| **Coding methodology**        | Cluster naming & theme synthesis done by a **single coder**. A second-coder reliability check would meaningfully strengthen it.                               |
| **Hypothesis vs. validation** | Findings **support but do not validate** the original hypothesis. The "decision-already-made" framing is itself a hypothesis under test.                      |
| **Privacy**                   | Quotes paraphrased. Usernames never collected. URLs/timestamps stripped — each row carries only an opaque hashed `post_id`. Raw data kept local & gitignored. |

---

## 🚀 How to Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

> The Reddit JSON endpoint used by `scripts/scrape_reddit.py` needs **no API key or OAuth** — only a `User-Agent` header. The anonymized coded dataset lives at `data/processed/coded_posts.csv`.

---

## 📚 Literature Review

**Impact on work & daily functioning**

- [The impact of premenstrual disorders on work disruptions](https://pmc.ncbi.nlm.nih.gov/articles/PMC11017212/) — *2024, PMC*
- [Changes in mood, cognitive performance and appetite in the late luteal and follicular phases](https://www.sciencedirect.com/science/article/abs/pii/S0018506X08000603) — *ScienceDirect*
- [Effects of PMS/PMDD on attention and short-term memory](https://dusunenadamdergisi.org/article/1518) — *Düşünen Adam*



**Lived experience, stigma & healthcare dismissal**

- [Double stigma of menstruation and premenstrual disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC11877803/) — *2025, PMC*
- [Patient Perspectives of Healthcare for PMDD in Australia](https://pmc.ncbi.nlm.nih.gov/articles/PMC12779906/) — *2026, PMC*
- [Self-perception of the illness experience… PMDD](https://www.longdom.org/open-access/selfperception-of-the-illness-experience-and-her-relation-with-healthprofessionals-in-a-sample-of-women-suffering-premen-41112.html) — *Longdom*



**Coping strategies**

- [Ways of coping with premenstrual change](https://pmc.ncbi.nlm.nih.gov/articles/PMC3880968/) — *PMC*
- [PMS Experiences and Coping Levels](https://bezmialemscience.org/articles/premenstrual-syndrome-experiences-and-coping-levels-of-university-students-a-mixed-method-study/bas.galenos.2023.86547) — *Bezmialem Science*



**App design for PMDD**

- [Developing a Mood and Menstrual Tracking App for People With PMDD](https://formative.jmir.org/2024/1/e59333) — *JMIR Formative, 2024*



---

## 🗂️ Repository Structure

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

---

## 🔗 Links
**Live MVP** [seuyoungc.github.io/clarvue-mvp](https://seuyoungc.github.io/clarvue-mvp/)
**Case study** [seuyoungc.craft.me/clarvue](https://seuyoungc.craft.me/clarvue)
