# Palindromic Tree (Eertree)

The **Palindromic Tree**, also called the **Eertree**, is a data structure that
stores *every distinct palindromic substring* of a string. Despite the fact that
a string of length `n` can contain up to `O(n^2)` palindromic *occurrences*, the
key theorem behind the eertree is that a string has **at most `n` distinct
palindromic substrings**. The eertree therefore uses only `O(n)` nodes (plus two
sentinel roots), and it is built **incrementally**: after appending each new
character, the structure is updated in amortized `O(1)` time (technically
`O(log |Σ|)` if you store outgoing edges in a hash map / balanced map).

## Structure at a glance

- **Two root nodes.** Root with length `-1` (the "imaginary" root, used so that
  single characters can be created) and root with length `0` (the empty string).
- **Every other node** represents exactly one distinct palindrome and stores:
  - its **length**,
  - **outgoing edges** labeled by a character `c`: following edge `c` from a
    palindrome `P` gives the palindrome `cPc`,
  - a **suffix link** to the *longest proper palindromic suffix* of this
    palindrome.
- A pointer **`last`** tracks the longest palindromic suffix of the current
  prefix; it is where each insertion begins its search.

## When to reach for it

Reach for an eertree whenever a problem asks you to reason about **palindromic
substrings collectively** rather than one candidate at a time:

- counting **distinct** palindromic substrings,
- counting **all** palindromic substrings (each node stores/propagates an
  occurrence count),
- the **longest** palindromic substring (largest node length),
- weighting palindromes, e.g. maximizing `length × occurrences`,
- **palindromic factorization** DP (minimum / number of ways to cut a string
  into palindromes), which becomes near-linear using the eertree's *series
  links* (difference of consecutive suffix-link lengths).

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Build over string of length `n` | `O(n · log \|Σ\|)` (or `O(n)` with array edges) | `O(n · \|Σ\|)` worst / `O(n)` with maps |
| Number of distinct palindromes | `O(1)` after build (`#nodes − 2`) | — |
| Count all occurrences | `O(n)` propagation over suffix links | `O(n)` |
| Palindromic factorization DP | `O(n · log n)` with series links | `O(n)` |

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Count Distinct Palindromic Substrings](problem-01-count-distinct-palindromic-substrings/PROBLEM.md) | Number of eertree nodes = number of distinct palindromes | Medium |
| 2 | [Longest Palindromic Substring](problem-02-longest-palindromic-substring/PROBLEM.md) | Node with the maximum length | Medium |
| 3 | [Count All Palindromic Substrings](problem-03-count-all-palindromic-substrings/PROBLEM.md) | Occurrence counting + suffix-link propagation | Medium |
| 4 | [Max Length × Occurrences](problem-04-max-length-times-occurrences/PROBLEM.md) | Weighting each palindrome by `len × count` | Hard |
| 5 | [Palindrome Partitioning II](problem-05-palindrome-partitioning-ii/PROBLEM.md) | Near-linear palindromic factorization via series links | Hard |
