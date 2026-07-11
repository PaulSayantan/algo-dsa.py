# Count Values ≤ K in a Range

**Difficulty:** Easy–Medium

Source: Classic offline/online range-query problem (a.k.a. "range less-than-or-
equal count"; appears as SPOJ/Codeforces-style problems and as the core
subroutine of many harder tasks).

## Description

You are given a **static** integer array `arr` of length `n`. Answer `q` queries
of the form:

> `rangeCountLeq(l, r, x)` — how many elements of the subarray `arr[l..r)`
> (0-based, left-inclusive, right-**exclusive**) are `<= x`?

From this single primitive you can also derive, in O(1) extra work:
- count of elements `< x`  → `rangeCountLeq(l, r, x - 1)`
- count of elements `== x` → `rangeCountLeq(l, r, x) - rangeCountLeq(l, r, x-1)`
- count in a value band `[a, b]` → `rangeCountLeq(l, r, b) - rangeCountLeq(l, r, a-1)`

Implement a class that preprocesses `arr` once and answers each query in
sublinear time.

## Constraints

- `1 <= n <= 10^5`
- `-10^9 <= arr[i], x <= 10^9`
- `1 <= q <= 10^5`
- `0 <= l < r <= n` for every query.

## Examples

Let `arr = [2, 5, 1, 4, 3]` (indices `0..4`).

### Example 1
```
Input:  rangeCountLeq(1, 4, 3)
Output: 1
Explanation: arr[1..4) = [5, 1, 4]. Elements <= 3 are just {1} -> count 1.
```

### Example 2
```
Input:  rangeCountLeq(0, 5, 4)
Output: 4
Explanation: The whole array is [2, 5, 1, 4, 3]. Elements <= 4 are
             {2, 1, 4, 3} -> count 4 (only 5 is excluded).
```

### Example 3
```
Input:  rangeCountLeq(0, 2, 10)
Output: 2
Explanation: arr[0..2) = [2, 5]. Both are <= 10 -> count 2.
```

## Hint

Build a **Wavelet Tree**. To count elements `<= x` in `arr[l..r)`, route the
window `[l, r)` down the tree: at a node with midpoint `mid`, all left-child
elements are `<= mid`, so if `x >= mid` you can add the entire left count for
free and recurse right; otherwise recurse into the mapped left window.
