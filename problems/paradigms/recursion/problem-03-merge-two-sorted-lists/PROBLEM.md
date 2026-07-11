# Merge Two Sorted Lists

**Difficulty:** Easy

**Source:** LeetCode 21 (Merge Two Sorted Lists)

## Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing
together the nodes of the first two lists. Return the head of the merged linked list.

Because a linked list is *a head node plus a smaller list*, merging has a naturally
recursive shape: pick the smaller of the two heads, and the rest of the answer is
simply the merge of "what's left" — a strictly smaller version of the same problem.

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
- Both `list1` and `list2` are sorted in **non-decreasing** order.

## Examples

### Example 1

```
Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

Explanation: Interleaving the two sorted lists in non-decreasing order gives
`1, 1, 2, 3, 4, 4`.

### Example 2

```
Input:  list1 = [], list2 = []
Output: []
```

Explanation: Merging two empty lists gives an empty list — the base case.

### Example 3

```
Input:  list1 = [], list2 = [0]
Output: [0]
```

Explanation: When one list is empty, the merged result is just the other list.

## Hint

Use **Recursion**: compare the two heads. The smaller head is the head of the merged
list, and its `next` is the merge of the remainder of that list with the other list.
The base case is when either list is empty — return the other one.
