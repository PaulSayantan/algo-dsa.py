# Kth Largest Element in a Stream

**Difficulty:** Easy

**Source:** LeetCode 703 — Kth Largest Element in a Stream

## Description

Design a class to find the `k`-th largest element in a stream of integers. Note that
it is the `k`-th largest element in **sorted order**, not the `k`-th distinct element —
duplicates count.

Implement the `KthLargest` class:

- `KthLargest(int k, int[] nums)` initializes the object with the integer `k` and the
  (possibly empty) initial stream of integers `nums`.
- `int add(int val)` appends the integer `val` to the stream and returns the element
  representing the `k`-th largest element in the stream so far.

It is guaranteed that when `add` is called, there are at least `k` elements in the
stream.

## Constraints

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the array when you search for the `k`-th element.

## Examples

### Example 1

```
Input:
  ["KthLargest", "add", "add", "add", "add", "add"]
  [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
  [null, 4, 5, 5, 8, 8]
```

**Explanation:**
Start with k = 3 and stream `[4, 5, 8, 2]`; the 3rd largest so far is 4.
- `add(3)` -> stream `[4,5,8,2,3]`, sorted desc `[8,5,4,3,2]`, 3rd largest = **4**
- `add(5)` -> `[8,5,5,4,3,2]`, 3rd largest = **5**
- `add(10)` -> `[10,8,5,5,4,3,2]`, 3rd largest = **5**
- `add(9)` -> `[10,9,8,5,5,4,3,2]`, 3rd largest = **8**
- `add(4)` -> `[10,9,8,5,5,4,4,3,2]`, 3rd largest = **8**

### Example 2

```
Input:
  ["KthLargest", "add", "add"]
  [[1, []], [-3], [-2]]
Output:
  [null, -3, -2]
```

**Explanation:**
k = 1 with an empty initial stream (we track the single largest element).
- `add(-3)` -> stream `[-3]`, largest = **-3**
- `add(-2)` -> stream `[-3, -2]`, largest = **-2**

## Hint

Keep only the `k` largest elements you have seen so far. Use **Top-K via Heap**: a
min-heap capped at size `k` puts the current answer right at its root.
