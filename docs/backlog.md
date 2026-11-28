# Backlog

Concrete coding tasks. Design decisions live in [`design.md`](design.md) and [`adr/`](adr/). Learning goals, reading and the roadmap are kept outside the repo.

Only the current sprint is planned. All other open tasks are in the backlog below, sorted by topic, with no sprint or date. When a sprint ends, unfinished tasks go back to the backlog or into the next sprint. Sprints are one week, Saturday to Friday.

## Current sprint: 2 (28 Nov – 4 Dec)
Coding on 28 and 29 Nov (about 6–7 h), then 5 travel days.

### Must
- [ ] Scrubbed fixture and expected items for Data Elixir issue 1, in `tests/fixtures/`. Done when: real markup and every kind of noise are kept, and no real content or tracking URLs remain. Fixture is committed; check with `backlog-check`, including the leak search (15–30 min)
- [ ] First failing parser test. Done when: it fails for the expected reason (30–60 min). Decide first what the parser returns: the expected JSON has `source` and `date` per item, the dataclasses have them on `NewsletterIssue`
- [ ] Data Elixir parser. Done when: the issue 1 test passes (3–5 h)
- [ ] Refactor, review, commit and open a PR (30–60 min)

### Stretch
- [ ] Validate Data Elixir on issue 2, with its fixture and expected items. Done when: the result is checked against its gold set (1.5–2.5 h)

### Optional on travel days
Never required. Finish the Must tasks first.
- [ ] Evening: architecture sketch, layers and entities, drawn; paper is fine (30–60 min)
- [ ] Evening: check whether Data Science Weekly and True Positive Weekly share the Data Elixir template. Check only (30 min)
- [ ] Evening: request a Google Takeout mail export and check that the original headers are kept. Keep it out of git (30–45 min, plus waiting for the export)
- [ ] Half day: URL canonicalization, test-first, with made-up URLs and no network. Redirect resolving and duplicate detection stay in the backlog (1.5–2.5 h)

## Open tasks by topic

### Parser
One source at a time: build against issue 1's gold set, then validate on the held-out issue 2. Output is raw mail → items (title, url, source, date, text). Tests first.

- [ ] Decode step: raw mail → decoded HTML, with its own test (see [design](design.md), section 12)
- [ ] Data Science Weekly parser: first check whether it shares a template. Done when: validated on issue 2
- [ ] True Positive Weekly parser: first check whether it shares a template. Done when: validated on issue 2

### Deduplication and grouping
Links are per-subscriber tracking redirects, so they have to be resolved first (see [ADR 0001](adr/0001-item-unit.md)).

- [ ] URL canonicalization and duplicate detection, with tests
- [ ] Cross-newsletter grouping: one canonical article with the list of newsletters that link it, and a count of **distinct sources**
- [ ] Count the overlap between sources (title join across the labeled links) and summarize the link mix ([data spike](data-spike.md), step 4)

### Data and baseline
- [ ] Export about 3 months of old newsletters, keeping the original headers. Keep the raw mail out of git
- [ ] Feedback table and a first manual labeling session (~100 items). Read/starred flags are per issue, so use them only for a per-source open rate, not as item labels
- [ ] Baseline: recency plus distinct-source count, with per-source open rate as a side feature. Evaluate with a **time-based split**

### Ranking model
- [ ] Embedding ranker (content-based, own feedback as labels) that beats the baseline on the time-based split. Done when: the margin and its uncertainty are known
- [ ] Topic clustering: embed title and text, group similar articles from different newsletters. Check with ~30 hand-labeled pairs (same topic or not). Use cluster size as a "trending" signal, with one digest entry per cluster
- [ ] Cold start: new sources and new items without feedback
- [ ] Optional: public news dataset (MIND small). Check its license and keep it in `data/`. Use it to test the evaluation code, and as a benchmark if the own labeled data is too small

### GenAI and evals
- [ ] LLM summaries and topic tags with structured output, behind an adapter
- [ ] Golden set (~30 items) and a measured prompt change
- [ ] Compare LLM ranker, embedding ranker and hybrid: same time-based split and metrics, plus cost and latency
- [ ] Decision note: when ML, when an LLM, when both

### Bandit and feedback loop
- [ ] Bandit for exploring new sources and topics, tested in an offline replay
- [ ] Bandit on real feedback, logging every decision for later offline evaluation
- [ ] Re-evaluate the rankers on real feedback

### Architecture, API and containers
- [ ] Architecture sketch: layers and entities, drawn (also optional in the current sprint)
- [ ] Refactor into layers: the core imports no framework, API client or database
- [ ] FastAPI: `/digest` and `/feedback` (👍/👎)
- [ ] Containerfile (hand-written); the app runs in Podman
- [ ] Optional: dev container, after the first Containerfile

### CI/CD and production
- [ ] CI: ruff, type check, tests and container build on every push
- [ ] Eval suite in CI on a small golden set
- [ ] Decide whether and where to deploy (Fly.io, Cloud Run, VPS, or stay local). Create an account only after deciding
- [ ] Daily digest delivered automatically, with 👍/👎. Done when: it runs for 3 days without manual steps
- [ ] Optional: add 1–2 external sources (RSS, arXiv or HN)

### Docs and sharing
- [ ] README and architecture diagram

## Blocked or parked
- [ ] **IMAP access (blocked):** app password stored in an environment variable, see [`setup-imap.md`](setup-imap.md). The parser does not depend on it. If switching to the Gmail API later: OAuth `gmail.readonly`, and publish the app "In production" so the refresh token does not expire after 7 days
- [ ] **Podman machine and first container (parked):** on 2026-11-23, `podman machine init` worked but `start` failed (`vfkit exited unexpectedly`). Podman 5.6.2, Intel Mac (i7-1068NG7, AVX-512), default Fedora CoreOS image (kernel 6.15.10): the guest logs an xsave warning at boot, hangs, and SSH never comes up. Ideas: an older machine image (`podman machine init --image ...`), a newer Podman, or Colima/Lima

## Done

### Sprint 1
- [x] Repo with uv, ruff, pytest and pre-commit
- [x] Type checker (mypy, strict)

### Sprint 0
- [x] Design: vision, user stories, scope, data flow, digest mock, metrics, open questions ([`design.md`](design.md))
- [x] Data spike and item-unit decision ([`data-spike.md`](data-spike.md), [ADR 0001](adr/0001-item-unit.md)). The skim of other source types was skipped on purpose
- [x] Fixture approach decided ([`design.md`](design.md), section 12)
- [x] Newsletter mailbox and source list set up; LLM API key with a spending limit; GitHub repo; Podman and Claude Code installed
