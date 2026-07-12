# Pratt Parsing / Operator-Precedence Parsing

Pratt (top-down operator-precedence) parsing assigns each operator a binding power and recursively parses expressions, consuming an operator only while its binding power exceeds the caller's threshold. It elegantly handles precedence and right-associativity (like `^`) and underlies many real expression compilers.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Pratt-Parse and Evaluate (with Power)](problem-01-pratt-evaluate/PROBLEM.md) | Binding-power parse | Hard |
