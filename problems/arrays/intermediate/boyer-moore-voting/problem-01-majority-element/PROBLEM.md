# Majority Element

**Difficulty:** Easy

**Source:** LeetCode 169 — Majority Element

## Description

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than ⌊n/2⌋ times**. You may assume
that the majority element **always exists** in the array.

Try to solve it in **linear time** and, as a follow-up, in **O(1) extra space**.

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The majority element is guaranteed to exist.

## Examples

### Example 1

```
Input:  nums = [3, 2, 3]
Output: 3
```

Explanation: `n = 3`, so a majority must appear more than ⌊3/2⌋ = 1 time. The value `3`
appears 2 times (> 1), so it is the majority element.

### Example 2

```
Input:  nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

Explanation: `n = 7`, so a majority must appear more than ⌊7/2⌋ = 3 times. The value `2`
appears 4 times (> 3); `1` appears only 3 times. The answer is `2`.

### Example 3

```
Input:  nums = [7]
Output: 7
```

Explanation: A single-element array; that element trivially appears more than ⌊1/2⌋ = 0
times.

## Hint

Because a strict majority element is guaranteed to exist, you can find it in one pass with
**Boyer–Moore Voting**: keep a single `candidate` and a `count`, adopting a new candidate
whenever the count hits zero.
