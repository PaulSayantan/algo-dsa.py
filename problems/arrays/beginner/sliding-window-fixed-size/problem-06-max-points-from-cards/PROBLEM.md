# Maximum Points You Can Obtain from Cards

**Difficulty:** Medium-Hard

**Source:** LeetCode 1423 — "Maximum Points You Can Obtain from Cards"

## Description

There are several cards arranged in a row, and each card has an associated number of
points given by the integer array `cardPoints`.

In one step, you take exactly one card from either the **beginning** or the **end** of
the row. You must take exactly `k` cards in total.

Your score is the sum of the points of the cards you have taken. Return the **maximum
score** you can obtain.

## Constraints

- `1 <= cardPoints.length <= 10^5`
- `1 <= cardPoints[i] <= 10^4`
- `1 <= k <= cardPoints.length`

## Examples

### Example 1

```
Input:  cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3
Output: 12
```

**Explanation:** The best choice is to take the three rightmost cards `5 + 6 + 1 = 12`.
Equivalently: the total of all cards is `22`, and you leave behind a contiguous block of
`n - k = 4` cards. The smallest such block is `[1, 2, 3, 4] = 10`, so the maximum score
is `22 - 10 = 12`.

### Example 2

```
Input:  cardPoints = [2, 2, 2], k = 2
Output: 4
```

**Explanation:** You must take 2 of the 3 cards, and each is worth `2`, so any pair
gives `4`. Via the complement view: total `6` minus the minimum leftover block of size
`n - k = 1` (which is `2`) equals `4`.

### Example 3

```
Input:  cardPoints = [9, 7, 7, 9, 7, 7, 9], k = 7
Output: 55
```

**Explanation:** You must take all `7` cards, so the score is the entire sum
`9 + 7 + 7 + 9 + 7 + 7 + 9 = 55`. Here `n - k = 0`, so no cards are left behind.

## Hint

Use a **Sliding Window (fixed size)** on the **complement**. Taking `k` cards from the
two ends is the same as *leaving behind* one contiguous block of `n - k` cards in the
middle. To maximize what you take, **minimize** the sum of that leftover block: slide a
fixed window of width `n - k` to find its minimum sum, then subtract it from the total.
