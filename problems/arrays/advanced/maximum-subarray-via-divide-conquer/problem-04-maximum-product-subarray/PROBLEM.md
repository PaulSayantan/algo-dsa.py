# Maximum Product Subarray

**Difficulty:** Medium/Hard

**Source:** LeetCode 152 — Maximum Product Subarray

## Description

Given an integer array `nums`, find the contiguous non-empty subarray that has the
largest **product**, and return that product.

Products are trickier than sums because of sign flips: multiplying by a negative
number turns the *smallest* (most negative) product into the *largest*, and a zero
resets everything. That means a divide & conquer combine step cannot get away with
tracking only the best crossing value — it must track, for each half, the maximum
**and** the minimum prefix/suffix product, so that when the two halves are joined
a negative-times-negative can be recognized as a new maximum.

It is guaranteed that the answer fits in a 32-bit signed integer.

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any prefix or suffix of `nums` fits in a 32-bit signed integer.
- The subarray must be non-empty.

## Examples

### Example 1

```
Input:  nums = [2, 3, -2, 4]
Output: 6
Explanation: The subarray [2, 3] has the largest product 2 * 3 = 6. Extending past
             the -2 would make the product negative.
```

### Example 2

```
Input:  nums = [-2, 0, -1]
Output: 0
Explanation: No subarray gives a product larger than 0. Any subarray spanning the
             zero yields 0, and the single negatives are worse.
```

### Example 3

```
Input:  nums = [-2, 3, -4]
Output: 24
Explanation: The whole array [-2, 3, -4] has product (-2) * 3 * (-4) = 24. The two
             negatives cancel, so spanning them beats any smaller slice.
```

## Hint

Use **Maximum Subarray via Divide & Conquer**, but have each recursive call return
a *summary* of its range: `(total, max_prefix, min_prefix, max_suffix, min_suffix,
best)`. When you merge two halves, the best crossing product comes from combining
the left's max/min **suffix** with the right's max/min **prefix** — take all four
sign combinations. Tracking the minimum is essential because two negatives can
multiply into the maximum.
