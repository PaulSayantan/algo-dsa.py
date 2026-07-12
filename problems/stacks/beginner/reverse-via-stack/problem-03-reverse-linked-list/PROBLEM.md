# Reverse a Linked List

**Difficulty:** Easy

**Source:** LeetCode 206 — Reverse Linked List

## Description

Given the `head` of a singly linked list, reverse the list and return the new head. Solve it with a stack: walk the list pushing every value, then pop the values back out (in reverse order) to relink the nodes.

The list is provided to the harness as a Python list of node values via the `build(...)` helper, and the result is read back with `to_list(...)`.

Constraints: `0 <= len(list) <= 5000`, node values fit in a machine int.

## Examples

### Example 1

```
Input:  head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

**Explanation:** Push `1,2,3,4,5`; popping yields `5,4,3,2,1`, the reversed order.

### Example 2

```
Input:  head = [1, 2]
Output: [2, 1]
```

**Explanation:** Two nodes swap ends.

## Hint

A stack pops in reverse insertion order — push each node's value, then pop to rebuild the list back-to-front.
