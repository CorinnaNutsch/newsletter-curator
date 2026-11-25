# ADR 0001: The item is an article link, not a newsletter issue

Status: accepted, 2026-11-23

## Context
The ranker, the digest, feedback and deduplication all operate on "items", so the item unit shapes almost everything else. Options: A, the whole newsletter issue; B, an article link inside an issue; C, both ([design.md](../design.md) section 6).

The data spike labeled 2 issues each of the 3 MVP sources (Data Elixir, Data Science Weekly, True Positive Weekly), 6 emails in total, by hand. See [data-spike.md](../data-spike.md).

## Decision
**One item is one article link (option B).** The issue is kept as context: each item records its source, issue and position within the issue.

## Evidence
- **Several unrelated topics per issue.** Data Elixir issue 595 alone covers ML career advice, Bayesian modeling, geospatial embeddings, R performance, forecasting, DuckDB and visualization. An issue-level label would say almost nothing, so classification and ranking have to work per link.
- **Relevant links per issue (same in both issues of each source, so it describes the template):**

  | Source | Items | All links in email |
  |---|---|---|
  | Data Elixir | 9 and 9 | 28 and 29 |
  | Data Science Weekly | 23 and 25 | 56 and 58 |
  | True Positive Weekly | 8 and 8 | 24 and 24 |

  Most links in an email are noise (sponsors, footer, feedback, repeats of last week), so extraction has to filter.
- **Blurbs vary by source.** Data Elixir: every item has a 2–4 sentence blurb. Data Science Weekly: most do, but its "Cutting Room Floor" section is title-only. True Positive Weekly: none.
- **The same article appears in several sources.** "How to Learn ML in 2026" is in Data Elixir 595 and Data Science Weekly 674. "Asking LLM for confidence" is in Data Science Weekly 674 and True Positive Weekly 184. Deduplication only makes sense per link.

## Consequences
- Parsing is per template: the parser must tell items from noise (sponsored items that look like normal ones, "last issue's top links", footers).
- **The blurb is optional.** For sources without blurbs an item may be only a title and a URL until the article is fetched.
- **Anchor text can be partial.** In True Positive Weekly the link covers only part of the headline (`[Project]` and other tags sit outside the link).
- **The URL is not an ID yet.** In all three sources every link is an opaque, per-subscriber tracking redirect. The target cannot be recovered from the email alone, so deduplication by canonical URL needs the redirects resolved first (an open problem, to be solved in the URL canonicalization work).
- **Forwarding:** `From` and `Return-Path` are the forwarder, with no `List-Id` or `X-Forwarded-*`. The source can only be identified from the forwarded text in the body, the subject and the link domains.

## Limits of the evidence
- Only three weekly curated-link sources, 2 issues each. The planned skim of other source types (a single-article Substack, a roundup, Medium) was skipped, so the decision is not tested on those.
- Newsletters without links (text only) are untested.
- The overlap between sources has been spot-checked, not counted.
- The relevance labels are by hand, and the first draft was prefilled by script and then reviewed.
