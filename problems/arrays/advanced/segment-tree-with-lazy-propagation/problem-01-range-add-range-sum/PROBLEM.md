# Range Add and Range Sum Query

**Difficulty:** Medium

**Source:** Classic segment-tree design problem (CSES "Range Update Queries" /
"Dynamic Range Sum Queries" family; the canonical introduction to lazy
propagation).

## Description

Design a data structure that is initialized from an integer array `nums`
(0-indexed) and then supports the following two operations, interleaved in any
order and any number of times:

- **`update(left, right, val)`** — add the integer `val` to *every* element whose
  index lies in the inclusive range `[left, right]`.
- **`sumRange(left, right)`** — return the sum of all elements whose index lies in
  the inclusive range `[left, right]`.

Each individual operation must run in `O(log n)` time; a naive implementation
that walks every element of the range on each update is too slow when there are
many large-range updates.

## Constraints

- `1 <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `0 <= left <= right < len(nums)`
- `-10^4 <= val <= 10^4`
- At most `10^5` calls total across `update` and `sumRange`.
- The running sum of any range fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:
  nums = [1, 2, 3, 4, 5]
  update(1, 3, 2)
  sumRange(0, 2)
  update(0, 4, 1)
  sumRange(2, 4)
Output:
  [10, 19]
Explanation:
  Start:            [1, 2, 3, 4, 5]
  update(1,3,2):    [1, 4, 5, 6, 5]   (added 2 to indices 1..3)
  sumRange(0,2):    1 + 4 + 5 = 10
  update(0,4,1):    [2, 5, 6, 7, 6]   (added 1 to every index)
  sumRange(2,4):    6 + 7 + 6 = 19
```

### Example 2

```
Input:
  nums = [0, 0, 0, 0]
  sumRange(0, 3)
  update(1, 2, 5)
  sumRange(0, 3)
  sumRange(0, 0)
Output:
  [0, 10, 0]
Explanation:
  Start:            [0, 0, 0, 0]
  sumRange(0,3):    0
  update(1,2,5):    [0, 5, 5, 0]
  sumRange(0,3):    0 + 5 + 5 + 0 = 10
  sumRange(0,0):    0   (index 0 was never touched)
```

## Hint

Use a **Segment Tree with Lazy Propagation**. Store the subtree sum in each node
and an additive "pending add" tag. When an update fully covers a node, bump its
sum by `val * (range length)` and accumulate `val` into its lazy tag instead of
recursing further.
