# Find K Closest Elements

**Difficulty:** Medium

Source: LeetCode 658 — "Find K Closest Elements"

## Description

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers
to `x` in the array. The result must be **sorted in ascending order**.

An integer `a` is closer to `x` than an integer `b` if:
- `|a - x| < |b - x|`, or
- `|a - x| == |b - x|` **and** `a < b` (ties break toward the smaller value).

The efficient shape of this problem is: (1) locate the position of `x` (or where it would go), then
(2) expand a window of size `k` outward. Step (1) is a search over sorted numeric keys — a perfect
fit for **Interpolation Search** to find the anchor in ~O(log log n) probes.

## Constraints

- `1 <= k <= len(arr) <= 10^4`
- `-10^4 <= arr[i], x <= 10^4`
- `arr` is sorted in ascending order (duplicates allowed).

## Examples

### Example 1
```
Input:  arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]
Explanation: The four closest values to 3 are 1, 2, 3, 4. Both 2 and 4 are distance 1 from 3,
but on the far edge we drop 5 (distance 2) before dropping 1 (distance 2) because ties favor
the smaller value.
```

### Example 2
```
Input:  arr = [1, 2, 3, 4, 5], k = 4, x = -1
Output: [1, 2, 3, 4]
Explanation: x is below the whole array, so the k smallest elements are the closest.
```

### Example 3
```
Input:  arr = [2, 3, 7, 8], k = 1, x = 6
Output: [7]
Explanation: |7 - 6| = 1 while |3 - 6| = 3, so 7 is the single closest element.
```

## Hint

Use **Interpolation Search** to find the anchor — the first index whose value is `>= x`
(the lower bound / insertion point). Then run two pointers outward, always keeping the side whose
element is closer to `x` (ties favor the left/smaller side), until the window holds `k` elements.
