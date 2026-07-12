# Decode String (Nested)

Expanding a nested run-length encoding like `3[a2[c]]` needs two stacks (or one stack of frames): one for the repeat counts and one for the partial strings built so far. A `[` opens a new frame; a `]` pops the count and prefix and splices the repeated substring back in.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Decode String](problem-01-decode-string/PROBLEM.md) | Two-stack expansion | Medium |
| 2 | [Score of Parentheses](problem-02-score-of-parentheses/PROBLEM.md) | Stack of frame scores | Medium |
| 3 | [Number of Atoms](problem-03-number-of-atoms/PROBLEM.md) | Stack of count maps | Medium |
| 4 | [Ternary Expression Parser](problem-04-ternary-expression-parser/PROBLEM.md) | Right-to-left stack fold | Medium |
| 5 | [Parse Boolean Expression](problem-05-parse-boolean-expression/PROBLEM.md) | Bracket-frame fold | Medium |
