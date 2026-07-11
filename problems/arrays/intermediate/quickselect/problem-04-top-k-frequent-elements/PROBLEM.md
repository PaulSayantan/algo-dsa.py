# Top K Frequent Elements

**Difficulty:** Medium

**Source:** LeetCode 347 — Top K Frequent Elements

## Description

Given an integer array `nums` and an integer `k`, return the `k` **most frequent
elements**. You may return the answer in **any order**.

It is guaranteed that the answer is **unique** — the k-th most frequent element has a
strictly greater count than the (k+1)-th, so there is no ambiguity about which elements
to include.

The interesting challenge: can you do better than `O(n log n)` (i.e. better than sorting
the distinct elements by frequency)?

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, number of distinct elements]`.

## Examples

### Example 1

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
```

**Explanation:** Frequencies are `{1: 3, 2: 2, 3: 1}`. The two most frequent elements are
`1` (count 3) and `2` (count 2). Order does not matter, so `[2, 1]` is also accepted.

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
```

**Explanation:** There is only one distinct element, `1`, so it is trivially the most
frequent.

### Example 3

```
Input:  nums = [4, 4, 4, 5, 5, 6, 7], k = 1
Output: [4]
```

**Explanation:** Frequencies are `{4: 3, 5: 2, 6: 1, 7: 1}`. The single most frequent
element is `4`.

## Hint

First build a frequency map, then reduce the problem to "find the top k of the **distinct
elements** ranked by count." That is a selection problem: apply **Quickselect** to the
list of unique elements, using each element's frequency as the comparison key, to isolate
the k highest-frequency elements in expected linear time.
