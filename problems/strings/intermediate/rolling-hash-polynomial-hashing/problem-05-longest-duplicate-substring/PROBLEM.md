# Longest Duplicate Substring

**Difficulty:** Hard

**Source:** LeetCode 1044 — "Longest Duplicate Substring". The canonical
**binary-search-on-length + rolling hash** problem.

## Description

Given a string `s`, a *duplicate substring* is a substring (of length `>= 1`)
that occurs in `s` **more than once**. The occurrences may overlap.

Return **any** duplicate substring of **maximum length**. If `s` has no duplicate
substring, return the empty string `""`.

Two observations combine into the intended solution:

1. **Monotonicity** — if a duplicate substring of length `L` exists, then a
   duplicate substring of length `L-1` exists too (take a prefix of it). So the
   set of achievable duplicate lengths is `{0, 1, ..., ans}`; binary search the
   largest feasible `L`.
2. **O(n) feasibility check via hashing** — for a fixed `L`, hash every length-`L`
   window with a rolling / prefix polynomial hash and look for two windows that
   share a hash. Using prefix hashes each window hash is `O(1)`, so one check is
   `O(n)`.

Together this yields `O(n log n)`.

## Constraints

- `2 <= len(s) <= 3 * 10^4`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "banana"
Output: "ana"
Explanation: "ana" occurs at index 1 and index 3 (overlapping) — length 3.
             "an"/"na" are shorter; no length-4 substring repeats.
             ("ana" is one valid answer; any longest duplicate is accepted.)
```

### Example 2

```
Input:  s = "abcd"
Output: ""
Explanation: Every substring of "abcd" is unique, so there is no duplicate
             substring and the answer is the empty string.
```

### Example 3

```
Input:  s = "aaaaa"
Output: "aaaa"
Explanation: "aaaa" occurs at index 0 and index 1 (overlapping) — length 4.
             The whole string "aaaaa" (length 5) occurs only once.
```

## Hint

Binary search the answer **length** `L` (feasibility is monotone). For each `L`,
fingerprint every length-`L` window with a **polynomial rolling hash** and detect
a collision via a set — a repeat of length `L` exists iff two windows share a
fingerprint. This is **Rolling Hash / Polynomial Hashing**.
