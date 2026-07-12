# Full Expression Evaluator (precedence + unary)

A complete infix calculator handles operator precedence, parentheses, AND unary minus. The two-stack method (an operand stack and an operator stack) applies a pending operator when a lower-or-equal-precedence one arrives; unary minus is detected by context (start, after an operator, or after '(') and folded into the operand.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Evaluate Expression with Unary Minus](problem-01-evaluate-with-unary/PROBLEM.md) | Precedence + unary | Hard |
