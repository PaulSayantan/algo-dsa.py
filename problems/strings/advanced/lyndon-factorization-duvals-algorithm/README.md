# Lyndon Factorization (Duval's Algorithm)

## What it is

A **Lyndon word** is a non-empty string that is *strictly* smaller (lexicographically)
than every one of its proper suffixes — equivalently, strictly smaller than all of its
non-trivial rotations. Examples: `a`, `ab`, `aab`, `abc`, `aabb`. Non-examples: `aa`
(equal to a rotation), `ba` (suffix `a` is smaller), `abab` (equals rotation, and
suffix `ab` is a prefix hence smaller).

The **Chen–Fox–Lyndon theorem** says every string `s` has a *unique* factorization

```
s = w1 w2 ... wk        with   w1 >= w2 >= ... >= wk
```

where each `wi` is a Lyndon word and the factors are **non-increasing**.

**Duval's algorithm (1983)** computes this factorization in **O(n) time** and
**O(1) extra space** (besides the output) using a clever three-pointer scan. It never
backtracks over the input more than a constant amortized amount.

## When to reach for it

- You need the Lyndon factorization itself.
- **Lexicographically smallest / largest rotation** of a string (run Duval on `s + s`).
- **Smallest cyclic shift** problems (SPOJ MINMOVE, "book of orders", necklace canonical form).
- **Maximal / minimal suffix** in O(n) with O(1) space — the last Lyndon factor is
  exactly the lexicographically smallest suffix of the string.
- Generating all Lyndon words up to length `n` (the FKM / Duval–Lentin–Perrin algorithm),
  used to build **de Bruijn sequences**.
- Any time you'd reach for a suffix array *just* to get the min/max rotation or suffix —
  Duval gives the same answer with far less overhead.

## Core idea (the three pointers)

Scan with a start pointer `i` (beginning of the current candidate factor), a
comparison pointer `j`, and a pointer `k` tracking the matched prefix:

- While `s[k] < s[j]`: the candidate is still Lyndon — reset `k = i`, advance `j`.
- While `s[k] == s[j]`: it may be a periodic Lyndon prefix — advance both `k` and `j`.
- When `s[k] > s[j]` (or `j` hits the end): the Lyndon word has period `j - k`; emit
  copies of that word of length `j - k` until `i` passes `k`, then restart.

The last (rightmost) Lyndon factor is always the smallest suffix of the whole string.

## Complexity

| Aspect | Cost |
|--------|------|
| Time | `O(n)` |
| Extra space | `O(1)` (excluding the output list) |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Check if a String is a Lyndon Word](problem-01-check-lyndon-word/PROBLEM.md) | Decide whether a string equals its own single Lyndon factor | Easy |
| 2 | [Lyndon Factorization of a String](problem-02-lyndon-factorization/PROBLEM.md) | Split a string into its unique non-increasing Lyndon factors | Medium |
| 3 | [Lexicographically Smallest Rotation](problem-03-least-cyclic-rotation/PROBLEM.md) | Find the minimal cyclic rotation of a string | Medium |
| 4 | [Last Substring in Lexicographical Order](problem-04-last-substring/PROBLEM.md) | Return the lexicographically largest suffix (LeetCode 1163) | Hard |
| 5 | [Orderly Queue](problem-05-orderly-queue/PROBLEM.md) | Smallest string after moving any of the first k letters to the end (LeetCode 899) | Hard |

Work through them top to bottom — each reuses the machinery of the previous one.
