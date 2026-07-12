# Bijection Mapping (Isomorphic / Pattern)

When a problem asks whether two sequences share the same *structure* of repetitions — isomorphic strings, a word pattern, a replace pattern — the key is to maintain a consistent one-to-one mapping. A single forward map is not enough: you must also keep a **reverse** map so two different source symbols can never collapse onto the same target. Assigning each symbol its first-occurrence index is an equivalent canonical form. The same rank-map idea also drives custom orderings like alien-dictionary checks and custom string sorts.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Isomorphic Strings](problem-01-isomorphic-strings/PROBLEM.md) | Two-way char map | Easy |
| 2 | [Word Pattern](problem-02-word-pattern/PROBLEM.md) | Letter<->word bijection | Easy |
| 3 | [Find and Replace Pattern](problem-03-find-and-replace-pattern/PROBLEM.md) | First-occurrence normalization | Medium |
| 4 | [Verifying an Alien Dictionary](problem-04-verifying-an-alien-dictionary/PROBLEM.md) | Rank map ordering | Easy |
| 5 | [Custom Sort String](problem-05-custom-sort-string/PROBLEM.md) | Rank-based stable sort | Medium |
