# Russian Doll Envelopes

**Difficulty:** Hard

**Source:** LeetCode 354 (Russian Doll Envelopes)

## Description

You are given a 2D array `envelopes` where `envelopes[i] = [w_i, h_i]` gives the width and
height of the `i`-th envelope.

One envelope can fit inside another (like Russian nesting dolls) **only if both** its
width and height are **strictly greater** than the other envelope's width and height.

Return the **maximum number of envelopes** you can nest (i.e. the length of the longest
chain where each envelope strictly fits inside the next). Rotation is not allowed.

## Constraints

- `1 <= envelopes.length <= 10^5`
- `envelopes[i].length == 2`
- `1 <= w_i, h_i <= 10^5`

## Examples

**Example 1**

```
Input:  envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
Output: 3
Explanation: The maximum nesting chain is [2,3] => [5,4] => [6,7]. Note [6,4] cannot
extend [5,4] into [6,7] because its height 4 is not strictly greater than 4.
```

**Example 2**

```
Input:  envelopes = [[1, 1], [1, 1], [1, 1]]
Output: 1
Explanation: All envelopes are identical, and equal dimensions do not nest (strict
inequality required), so only a single envelope can be chosen.
```

**Example 3**

```
Input:  envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
Output: 4
Explanation: One longest chain is [1,1] => [2,3] => [4,5] => [6,7] (length 4). [4,6]
cannot follow [4,5] since the width 4 is not strictly greater than 4.
```

## Hint

Use **Sorting as Preprocessing**: sort by width ascending and, crucially, break width
ties by height **descending**. Then the answer is the Longest Increasing Subsequence of
the heights, which a binary-search sweep computes in O(n log n).
