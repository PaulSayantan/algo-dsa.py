# Minimum Window Substring

**Difficulty:** Hard

**Source:** LeetCode 76 — Minimum Window Substring

## Description

Given strings `s` and `t`, return the shortest substring of `s` that contains every character of `t` (including multiplicity). If no such window exists, return the empty string. The answer is unique when it exists; return that leftmost minimal window.

## Examples

### Example 1

```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Explanation:** The minimum window covering A, B and C is "BANC".

### Example 2

```
Input:  s = "a", t = "aa"
Output: ""
```

**Explanation:** There are not two "a" in s, so no valid window.

## Hint

need = Counter(t) and a 'missing' counter; expand right, contract left while missing == 0.
