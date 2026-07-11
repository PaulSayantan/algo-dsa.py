# Intersection of Two Sorted Arrays (Galloping)

**Difficulty:** Hard

**Source:** Classic "intersection of two sorted lists" (the galloping/one-sided
binary search that powers Timsort's merge and inverted-index intersection in
search engines); related to LeetCode 349

## Description

You are given two arrays `a` and `b`, each sorted in **ascending order**, and
you want their intersection: the set of values that appear in **both**. The twist
is that the arrays can have **wildly different sizes** — imagine `a` has a few
thousand elements while `b` has hundreds of millions. Return the common values
in ascending order (each common value once; both inputs contain distinct values).

A standard two-pointer linear merge is `O(m + n)`, which is dominated by the
huge array. Instead, for each element of the **smaller** array, use
**galloping search** to jump forward through the **larger** array: double the
step (`1, 2, 4, 8, ...`) until you overshoot the value you are looking for, then
binary-search the bracket. This turns each lookup into `O(log(gap))` where `gap`
is the distance advanced, giving `O(m * log(n / m))` overall.

## Constraints

- `0 <= len(a), len(b) <= 2 * 10^8`
- `-10^9 <= a[i], b[i] <= 10^9`
- Both `a` and `b` are strictly increasing (values within each array are
  distinct).
- The result must be sorted ascending, with each shared value listed once.

## Examples

**Example 1**

```
Input:  a = [1, 4, 9], b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [1, 4, 9]
Explanation: Every element of the small array is present in the large one. For
each of 1, 4, 9 we gallop from where we left off in b, so we never rescan the
skipped-over elements.
```

**Example 2**

```
Input:  a = [2, 5, 100], b = [1, 2, 3, 4, 5, 6]
Output: [2, 5]
Explanation: 2 and 5 are common; 100 is galloped past the end of b and found
absent, so it is excluded.
```

**Example 3**

```
Input:  a = [10, 20, 30], b = [1, 2, 3]
Output: []
Explanation: The ranges do not overlap; galloping for 10 immediately overshoots
the end of b, and no common value exists.
```

## Hint

Use Exponential (Galloping) Search: iterate over the smaller array and, keeping a
cursor into the larger array, gallop (`1, 2, 4, ...` from the cursor) until you
overshoot the current value, then binary-search the bracket. Advance the cursor
so each search starts where the previous one ended.
