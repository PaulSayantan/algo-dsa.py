# Count Subsets with a Given XOR

**Difficulty:** Medium

**Source:** Classic linear-basis counting problem (variants on Codeforces, and closely
related to LeetCode 1442 / GfG "Count number of subsets having a particular XOR value").

## Description

You are given an array `nums` of `n` non-negative integers and a target value `k`. Count
the number of **subsets** (including the empty subset) whose XOR equals `k`. Two subsets
are different if they use a different set of *indices*, even if the element values are
equal (so duplicates are counted independently).

Because the answer can be astronomically large, return it **modulo `10^9 + 7`**.

## Constraints

- `1 <= n <= 10^5`
- `0 <= nums[i] < 2^20`
- `0 <= k < 2^20`

## Examples

### Example 1

```
Input: nums = [1, 2, 3], k = 0
Output: 2

Explanation:
Subsets whose XOR is 0: {} (empty) and {1,2,3} (1 XOR 2 XOR 3 = 0).
That is 2 subsets.
```

### Example 2

```
Input: nums = [1, 2, 3], k = 3
Output: 2

Explanation:
Subsets whose XOR is 3: {3} and {1,2} (1 XOR 2 = 3). That is 2 subsets.
```

### Example 3

```
Input: nums = [5, 5], k = 1
Output: 0

Explanation:
The reachable XOR values are {0 (from {} or {5,5}), 5 (from either single 5)}.
The value 1 is not reachable, so the count is 0.
```

## Hint

Build a **GF(2) linear basis** with **Gaussian Elimination** and let `r` be its rank (the
number of pivots). If `k` lies in the span of `nums`, then exactly `2^(n - r)` subsets XOR
to `k`; otherwise the answer is `0`. Every reachable target is hit by the *same* number of
subsets.
