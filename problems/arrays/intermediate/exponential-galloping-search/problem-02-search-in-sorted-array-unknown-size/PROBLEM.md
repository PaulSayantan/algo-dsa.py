# Search in a Sorted Array of Unknown Size

**Difficulty:** Medium

**Source:** LeetCode 702 — Search in a Sorted Array of Unknown Size

## Description

You have an integer array `secret` that is sorted in **ascending order** and
contains **unique** values, but you are **not** given its length. Instead you
are given an `ArrayReader` interface with a single method:

- `reader.get(i)` returns the element at index `i` (0-indexed) if `0 <= i < n`,
  and returns `2^31 - 1` (i.e. `2147483647`) if `i` is out of bounds.

Given the `reader` and an integer `target`, return the index `k` such that
`reader.get(k) == target`, or `-1` if `target` is not in the array.

You may not query the length directly — the out-of-bounds sentinel is your only
signal that you have gone past the end. Because `n` is hidden, you cannot seed a
binary search with a right endpoint; you must **discover** a valid upper bound
first.

## Constraints

- `1 <= secret.length <= 10^4`
- `-10^4 <= secret[i], target <= 10^4`
- All values in `secret` are **unique**.
- The out-of-bounds return value is `2^31 - 1`, which is strictly greater than
  any real element (so it always compares as "too big").

## Examples

**Example 1**

```
Input:  secret = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: Probing 1, 2, 4 (get(4) == 9 >= target) bounds the answer in
[2, 4]. Binary search finds 9 at index 4.
```

**Example 2**

```
Input:  secret = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in the array, so return -1.
```

**Example 3**

```
Input:  secret = [5], target = 5
Output: 0
Explanation: get(0) == 5 == target. Probing index 1 returns the sentinel
2147483647 (out of bounds), which is >= target, so the window collapses to
[0, 1] and binary search lands on index 0.
```

## Hint

Use Exponential (Galloping) Search: double the probe index until `reader.get(bound)`
is `>= target` (the out-of-bounds sentinel `2^31 - 1` counts as "too big" and
ends the doubling), then binary-search the window `[bound // 2, bound]`.
