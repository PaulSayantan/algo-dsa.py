# Russian Doll Envelopes

**Difficulty:** Hard

**Source:** LeetCode 354 — Russian Doll Envelopes

## Description

You are given a 2D array `envelopes` where
`envelopes[i] = [w_i, h_i]` represents the width and the height of the `i`-th
envelope.

One envelope can fit into another **if and only if** both its width and height
are strictly greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian-doll (i.e., nest one
inside another, forming a chain where each envelope strictly contains the
previous one). Rotation is not allowed.

## Constraints

- `1 <= envelopes.length <= 10^5`
- `envelopes[i].length == 2`
- `1 <= w_i, h_i <= 10^5`

## Examples

### Example 1

```
Input:  envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
Output: 3
Explanation: The longest chain is [2, 3] => [5, 4] => [6, 7], so 3 envelopes
             can be nested. Note [6, 4] cannot follow [5, 4] because the
             heights would need to strictly increase too, but 4 is not > 4
             — and it cannot precede [6, 7] either since widths tie at 6.
```

### Example 2

```
Input:  envelopes = [[1, 1], [1, 1], [1, 1]]
Output: 1
Explanation: All envelopes are identical, so none can contain another
             (strict inequality fails on both dimensions). At most one.
```

### Example 3

```
Input:  envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
Output: 4
Explanation: A valid chain is [1, 1] => [2, 3] => [4, 5] => [6, 7], length 4.
             [4, 6] cannot be inserted between [4, 5] and [6, 7] as a fifth
             because its width 4 ties with [4, 5].
```

## Hint

Sort cleverly, then it collapses to Longest Increasing Subsequence (patience /
binary search) on a single dimension. The sort must handle the tie-breaking so
that equal widths can never both appear in the chain.
