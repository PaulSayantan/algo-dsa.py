# Shunting-Yard / Infix Conversion

Dijkstra's shunting-yard algorithm converts an infix expression to postfix (RPN) using an operator stack that respects precedence and associativity: numbers go straight to the output, and an incoming operator first pops all stacked operators of greater-or-equal precedence. One O(n) pass yields a parenthesis-free form ready for stack evaluation.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Infix to Postfix Conversion](problem-01-infix-to-postfix/PROBLEM.md) | Infix->postfix | Medium |
| 2 | [Infix to Prefix Conversion](problem-02-infix-to-prefix/PROBLEM.md) | Infix->prefix (reversed pass) | Medium |
| 3 | [Evaluate Infix Arithmetic Expression](problem-03-evaluate-infix-expression/PROBLEM.md) | Two-stack evaluation | Medium |
| 4 | [Infix to Postfix with Right-Associative Exponent](problem-04-infix-to-postfix-with-exponent/PROBLEM.md) | Precedence + associativity | Medium |
| 5 | [Fully Parenthesize an Infix Expression](problem-05-fully-parenthesize-expression/PROBLEM.md) | Operand-string rebuild | Medium |
