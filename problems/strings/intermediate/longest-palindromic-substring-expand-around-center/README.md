# Longest Palindromic Substring — Expand Around Center

## What it is

**Expand around center** is a technique for finding palindromes inside a string.
The key observation is that every palindrome has a *center* and reads the same
outward in both directions from that center. Instead of checking every possible
substring for the palindrome property (which is expensive), we fix a center and
grow a window outward as long as the two mirror characters match.

A string of length `n` has exactly `2n - 1` possible centers:

- `n` **odd-length** centers — one on each character (e.g. center on `b` in `aba`).
- `n - 1` **even-length** centers — one between each pair of adjacent characters
  (e.g. center between the two `b`s in `abba`).

For each center we run a two-pointer expansion:

```
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left  -= 1
        right += 1
    # s[left+1 : right] is the palindrome we found (exclusive right)
    return left + 1, right - 1   # inclusive [start, end]
```

Handling odd and even centers is just a matter of how you seed `left` and
`right`: `expand(i, i)` for odd, `expand(i, i + 1)` for even.

## When to reach for it

- You need the **longest** palindromic substring, or the **count** of palindromic
  substrings, or to know **which substrings are palindromes**.
- The input size is moderate (roughly `n ≤ a few thousand`), so an `O(n²)`
  scan is acceptable.
- You want something far simpler to write and reason about than Manacher's
  algorithm (which solves the same problems in `O(n)` but is fiddly).

If `n` is very large (10⁵+) and you need linear time, prefer **Manacher's
algorithm**. Expand-around-center is the go-to interview technique because it is
short, needs `O(1)` extra space, and is easy to get right.

## Complexity

| Metric | Cost |
|--------|------|
| Time   | `O(n²)` — `2n - 1` centers, each expanding up to `O(n)` |
| Space  | `O(1)` extra (ignoring the output) |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Longest Palindromic Substring](problem-01-longest-palindromic-substring/PROBLEM.md) | Return the longest palindromic substring of `s`. | Medium |
| 2 | [Palindromic Substrings](problem-02-palindromic-substrings-count/PROBLEM.md) | Count how many substrings of `s` are palindromes. | Medium |
| 3 | [Count Distinct Palindromic Substrings](problem-03-count-distinct-palindromic-substrings/PROBLEM.md) | Count the number of *distinct* palindromic substrings. | Medium |
| 4 | [Palindrome Partitioning IV](problem-04-palindrome-partitioning-iv/PROBLEM.md) | Decide if `s` splits into three non-empty palindromes. | Hard |
| 5 | [Maximum Non-overlapping Palindrome Substrings](problem-05-maximum-non-overlapping-palindrome-substrings/PROBLEM.md) | Max count of non-overlapping palindromes each of length ≥ `k`. | Hard |
