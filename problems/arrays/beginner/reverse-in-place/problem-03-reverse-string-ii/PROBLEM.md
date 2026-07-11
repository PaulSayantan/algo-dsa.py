# Reverse String II

**Difficulty:** Easy

**Source:** LeetCode 541 — Reverse String II

## Description

Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k`
characters counting from the start of the string.

Apply the following rule while scanning the string in blocks of `2k`:

- If there are fewer than `k` characters left, reverse all of the remaining characters.
- If there are at least `k` but fewer than `2k` characters left, reverse the first `k`
  characters and leave the rest as they are.

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters only.
- `1 <= k <= 10^4`

## Examples

### Example 1

```
Input:  s = "abcdefg", k = 2
Output: "bacdfeg"
```

Explanation: Walk the string in windows of `2k = 4`.
- Indices 0-3 (`"abcd"`): reverse the first `k = 2` -> `"ba"`, keep `"cd"` -> `"bacd"`.
- Indices 4-6 (`"efg"`): only 3 characters remain. Reverse the first `k = 2` -> `"fe"`,
  keep `"g"` -> `"feg"`.

Concatenating gives `"bacd" + "feg" = "bacdfeg"`.

### Example 2

```
Input:  s = "abcd", k = 2
Output: "bacd"
```

Explanation: One window of `2k = 4` covers the whole string. Reverse the first `k = 2`
characters (`"ab"` -> `"ba"`) and leave the remaining two (`"cd"`) untouched, giving
`"bacd"`.

## Hint

Use **Reverse In-Place**: step through the string in jumps of `2k`, and at each block
start reverse the `[i, i + k - 1]` sub-range with the two-pointer swap (clamping the
right pointer to the end of the string).
