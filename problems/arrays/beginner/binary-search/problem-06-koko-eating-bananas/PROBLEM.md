# Koko Eating Bananas

**Difficulty:** Medium

**Source:** LeetCode 875 — Koko Eating Bananas

## Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has
`piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed `k`. Each hour, she chooses
some pile and eats `k` bananas from it. If the pile has fewer than `k` bananas,
she eats all of them instead and will **not** eat any more bananas during that
hour (she cannot move to another pile in the same hour).

Koko likes to eat slowly but still wants to finish all the bananas before the
guards return. Return the **minimum integer speed `k`** such that she can eat all
the bananas within `h` hours.

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Examples

### Example 1

```
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
Explanation: At speed 4 the hours are ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4)
= 1 + 2 + 2 + 3 = 8 hours, which fits. At speed 3 it would take
1 + 2 + 3 + 4 = 10 > 8 hours, so 4 is the minimum.
```

### Example 2

```
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
Explanation: There are 5 piles and exactly 5 hours, so each pile must be
finished in a single hour. The speed must be at least the largest pile, 30.
```

### Example 3

```
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
Explanation: With 6 hours she has one extra hour, so the largest pile (30) can
be split across two hours. Speed 23 needs
ceil(30/23)+ceil(11/23)+ceil(23/23)+ceil(4/23)+ceil(20/23)
= 2 + 1 + 1 + 1 + 1 = 6 hours; speed 22 needs 7 hours, so 23 is the minimum.
```

## Hint

**Binary Search on the answer.** The eating speed itself is the search space:
`hours_needed(k)` decreases monotonically as `k` grows. Binary search over
`k` in `[1, max(piles)]` for the smallest speed whose required hours is `<= h`.
