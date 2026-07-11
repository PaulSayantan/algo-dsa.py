# First Missing Positive

**Difficulty:** Hard

**Source:** LeetCode 41 — First Missing Positive

## Description

Given an unsorted integer array `nums`, return the smallest **positive** integer
that is **not** present in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)`
auxiliary space. Unlike the earlier problems in this section, the values here
are arbitrary integers (they may be negative, zero, or larger than `n`), so you
cannot assume they are already valid indices. The key realization is that the
answer must lie in the range `[1, n + 1]`, which lets you use the array of size
`n` as an in-place hash table: try to place each value `v` into slot `v - 1`,
then scan for the first slot that does not hold the value it should.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples

### Example 1

```
Input:  nums = [1,2,0]
Output: 3
```

**Explanation:** `1` and `2` are present, so the smallest missing positive
is `3`.

### Example 2

```
Input:  nums = [3,4,-1,1]
Output: 2
```

**Explanation:** `1` is present, but `2` is not, so the answer is `2`. The
values `-1` and `4` are irrelevant to the smallest gap.

### Example 3

```
Input:  nums = [7,8,9,11,12]
Output: 1
```

**Explanation:** No value in `1..n` is present at all, so the smallest missing
positive is `1`.

## Hint

Use the **Set Matrix Zeroes** family of in-place marking, specifically **index
placement (cyclic sort)**. The answer is always in `[1, n + 1]`, so treat the
array as a hash where value `v` belongs at index `v - 1`; swap values into their
correct slots, then the first index `i` whose `nums[i] != i + 1` reveals the
answer `i + 1`.
