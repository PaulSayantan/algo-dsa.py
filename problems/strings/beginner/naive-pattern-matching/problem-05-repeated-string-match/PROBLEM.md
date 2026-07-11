# Repeated String Match

**Difficulty:** Medium

**Source:** LeetCode 686 — Repeated String Match

## Description

Given two strings `a` and `b`, return the **minimum** number of times you have to repeat
string `a` so that `b` becomes a **substring** of the repeated string. If it is
impossible for `b` to ever be a substring no matter how many times `a` is repeated,
return `-1`.

For example, if `a = "abcd"` and `b = "cdabcdab"`, then repeating `a` three times gives
`"abcdabcdabcd"`, and `b = "cdabcdab"` is a substring of it, so the answer is `3`.

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  a = "abcd", b = "cdabcdab"
Output: 3
```

**Explanation:** Repeating `a` twice gives `"abcdabcd"` (length 8) which does **not**
contain `b`. Repeating it three times gives `"abcdabcdabcd"`, which contains
`"cdabcdab"` starting at index 2. Three is the minimum, so the answer is `3`.

### Example 2

```
Input:  a = "a", b = "aa"
Output: 2
```

**Explanation:** Repeating `"a"` twice gives `"aa"`, which contains `b = "aa"`. One copy
(`"a"`) is too short, so the minimum is `2`.

### Example 3

```
Input:  a = "abc", b = "wxyz"
Output: -1
```

**Explanation:** No matter how many times `"abc"` is repeated, `"wxyz"` can never be a
substring (it contains characters not in `a`), so we return `-1`.

## Hint

The number of copies needed is either `k = ceil(len(b) / len(a))` or `k + 1` — enough
copies to cover `b`'s length, plus possibly one more to absorb a misaligned start. Build
`a` repeated `k` times, then `k + 1` times, and test with **Naive Pattern Matching**
whether `b` is a substring of each; return the first that works, else `-1`.
