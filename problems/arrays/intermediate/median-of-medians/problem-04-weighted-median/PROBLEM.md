# Weighted Median

**Difficulty:** Medium

Source: CLRS Problem 9-2 ("Weighted median"). A classic application that shows
Median of Medians / linear selection extends beyond the plain median.

## Description

You are given `n` distinct values `nums[0..n-1]` with associated positive
weights `weights[0..n-1]`. Let `W = sum(weights)` be the total weight.

The **lower weighted median** is the value `x_k` such that

```
sum of weights of all values strictly less than x_k   <  W / 2
sum of weights of all values strictly greater than x_k <= W / 2
```

Equivalently: sort the values in increasing order; walking through them and
accumulating weight, the lower weighted median is the first value at which the
running total reaches **at least `W / 2`**.

Special cases of the definition:
- If all weights are equal, the weighted median is just the ordinary lower
  median.
- The weighted median minimizes `sum_i weights[i] * |x_k - nums[i]|` over all
  choices of a point `x_k` — it is the "post office location" optimum on a line.

Return the lower weighted median **value**. Aim for **worst-case O(n)** time.

## Constraints

- `1 <= n <= 10^5`
- The `nums` values are distinct.
- `weights[i] > 0` (weights may be integers or reals).
- `W = sum(weights) > 0`.

## Examples

### Example 1
```
Input:  nums = [1, 2, 3, 4, 5], weights = [0.2, 0.2, 0.2, 0.2, 0.2]
Output: 3
Explanation: Total weight W = 1, so W / 2 = 0.5. Accumulating weight over the
sorted values gives 0.2, 0.4, 0.6, ... The running total first reaches 0.5 at
value 3 (cumulative 0.6). With equal weights this is just the ordinary median.
```

### Example 2
```
Input:  nums = [10, 35, 5, 20, 60], weights = [10, 35, 5, 20, 30]
Output: 35
Explanation: Sorted by value: 5, 10, 20, 35, 60 with weights 5, 10, 20, 35, 30.
Total W = 100, so W / 2 = 50. Cumulative weights are 5, 15, 35, 70, 100. The
running total first reaches 50 at value 35 (cumulative 70). Check:
weight below 35 = 5 + 10 + 20 = 35 < 50, and weight above 35 = 30 <= 50.
```

### Example 3
```
Input:  nums = [1, 2, 3], weights = [0.1, 0.1, 0.8]
Output: 3
Explanation: W = 1, W / 2 = 0.5. Cumulative weights over sorted values are
0.1, 0.2, 1.0. The total first reaches 0.5 at value 3 (cumulative 1.0). The
heavy weight on 3 pulls the weighted median to it.
```

## Hint

Don't sort. Recurse with **Median of Medians**: partition around the
median-of-medians pivot, add up the weight on each side, and decide which side
holds the weighted median — carrying the "already-accounted" weight downward.
This gives worst-case linear time.
