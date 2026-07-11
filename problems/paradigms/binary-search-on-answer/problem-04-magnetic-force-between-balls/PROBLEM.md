# Magnetic Force Between Two Balls

**Difficulty:** Medium

**Source:** LeetCode 1552 (Magnetic Force Between Two Balls) — the classic
"Aggressive Cows" problem.

## Description

In the universe Earth C-137, Rick discovered a special form of magnetic force
between two balls if they are put in his new invented basket. Rick has `n` empty
baskets, the `i`-th basket is at `position[i]`, and Morty has `m` balls and needs
to distribute the balls into the baskets such that the **minimum magnetic force**
between any two balls is **maximum**.

Rick stated that the magnetic force between two different balls at positions `x`
and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`, return the **required
force** — that is, the largest possible value of the minimum pairwise distance
when the `m` balls are placed into `m` distinct baskets.

## Constraints

- `n == position.length`
- `2 <= n <= 10^5`
- `1 <= position[i] <= 10^9`
- All integers in `position` are **distinct**.
- `2 <= m <= position.length`

## Examples

### Example 1

```
Input:  position = [1, 2, 3, 4, 7], m = 3
Output: 3
```

Explanation: Placing the `3` balls at positions `1`, `4`, and `7` gives pairwise
distances `3`, `3`, and `6`; the minimum is `3`. No placement achieves a minimum
gap of `4` (there is no way to pick 3 baskets each at least 4 apart), so `3` is
optimal.

### Example 2

```
Input:  position = [5, 4, 3, 2, 1, 1000000000], m = 2
Output: 999999999
```

Explanation: With only `2` balls we simply want the two farthest baskets: place
them at `1` and `1000000000`, for a minimum (and only) distance of `999999999`.

## Hint

If a minimum gap `d` is achievable, then any smaller gap is also achievable — so
"can we place all `m` balls at least `d` apart?" is a **monotonic** predicate.
**Binary Search on Answer** over the gap `d`, and greedily check each candidate by
placing balls left to right on the sorted positions. This is a *maximize-the-min*
search.
