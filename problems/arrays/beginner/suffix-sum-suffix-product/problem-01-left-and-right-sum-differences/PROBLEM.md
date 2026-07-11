# Left and Right Sum Differences

**Difficulty:** Easy

**Source:** LeetCode 2574 — Left and Right Sum Differences

## Description

Given a 0-indexed integer array `nums`, find a 0-indexed integer array `answer`
where:

- `answer.length == nums.length`
- `answer[i] = |leftSum[i] - rightSum[i]|`

where:

- `leftSum[i]` is the sum of elements **to the left** of index `i` in the array
  `nums`. If there is no such element, `leftSum[i] = 0`.
- `rightSum[i]` is the sum of elements **to the right** of index `i` in the array
  `nums`. If there is no such element, `rightSum[i] = 0`.

Return the array `answer`.

Note that the element at index `i` itself is **not** included in either
`leftSum[i]` or `rightSum[i]`.

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`

## Examples

### Example 1

```
Input:  nums = [10, 4, 8, 3]
Output: [15, 1, 11, 22]

Explanation:
The array leftSum  is [0, 10, 14, 22].
The array rightSum is [15, 11, 3, 0].
answer[i] = |leftSum[i] - rightSum[i]|:
  i=0: |0  - 15| = 15
  i=1: |10 - 11| = 1
  i=2: |14 - 3|  = 11
  i=3: |22 - 0|  = 22
So answer = [15, 1, 11, 22].
```

### Example 2

```
Input:  nums = [1]
Output: [0]

Explanation:
The array leftSum  is [0].
The array rightSum is [0].
answer[0] = |0 - 0| = 0, so answer = [0].
```

### Example 3

```
Input:  nums = [1, 2, 3]
Output: [5, 2, 3]

Explanation:
leftSum  = [0, 1, 3], rightSum = [5, 3, 0].
  i=0: |0 - 5| = 5
  i=1: |1 - 3| = 2
  i=2: |3 - 0| = 3
So answer = [5, 2, 3].
```

## Hint

Use a **Suffix Sum** for the right side and a running **prefix sum** for the left
side. `rightSum[i]` is the suffix sum starting at index `i + 1`; scan once to
build it (or maintain it while sweeping left to right).
