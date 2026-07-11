# Count of Smaller Numbers After Self

**Difficulty:** Hard

**Source:** LeetCode 315 — Count of Smaller Numbers After Self

## Description

You are given an integer array `nums`. Return an integer array `counts` where `counts[i]`
is the number of elements to the **right** of `nums[i]` that are strictly smaller than
`nums[i]`.

A natural strategy is to scan from right to left, maintaining a frequency structure keyed
by value, and for each element query "how many values seen so far are strictly less than
this one?" A Fenwick tree (Binary Indexed Tree) answers that prefix-count query in
`O(log n)` — but only if it is indexed by a *small* range. Since values can be as large as
`10^8` in magnitude, we compress the values first.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

(The technique is unchanged, and remains necessary, for the harder value range
`-10^8 <= nums[i] <= 10^8` that many variants of this problem use.)

## Examples

### Example 1

```
Input:  nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

**Explanation:**
- To the right of 5 there are {2, 1} smaller -> 2.
- To the right of 2 there is {1} smaller -> 1.
- To the right of 6 there is {1} smaller -> 1.
- To the right of 1 there is nothing -> 0.

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
```

**Explanation:** For each `-1` the only element to the right is another `-1`, which is not
*strictly* smaller, so both counts are 0.

### Example 3

```
Input:  nums = [2, 0, 1]
Output: [2, 0, 0]
```

**Explanation:** To the right of 2 are {0, 1}, both smaller -> 2. To the right of 0 is {1},
not smaller -> 0. Nothing is to the right of the final 1 -> 0.

## Hint

Use **Coordinate Compression** to map the values into `[0, k-1]`, then sweep right-to-left
using a Fenwick tree (BIT) to count how many already-seen values are strictly smaller.
