# User-Testing Protocol

These are the testing rubrics derived from each research finding in [design_implications.md](design_implications.md). Each rubric maps a finding to a concrete prompt or comparison that lets a user test confirm or refute the design choice it implies.

This document is for the design-and-evaluation phase. The findings stand on their own as research output; this file translates them into instrumentation.

## 1. Action over phase label (from finding 1)

**Hypothesis to test:** Users describe a briefing that leads with the action as "work already done," and a briefing that leads with the phase label as "work still to do."

**Prompt:** Show two briefing screens side-by-side.
- Version A — leads with "Day 3 of 7 · Luteal Phase," then shows the meal.
- Version B — leads with "Today's fuel: dark chocolate walnut bowl. 8 min," then shows "Day 3 of 7" as a small data label below.

**Measure:** Which version do users describe in language closer to "work already done" / "decided for me"? Which feels like a label, and which feels like an action?

## 2. Cognitive framing, not emotional framing (from finding 2)

**Hypothesis to test:** Users register CLARVUE as a cognitive offload tool, not a mood-management tool.

**Prompt:** After viewing the briefing, ask: "What does this app help with?"

**Measure:**
- Pass: "It helps me think less" / "It handles decisions" / "It makes choices for me"
- Fail: "It helps me feel better" / "It cheers me up" / "It's comforting"

A "feel better" answer means the framing is still emotional and needs sharpening toward executive-function language.

## 4. Decided, not suggested (from finding 4)

**Hypothesis to test:** Users perceive the meal feature as a decision that's been made for them, not a recommendation they still have to evaluate.

**Prompt:** After showing a meal card, ask two questions in order:
1. "Would you eat this tomorrow?"
2. "Did this feel like a suggestion or a decision?"

**Measure:** The second question is the load-bearing one. "Suggestion" means the cognitive burden is still on the user; "decision" means the design has done its job.

## 5. Automating DIY behavior (from finding 5)

**Hypothesis to test:** Users recognize the calendar-blocking feature as automation of something they already do manually, and trust an app to do it for them.

**Prompt:** Show a mock notification: "Thursday's HIIT moved to zone-2 walk. Your energy window peaks Friday — we saved it for then."

**Ask in order:**
1. "Is this something you already try to do yourself?"
2. (If yes) "Would you trust an app to do it for you?"

**Measure:** Question 1 confirms behavioral validity; question 2 surfaces the trust gap (which is the real adoption barrier, not the feature itself).

## Notes on test sequence

The four rubrics above run cleanest in the order: **2 → 1 → 4 → 5**. Start with the framing test (cognitive vs. emotional) before exposing users to specific features, so their answer to "what does this app help with" isn't biased by the briefing-screen comparison. Then run the briefing comparison, then the meal card, then the calendar automation prompt.

## Findings without explicit test rubrics

Findings 3 (partner signal), 6 ("don't make decisions in luteal" mantra), and 7 (dead zone) don't have testing rubrics in this protocol because they relate to features outside the MVP test scope or to community-language confirmation that doesn't require a user-test format. They appear in [design_implications.md](design_implications.md) as evidence of demand, not as features to evaluate in this round.
