# Rabin-Karp Pattern Matching

**Rabin-Karp** finds a pattern inside a text by comparing hashes instead of characters. Each length-`m` window is treated as a base-`B` number modulo a large prime `M` (a **polynomial hash**), and the window hash is *rolled* forward in O(1): drop the leading character's weighted contribution, shift left by multiplying by `B`, and add the new trailing character. Because equal strings always hash equally, every real match is found; because unequal strings can collide, each hash hit is verified with a direct comparison. With a large prime the expected running time is O(n + m).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [All Pattern Match Indices (Rabin-Karp)](problem-01-all-match-indices/PROBLEM.md) | Rolling hash, all matches | Medium |
| 2 | [Count Pattern Occurrences](problem-02-count-occurrences/PROBLEM.md) | Rolling hash, count | Medium |
| 3 | [Find the Index of the First Occurrence in a String](problem-03-first-occurrence/PROBLEM.md) | First occurrence | Easy |
