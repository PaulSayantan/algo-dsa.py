# Postfix (Reverse Polish Notation) Evaluation

In postfix notation the operator follows its operands, so no parentheses or precedence rules are needed. Evaluate with a stack: push numbers, and on an operator pop the top two, combine, and push the result. One left-to-right pass, O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Evaluate Reverse Polish Notation](problem-01-evaluate-rpn/PROBLEM.md) | Postfix stack eval | Medium |
| 2 | [Baseball Game](problem-02-baseball-game/PROBLEM.md) | Stack sweep with combine/pop operators | Easy |
| 3 | [Postfix to Infix Conversion](problem-03-postfix-to-infix/PROBLEM.md) | Postfix stack building infix strings | Easy |
| 4 | [Postfix to Prefix Conversion](problem-04-postfix-to-prefix/PROBLEM.md) | Postfix stack building prefix strings | Easy |
| 5 | [Evaluate Boolean Postfix Expression](problem-05-boolean-postfix-eval/PROBLEM.md) | Postfix eval with logical + unary operators | Easy |
