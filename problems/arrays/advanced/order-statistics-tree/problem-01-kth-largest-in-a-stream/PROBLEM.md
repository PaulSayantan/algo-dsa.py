# Kth Largest Element in a Stream

**Difficulty:** Easy

**Source:** LeetCode 703 — Kth Largest Element in a Stream

## Description

Design a class to find the k-th largest element in a stream of integers. Note that
it is the k-th largest element in **sorted order** (counting duplicates), not the
k-th distinct element.

Implement `KthLargest`:

- `KthLargest(int k, int[] nums)` initializes the object with the integer `k` and
  the initial stream of numbers `nums`.
- `int add(int val)` appends the integer `val` to the stream and returns the element
  representing the k-th largest element in the stream so far.

It is guaranteed that, at the time of each `add`, the stream contains at least `k`
elements.

This problem is the canonical "select" use case: after each insertion into a
dynamic multiset of size `n`, the k-th largest element is exactly the
`(n - k + 1)`-th **smallest** element, which an order-statistics tree returns in
`O(log n)`.

## Constraints

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.
- It is guaranteed that there are at least `k` elements in the array when you search
  for the k-th element.

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
```
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // stream = [2,3,4,5,8],        3rd largest = 4
kthLargest.add(5);   // stream = [2,3,4,5,5,8],      3rd largest = 5
kthLargest.add(10);  // stream = [2,3,4,5,5,8,10],   3rd largest = 5
kthLargest.add(9);   // stream = [2,3,4,5,5,8,9,10], 3rd largest = 8
kthLargest.add(4);   // stream = [2,3,4,4,5,5,8,9,10],3rd largest = 8
```

### Example 2

```
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[1, []], [-3], [-2], [-4], [0], [4]]

Output:
[null, -3, -2, -2, 0, 4]
```

**Explanation:** With `k = 1` we always want the largest (maximum) element seen so
far. After adding -3 the max is -3; after -2 the max is -2; adding -4 does not beat
-2; then 0 and 4 each become the new max.

## Hint

Maintain the stream as a dynamic multiset in an **Order-Statistics Tree** augmented
with subtree sizes. After each insertion the answer is the `(size - k + 1)`-th
smallest key, retrievable with a `select` operation in `O(log n)`.
