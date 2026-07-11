# Top K Frequent Elements

**Difficulty:** Medium

**Source:** LeetCode 347 (Top K Frequent Elements)

## Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
You may return the answer in **any order**.

It is guaranteed that the answer is **unique** — the set of `k` most frequent elements is
well-defined (no ambiguous frequency ties at the cutoff).

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.

## Examples

### Example 1

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
```

Explanation: The value `1` appears 3 times, `2` appears twice, and `3` appears once. The
two most frequent are `1` and `2`, so the answer is `[1, 2]` (any order).

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
```

Explanation: There is a single distinct value `1` (frequency 1), and `k = 1`, so it is
the only and most frequent element.

### Example 3

```
Input:  nums = [4, 1, -1, 2, -1, 2, 3], k = 2
Output: [-1, 2]
```

Explanation: Frequencies are `-1 -> 2`, `2 -> 2`, and `4, 1, 3 -> 1` each. The two most
frequent are `-1` and `2`, so the answer is `[-1, 2]` (any order).

## Hint

Use a **Heap / Priority Queue**. First count frequencies with a hash map, then push the
`(count, value)` pairs and use a **size-`k` min-heap** (keyed on count) to keep the `k`
highest-frequency values — the least frequent of your current top `k` sits at the root
and gets evicted by anything more frequent.
