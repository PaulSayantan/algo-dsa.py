# Top K Frequent Elements

**Difficulty:** Medium

**Source:** LeetCode 347 — Top K Frequent Elements

## Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
You may return the answer in **any order**.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is unique (the top `k` frequencies are unambiguous).

## Examples

### Example 1

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
```

**Explanation:** Frequencies are `{1: 3, 2: 2, 3: 1}`. The two most frequent elements are
1 (appears 3 times) and 2 (appears 2 times).

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
```

**Explanation:** Only one element exists, so it is trivially the single most frequent.

### Example 3

```
Input:  nums = [4, 4, 4, 5, 5, 6], k = 2
Output: [4, 5]
```

**Explanation:** Frequencies are `{4: 3, 5: 2, 6: 1}`. The two most frequent are 4 and 5.

## Hint

First count occurrences with a hash map, then select the `k` entries with the largest
counts. Use **Top-K via Heap** — a size-`k` min-heap keyed on frequency — or bucket sort by
count for an `O(n)` solution.
