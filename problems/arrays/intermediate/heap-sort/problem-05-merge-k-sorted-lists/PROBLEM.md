# Merge k Sorted Lists

**Difficulty:** Hard

**Source:** LeetCode 23 — Merge k Sorted Lists

## Description

You are given an array of `k` linked lists `lists`, where each list is sorted in
**ascending order**. Merge all the lists into **one sorted linked list** and
return its head.

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

The linked-list node is defined as:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Examples

### Example 1

```
Input:  lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Explanation:** The three lists are `1->4->5`, `1->3->4`, and `2->6`. Merged
into one non-decreasing list, the values are `1,1,2,3,4,4,5,6`.

### Example 2

```
Input:  lists = []
Output: []
```

**Explanation:** No lists to merge, so the result is empty.

### Example 3

```
Input:  lists = [[]]
Output: []
```

**Explanation:** A single empty list produces an empty merged list.

## Hint

Use a **min-heap over the current fronts** of the `k` lists. Seed the heap with
each list's head node. Repeatedly pop the smallest node, append it to the output,
and push that node's `next` if it exists. The heap always exposes the global
minimum among the live fronts — the same "repeatedly extract the min" pattern as
heap sort, generalized to `k` streams. Runs in `O(N log k)` for `N` total nodes.
