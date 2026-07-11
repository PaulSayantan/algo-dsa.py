# Beautiful Arrangement

**Difficulty:** Medium

**Source:** LeetCode 526 (Beautiful Arrangement)

## Description

Suppose you have `n` integers labeled `1` through `n`. A permutation of those
`n` integers `perm` (**1-indexed**) is considered a **beautiful arrangement**
if for every index `i` (with `1 <= i <= n`) **at least one** of the following
holds:

- `perm[i]` is divisible by `i`, or
- `i` is divisible by `perm[i]`.

Given an integer `n`, return the number of beautiful arrangements you can
construct.

## Constraints

- `1 <= n <= 15`

## Examples

### Example 1

```
Input: n = 2
Output: 2
```

Explanation: The two beautiful arrangements are:
- `[1, 2]` — position 1: `1 % 1 == 0`; position 2: `2 % 2 == 0`.
- `[2, 1]` — position 1: `2 % 1 == 0`; position 2: `2 % 1 == 0` (i.e. `i = 2`
  is divisible by `perm[2] = 1`).

### Example 2

```
Input: n = 3
Output: 3
```

Explanation: The beautiful arrangements are `[1, 2, 3]`, `[2, 1, 3]`, and
`[3, 2, 1]`. For instance `[3, 2, 1]` works because `3 % 1 == 0`,
`2 % 2 == 0`, and `3 % 1 == 0` (position 3 holds value 1). Arrangements such as
`[1, 3, 2]` fail because at position 2 neither `3 % 2` nor `2 % 3` is `0`.

### Example 3

```
Input: n = 1
Output: 1
```

Explanation: The only arrangement `[1]` satisfies `1 % 1 == 0`.

## Hint

Fill the positions one at a time and track which numbers you have already
placed as a subset encoded in an integer. This is **Bitmask DP** — the number
of set bits tells you which position you are filling next.
