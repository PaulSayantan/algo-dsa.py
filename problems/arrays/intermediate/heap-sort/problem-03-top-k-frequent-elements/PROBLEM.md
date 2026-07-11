# Top K Frequent Elements

**Difficulty:** Medium

**Source:** LeetCode 347 — Top K Frequent Elements

## Description

Given an integer array `nums` and an integer `k`, return the `k` **most
frequent** elements. You may return the answer in **any order**.

Your algorithm's time complexity must be **better than `O(n log n)`**, where `n`
is the array's size.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`
- It is **guaranteed** that the answer is unique.

## Examples

### Example 1

```
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Explanation:** `1` appears 3 times and `2` appears 2 times — the two most
frequent. `3` appears once and is excluded.

### Example 2

```
Input:  nums = [1], k = 1
Output: [1]
```

**Explanation:** Only one distinct element, so it is trivially the most
frequent.

### Example 3

```
Input:  nums = [4,4,4,5,5,6], k = 2
Output: [4,5]
```

**Explanation:** Counts are `4 -> 3`, `5 -> 2`, `6 -> 1`. The two highest-count
values are `4` and `5`.

## Hint

Count frequencies with a hash map, then use a **heap keyed on frequency**.
Maintain a **min-heap of size `k`** over `(count, value)` pairs — push each pair
and evict the smallest count when the heap exceeds `k`. What remains are the `k`
most frequent. This runs in `O(m log k)` where `m` is the number of distinct
values, beating a full `O(n log n)` sort.
