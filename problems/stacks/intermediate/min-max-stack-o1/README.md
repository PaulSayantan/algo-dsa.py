# Min / Max Stack (O(1))

A stack can report its current minimum (or maximum) in O(1) by storing, alongside each pushed value, the best-so-far seen up to that point. Popping discards both, so the running extreme is always correct. This 'carry the aggregate' trick generalizes to any prefix-computable statistic.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Min Stack](problem-01-min-stack/PROBLEM.md) | Carry running min | Medium |
| 2 | [Max Stack](problem-02-max-stack/PROBLEM.md) | Max retrieval/removal | Hard |
| 3 | [Min-Max Stack](problem-03-min-max-stack/PROBLEM.md) | Carry running min and max | Medium |
| 4 | [GCD Stack](problem-04-gcd-stack/PROBLEM.md) | Carry running GCD | Medium |
| 5 | [Bitwise-AND Stack](problem-05-bitwise-and-stack/PROBLEM.md) | Carry running bitwise AND | Medium |
