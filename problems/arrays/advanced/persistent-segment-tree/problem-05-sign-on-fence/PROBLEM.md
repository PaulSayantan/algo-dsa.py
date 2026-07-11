# Sign on Fence

**Difficulty:** Very Hard

Source: Codeforces Round 276 Div. 1 Problem E — **484E "Sign on Fence"**.

## Description

A fence is made of `n` vertical planks standing side by side. Plank `i`
(0-indexed) has integer height `heights[i]` and unit width. You want to hang
rectangular signs on the fence. A sign of width `w` can be hung on a range if
there exist `w` **consecutive** planks, all lying inside the queried range, and
the sign hangs at the height of the shortest of those `w` planks.

You are given `q` queries. Each query is a triple `(l, r, w)` and asks:

> Considering only planks with indices in `[l, r]` (inclusive), place a sign of
> width `w` on some block of `w` consecutive planks that lie entirely within
> `[l, r]`. The sign's height equals the **minimum** plank height in that block.
> What is the **maximum** height at which such a sign can be hung?

Formally, return
`max over i in [l, r-w+1] of ( min(heights[i .. i+w-1]) )`.
It is guaranteed that `w ≤ r − l + 1`, so at least one placement exists.

## Constraints

- `1 ≤ n ≤ 10^5`
- `1 ≤ heights[i] ≤ 10^9`
- `1 ≤ q ≤ 10^5`
- `0 ≤ l ≤ r < n`
- `1 ≤ w ≤ r − l + 1`

## Examples

### Example 1

```
Input:
  heights = [2, 6, 4, 3, 5, 7, 1, 8]
  queries = [
    (1, 4, 2),     # planks 1..4 = [6,4,3,5], width-2 block
    (0, 7, 3),     # whole fence, width-3 block
  ]

Output: [4, 3]
```

Explanation:
- For `(1, 4, 2)` the width-2 blocks inside `[1,4]` are `[6,4]→4`, `[4,3]→3`,
  `[3,5]→3`. The best (max of these mins) is `4`.
- For `(0, 7, 3)` the width-3 block mins are `2, 3, 3, 3, 1, 1`; the maximum is
  `3` (e.g. block `[6,4,3]` or `[3,5,7]`).

### Example 2

```
Input:
  heights = [5, 3, 8, 6]
  queries = [
    (0, 3, 1),     # width 1 -> just the tallest plank in range
    (0, 3, 4),     # width 4 -> the whole fence, so the shortest plank
    (2, 3, 2),     # planks [8,6], width 2
  ]

Output: [8, 3, 6]
```

Explanation:
- Width `1` means each single plank is its own "block"; the best height is the
  maximum plank, `8`.
- Width `4` forces the only block `[5,3,8,6]`, whose min is `3`.
- Planks `[8,6]` with width `2` give a single block with min `6`.

## Hint

Sort planks by height, tallest first, and insert their positions one by one into
a **Persistent Segment Tree** over positions that tracks the longest run of
consecutive inserted planks. Version `k` contains the `k` tallest planks.
**Binary search on the version:** find the fewest tallest planks (equivalently
the highest threshold height) for which the longest consecutive run *inside
`[l, r]`* reaches width `w`. That threshold height is the answer.
