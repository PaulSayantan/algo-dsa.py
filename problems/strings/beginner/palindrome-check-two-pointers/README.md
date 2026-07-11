# Palindrome Check (Two Pointers)

## What it is

A **palindrome** is a sequence that reads the same forwards and backwards
(e.g. `racecar`, `abba`, `12321`). The **two-pointer** technique checks the
palindrome property without allocating a reversed copy of the input:

- Place one pointer `left` at the start and another `right` at the end.
- Compare the two characters they point at.
- If they differ, it is **not** a palindrome. If they match, move `left`
  one step right and `right` one step left, and repeat.
- Stop when the pointers meet or cross. If you never found a mismatch,
  it **is** a palindrome.

There are two closely related flavors of the same idea:

1. **Inward scan** — pointers start at the two ends and move toward the
   center. This is the canonical "is this a palindrome?" check.
2. **Expand around center** — pointers start together at a center and move
   *outward*, growing the palindrome as long as the two ends match. This
   is the go-to trick for finding or counting palindromic substrings.

## When to reach for it

- You need to test whether a string, list, or number is a palindrome.
- You need the longest / count of palindromic substrings (expand outward).
- You want to verify symmetry cheaply, in place, with O(1) extra space.
- More generally, whenever a problem involves comparing elements from the
  two ends of a sequence and shrinking or growing a window symmetrically.

## Complexity

| Flavor | Time | Space |
|---|---|---|
| Inward palindrome check | O(n) | O(1) |
| Expand around center (one center) | O(n) | O(1) |
| Longest / count via all centers | O(n^2) | O(1) |

The inward check touches each character at most once. Expanding around a
single center is O(n) in the worst case; doing it for all `2n - 1` centers
gives O(n^2).

## Problems

| # | Problem | Technique flavor | Difficulty |
|---|---------|------------------|------------|
| 1 | [Valid Palindrome](problem-01-valid-palindrome/PROBLEM.md) | Inward scan, skip non-alphanumeric | Easy |
| 2 | [Valid Palindrome II](problem-02-valid-palindrome-ii/PROBLEM.md) | Inward scan with one allowed deletion | Easy/Medium |
| 3 | [Palindrome Linked List](problem-03-palindrome-linked-list/PROBLEM.md) | Find middle, reverse half, inward compare | Easy/Medium |
| 4 | [Longest Palindromic Substring](problem-04-longest-palindromic-substring/PROBLEM.md) | Expand around center (outward) | Medium |
| 5 | [Palindromic Substrings](problem-05-palindromic-substrings/PROBLEM.md) | Count via expand around center | Medium |
