---
name: backlog-check
description: Check which tasks in docs/backlog.md my changes complete. Use before a commit, or when I ask whether a backlog task is done.
---
Check my work against `docs/backlog.md`. Do not change, stage or commit any files.

1. Find the changes. Use the staged diff (`git diff --cached`). If nothing is staged, use the
   uncommitted changes, including untracked files, and say so. If there are no changes, say so
   and stop. If I name a task, check that task against the current repo instead.
2. Pick the open tasks that the changes relate to. Ignore the rest.
3. For each one, check every part of the task, including its "Done when" text if it has one.
   - Require evidence: a file and line, or the output of a command you ran.
   - Code existing is not enough. For parsers and other logic, run the relevant tests.
   - If only staged changes are checked and there are also unstaged ones, say that test
     results reflect the working tree, not just what will be committed.
   - Never print raw email content or real tracking URLs.
4. Give each task one verdict:
   - **Done:** every part has evidence.
   - **Partly done:** say what is missing.
   - **Unclear:** say what you could not verify, for example something done outside the repo.
     If the task has no checkable criterion, suggest I add a "Done when".

Output: one entry per related task with the task name, verdict and evidence. If no task is
related, say so in one line. End with the checkbox lines you suggest I tick. I tick them myself.
If a finished change matches no task, mention it, but do not invent a task for it.
