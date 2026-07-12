# Replace the Substring for Balanced String

**Difficulty:** Medium

**Source:** LeetCode 1234 — Replace the Substring for Balanced String

## Description

A string `s` of length `n` (a multiple of 4) containing only `Q`, `W`, `E`, `R` is **balanced** when each letter occurs exactly `n/4` times. You may replace one contiguous substring with any string of the same length. Return the minimum length of the substring to replace so that `s` becomes balanced (0 if it is already balanced).

## Examples

### Example 1

```
Input:  s = "QWER"
Output: 0
```

**Explanation:** The string is already balanced.

### Example 2

```
Input:  s = "QQWE"
Output: 1
```

**Explanation:** Replace one "Q" with "R" to balance the string.

### Example 3

```
Input:  s = "QQQW"
Output: 2
```

**Explanation:** Replace the leading "QQ" with "ER".

## Hint

Find the shortest window such that the counts OUTSIDE it are each <= n/4; the inside can be freely rewritten.
