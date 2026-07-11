# Find Median from Data Stream

**Difficulty:** Hard

**Source:** LeetCode 295 — Find Median from Data Stream

## Description

The **median** is the middle value in an ordered list of numbers. If the list
has an even number of elements, the median is the mean of the two middle values.

- For `arr = [2,3,4]`, the median is `3`.
- For `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:

- `MedianFinder()` initializes the object.
- `void addNum(int num)` adds the integer `num` from the data stream to the
  structure.
- `double findMedian()` returns the median of all elements added so far. Answers
  within `10^-5` of the actual value are accepted.

## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element before `findMedian` is called.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

## Examples

### Example 1

```
Input:
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
Output:
[null, null, null, 1.5, null, 2.0]
```

**Explanation:** After adding `1` and `2`, the stream is `[1,2]` and the median
is `(1 + 2) / 2 = 1.5`. After adding `3`, the stream is `[1,2,3]` and the median
is the middle value `2.0`.

### Example 2

```
Input:
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[5],[],[10],[]]
Output:
[null, null, 5.0, null, 7.5]
```

**Explanation:** After adding `5`, the only element is `5`, so the median is
`5.0`. After adding `10`, the stream is `[5,10]` and the median is
`(5 + 10) / 2 = 7.5`.

## Hint

Keep the data split into a **max-heap of the smaller half** and a **min-heap of
the larger half**. After each insertion, rebalance so the two heaps differ in
size by at most one. The median is then either the root of the larger heap or
the average of the two roots — both `O(1)`. Each `addNum` is `O(log n)`; this is
the two-heap application of the "extract from the top" idea behind heap sort.
