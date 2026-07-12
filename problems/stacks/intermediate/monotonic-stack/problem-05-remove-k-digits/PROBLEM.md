# Remove K Digits

**Difficulty:** Medium

**Source:** LeetCode 402 — Remove K Digits

## Description

Given a non-negative integer represented as a string `num` and an integer `k`, remove exactly `k` digits so that the resulting number is the **smallest** possible. Return that number as a string, without leading zeros. If everything is removed, return `"0"`.

Constraints: `1 <= len(num) <= 10^5`; `0 <= k <= len(num)`; `num` has no leading zeros except when it is `"0"` itself.

## Examples

### Example 1

```
Input:  num = "1432219", k = 3
Output: "1219"
```

**Explanation:** Dropping the digits `4`, `3`, and one `2` leaves `1219`, the smallest attainable number.

## Hint

Keep a monotonic increasing stack of digits; whenever the top is larger than the incoming digit and you still have removals left, pop it — a bigger digit in a higher place value always hurts.
