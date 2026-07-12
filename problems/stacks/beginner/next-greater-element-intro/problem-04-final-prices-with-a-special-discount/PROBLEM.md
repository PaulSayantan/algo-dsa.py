# Final Prices With a Special Discount in a Shop

**Difficulty:** Easy

**Source:** LeetCode 1475 — Final Prices With a Special Discount in a Shop

## Description

Given an integer array `prices` where `prices[i]` is the price of the `i`-th item, there is a special discount: if you buy item `i`, you receive a discount equal to `prices[j]`, where `j` is the smallest index with `j > i` and `prices[j] <= prices[i]`. If no such `j` exists you get no discount. Return an array `answer` where `answer[i]` is the final price you pay for item `i` after the discount.

Constraints: `1 <= len(prices) <= 500`, `1 <= prices[i] <= 1000`.

## Examples

### Example 1

```
Input:  prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
```

**Explanation:** Item 0 (`8`) is discounted by the next price that is `<= 8`, namely `4`, so you pay `4`. Item 2 (`6`) is discounted by `2`, paying `4`. Items 3 and 4 have no later price `<=` them, so they keep their full price.

## Hint

It is the "next greater element" scan flipped: keep a stack of item indices and, when a price arrives that is `<=` a waiting item's price, that price is the waiting item's discount — pop it and subtract.
