# Interpolation Search Basics

**Difficulty:** Easy

Source: Classic algorithm exercise (CLRS / GeeksforGeeks "Interpolation Search")

## Description

You are given a **sorted array of distinct integers** `arr` in strictly increasing order and a
target integer `x`. The values are drawn from a roughly **uniform distribution** (evenly spaced
numbers), which is exactly the setting where a smarter-than-binary probe pays off.

Return the **index** of `x` in `arr`, or `-1` if `x` is not present.

Your goal is not merely to find the element, but to find it while probing positions that are
*estimated from the value of `x` relative to the endpoints of the current window*, rather than
always splitting the window in half.

## Constraints

- `1 <= len(arr) <= 10^6`
- `arr` is sorted in strictly increasing order (all elements distinct).
- `-10^9 <= arr[i], x <= 10^9`

## Examples

### Example 1
```
Input:  arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], x = 70
Output: 6
Explanation: arr[6] == 70. Because the values are evenly spaced by 10, the interpolation
probe pos = 0 + ((70 - 10) * (9 - 0)) // (100 - 10) = 0 + (60 * 9)//90 = 6 lands directly
on the answer in a single probe.
```

### Example 2
```
Input:  arr = [1, 2, 4, 8, 16, 32, 64], x = 5
Output: -1
Explanation: 5 is not in the array. The window shrinks (arr[lo] <= 5 <= arr[hi] eventually
fails or the probe passes over the gap between 4 and 8), so the search terminates with -1.
```

### Example 3
```
Input:  arr = [7], x = 7
Output: 0
Explanation: Single-element array; arr[0] == 7 so the answer is index 0.
```

## Hint

Replace binary search's `mid = (lo + hi) // 2` with an **Interpolation Search** probe that
estimates where `x` should sit based on how far `x` is between `arr[lo]` and `arr[hi]`.
