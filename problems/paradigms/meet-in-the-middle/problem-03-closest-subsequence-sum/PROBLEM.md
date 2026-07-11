# Closest Subsequence Sum

**Difficulty:** Hard

**Source:** LeetCode 1755 — Closest Subsequence Sum

## Description

You are given an integer array `nums` and an integer `goal`.

You want to choose a **subsequence** of `nums` (any subset of the elements,
including the empty subsequence) and compute its sum. Let `sum` be the sum of
the chosen subsequence.

Return the **minimum possible value of `abs(sum - goal)`** over all
subsequences.

Note: a subsequence here is any subset of the array elements — order does not
matter and elements need not be contiguous.

## Constraints

- `1 <= nums.length <= 40`
- `-10^7 <= nums[i] <= 10^7`
- `-10^9 <= goal <= 10^9`

## Examples

### Example 1

```
Input:  nums = [5, -7, 3, 5], goal = 6
Output: 0
```

**Explanation:** Choose the whole array as a subsequence: `5 + (-7) + 3 + 5 = 6`,
which equals `goal`, so `abs(6 - 6) = 0`.

### Example 2

```
Input:  nums = [7, -9, 15, -2], goal = -5
Output: 1
```

**Explanation:** The subsequence `{7, -9, -2}` sums to `-4`, giving
`abs(-4 - (-5)) = 1`. No subsequence sums to exactly `-5` (the achievable sums
nearest to `-5` are `-4` at distance 1 and `-9` at distance 4), so the minimum
distance is `1`.

### Example 3

```
Input:  nums = [1, 2, 3], goal = -7
Output: 7
```

**Explanation:** The smallest achievable sum is the empty subsequence `0`
(every element is positive, so no subset drops below 0). `abs(0 - (-7)) = 7`
is the closest we can get.

## Hint

`2^40` subsequence sums cannot be listed, but `2^20` per half can. Split the
array in two, enumerate each half's subset sums, then **meet in the middle**:
for each left-half sum, the best partner from the right half is the one closest
to `goal - leftSum` — find it with sorting plus binary search.
