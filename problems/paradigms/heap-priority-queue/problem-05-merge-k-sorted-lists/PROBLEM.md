# Merge k Sorted Lists

**Difficulty:** Hard

**Source:** LeetCode 23 (Merge k Sorted Lists)

## Description

You are given an array of `k` linked lists `lists`, where each linked list is sorted in
**ascending** order.

Merge all the linked lists into **one sorted linked list** and return its head.

Each list is represented by its head `ListNode`. A `ListNode` has an integer `val` and a
`next` pointer. Some of the `k` lists may be empty (represented by `None`).

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- Each `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Examples

### Example 1

```
Input:  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

Explanation: The three sorted lists are `1->4->5`, `1->3->4`, and `2->6`. Merging them in
ascending order interleaves the nodes into `1->1->2->3->4->4->5->6`.

### Example 2

```
Input:  lists = []
Output: []
```

Explanation: There are no lists at all, so the merged result is the empty list.

### Example 3

```
Input:  lists = [[]]
Output: []
```

Explanation: There is a single list and it is empty, so the merged result is still empty.

## Hint

Use a **Heap / Priority Queue**. Keep a **min-heap holding the current front node of each
of the `k` lists**. Repeatedly pop the global minimum, append it to the output, and push
that node's successor. The heap always exposes the smallest available element in
`O(log k)`.
