# Split Array Largest Sum

**Difficulty:** Hard

**Source:** LeetCode 410 — Split Array Largest Sum

## Description

Given an integer array `nums` and an integer `k`, split `nums` into `k` **non-empty**, **contiguous** subarrays.

Let the *largest sum* among these `k` subarrays be the maximum of the sums of each subarray. Return the **minimized** largest sum — that is, arrange the split so that the biggest subarray sum is as small as possible, and return that value.

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= min(50, nums.length)`

## Examples

### Example 1

```
Input:  nums = [7, 2, 5, 10, 8], k = 2
Output: 18
Explanation: There are several ways to split into 2 subarrays. The best is
[7, 2, 5] and [10, 8], whose sums are 14 and 18. The largest sum is 18, and no
other split into 2 parts produces a smaller maximum (e.g. [7,2,5,10],[8] gives 24).
```

### Example 2

```
Input:  nums = [1, 2, 3, 4, 5], k = 2
Output: 9
Explanation: The best split is [1, 2, 3] and [4, 5], with sums 6 and 9. The
largest sum is 9. Splitting as [1,2,3,4],[5] gives 10, which is worse.
```

### Example 3

```
Input:  nums = [1, 4, 4], k = 3
Output: 4
Explanation: With k = 3 each element is its own subarray: [1], [4], [4]. The
largest of these sums is 4, and there is no other way to make 3 non-empty parts.
```

## Hint

The answer (the minimized largest sum) lies in `[max(nums), sum(nums)]`. "Can we split into at most `k` contiguous parts each with sum <= X?" is monotonic in `X`. Use **Binary Search on Answer** to find the smallest feasible `X`.
