# Merge k Sorted Lists

**Difficulty:** Hard

**Source:** LeetCode 23 — Merge k Sorted Lists

## Description

You are given an array of `k` linked lists `lists`, where each linked list is sorted in
**non-decreasing** order.

Merge all the linked lists into one sorted linked list and return its head.

Each node is defined as:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- Each `lists[i]` is sorted in non-decreasing order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Examples

### Example 1

```
Input:  lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: Merging the three sorted lists
             1->4->5, 1->3->4, 2->6
             into one sorted list gives 1->1->2->3->4->4->5->6.
```

### Example 2

```
Input:  lists = []
Output: []
Explanation: There are no lists to merge, so the result is empty.
```

### Example 3

```
Input:  lists = [[]]
Output: []
Explanation: The single list is empty, so the merged result is empty.
```

## Hint

Build on the pairwise **Two-Pointer Merge** of two sorted lists (see Problem 2). Merging
the lists one at a time into an accumulator is `O(k * N)`; instead pair them up and merge
in `log k` rounds (divide and conquer). A min-heap over the `k` current heads is an
equivalent way to always pull the global minimum next.
