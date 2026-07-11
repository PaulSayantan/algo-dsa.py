# Reverse Linked List

**Difficulty:** Easy

**Source:** LeetCode 206 (Reverse Linked List)

## Description

Given the `head` of a singly linked list, reverse the list and return the new head.

A singly linked list is a **recursively defined structure**: a list is either empty,
or a single node followed by a smaller list. That makes it a natural fit for recursion
— reverse the *rest* of the list first, then fix up the link for the current node as
the recursion unwinds.

Each node is defined as:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Examples

### Example 1

```
Input:  head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

Explanation: The list `1 -> 2 -> 3 -> 4 -> 5` becomes `5 -> 4 -> 3 -> 2 -> 1`.

### Example 2

```
Input:  head = [1, 2]
Output: [2, 1]
```

Explanation: The two nodes swap order; `2` becomes the new head and points to `1`.

### Example 3

```
Input:  head = []
Output: []
```

Explanation: An empty list reverses to an empty list — this is the base case.

## Hint

Use **Recursion**: recursively reverse the sublist starting at `head.next`. When that
call returns, `head.next` is the tail of the reversed portion, so set
`head.next.next = head` to point it back at the current node, then sever `head.next`.
The base case is an empty list or a single node.
