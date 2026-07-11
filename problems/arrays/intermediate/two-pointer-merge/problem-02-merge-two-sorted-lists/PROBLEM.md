# Merge Two Sorted Lists

**Difficulty:** Easy

**Source:** LeetCode 21 — Merge Two Sorted Lists

## Description

You are given the heads of two sorted linked lists `list1` and `list2`, each sorted in
**non-decreasing** order.

Merge the two lists into one **sorted** linked list. The list should be made by
splicing together the nodes of the first two lists (i.e. reuse the existing nodes rather
than allocating new values).

Return the head of the merged linked list.

Each node is defined as:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Examples

### Example 1

```
Input:  list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Explanation: Interleaving the two sorted lists by always taking the smaller current
             node produces 1,1,2,3,4,4.
```

### Example 2

```
Input:  list1 = [], list2 = []
Output: []
Explanation: Both lists are empty, so the merged list is empty.
```

### Example 3

```
Input:  list1 = [], list2 = [0]
Output: [0]
Explanation: list1 is empty, so the result is just list2.
```

## Hint

Use the **Two-Pointer Merge** technique with one pointer per list. A **dummy head**
node makes it easy to append the smaller node each step and, at the end, attach the
non-empty remainder of whichever list still has nodes.
