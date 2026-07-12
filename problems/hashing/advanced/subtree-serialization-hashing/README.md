# Subtree Serialization / Duplicate Subtrees

Two subtrees are identical iff their **canonical serializations** are equal. Serialize each subtree bottom-up as `value + left-serialization + right-serialization` (with a sentinel like `#` for a null child), then use the serialization STRING as a dictionary key mapping to a count. Structural questions — how many duplicate subtree classes exist, how many distinct subtrees, are two trees identical — reduce to counting or comparing these canonical strings, all in O(n) work per node (using the string key directly, never the salted built-in `hash()`).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Find Duplicate Subtrees](problem-01-find-duplicate-subtrees/PROBLEM.md) | Serialization -> count map | Medium |
| 2 | [Count Distinct Subtrees](problem-02-count-distinct-subtrees/PROBLEM.md) | Distinct serializations | Medium |
| 3 | [Identical Trees via Serialization](problem-03-same-tree-serialization/PROBLEM.md) | Serialization equality | Easy |
