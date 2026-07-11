# Peak Index in a Mountain Array

**Difficulty:** Easy

**Source:** LeetCode 852 — Peak Index in a Mountain Array

## Description

An array `arr` is a **mountain array** if it has at least 3 elements and there exists
some index `i` with `0 < i < len(arr) - 1` such that

```
arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[len(arr)-1]
```

That is, the values strictly increase up to a single peak and then strictly decrease.
Given such a mountain array, return the index `i` of the peak element.

Because the array **strictly increases then strictly decreases**, the function
`f(index) = arr[index]` is **unimodal** — it has exactly one maximum. You are asked
for the *location* (argmax) of that maximum, so this is an optimization query, not a
target search.

## Constraints

- `3 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^6`
- `arr` is guaranteed to be a mountain array.

## Examples

### Example 1

```
Input:  arr = [0, 1, 0]
Output: 1
```

Explanation: The values rise from `0` to `1`, then fall back to `0`. The peak value
`1` sits at index `1`.

### Example 2

```
Input:  arr = [0, 2, 4, 6, 5, 3, 1]
Output: 3
```

Explanation: The array increases `0 < 2 < 4 < 6`, peaks at `arr[3] = 6`, then
decreases `6 > 5 > 3 > 1`. The peak index is `3`.

### Example 3

```
Input:  arr = [3, 4, 5, 1]
Output: 2
```

Explanation: It rises `3 < 4 < 5` and then drops to `1`. The maximum `5` is at
index `2`.

## Hint

The array is unimodal (strictly up, then strictly down), so use **Ternary Search** on
the *index domain*: probe two interior indices `m1 < m2`, compare `arr[m1]` with
`arr[m2]`, and discard the third that cannot contain the peak.
