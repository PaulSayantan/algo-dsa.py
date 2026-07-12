# Tree Isomorphism / Canonical Hashing

The **AHU (Aho-Hopcroft-Ullman)** algorithm assigns every rooted tree a canonical signature: recursively compute each child's signature, **sort** them (so sibling order is irrelevant), and wrap the concatenation in brackets. Two rooted trees are isomorphic iff their canonical signatures are identical, so isomorphism testing, counting distinct tree shapes in a forest, and computing a canonical fingerprint all reduce to building and comparing these strings. Trees are given as parent arrays (`-1` marks the root); using the canonical STRING as the key keeps everything deterministic (no salted built-in `hash()`).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Are Two Rooted Trees Isomorphic?](problem-01-rooted-tree-isomorphism/PROBLEM.md) | AHU isomorphism | Medium |
| 2 | [Count Distinct Rooted-Tree Shapes](problem-02-count-distinct-shapes/PROBLEM.md) | Distinct shapes via canonical set | Medium |
| 3 | [Canonical Hash of a Rooted Tree](problem-03-canonical-hash/PROBLEM.md) | Canonical signature string | Medium |
