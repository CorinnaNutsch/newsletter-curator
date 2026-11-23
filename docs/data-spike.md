# Data spike: decide the item unit, label three sources

Sprint 0 / first day of Sprint 1. Goal: decide the **item unit** (Project Design, section 6: issue, article link, or both) on real emails, and produce the first **gold sets** for the parser.

MVP sources: **Data Elixir, Data Science Weekly, True Positive Weekly** (all weekly curated-link lists).

Raw emails stay local. Save them under `data/spike/` (`data/`, `*.eml` and `*.mbox` are gitignored). Never commit them.

## Why a small slice, labeled by hand
- Newsletters from one source share a **template**. The unit of generalization is the template, not the email, so 2 issues per source tell you almost everything about it.
- Your hand-labeled links are the **gold set**: the links a correct parser should return. Anything extra the parser returns counts as a false positive automatically, so only **relevant links** need labeling, not the noise.

## 1. Collect (~20 min)
- 2 issues each of the three sources, preferably consecutive. 6 emails.
- Download via Gmail ("Download message") into `data/spike/`.
- All mail was forwarded: on the first 2-3 emails open "Show original" and check which headers survive (`From`, `Reply-To`, `Return-Path`, `X-Forwarded-*`, `List-Id`). Can you still identify the source?

## 2. Skim the other sources (~30 min, notes only)
So the item unit is not decided on three sources alone. Open 1 issue each from about 5 other sources (a single-article Substack, a roundup, Medium, ...). Write 3-5 lines per source: items per issue, blurb per link or not, one article or a list of links, layout. No tables.

## 3. Label (~45 min)
Per source, issue 1 and issue 2. Copy the templates from `docs/templates/` to `data/spike/`:

- `emails.csv`: one row per email (source, date, forwarded, link counts, blurbs, source identifiable, `template_notes`)
- `links.csv`: one row per **relevant** link (position, anchor text, raw URL, final URL if known, blurb)

Read the **rendered** email to decide what is relevant, not only the HTML source. Put the noise in words in `template_notes` (for example: "footer with 6 links, sponsor block after item 3").

## 4. Decide and write up
- [ ] Item unit written into Project Design, section 6, with the evidence
- [ ] "Item unit" ticked in section 12
- [ ] Answers to: link mix, blurbs, tracking URLs (recoverable from the email alone?), forwarding, rough overlap between the three sources

## 5. Then (Sprint 1, tests first)
1. Write the first **failing test** for source 1 against its issue 1 gold set.
2. Build the parser until it passes. Hints from the mentor, not solutions.
3. Validate on **issue 2**, which stays held out until the rules are written. Passing only on the issue you built against shows the parser memorized an email; passing on the other issue shows it parsed the template.
4. Decide how to keep fixtures in git (anonymize/trim a few emails, or write small synthetic ones), because `*.eml` is gitignored on purpose.
5. Repeat for sources 2 and 3. Check whether the template is shared before writing a new parser.
