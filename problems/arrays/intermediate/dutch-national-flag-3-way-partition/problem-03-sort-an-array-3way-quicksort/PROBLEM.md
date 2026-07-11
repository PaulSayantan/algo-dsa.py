# Sort an Array (3-way Quicksort)

**Difficulty:** Medium

**Source:** LeetCode 912 — Sort an Array

## Description

Given an array of integers `nums`, sort the array in **ascending order** and return it.

You must solve the problem **without using any built-in sort function** and with the best
possible time complexity. The intended approach here is **quicksort whose partition step is
the Dutch National Flag 3-way partition**: pick a pivot value, split the current subarray
into `< pivot`, `== pivot`, and `> pivot`, then recurse only on the `<` and `>` parts. This
handles inputs with **many duplicate keys** in near-linear time, avoiding the classic
quicksort blow-up on repeated values.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

Explanation: The array sorted in ascending order.

### Example 2

```
Input:  nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
```

Explanation: With many duplicates, a 3-way partition groups all equal keys together in one
step, so equal elements are never re-partitioned.

### Example 3

```
Input:  nums = [3, 3, 3]
Output: [3, 3, 3]
```

Explanation: All keys equal. A single 3-way partition places every element in the "equal"
region and there is nothing left to recurse on — O(n) total.

## Hint

Use quicksort, but replace the usual 2-way (Lomuto/Hoare) split with a **Dutch National Flag
(3-way partition)** so all elements equal to the pivot are grouped in the middle and excluded
from recursion.
