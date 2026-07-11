# Capacity To Ship Packages Within D Days

**Difficulty:** Medium

**Source:** LeetCode 1011 (Capacity To Ship Packages Within D Days)

## Description

A conveyor belt has packages that must be shipped from one port to another within
`days` days.

The `i`-th package on the belt has a weight of `weights[i]`. Each day, we load the
ship with packages on the belt **in the given order**. We may not load more weight
than the maximum weight capacity of the ship.

Return the **least weight capacity** of the ship that will result in all the
packages being shipped within `days` days.

Note that the relative order of the packages must be preserved: on each day you
take a **contiguous prefix** of the remaining packages, as many as fit under the
capacity.

## Constraints

- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

## Examples

### Example 1

```
Input:  weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
Output: 15
```

Explanation: A ship capacity of `15` ships everything in `5` days as follows:
day 1: `1, 2, 3, 4, 5` (sum 15); day 2: `6, 7` (sum 13); day 3: `8` (sum 8);
day 4: `9` (sum 9); day 5: `10` (sum 10). A capacity of `14` would need `6` days,
so `15` is minimal.

### Example 2

```
Input:  weights = [3, 2, 2, 4, 1, 4], days = 3
Output: 6
```

Explanation: With capacity `6`: day 1: `3, 2` (5); day 2: `2, 4` (6); day 3:
`1, 4` (5). That is `3` days. Capacity `5` would need `4` days.

### Example 3

```
Input:  weights = [1, 2, 3, 1, 1], days = 4
Output: 3
```

Explanation: With capacity `3`: day 1: `1, 2` (3); day 2: `3` (3); day 3: `1, 1`
(2). That is only `3` days, which is `<= 4`. Capacity `3` equals the largest
single weight, so it cannot be reduced further.

## Hint

A larger capacity never requires *more* days, so "can we ship within `days` days
at capacity `c`?" is a **monotonic** predicate. Use **Binary Search on Answer**
over the capacity range `[max(weights), sum(weights)]`.
