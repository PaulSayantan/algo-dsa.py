# Range Count of Elements ≤ X

**Difficulty:** Medium

Source: Classic Merge Sort Tree exercise (equivalent to Codeforces / CSES "Range
count" style problems; a direct generalization of SPOJ KQUERY / KQUERYO).

## Description

You are given a static integer array `nums` of length `n`. The array never changes.
You must answer `q` independent queries. Each query is a triple `(l, r, x)` and asks:

> How many indices `i` with `l <= i <= r` satisfy `nums[i] <= x`?

Indices `l` and `r` are **0-based and inclusive**. Return the answer to every query,
in order, as a list.

Because the array is static and there can be many queries, you should preprocess the
array once so that each query is answered in polylogarithmic time. This is the
textbook use case for a Merge Sort Tree: build a segment tree whose nodes store the
sorted elements of their range, then answer each query by decomposing `[l, r]` into
`O(log n)` nodes and binary searching for `x` inside each node.

## Constraints

- `1 <= n <= 10^5`
- `1 <= q <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= x <= 10^9`
- `0 <= l <= r <= n - 1`

## Examples

### Example 1

```
Input:  nums = [2, 5, 1, 4, 3], queries = [[0, 4, 3], [1, 3, 4], [2, 2, 0]]
Output: [3, 2, 0]
```

Explanation:
- Query `(0, 4, 3)`: the whole array `[2, 5, 1, 4, 3]`; elements `<= 3` are `2, 1, 3` -> **3**.
- Query `(1, 3, 4)`: subarray `[5, 1, 4]`; elements `<= 4` are `1, 4` -> **2**.
- Query `(2, 2, 0)`: subarray `[1]`; elements `<= 0`: none -> **0**.

### Example 2

```
Input:  nums = [10, 10, 10], queries = [[0, 2, 10], [0, 2, 9], [1, 2, 10]]
Output: [3, 0, 2]
```

Explanation:
- Query `(0, 2, 10)`: all three `10`s are `<= 10` -> **3**.
- Query `(0, 2, 9)`: no element is `<= 9` -> **0**.
- Query `(1, 2, 10)`: subarray `[10, 10]`, both `<= 10` -> **2**.

## Hint

Build a **Merge Sort Tree**: a segment tree where each node holds the sorted list of
its range. To count elements `<= x` in a node, binary search (`upper_bound`) for `x` in
that node's sorted list. Sum these counts across the `O(log n)` nodes that cover `[l, r]`.
