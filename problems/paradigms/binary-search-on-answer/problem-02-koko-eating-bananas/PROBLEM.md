# Koko Eating Bananas

**Difficulty:** Medium

**Source:** LeetCode 875 (Koko Eating Bananas)

## Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has
`piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses
some pile of bananas and eats `k` bananas from that pile. If the pile has fewer
than `k` bananas, she eats all of them instead and **will not eat any more
bananas during that hour**.

Koko likes to eat slowly but still wants to finish eating all the bananas
**before the guards return**. Return the **minimum integer** `k` such that she can
eat all the bananas within `h` hours.

The number of hours needed to finish a single pile of size `p` at speed `k` is
`ceil(p / k)`.

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Examples

### Example 1

```
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
```

Explanation: At speed `4` the hours are `ceil(3/4) + ceil(6/4) + ceil(7/4) +
ceil(11/4) = 1 + 2 + 2 + 3 = 8 <= 8`. At speed `3` they would be `1 + 2 + 3 + 4 =
10 > 8`, so `4` is the smallest speed that works.

### Example 2

```
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
```

Explanation: There are `5` piles and `h = 5`, so Koko must clear one pile per
hour. The largest pile is `30`, so the speed must be at least `30`. At `30` the
hours are `1 + 1 + 1 + 1 + 1 = 5 <= 5`.

### Example 3

```
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
```

Explanation: At speed `23` the hours are `ceil(30/23) + ceil(11/23) +
ceil(23/23) + ceil(4/23) + ceil(20/23) = 2 + 1 + 1 + 1 + 1 = 6 <= 6`. At speed
`22` the total becomes `2 + 1 + 2 + 1 + 1 = 7 > 6`, so `23` is minimal.

## Hint

The higher Koko's speed, the fewer hours she needs — the total-hours function is
**monotonically non-increasing** in the speed `k`. So "can she finish within `h`
hours at speed `k`?" is a monotonic predicate. Use **Binary Search on Answer**
over the speed range `[1, max(piles)]`.
