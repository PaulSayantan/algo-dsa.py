# Capacity To Ship Packages Within D Days

**Difficulty:** Medium

**Source:** LeetCode 1011 — Capacity To Ship Packages Within D Days

## Description

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `i`-th package on the belt has a weight of `weights[i]`. Each day, the ship loads packages in the **order given** by `weights` (you may **not** reorder them). The total weight loaded on any single day must not exceed the ship's maximum weight **capacity**.

Return the **least** weight capacity of the ship that will allow all the packages on the belt to be shipped within `days` days.

## Constraints

- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

## Examples

### Example 1

```
Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 ships all packages in 5 days as follows:
day 1: 1, 2, 3, 4, 5   (sum 15)
day 2: 6, 7            (sum 13)
day 3: 8               (sum 8)
day 4: 9               (sum 9)
day 5: 10              (sum 10)
Any capacity below 15 would need more than 5 days, and note we cannot split a
package (e.g. capacity 14 cannot even fit the group 1..5 as one day of 15).
```

### Example 2

```
Input:  weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 ships all packages in 3 days:
day 1: 3, 2     (sum 5)
day 2: 2, 4     (sum 6)
day 3: 1, 4     (sum 5)
Capacity 5 would require 4 days, so 6 is the minimum.
```

### Example 3

```
Input:  weights = [1,2,3,1,1], days = 4
Output: 3
Explanation: With capacity 3:
day 1: 1, 2   (sum 3)
day 2: 3      (sum 3)
day 3: 1, 1   (sum 2)
That uses 3 days, which is within 4. Capacity 2 is impossible because it cannot
even hold the package of weight 3, so 3 (the heaviest single package) is minimal.
```

## Hint

The answer (a capacity) lies between `max(weights)` and `sum(weights)`. "Can we ship within `days` days using capacity `c`?" is monotonic — a bigger ship never needs more days. Use **Binary Search on Answer** to find the smallest feasible capacity.
