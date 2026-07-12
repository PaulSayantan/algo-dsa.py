# Min-Stack Aggregate Generalization

The Min-Stack trick — carry the running minimum alongside each element — generalizes to *any* associative aggregate: store the fold of the whole stack (min, max, gcd, sum, and/or) with each frame so a push/pop keeps it current and the whole-stack query is O(1).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Stack with O(1) Min, Max, and GCD](problem-01-aggregate-stack/PROBLEM.md) | Associative fold per frame | Medium |
