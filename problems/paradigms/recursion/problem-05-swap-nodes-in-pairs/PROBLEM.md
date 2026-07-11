# Swap Nodes in Pairs

**Difficulty:** Medium

**Source:** LeetCode 24 (Swap Nodes in Pairs)

## Description

Given the `head` of a linked list, swap every two adjacent nodes and return the head of
the modified list. You must solve the problem **without modifying the values** in the
list's nodes (i.e., only the nodes themselves may be changed — you must actually
re-link pointers).

This is a step up from a plain reversal: you handle the list *two nodes at a time*.
Swap the first pair, then the rest of the list is the same problem on a shorter list —
a textbook recursive reduction. If a lone node is left at the end, it stays in place.

Each node is defined as:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Constraints

- The number of nodes in the list is in the range `[0, 100]`.
- `0 <= Node.val <= 100`

## Examples

### Example 1

```
Input:  head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]
```

Explanation: Swap `(1, 2)` to get `2, 1` and swap `(3, 4)` to get `4, 3`.

### Example 2

```
Input:  head = [1, 2, 3]
Output: [2, 1, 3]
```

Explanation: The first pair `(1, 2)` is swapped to `2, 1`; the lone final node `3` has
no partner, so it stays in place.

### Example 3

```
Input:  head = [1]
Output: [1]
```

Explanation: A single node has no pair to swap with, so the list is unchanged — one of
the base cases.

## Hint

Use **Recursion**: if there are fewer than two nodes, return `head` unchanged (base
case). Otherwise let `first = head` and `second = head.next`; recursively swap the rest
of the list starting at `second.next`, attach that result to `first.next`, then set
`second.next = first` and return `second` as the new head of this pair.
