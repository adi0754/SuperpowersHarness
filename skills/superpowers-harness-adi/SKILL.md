---
name: SuperpowersHarness
description: Use when a developer wants to drive a complex project or large feature with a controlled superpowers workflow, especially when they mention sh-start, sh-pack, sh-run, or sh-recover, or they need bounded scoping, execution-package creation, controlled implementation, or project recovery.
---

# Superpowers Harness

Treat this skill as a workflow entry layer on top of superpowers.

Its job is to:

1. reduce repeated prompt writing
2. give the developer a stable default workflow
3. keep the human in charge of goals, boundaries, route choices, and recovery

## Core Rule

Never enter the actual workflow until the active entry passes input check.

If the user's input is short or missing key fields:

1. If intent is readable (even from a brief description): draft all template fields, present as "草稿待确认", and ask the user to confirm or correct before proceeding.
2. If intent is too vague to draft: return the matching template from `templates/` and ask the user to fill it.
3. For `sh-run`: a missing execution package is always a hard stop — no drafting can substitute for an actual package.

Read `references/input-checks.md` before choosing how to handle missing information.

## Entry Map

| Entry | Use for | Internal route |
| --- | --- | --- |
| `sh-start` | new project start; large feature start on an existing project | `brainstorming` -> user decision -> `writing-plans` |
| `sh-pack` | turning an approved direction into one current execution package | `writing-plans` |
| `sh-run` | implementing an already-written execution package | `executing-plans` |
| `sh-recover` | regaining control after project drift or narrative drift | `brainstorming` -> optional `writing-plans` |

## Step 1: Identify the Entry

Map the user's wording to the nearest entry.

Examples:

- "start this project" -> `sh-start`
- "plan this large feature" -> `sh-start`
- "create the current execution package" -> `sh-pack`
- "start implementation" -> `sh-run`
- "this project has drifted" -> `sh-recover`

If the user explicitly names an entry, trust it unless it is clearly impossible.

## Step 2: Run Input Check

Read `references/input-checks.md`.

Rules:

1. If input is short (fewer than 30 words): apply the Minimal Trigger Rule — draft all template fields from the user's intent, label it "草稿待确认", and ask for confirmation before proceeding.
2. If only one small detail is missing, ask for that one detail.
3. If multiple key fields are missing but intent is readable: apply the Minimal Trigger Rule.
4. If intent is too vague to draft anything meaningful: return the matching template from `templates/`.
5. If `sh-run` lacks a current execution package or equivalent information, do not continue even after drafting. Tell the user to fill the `sh-run` template or go back to `sh-pack`.

## Step 3: Execute the Right Route

### `sh-start`

Use `superpowers:brainstorming` first.

Focus on:

1. what problem this work actually solves
2. current MVP
3. explicit non-goals
4. key risks and route options
5. what the human must decide

Do not jump into implementation or heavy PRD.

Brainstorming output format constraints:

- Give at most 3 route options.
- Each route must include all six fields: applicable conditions, advantages, trade-offs, impact on MVP, impact on learning value, when to abandon this route.
- End with a convergence section: recommended route, reason for recommendation, key reason for not recommending the others.

After brainstorming output, prompt the user to leave a decision record before continuing. The minimum decision record must cover:

1. one-sentence goal
2. current MVP
3. explicit non-goals
4. chosen route
5. reason for not choosing the other routes

Do not switch to `superpowers:writing-plans` until the user has left this record.

After the user leaves the decision record, switch to `superpowers:writing-plans` and write one concise main document for the project or feature.

Main document constraints:

- Milestones: at most 3. Each milestone must be result-oriented (e.g. "core loop is working"), not tech-module-oriented (e.g. "build the backend").
- Prioritize: why this exists, what the goal is, what is explicitly not in scope, what the completion standard is, which points require human approval.
- Do not expand into a heavy PRD. Do not generate stage task documents as a side effect.

Required output shape:

1. one-sentence goal
2. current MVP
3. explicit non-goals
4. recommended route
5. human decision record (confirmed by user)
6. concise main document (goal, MVP, non-goals, route, at most 3 milestones, completion standards, human approval points, highest drift risks)

### `sh-pack`

Use `superpowers:writing-plans`.

Build one current execution package only.

Allowed document types for `writing-plans`. Only generate documents from this list:

1. Project Main Document (项目主文档)
2. Current Execution Package (当前里程碑执行包)
3. Milestone Retrospective (阶段复盘)
4. Anomaly Root Cause Card (异常归因卡)
5. Final Project Retrospective (最终项目复盘)
6. Interview Expression Pack (面试表达素材包)

Do not generate documents outside this list. Do not generate heavy PRDs. Do not generate multi-level stage systems.

Required package sections:

1. target result
2. why now
3. explicit non-goals
4. task list (4–6 tasks, not too granular)
5. dependencies between tasks
6. acceptance criteria
7. stop lines
8. drift risks

Do not grow extra stages or future packages by default.

### `sh-run`

Use `superpowers:executing-plans`.

Before execution:

1. confirm the execution package exists
2. restate current goal
3. restate explicit non-goals
4. restate stop conditions

During execution:

1. stay inside the current package
2. stop and report if any of the following occur:
   - a new external service or dependency is required
   - core data structures or state structures need to change
   - the current technical route needs to change
   - the execution package goal itself needs to be rewritten
   - the current problem has become a scope change, not an implementation problem

New situation handling:

- Any new situation encountered during execution defaults to an Anomaly Root Cause Card entry, not a new stage.
- Only escalate to main document or milestone level if the new situation affects the core loop, project main structure, or project main route.
- Do not silently absorb scope changes. Surface them to the human.

Execution report must include (read `references/output-contracts.md` for full format):

1. completed work
2. unresolved risks
3. hard parts
4. trade-offs
5. human decisions needed
6. structured learning summary (4 required fields)
7. developer validation record template (return to user to fill)

### `sh-recover`

Use `superpowers:brainstorming` to re-establish control.

Read the current evidence first:

1. code and real artifacts
2. current truth documents
3. execution documents
4. legacy or archive materials only when needed

Focus on:

1. what the current mainline really is
2. what drifted
3. what should stop
4. what remains current vs execution vs legacy
5. whether the main document or current execution package must be rewritten

If a rewritten current truth or execution package is needed, switch to `superpowers:writing-plans`.

## Human Control Points

The human must approve or record decisions for:

1. one-sentence goal
2. MVP boundary
3. explicit non-goals
4. route choice
5. current execution package boundary
6. any scope, route, or structure change discovered during execution

Never let the skill silently absorb these choices.

## Output Style

All planning outputs must follow this style:

1. Explain why before explaining what. Lead with purpose, not implementation detail.
2. Use plain language. Avoid stacking low-level implementation terms when a plain description is clearer.
3. Write for the project lead's understanding first, the executor's needs second.
4. Every planning output must explicitly state: current goal, why now, explicit non-goals, completion standard, points requiring human approval.
5. Do not expand requirements, stages, or documents for the sake of completeness.

## Guardrails

1. Do not expand the project for completeness.
2. Do not generate heavy PRDs by default.
3. Do not create extra stages unless the current line truly changed.
4. Do not let `sh-run` start without stop lines.
5. Do not let `sh-start` generate the main document before the user leaves a decision record.
6. Do not silently absorb new situations into new stages during `sh-run`. Surface them first.
7. Prefer outputs written for the project lead, not just the executor.

## Output Contract

Read `references/output-contracts.md` when composing the final response for an entry.
