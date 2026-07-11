# Suffix Automaton

A **Suffix Automaton (SAM)** of a string `s` is the smallest deterministic finite
automaton (DFA) that recognizes exactly the set of all substrings of `s`. Every
path starting at the initial state spells out a distinct substring of `s`, and
every substring of `s` corresponds to exactly one such path.

Despite recognizing all `O(n^2)` substrings, the automaton has at most `2n - 1`
states and `3n - 4` transitions for `n >= 3`, and it can be built **online**
(character by character) in linear time over a constant-size alphabet.

## Core structure

- **States** are equivalence classes of substrings that share the same set of
  end positions (`endpos`). Each state `v` stores:
  - `len[v]`: length of the longest substring in the class.
  - `link[v]`: the **suffix link**, pointing to the state of the longest proper
    suffix that lies in a different `endpos` class.
  - `next[v]`: labeled transitions (a `char -> state` map).
- The suffix links form a tree (the **suffix-link tree**) rooted at the initial
  state; this tree is the parse/refinement tree of the `endpos` classes and is
  where most counting work happens.
- A single state `v` represents all substrings whose lengths lie in the interval
  `(len[link[v]], len[v]]`, so it accounts for exactly `len[v] - len[link[v]]`
  distinct substrings.

## When to reach for a Suffix Automaton

Reach for a SAM when a problem asks about the *set of all substrings* of a string
(or shared substrings between strings), especially:

- Counting the number of **distinct substrings** (and the sum of their lengths).
- Counting how many times a substring **occurs** (via `endpos` set sizes).
- Finding the **longest common substring** of two or more strings.
- Answering **k-th smallest substring** lexicographically.
- Matching / cyclic-rotation queries against a fixed text.

## Complexity

| Operation                                   | Time        | Space  |
| ------------------------------------------- | ----------- | ------ |
| Build automaton over alphabet `Sigma`       | `O(n * log Sigma)` (or `O(n)` with arrays) | `O(n * Sigma)` |
| Count distinct substrings / total length    | `O(n)` after build | `O(n)` |
| Occurrence count of a pattern `p`           | `O(|p|)` after preprocessing `endpos` sizes | `O(n)` |
| Longest common substring with string `t`    | `O(|t|)` after build | `O(n)` |

`n = |s|`. With a hash-map `next`, transitions cost an extra `log Sigma` (or
average `O(1)`); with fixed-size arrays it is strictly linear.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Count Distinct Substrings](problem-01-count-distinct-substrings/PROBLEM.md) | `sum(len[v] - len[link[v]])` over states | Medium |
| 2 | [Total Length of Distinct Substrings](problem-02-total-length-distinct-substrings/PROBLEM.md) | Sum of length-intervals per state | Medium |
| 3 | [Count Substring Occurrences](problem-03-count-substring-occurrences/PROBLEM.md) | `endpos` sizes via suffix-link tree | Medium |
| 4 | [Longest Common Substring of Two Strings](problem-04-longest-common-substring-two-strings/PROBLEM.md) | Run string `t` through SAM of `s` | Hard |
| 5 | [K-th Lexicographic Distinct Substring](problem-05-kth-lexicographic-substring/PROBLEM.md) | Count paths in the DAG + greedy DFS | Hard |
| 6 | [Cyclical Quest](problem-06-cyclical-quest/PROBLEM.md) | Cyclic matching + occurrence counts | Hard |
