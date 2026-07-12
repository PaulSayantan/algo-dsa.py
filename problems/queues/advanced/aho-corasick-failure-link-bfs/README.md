# Aho–Corasick Failure-Link BFS Build

Aho–Corasick matches many patterns at once with a trie augmented by failure links (the longest proper suffix that is also a trie prefix). Those links are computed by a BFS over the trie in increasing depth, guaranteeing each node's dependencies are ready. Matching is then linear in the text.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Count Multi-Pattern Occurrences](problem-01-count-pattern-occurrences/PROBLEM.md) | BFS failure links | Hard |
