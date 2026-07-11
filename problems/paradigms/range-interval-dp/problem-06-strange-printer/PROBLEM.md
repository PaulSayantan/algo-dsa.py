# Strange Printer

**Difficulty:** Hard

**Source:** LeetCode 664 — Strange Printer

## Description

There is a strange printer with the following two special properties:

1. The printer can only print a sequence of **the same character** each time.
2. At each turn, the printer can print new characters starting from and ending at
   any place, and will **cover** the original existing characters.

Given a string `s`, return the **minimum number of turns** the printer needs to
print it.

## Constraints

- `1 <= s.length <= 100`
- `s` consists of lowercase English letters only.

## Examples

### Example 1
```
Input:  s = "aaabbb"
Output: 2
Explanation: Print "aaaaaa" (or "aaa") first, then print "bbb" over the last
three positions. Two turns total.
```

### Example 2
```
Input:  s = "aba"
Output: 2
Explanation: Print "aaa" first, then print "b" over the middle position.
Two turns total.
```

### Example 3
```
Input:  s = "abcba"
Output: 3
Explanation: Print "aaaaa", then "bbb" over positions 1..3, then "c" over
position 2 -> "abcba". Three turns; no fewer is possible.
```

## Hint

Think **Range / Interval DP**: let `dp[i][j]` be the minimum turns to print
`s[i..j]`, and exploit the case where a later character equals `s[i]`, letting
one print cover both in the same turn.
