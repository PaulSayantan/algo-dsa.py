# Find Beautiful Indices in the Given Array I

**Difficulty:** Medium

**Source:** LeetCode 3006 — "Find Beautiful Indices in the Given Array I"

## Description

You are given a 0-indexed string `s`, a string `a`, a string `b`, and an integer
`k`.

An index `i` (where `0 <= i < s.length`) is **beautiful** if:

- `s[i .. i + a.length - 1] == a` (an occurrence of `a` starts at `i`), and
- there exists an index `j` such that:
  - `s[j .. j + b.length - 1] == b` (an occurrence of `b` starts at `j`), and
  - `abs(j - i) <= k`.

Return the array of beautiful indices in **sorted order** (increasing).

The natural approach is: find **all** start positions of `a` in `s`, find **all**
start positions of `b` in `s`, then for each occurrence of `a`, check whether
some occurrence of `b` lies within distance `k`. The two "find all occurrences"
steps are exactly single-pattern searches.

## Constraints

- `1 <= k <= s.length <= 10^5`
- `1 <= a.length, b.length <= 10`
- `s`, `a`, and `b` contain only lowercase English letters.

## Examples

### Example 1
```
Input:  s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15
Output: [16, 33]
Explanation: Occurrences of a = "my" start at 16 and 33.
             Occurrences of b = "squirrel" start at 4 and 18.
             - i = 16: j = 18 gives |16 - 18| = 2 <= 15, so 16 is beautiful.
             - i = 33: j = 18 gives |33 - 18| = 15 <= 15, so 33 is beautiful.
             Both qualify, so the answer is [16, 33].
```

### Example 2
```
Input:  s = "abcd", a = "a", b = "a", k = 4
Output: [0]
Explanation: "a" occurs only at index 0. With i = 0 and j = 0,
             |0 - 0| = 0 <= 4, so 0 is beautiful. It is the only match.
```

## Hint

Collect all start indices of `a` and of `b` separately, then pair them up under
the distance constraint (a sorted list of `b`'s indices plus binary search makes
the pairing fast). Do both "find all occurrences" scans with **Boyer–Moore
(string search)**.
