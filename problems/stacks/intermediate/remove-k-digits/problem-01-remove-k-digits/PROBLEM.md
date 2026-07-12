# Remove K Digits

**Difficulty:** Medium

**Source:** LeetCode 402 — Remove K Digits

## Description

Given a non-negative integer as a string `num` and an integer `k`, remove `k` digits so the remaining number is the smallest possible. Return it as a string without leading zeros (`"0"` if empty).

## Examples

### Example 1

```
Input:  num = "1432219", k = 3
Output: "1219"
```

## Hint

Increasing digit stack; pop a larger top when the incoming digit is smaller and k remains.
