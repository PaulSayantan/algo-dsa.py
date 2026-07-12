# Polynomial Prefix Hashing (Substring Equality)

Precomputing **prefix hashes** turns any substring's polynomial hash into an O(1) lookup. With `H[i]` the hash of the first `i` characters and `PW[k] = B^k mod M`, the hash of `s[l..r]` is `(H[r+1] - H[l]*PW[r-l+1]) mod M`: the leading prefix is shifted left to line up digit-for-digit and subtracted away. After an O(n) build, substring-equality queries, distinct-substring counting, and duplicate detection all become constant-time hash comparisons.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Substring Equality Queries](problem-01-substring-equality-queries/PROBLEM.md) | Prefix hash, O(1) query | Medium |
| 2 | [Count Distinct Substrings of Length L](problem-02-count-distinct-of-length/PROBLEM.md) | Distinct substrings | Medium |
| 3 | [Check If Two Substrings Are Equal](problem-03-check-two-substrings-equal/PROBLEM.md) | O(1) equality | Easy |
