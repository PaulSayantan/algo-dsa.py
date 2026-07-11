# Koko Eating Bananas

**Difficulty:** Medium

**Source:** LeetCode 875 — Koko Eating Bananas

## Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko decides her constant banana-eating speed of `k` bananas per hour. Each hour, she chooses some pile and eats `k` bananas from it. If the pile has fewer than `k` bananas, she eats all of them instead and will not eat any more bananas during that hour (she does not carry the extra eating capacity to another pile).

Koko likes to eat slowly but still wants to finish eating **all** the bananas before the guards return.

Return the **minimum** integer `k` such that she can eat all the bananas within `h` hours.

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Examples

### Example 1

```
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4
Explanation: At speed k = 4, the hours needed are
ceil(3/4)=1 + ceil(6/4)=2 + ceil(7/4)=2 + ceil(11/4)=3 = 8 hours <= 8.
At speed k = 3 it would take 1 + 2 + 3 + 4 = 10 > 8 hours, so 4 is the minimum.
```

### Example 2

```
Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30
Explanation: There are 5 piles and only h = 5 hours, so Koko must finish each
pile in exactly one hour. That forces k to be at least the largest pile, 30.
```

### Example 3

```
Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
Explanation: With one extra hour (h = 6), speed k = 23 works:
ceil(30/23)=2 + ceil(11/23)=1 + ceil(23/23)=1 + ceil(4/23)=1 + ceil(20/23)=1 = 6.
Speed 22 needs ceil(30/22)=2 + 1 + ceil(23/22)=2 + 1 + 1 = 7 > 6, so 23 is minimal.
```

## Hint

The answer `k` lies in the range `[1, max(piles)]`, and "can Koko finish within `h` hours at speed `k`?" is monotonic — a faster speed never needs more hours. Use **Binary Search on Answer** to find the smallest feasible `k`.
