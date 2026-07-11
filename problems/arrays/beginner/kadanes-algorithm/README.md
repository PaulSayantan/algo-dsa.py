# Kadane's Algorithm

**Kadane's Algorithm** is a dynamic-programming technique for finding the
maximum-sum contiguous subarray of a one-dimensional array in a single pass.

## The core idea

As you scan the array left to right, keep a running sum of the "best subarray
ending at the current index." At each element you make one local decision:

```
current = max(x, current + x)
```

In words: *either extend the previous subarray by adding the current element, or
throw away the previous subarray and start fresh at the current element.* You
start fresh whenever the running sum has become a liability (dropped below the
element's own value — i.e. the accumulated prefix is negative). A separate
variable tracks the best running sum ever seen.

## When to reach for it

- You need the maximum (or minimum) sum of a **contiguous** subarray.
- The problem can be reframed as a maximum-subarray problem — e.g. maximizing
  profit from stock prices (Kadane on the day-to-day price differences), the
  maximum absolute subarray sum (run Kadane for both max and min), or the
  maximum product subarray (track running max **and** min because of negatives).
- More advanced variants: circular arrays (LeetCode 918) and concatenated
  arrays (LeetCode 1191) build directly on the same running-sum invariant.

## Complexity

| Metric | Value |
| --- | --- |
| Time | **O(n)** — one linear scan |
| Space | **O(1)** — a couple of scalar accumulators |

## Problems

| # | Problem | Summary | Difficulty |
| --- | --- | --- | --- |
| 1 | [Maximum Subarray](problem-01-maximum-subarray/PROBLEM.md) | The canonical max contiguous subarray sum (LeetCode 53). | Easy |
| 2 | [Best Time to Buy and Sell Stock](problem-02-best-time-to-buy-and-sell-stock/PROBLEM.md) | Max single-transaction profit, reframed as Kadane on price differences (LeetCode 121). | Easy |
| 3 | [Maximum Absolute Sum of Any Subarray](problem-03-maximum-absolute-sum-of-any-subarray/PROBLEM.md) | Largest absolute subarray sum — run Kadane for both max and min (LeetCode 1749). | Medium |
| 4 | [Maximum Product Subarray](problem-04-maximum-product-subarray/PROBLEM.md) | Max contiguous product; track running min and max for negatives (LeetCode 152). | Medium |
| 5 | [Maximum Sum Circular Subarray](problem-05-maximum-sum-circular-subarray/PROBLEM.md) | Max subarray sum on a circular array via two Kadane passes (LeetCode 918). | Medium |
| 6 | [K-Concatenation Maximum Sum](problem-06-k-concatenation-maximum-sum/PROBLEM.md) | Max subarray sum of an array repeated k times (LeetCode 1191). | Hard |
