# Prefix (Polish Notation) Evaluation

Prefix (Polish) notation places the operator before its operands. Evaluate by scanning **right to left** with a stack: push operands, and on an operator pop the top two (first popped is the left operand), combine, and push. Like postfix, it needs no precedence rules.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Evaluate a Prefix Expression](problem-01-evaluate-prefix/PROBLEM.md) | Prefix stack eval | Medium |
| 2 | [Prefix to Infix Conversion](problem-02-prefix-to-infix/PROBLEM.md) | Right-to-left stack build | Easy |
| 3 | [Prefix to Postfix Conversion](problem-03-prefix-to-postfix/PROBLEM.md) | Right-to-left stack build | Easy |
| 4 | [Evaluate a Boolean Prefix Expression](problem-04-evaluate-boolean-prefix/PROBLEM.md) | Prefix stack eval (boolean) | Easy |
| 5 | [Validate a Prefix Expression](problem-05-validate-prefix-expression/PROBLEM.md) | Prefix arity check via stack | Easy |
