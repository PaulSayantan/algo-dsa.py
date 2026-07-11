# Majority Element II

**Difficulty:** Medium

**Source:** LeetCode 229 — Majority Element II

## Description

Given an integer array `nums` of size `n`, return **all** elements that appear **more than
⌊n/3⌋ times**.

There can be **at most two** such elements (if three distinct values each appeared more than
n/3 times, their total count would exceed n). The order of the returned values does not
matter, and a majority element here is **not** guaranteed to exist.

Design an algorithm that runs in **linear time** and uses **O(1) extra space**.

## Constraints

- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [3, 2, 3]
Output: [3]
```

Explanation: `n = 3`, so a value must appear more than ⌊3/3⌋ = 1 time to qualify. Only `3`
(count 2) exceeds 1; `2` appears once and does not qualify.

### Example 2

```
Input:  nums = [1]
Output: [1]
```

Explanation: `n = 1`, threshold is ⌊1/3⌋ = 0. The value `1` appears once (> 0), so it
qualifies.

### Example 3

```
Input:  nums = [1, 2, 2, 3, 2, 1, 1]
Output: [1, 2]
```

Explanation: `n = 7`, threshold is ⌊7/3⌋ = 2, so a value must appear at least 3 times. `1`
appears 3 times and `2` appears 3 times (both > 2); `3` appears once. The answer is `[1, 2]`
(any order).

## Hint

Extend **Boyer–Moore Voting** to track **two** candidates with two independent counts. Any
value exceeding ⌊n/3⌋ must survive as one of the two candidates — then verify each candidate
with a second counting pass.
