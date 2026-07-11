# Range Assign and Range Minimum Query

**Difficulty:** Medium

**Source:** Classic segment-tree design problem (competitive-programming staple;
"range assign / range min" is the canonical drill for an *overwrite* lazy tag).

## Description

Design a data structure initialized from an integer array `nums` (0-indexed) that
supports these operations, interleaved in any order:

- **`assign(left, right, val)`** — set *every* element whose index lies in the
  inclusive range `[left, right]` to the value `val` (an overwrite, **not** an
  add).
- **`minRange(left, right)`** — return the minimum element whose index lies in the
  inclusive range `[left, right]`.

Each operation must run in `O(log n)`.

The key difference from a range-*add* structure: an assignment *replaces* whatever
was there, so a pending assignment on a node must **wipe out** any earlier pending
change on the same range rather than combine with it.

## Constraints

- `1 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= left <= right < len(nums)`
- `-10^9 <= val <= 10^9`
- At most `10^5` calls total across `assign` and `minRange`.

## Examples

### Example 1

```
Input:
  nums = [5, 3, 8, 1, 9]
  minRange(0, 4)
  assign(1, 3, 4)
  minRange(0, 2)
  minRange(3, 4)
Output:
  [1, 4, 4]
Explanation:
  Start:            [5, 3, 8, 1, 9]
  minRange(0,4):    min(5,3,8,1,9) = 1
  assign(1,3,4):    [5, 4, 4, 4, 9]   (indices 1..3 set to 4)
  minRange(0,2):    min(5,4,4) = 4
  minRange(3,4):    min(4,9) = 4
```

### Example 2

```
Input:
  nums = [2, 2, 2, 2]
  assign(0, 3, 7)
  minRange(0, 3)
  assign(2, 2, -1)
  minRange(0, 3)
Output:
  [7, -1]
Explanation:
  Start:            [2, 2, 2, 2]
  assign(0,3,7):    [7, 7, 7, 7]
  minRange(0,3):    7
  assign(2,2,-1):   [7, 7, -1, 7]     (single element overwrite)
  minRange(0,3):    min(7,7,-1,7) = -1
```

## Hint

Use a **Segment Tree with Lazy Propagation** where the aggregate is the range
minimum and the lazy tag is a pending *assignment*. Because assignment overwrites,
a new tag should **replace** the node's value and its child tag — and you need a
sentinel (e.g. `None`) to mark "no pending assignment".
