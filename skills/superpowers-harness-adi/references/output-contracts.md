# Output Contracts

## `sh-start`

Return in this order:

1. current understanding of the problem
2. MVP and explicit non-goals
3. route options (at most 3), each with: applicable conditions, advantages, trade-offs, impact on MVP, impact on learning value, when to abandon
4. convergence section: recommended route, reason, key reason for not recommending others
5. prompt user to fill and confirm the decision record:
   - one-sentence goal
   - current MVP
   - explicit non-goals
   - chosen route
   - reason for not choosing other routes
6. the concise main document only after the decision record is confirmed, containing: goal, MVP, non-goals, route, at most 3 result-oriented milestones, completion standards, human approval points, highest drift risks

## `sh-pack`

Return one current execution package with:

1. target result
2. why now
3. explicit non-goals
4. task list
5. dependencies
6. acceptance criteria
7. stop lines
8. drift risks

## `sh-run`

Return an execution report with:

1. completed work
2. unresolved risks
3. hard parts
4. trade-offs
5. human decisions needed
6. learning summary — must include all four fields:
   - the most critical technical challenge this round
   - why the chosen approach was selected
   - what alternative approaches were abandoned
   - the one point most worth discussing in a future interview or retrospective
7. developer validation record — return this template to the user after the report and ask them to fill it:

```
我的验收判断：
1. 这轮是否通过：
2. 是否更接近当前里程碑目标：
3. 是否引入了不想要的复杂度：
4. 下一步继续什么：
5. 下一步不做什么：
6. 本轮需要记录的关键决策或异常：
```

## `sh-recover`

Return:

1. current mainline
2. what drifted
3. what should stop
4. what stays current vs execution vs legacy
5. whether documents need rewriting
6. the next recommended entry
