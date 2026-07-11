# Find Median from Data Stream

**Difficulty:** Hard

**Source:** LeetCode 295 (Find Median from Data Stream)

## Description

The **median** is the middle value in an ordered list of numbers. If the list has an odd
number of values, the median is the middle element. If it has an even number of values,
there is no single middle element, so the median is the **mean of the two middle values**.

- For example, the median of `[2, 3, 4]` is `3`.
- For example, the median of `[2, 3]` is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:

- `MedianFinder()` initializes the object.
- `void addNum(int num)` adds the integer `num` from the data stream to the structure.
- `double findMedian()` returns the median of all elements added so far. Answers within
  `10^-5` of the true median are accepted.

## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element in the structure before `findMedian` is called.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

## Examples

### Example 1

```
Input:
  ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
  [[], [1], [2], [], [3], []]
Output:
  [null, null, null, 1.5, null, 2.0]
```

Explanation:
```
MedianFinder()   // empty structure
addNum(1)        // stream = [1]
addNum(2)        // stream = [1, 2]
findMedian()     // -> (1 + 2) / 2 = 1.5
addNum(3)        // stream = [1, 2, 3]
findMedian()     // -> 2.0  (middle of the sorted [1, 2, 3])
```

### Example 2

```
Input:
  ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian"]
  [[], [-1], [], [-2], []]
Output:
  [null, null, -1.0, null, -1.5]
```

Explanation: After `addNum(-1)` the stream is `[-1]`, median `-1.0`. After `addNum(-2)`
the sorted stream is `[-2, -1]`, median `(-2 + -1) / 2 = -1.5`.

## Hint

Use **two Heaps / Priority Queues**. Keep a **max-heap for the smaller half** and a
**min-heap for the larger half**, kept balanced in size (differing by at most one). The
two heap roots straddle the middle, so the median is a root (odd total) or the average of
both roots (even total) — all in `O(log n)` per insert and `O(1)` per query.
