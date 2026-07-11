# Decompress Run-Length Encoded List

**Difficulty:** Easy

Source: LeetCode 1313 — "Decompress Run-Length Encoded List"

## Description

You are given an integer array `nums` that represents a run-length encoded
sequence. Read the array in adjacent pairs: for every pair
`(nums[2*i], nums[2*i + 1])`, the first element `freq = nums[2*i]` is a frequency
and the second element `val = nums[2*i + 1]` is a value. Each pair expands to
`freq` copies of `val`.

Concatenate the expansions of all pairs, in order, and return the resulting
decompressed list.

## Constraints

- `2 <= nums.length <= 100`
- `nums.length` is **even**.
- `1 <= nums[i] <= 100`

## Examples

### Example 1
```
Input:  nums = [1, 2, 3, 4]
Output: [2, 4, 4, 4]
Explanation: The pairs are (freq=1, val=2) and (freq=3, val=4).
             (1, 2) -> [2]
             (3, 4) -> [4, 4, 4]
             Concatenated: [2, 4, 4, 4].
```

### Example 2
```
Input:  nums = [1, 1, 2, 3]
Output: [1, 3, 3]
Explanation: (freq=1, val=1) -> [1]; (freq=2, val=3) -> [3, 3].
             Concatenated: [1, 3, 3].
```

### Example 3
```
Input:  nums = [4, 5]
Output: [5, 5, 5, 5]
Explanation: A single pair (freq=4, val=5) expands to four 5s.
```

## Hint

The input is already in **Run-Length Encoding** form as `(frequency, value)`
pairs; you only need to *decode* it by repeating each value the given number of
times. Step through the array two elements at a time.
