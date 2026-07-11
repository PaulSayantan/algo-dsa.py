# Kth Largest Element in a Stream

**Difficulty:** Easy

**Source:** LeetCode 703 (Kth Largest Element in a Stream)

## Description

Design a class to find the **kth largest** element in a stream of integers. Note that
it is the kth largest element in the *sorted order*, not the kth distinct element.

Implement the `KthLargest` class:

- `KthLargest(int k, int[] nums)` initializes the object with the integer `k` and the
  (possibly empty) initial stream `nums`.
- `int add(int val)` appends `val` to the stream and returns the element representing
  the kth largest element **after** the insertion.

You may assume that after every `add` call the stream contains at least `k` elements.

## Constraints

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the array when you
  search for the kth element.

## Examples

### Example 1

```
Input:
  ["KthLargest", "add", "add", "add", "add", "add"]
  [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
  [null, 4, 5, 5, 8, 8]
```

Explanation:
```
KthLargest(3, [4, 5, 8, 2])   // stream sorted desc: [8, 5, 4, 2], 3rd largest = 4
add(3)  -> [8, 5, 4, 3, 2],        3rd largest = 4
add(5)  -> [8, 5, 5, 4, 3, 2],     3rd largest = 5
add(10) -> [10, 8, 5, 5, 4, 3, 2], 3rd largest = 5
add(9)  -> [10, 9, 8, 5, 5, ...],  3rd largest = 8
add(4)  -> [10, 9, 8, 5, 5, 4,...],3rd largest = 8
```

### Example 2

```
Input:
  ["KthLargest", "add", "add"]
  [[1, []], [-3], [-2]]
Output:
  [null, -3, -2]
```

Explanation: With `k = 1` we always want the single largest element seen so far.
After `add(-3)` the stream is `[-3]`, largest is `-3`. After `add(-2)` the stream is
`[-3, -2]`, largest is `-2`.

## Hint

Use a **Heap / Priority Queue**. Keep a **min-heap of size `k`** holding the `k`
largest elements seen so far — its root (smallest of those `k`) is exactly the kth
largest overall. On each `add`, push and, if the heap grew past `k`, pop the smallest.
