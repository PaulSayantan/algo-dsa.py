# Basic Calculator

Evaluating an infix arithmetic string directly with a stack: keep a running value and a pending operator, push partial results for `+`/`-`, and fold `*`/`/` into the last pushed term immediately. Parentheses are handled by recursing or by stacking the context. Summing the stack at the end gives the answer in O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Basic Calculator II](problem-01-basic-calculator-ii/PROBLEM.md) | Precedence via term stack | Medium |
| 2 | [Basic Calculator](problem-02-basic-calculator/PROBLEM.md) | Parentheses via sign stack | Hard |
| 3 | [Basic Calculator III](problem-03-basic-calculator-iii/PROBLEM.md) | Precedence + nested parens | Medium |
| 4 | [Clumsy Factorial](problem-04-clumsy-factorial/PROBLEM.md) | Precedence via term stack | Medium |
| 5 | [Score of Parentheses](problem-05-score-of-parentheses/PROBLEM.md) | Depth-frame context stack | Medium |
