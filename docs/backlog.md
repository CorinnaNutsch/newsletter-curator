# Backlog

Concrete tasks for the current and next sprint. Design decisions live in [`design.md`](design.md) and [`adr/`](adr/). Learning goals, reading and long-term planning are kept outside the repo.

Current sprint: **1** (scheduled 19–25 Nov, still in progress).

## Sprint 1: setup, data and baseline

### Setup and design
- [x] Repo with uv, ruff, pytest and pre-commit
- [x] Type checker (mypy, strict)
- [ ] Architecture sketch: layers and entities, drawn

### Parser
One source at a time: build against issue 1's gold set, then validate on the held-out issue 2. Output is raw mail → items (title, url, source, date, text). Tests first.

- [ ] Scrubbed fixture and expected items for Data Elixir issue 1, in `tests/fixtures/`. Done when: real markup and every kind of noise are kept, and no real content or tracking URLs remain
- [ ] First failing parser test. Done when: it fails for the expected reason
- [ ] Data Elixir parser. Done when: the issue 1 test passes
- [ ] Validate Data Elixir on issue 2. Done when: the result is checked against its gold set
- [ ] Data Science Weekly parser: first check whether it shares a template. Done when: validated on issue 2
- [ ] True Positive Weekly parser: first check whether it shares a template. Done when: validated on issue 2

### Deduplication
Links are per-subscriber tracking redirects, so they have to be resolved first (see [ADR 0001](adr/0001-item-unit.md)).

- [ ] URL canonicalization and duplicate detection, with tests
- [ ] Cross-newsletter grouping: one canonical article with the list of newsletters that link it, and a count of **distinct sources**
- [ ] Count the overlap between sources (title join across the labeled links) and summarize the link mix ([data spike](data-spike.md), step 4)

### Data and baseline
- [ ] Export about 3 months of old newsletters, keeping the original headers. Keep the raw mail out of git
- [ ] Feedback table and a first manual labeling session (~100 items). Read/starred flags are per issue, so use them only for a per-source open rate, not as item labels
- [ ] Baseline: recency plus distinct-source count, with per-source open rate as a side feature. Evaluate with a **time-based split**

## Sprint 2: model and architecture
- [ ] Refactor Sprint 1 code into layers: the core imports no framework, API client or database
- [ ] Topic clustering: embed title and text, group similar articles from different newsletters. Check with ~30 hand-labeled pairs (same topic or not). Use cluster size as a "trending" signal, with one digest entry per cluster. Can be pulled into Sprint 1 if ahead
- [ ] Embedding ranker (content-based, own feedback as labels) that beats the baseline on the time-based split. Done when: the margin and its uncertainty are known
- [ ] Cold start: new sources and new items without feedback
- [ ] FastAPI: `/digest` and `/feedback` (👍/👎)
- [ ] Containerfile (hand-written); the app runs in Podman
- [ ] Optional: dev container, after the first Containerfile
- [ ] Optional: public news dataset (MIND small). Check its license and keep it in `data/`. Use it to test the evaluation code, and as a benchmark if the own labeled data is too small

## Blocked or parked
- [ ] **IMAP access (blocked):** app password stored in an environment variable, see [`setup-imap.md`](setup-imap.md). The parser does not depend on it. If switching to the Gmail API later: OAuth `gmail.readonly`, and publish the app "In production" so the refresh token does not expire after 7 days
- [ ] **Podman machine and first container (parked until Sprint 2):** on 2026-11-23, `podman machine init` worked but `start` failed (`vfkit exited unexpectedly`). Podman 5.6.2, Intel Mac (i7-1068NG7, AVX-512), default Fedora CoreOS image (kernel 6.15.10): the guest logs an xsave warning at boot, hangs, and SSH never comes up. Ideas: an older machine image (`podman machine init --image ...`), a newer Podman, or Colima/Lima

## Decide later
- [ ] By Sprint 3: whether and where to deploy (Fly.io, Cloud Run, VPS, or stay local). Create an account only after deciding

## Done in Sprint 0
- [x] Design: vision, user stories, scope, data flow, digest mock, metrics, open questions ([`design.md`](design.md))
- [x] Data spike and item-unit decision ([`data-spike.md`](data-spike.md), [ADR 0001](adr/0001-item-unit.md)). The skim of other source types was skipped on purpose
- [x] Fixture approach decided ([`design.md`](design.md), section 12)
- [x] Newsletter mailbox and source list set up; LLM API key with a spending limit; GitHub repo; Podman and Claude Code installed
