# Maximum XOR With an Element From Array

**Difficulty:** Hard

**Source:** LeetCode 1707 (Maximum XOR With an Element From Array)

## Description

You are given an array `nums` consisting of non-negative integers. You are also
given a `queries` array, where `queries[i] = [x_i, m_i]`.

The answer to the `i`-th query is the **maximum bitwise XOR** value of `x_i` with
any element of `nums` that does **not exceed** `m_i`. In other words, the answer is
`max(nums[j] XOR x_i)` over all `j` such that `nums[j] <= m_i`. If **all** elements
in `nums` are larger than `m_i`, then the answer to this query is `-1`.

Return an integer array `answer` where `answer.length == queries.length` and
`answer[i]` is the answer to the `i`-th query. Answers must be in the original
query order.

## Constraints

- `1 <= nums.length, queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= nums[j], x_i, m_i <= 10^9`

## Examples

### Example 1

```
Input:  nums = [0, 1, 2, 3, 4]
        queries = [[3, 1], [1, 3], [5, 6]]
Output: [3, 3, 7]
```

Explanation:
- `[3, 1]`: usable elements are `{0, 1}` (values `<= 1`). Best XOR: `3 XOR 0 = 3`.
- `[1, 3]`: usable elements are `{0, 1, 2, 3}`. Best XOR: `1 XOR 2 = 3`.
- `[5, 6]`: usable elements are `{0, 1, 2, 3, 4}`. Best XOR: `5 XOR 2 = 7`.

### Example 2

```
Input:  nums = [5, 2, 4, 6, 6, 3]
        queries = [[12, 4], [8, 1], [6, 3]]
Output: [15, -1, 5]
```

Explanation:
- `[12, 4]`: usable elements `{2, 3, 4}`. Best XOR: `12 XOR 3 = 15`.
- `[8, 1]`: no element is `<= 1`, so the answer is `-1`.
- `[6, 3]`: usable elements `{2, 3}`. Best XOR: `6 XOR 3 = 5`.

## Hint

A binary trie can find the maximum XOR of `x` against a *set* of numbers in
`O(bits)`, but each query restricts the set to values `<= m_i`. Rather than
rebuild the trie per query, use **Offline Query Processing**: sort the queries by
`m_i` ascending and insert `nums` values into the trie in ascending order, so the
trie always holds exactly the values allowed for the current query.
