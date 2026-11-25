---
name: clean-code-review
description: Review my changed code against Clean Code and Clean Architecture. Use when I ask for a review or before a commit.
---
Review the current diff. Do not change any files.

Check, in this order:
1. Names: do they say what things are and do?
2. Functions: does each do one thing? Too many arguments?
3. Dependency rule: does domain or use_cases import a framework, API client or database?
4. Tests: is new logic covered? Are tests readable?
5. Error handling: specific exceptions, no silent failures?
6. Secrets or hard-coded config?

Output: max 5 findings, most important first. For each: where, what, why it matters,
and a hint how to fix it, not the fixed code. End with one thing I did well.
```
