# Sliding Window on Strings

## What it is

The **sliding window** technique keeps a contiguous range `[left, right]` of a
string in view and slides it across the input, maintaining just enough state
(usually a running character-frequency count) to answer a question about the
current window in O(1) amortized time per step. Instead of re-examining every
substring from scratch (which is O(n^2) or worse), you *extend* the window on
the right and *shrink* it on the left only when a constraint is violated.

There are two flavors you will meet constantly:

1. **Fixed-size window** — the window always has length `k` (or `len(pattern)`).
   You add the entering character on the right, remove the leaving character on
   the left, and check the window each step. Used for "does a substring of
   length k satisfy X" questions (anagrams, permutations).
2. **Variable-size window** — the window grows greedily on the right and
   shrinks from the left whenever it becomes invalid. You track the best window
   seen (longest / shortest). Used for "longest / shortest substring such
   that ..." questions.

The shared invariant: **each of `left` and `right` only ever moves forward**,
so the two pointers together traverse the string in linear time, even though
the window itself expands and contracts.

## When to reach for it

- The problem asks about a **contiguous substring** (not a subsequence).
- You want the longest / shortest / count of substrings satisfying a property
  that is *monotone* — adding characters can only make the window "more
  invalid," so once valid-again you can stop shrinking.
- You need to compare a window's character composition against a target
  (anagram, permutation, "contains all of t").
- A brute-force "check every substring" is O(n^2) and you need O(n).

## Complexity

| Variant | Time | Space |
|---|---|---|
| Variable window (longest/shortest) | O(n) | O(k) for the alphabet / distinct chars |
| Fixed window of size k | O(n) | O(k) |
| Window with need/have match counts | O(n + m) | O(m) for pattern counts |

`n` is the length of the string being scanned and `m` the pattern length. The
space is bounded by the alphabet size (O(1) if you assume a fixed alphabet such
as lowercase ASCII).

## Problems

| # | Problem | Summary | Difficulty |
|---|---|---|---|
| 1 | [Longest Substring Without Repeating Characters](problem-01-longest-substring-without-repeating-characters/PROBLEM.md) | Longest window with all-distinct characters | Medium |
| 2 | [Longest Substring with At Most K Distinct Characters](problem-02-longest-substring-with-at-most-k-distinct/PROBLEM.md) | Longest window holding at most `k` distinct characters | Medium |
| 3 | [Permutation in String](problem-03-permutation-in-string/PROBLEM.md) | Does a fixed-size window equal a permutation of the pattern | Medium |
| 4 | [Longest Repeating Character Replacement](problem-04-longest-repeating-character-replacement/PROBLEM.md) | Longest window makeable uniform with `k` replacements | Medium |
| 5 | [Minimum Window Substring](problem-05-minimum-window-substring/PROBLEM.md) | Shortest window containing every character of `t` | Hard |
