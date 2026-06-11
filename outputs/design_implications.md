# Design Implications

Seven patterns from a thematic analysis of ~500 anonymized Reddit posts (r/PMDD, r/pms, r/Periods, April 2026) — a synthesis of how people describe planning, deciding, and coping during the luteal phase.

Three of the seven (marked ★) were selected to test in the MVP, based on their directness as product surfaces. The remaining four are validated signals held for future iterations.

> ⚠️ Exploratory, hypothesis-generating analysis of public posts — not a clinical study. Findings **support** the project's hypotheses; they do not validate them. Quotes are paraphrased and examples generalized to avoid reverse-searchability. Full pipeline in [`notebooks/analysis.ipynb`](notebooks/analysis.ipynb).

---

## ★ 1. The briefing must answer "what do I do" — not "what phase am I in"

Every competing app stops at the **label**. Across the dataset, users describe opening a tracker, seeing *"Day 24. Luteal phase,"* and reading it as the app stating the obvious rather than helping — the information they least needed, presented as if it were the point. They are already on the couch; they do not need to be told they are on the couch. What they want is the **next move**, with phase information demoted to secondary context.

This is reinforced by an absence that runs through the qualitative set: across every post that mentions a tracker, calendar, or logging tool, **no poster names a current app as having helped them through a luteal episode.** The category is used and abandoned. Tracking is treated as a precondition to help, not help itself — and the help never arrives.

> **Implication.** The value is in delivering a decided, executable action; phase information is metadata, not the lede. The opportunity begins exactly where existing apps stop — at the moment after the label.

## ★ 2. Cognition is the design target, not mood

This is the central re-framing of the project. Across the dataset, **brain fog and executive dysfunction are described as worse than emotional symptoms — because they cannot be hidden.** Users report being able to mask anxiety or low mood at work and in front of family; they cannot fake clear thinking. The cognitive collapse is what becomes visible to colleagues, what derails parenting, what erodes relationships. The emotional symptoms are private and survivable; the cognitive ones are public and uncontainable.

The breakdown is concrete, not abstract. Posters describe **decision paralysis around ordinary tasks** — unable to initiate a routine phone call (a hair appointment, a doctor) because they spiral into worst-case outcomes before dialing. The failure isn't sadness; it's the inability to execute simple, known steps.

The community already has a theoretical frame for this: **spoon theory** — the chronic-illness model that a person has a finite number of "spoons" of mental and physical energy per day. The single most positive coping report in the entire qualitative dataset comes from a poster who triaged her day to the three tasks she had spoons for and described that as the thing that got her through. The intervention worked — but it *still* required cognitive overhead to choose the three tasks. Users in this space don't need to be taught the model; they're already using it. The unmet need is having the triage done *for* them.

> **Implication.** The design direction is a **cognitive offload**, not a soothing or wellness tone. The unit of design is the spoon, not the mood — and the guiding question for any feature is whether it adds cognitive work or removes it.

## 3. The partner signal is a sleeper feature with massive demand

The highest-scoring post in the app-signal dataset (**842 upvotes**) describes a user who built physical flip cards in Canva so her partner could see which cycle phase she was in. The partner has ADHD and asked for a **physical object**, not an app notification. That post outscores everything else in the app-signal set by a wide margin — a signal of depth of need, not just breadth.

The underlying pattern is broader than one post. The qualitative set is full of **relationship erosion on a schedule**: posts orbiting whether others "almost get divorced every month," one thread describing a partner secretly venting about the user's PMDD to an AI chatbot. The recurring shape is the same — luteal behavior damages trust, and there is no system to protect the relationship from a self the user can't fully control that week. The flip-card post is the community's own prototype of the missing solution: a simple, non-clinical way to signal *"today is rough"* without re-explaining PMDD from scratch every cycle.

> **Implication.** Partner-facing status communication is a validated unmet need with unusually high intensity. The form factor (app, physical object, ambient signal) is open; the demand is not in question.

## ★ 4. Food is the first system that breaks

Among the systems that collapse during luteal, **meals go first.** Users describe cravings spiraling, ordering $50 of takeout, skipping food for days, or defaulting to frozen meals because planning is impossible. Food is where willpower fails soonest — often *before* a user would have classified herself as "in luteal" — which makes it both the earliest warning sign and the earliest place an intervention can land.

It is also the cleanest match between pain and intervention point. A meal decision is **high-frequency** (every day, multiple times), **high-friction** (it fails reliably and early), and **low-cost to deliver** (the meal doesn't need to be elaborate — it needs to be *decided*). Unlike calendar coordination or partner signaling, it requires no integration and no second party — the value is verifiable immediately.

> **Implication.** A meal-decision surface is the smallest unit that tests the core thesis — decision removal over information delivery — at high pain and low cost, before any heavier intervention is attempted.

## 5. Calendar blocking is validated DIY behavior

Multiple users in the dataset already schedule their luteal phase in Google Calendar, set reminders, and pre-decline social plans. They are **already automating the cognitive work** of *"should I commit to this thing two weeks from now"* — by hand, with sticky notes and calendar entries. This is the strongest possible adoption signal: the behavior exists, it's just fragile and manual.

The significance is strategic. A solution that *introduces* a new behavior has to overcome inertia; one that *replaces a manual version of an existing behavior* only has to be better than sticky notes. The user has already decided the job is worth doing — they've been doing it themselves.

> **Implication.** Calendar coordination doesn't need to be sold or explained — it is automation of something users already do by hand: *"this saves you the work you're already doing,"* not *"this introduces a new behavior."*

## 6. "Don't make decisions in luteal" is a community mantra

Two posts in the dataset use that exact phrase, both with **600+ upvotes**. The community has already articulated the core value proposition in its own words. This is unusual: most products must construct their value-prop language from scratch and then teach it. Here it's already in circulation, already upvoted, already shared.

> **Implication.** Surface language should reflect this phrasing where it fits — not as a borrowed slogan, but as evidence of alignment with how the community already frames its own survival strategy.

## 7. The dead zone is the highest-stakes failure case

Users who forget they're in luteal and make impulsive, irreversible decisions — quitting jobs, ending relationships, spiraling into ideation — represent the most dangerous pattern in the data. Multiple posts contain a version of the line *"I looked at my calendar and realized."* The window **between** cycles, where attention to phase fades and tools go silent, is precisely when the worst decisions get made.

This is also the hardest unsolved problem in the space: the moment the user most needs a signal is the moment nothing is watching. The finding reframes that silence — it is not a retention gap, it is a **safety gap**.

> **Implication.** A dead-zone alert is a safety feature, not an engagement one — and any design in this space needs an answer for it, even a deliberately minimal one (a single ambient signal a few days before a known difficult window). Of the four deferred findings, this carries the highest stakes: the cost of getting it wrong is measured in harm, not churn.
