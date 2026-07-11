# Palindrome Partitioning II (Minimum Cuts)

**Difficulty:** Hard

Source: LeetCode 132 — "Palindrome Partitioning II".

## Description

Given a string `s`, partition it so that **every** piece is a palindrome. Return
the **minimum number of cuts** needed for such a partition. A partition into `k`
palindromic pieces uses `k - 1` cuts, so equivalently you are minimizing
`(number of palindromic pieces) - 1`.

The standard `O(n^2)` DP is well known. The point of this exercise is the
**online / near-linear** solution driven by a **Palindromic Tree (Eertree)** with
**series links** — a technique that answers "minimum palindromic factorization"
in `O(n log n)` and generalizes to counting factorizations and to processing the
string as it streams in.

## Constraints

- `1 <= len(s) <= 2000` (original LeetCode). The eertree + series-link method
  scales to `len(s) <= 10^5` and beyond.
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "aab"
Output: 1
Explanation: One cut splits "aab" into ["aa", "b"], both palindromes.
             That is 2 pieces, i.e. 1 cut. No zero-cut partition exists because
             "aab" itself is not a palindrome.
```

### Example 2

```
Input:  s = "a"
Output: 0
Explanation: "a" is already a palindrome; no cut is needed.
```

### Example 3

```
Input:  s = "bananas"
Output: 2
Explanation: A minimal partition is ["b", "anana", "s"] -> 3 palindromic pieces,
             i.e. 2 cuts. No partition into fewer than 3 palindromes exists.
```

## Hint

Run a **Palindromic Tree (Eertree)** while streaming `s`. Using **series links**
(grouping suffix palindromes whose consecutive length differences are equal),
you can update a factorization DP in `O(log n)` amortized per character. The
minimum number of palindromic pieces minus one is the answer.
