# Count Subsets with a Given Sum (n up to 40)

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (e.g. Codeforces / CSES
"Meet in the Middle" family). Also the counting variant of the subset-sum /
knapsack decision problem in CLRS.

## Description

You are given an array `nums` of `n` integers (values may be large, possibly
negative) and a target integer `target`.

Return the number of **subsets** of `nums` (including the empty subset) whose
elements sum to exactly `target`.

A subset is defined by which indices are chosen; two subsets are different if
they choose different index sets, even if they contain equal values.

The key twist versus classic DP: because element values can be huge (up to
`10^9` in magnitude), a `O(n * target)` dynamic-programming table is
impossible. But `n` is small enough (`<= 40`) that an exponential-in-`n/2`
approach is fast.

## Constraints

- `1 <= n <= 40`
- `-10^9 <= nums[i] <= 10^9`
- `-4 * 10^10 <= target <= 4 * 10^10`

## Examples

### Example 1

```
Input:  nums = [1, 2, 3], target = 3
Output: 2
```

**Explanation:** The subsets summing to 3 are `{3}` and `{1, 2}`.

### Example 2

```
Input:  nums = [2, 2, 2], target = 4
Output: 3
```

**Explanation:** Choosing any two of the three 2's gives sum 4. There are
`C(3, 2) = 3` such subsets (they are distinct because they use different
indices), so the answer is 3.

### Example 3

```
Input:  nums = [1, -1, 2], target = 0
Output: 2
```

**Explanation:** The subsets summing to 0 are the empty subset `{}` and
`{1, -1}`.

## Hint

`2^40 ≈ 10^12` subsets is too many to list, but `2^20 ≈ 10^6` is trivial.
Split the array into two halves, enumerate all subset sums of each half, and
**meet in the middle**: count how many left-half sums pair with a right-half
sum to reach the target.
