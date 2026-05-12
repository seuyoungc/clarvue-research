# Design Implications

Seven patterns from a thematic analysis of ~500 anonymized Reddit posts (r/PMDD, r/pms, r/Periods, April 2026). Not a clinical claim — a synthesis of how people describe planning, deciding, and coping during the luteal phase. [Method →](../notebooks/analysis.ipynb)

## 1. The briefing must answer "what do I do" — not "what phase am I in"

Every competing app stops at the label. Users in this dataset describe opening Flo and seeing "Day 24. Luteal phase," and reading that as the app stating the obvious instead of helping. They want the action already taken — the meal already decided, the schedule already adjusted — and phase information as secondary context, not the headline.

> **Implication.** The briefing surface must lead with a decided, executable action. Phase information is metadata, not the lede.

## 2. Cognition is the design target, not mood

Across the dataset, brain fog and executive dysfunction are described as *worse* than emotional symptoms — because they can't be hidden. Users say they can mask anxiety or low mood; they can't fake clear thinking. The cognitive symptoms are what break work, parenting, and relationships.

The community already has a theoretical frame for this: **spoon theory** — the idea, originating in chronic-illness communities, that a person has a finite number of "spoons" of mental and physical energy per day. The single most positive coping report in the qualitative dataset comes from a poster who triaged her day to three tasks using spoon theory and described it as the thing that got her through. Users in this space don't need to be taught the model — they're already using it.

> **Implication.** Copy and interactions should frame the product as a cognitive offload — "your thinking is slower this week, the meal is handled" — not a soothing or wellness tone. The unit of design is the spoon, not the mood.

## 3. The partner signal is a sleeper feature with massive demand

The highest-scoring post in the app-signal dataset (842 upvotes) was about a user who built physical flip cards in Canva so her partner could see what cycle phase she was in. Her partner has ADHD and asked for a physical object, not an app notification. That post outscores everything else by a wide margin, indicating a deep unmet need: a simple, non-clinical way to signal "today is rough" to a partner without explaining PMDD from scratch every month.

> **Implication.** Partner-facing status communication is a validated unmet need. The form factor (app, physical object, ambient) is open; the demand is clear.

## 4. Food is the first system that breaks

Meals collapse first during luteal. Users describe cravings spiraling, ordering $50 of takeout, skipping food entirely for days, or eating frozen food because they can't plan. The meal-decision intervention point is the highest-friction, lowest-effort fix: the meal doesn't need to be elaborate, it needs to be *decided* without the user having to think.

> **Implication.** A meal-decision feature is the right first product surface — high pain, low cognitive cost to deliver, immediately verifiable.

## 5. Calendar blocking is validated DIY behavior

Multiple users in the dataset already schedule their luteal phase in Google Calendar, set reminders, and pre-decline social plans. They are already automating the cognitive work of "should I commit to this thing two weeks from now" — by hand, with sticky notes and calendar reminders.

> **Implication.** A calendar-coordination feature doesn't need to be sold or explained. It needs to be shown as automation of something users already do manually. The product framing is "this saves you the work you're already doing," not "this introduces a new behavior."

## 6. "Don't make decisions in luteal" is a community mantra

Two posts in the dataset use that exact phrase, both with 600+ upvotes. The community has already articulated the value proposition in their own words. This is unusual — most products have to construct their own value-prop language; here it's already in circulation.

> **Implication.** Product copy and surface language should reference this phrasing where appropriate, not as a borrowed slogan but as evidence of alignment with the community's own framing.

## 7. The dead zone is the highest-stakes failure case

Users who forget they're in luteal and make impulsive decisions — quitting jobs, ending relationships, spiraling into ideation — represent the most dangerous pattern in the data. Multiple posts contain the line "I looked at my calendar and realized." The window between cycles, where attention to phase fades, is when the worst decisions get made.

> **Implication.** A dead-zone alert is not a retention feature; it is a safety feature. Any design in this space needs an answer for it, even if that answer is intentionally minimal (e.g., a single ambient signal a few days before a known difficult window).
