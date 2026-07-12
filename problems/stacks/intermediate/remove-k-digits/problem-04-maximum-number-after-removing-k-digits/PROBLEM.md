# Maximum Number After Removing K Digits

**Difficulty:** Medium

**Source:** Classic — maximize the number after removing `k` digits (the mirror of LeetCode 402)

## Description

Given a non-negative integer as a string `num` and an integer `k`, remove exactly `k` digits from `num` so the remaining digits form the largest possible number. Return the result as a string, preserving the original relative order of the kept digits.

Constraints: `1 <= len(num)`, `0 <= k <= len(num)`, `num` contains only digits `0`-`9`.

## Examples

### Example 1

```
Input:  num = "1432219", k = 3
Output: "4329"
```

**Explanation:** Removing `1`, `2`, and one `1` leaves the largest 4-digit number `4329`.

### Example 2

```
Input:  num = "1234", k = 2
Output: "34"
```

**Explanation:** Drop the two smallest leading digits so the biggest ones survive.

## Hint

Use a monotonic *decreasing* stack: pop a smaller top whenever a larger digit arrives and `k` removals remain; if any budget is left over, trim from the end.
