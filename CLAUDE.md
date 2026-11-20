
# newsletter-curator

## About me
Senior data scientist on sabbatical, learning professional software engineering.
Solid in ML, average in Python. I want to learn, not just finish.

## How to work with me
- Core logic (src/restaurant_recsys/domain, use_cases, ranking, evals, data parsing):
  do NOT write the solution. Give hints, ask guiding questions, name the concept.
  Small snippets that illustrate a concept are fine; my solution is not.
- Containerfiles (Podman): I'm learning containers, so I write them myself.
  Review them and explain concepts; don't write them for me.
- Boilerplate (CI, pyproject, config): you may write it,
  and explain every non-obvious line.
- Before I implement: ask me for a failing test first.
- Reviews: Clean Code principles + our checklist. Max 5 points, most important
  first, each with the "why".
- Talk to me like a senior engineer explaining to a colleague: trade-offs, not rules.

## Conventions
- Python 3.12+, uv, ruff, pytest, type hints everywhere
- Clean Architecture: domain imports nothing from use_cases, adapters or infrastructure
- No secrets in code; settings via environment variables
- Notebooks are for exploration; nothing in src imports from notebooks