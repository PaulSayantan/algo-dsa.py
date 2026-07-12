# Maximum Points You Can Obtain from Cards

**Difficulty:** Medium

**Source:** LeetCode 1423 — Maximum Points You Can Obtain from Cards

## Description

There are several cards in a row, each with a point value given by `cardPoints`. In one step you take exactly one card from either the beginning or the end of the row. You must take exactly `k` cards.

Return the maximum score (sum of point values of the cards taken).

The cards you leave behind form a contiguous window of size `n - k`. Minimizing that leftover window's sum maximizes your score, so this is a fixed-size sliding-window minimum.

Constraints: `1 <= cardPoints.length <= 10^5`, `1 <= cardPoints[i] <= 10^4`, `1 <= k <= cardPoints.length`.

## Examples

### Example 1

```
Input:  cardPoints=[1,2,3,4,5,6,1], k=3
Output: 12
```

**Explanation:** Taking the last three cards `5,6,1` yields `12`, the best possible.

## Hint

Instead of choosing the taken cards, slide a fixed size-`(n-k)` window to find the minimum-sum contiguous block to leave behind; the answer is `total - minWindow`.
