# Majority Element

**Difficulty:** Easy

**Source:** LeetCode 169 (https://leetcode.com/problems/majority-element/)

## Description

Given an array `nums` of size `n`, return the **majority element** — the element
that appears **more than `⌊n / 2⌋` times**.

You may assume that the majority element always exists in the array.

Because one value occupies more than half of all positions, counting how often
each value appears immediately reveals the answer: it is the unique value whose
count exceeds `n / 2`.

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
Explanation: n = 3, so a majority element must appear more than 1 time. The
value 3 appears twice, which is more than 1.
```

### Example 2

```
Input:  nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
Explanation: n = 7, so a majority element must appear more than 3 times. The
value 2 appears four times.
```

### Example 3

```
Input:  nums = [1]
Output: 1
Explanation: With a single element, that element trivially appears more than
0 times.
```

## Hint

Use **Frequency Counting with a Hash Map**: tally occurrences of each value and
return the one whose count exceeds `n / 2`. (A follow-up asks for an `O(1)`-space
solution via the Boyer-Moore voting algorithm.)
