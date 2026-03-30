# Input Checks

## Minimal Trigger Rule (applies to all entries)

If the user's input is short (fewer than 30 words) or clearly missing most required fields, do not return a blank template. Instead:

1. Read the user's intent from their brief description.
2. Draft all required template fields based on that intent.
3. Present the draft clearly, labeled as "草稿待确认 / Draft for Confirmation".
4. Ask the user to confirm or correct before entering the workflow.
5. Treat the confirmed draft as the validated input and proceed.

Only return a blank template when the user's intent is too vague to draft any meaningful fields (e.g. a single word with no context).

## Shared Rule

Always inspect the user's request before routing into the real workflow.

- Short input (< 30 words): apply Minimal Trigger Rule above, draft and confirm.
- Missing one lightweight detail: ask for it directly.
- Missing multiple key details: apply Minimal Trigger Rule if intent is readable; return the matching template only if intent is too vague.
- For `sh-run`, missing a current execution package is a hard stop even after drafting.

## `sh-start`

Minimum required input:

1. current project or feature background
2. the problem to solve
3. why now
4. known constraints

If several of these are missing, return `templates/sh-start.md`.

## `sh-pack`

Minimum required input:

1. current main goal
2. what this round should complete
3. explicit non-goals
4. upstream decision record or main document

If several of these are missing, return `templates/sh-pack.md`.

## `sh-run`

Minimum required input:

1. current execution package or equivalent summary
2. current round goal
3. explicit non-goals
4. stop conditions or escalation conditions

If the package is missing, return `templates/sh-run.md` and recommend `sh-pack`.

## `sh-recover`

Minimum required input:

1. current project or feature
2. where drift is happening
3. what the human wants to regain first
4. available evidence

If several of these are missing, return `templates/sh-recover.md`.
