# Ceiling in a Sorted Array

**Difficulty:** Medium

Source: Classic interview problem (GeeksforGeeks "Ceiling in a sorted array")

## Description

The **ceiling** of `x` in a sorted array is the **smallest element that is greater than or equal
to `x`**. Given a **sorted array of distinct integers** `arr` (ascending) and a value `x`, return
the **index** of the ceiling of `x`. If `x` is larger than every element (no ceiling exists),
return `-1`.

Because the search is over sorted, numeric keys, you can use **Interpolation Search** to jump
close to the target quickly and then settle on the successor position.

## Constraints

- `1 <= len(arr) <= 10^5`
- `arr` is sorted in strictly increasing order (distinct values).
- `-10^9 <= arr[i], x <= 10^9`

## Examples

### Example 1
```
Input:  arr = [1, 2, 8, 10, 12, 19], x = 5
Output: 2
Explanation: The smallest element >= 5 is 8, located at index 2.
```

### Example 2
```
Input:  arr = [1, 2, 8, 10, 12, 19], x = 20
Output: -1
Explanation: 20 is greater than the maximum element 19, so no ceiling exists.
```

### Example 3
```
Input:  arr = [1, 2, 8, 10, 12, 19], x = 8
Output: 2
Explanation: 8 is present at index 2, and an exact match is its own ceiling.
```

## Hint

Run **Interpolation Search** for `x`; on an exact hit that index is the answer, otherwise the
window collapses to the boundary between the predecessor and successor — return the successor
index (`lo`), or `-1` if it runs past the end.
