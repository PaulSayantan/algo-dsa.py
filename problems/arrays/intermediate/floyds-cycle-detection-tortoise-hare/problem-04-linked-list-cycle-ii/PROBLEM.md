# Linked List Cycle II

**Difficulty:** Medium

**Source:** LeetCode 142 — Linked List Cycle II

## Description

Given the `head` of a linked list, return *the node where the cycle begins*. If
there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the `next` pointer. Internally, a
position `pos` is used to denote the index of the node that the tail's `next`
pointer is connected to (0-indexed). It is `-1` if there is no cycle. Note that
`pos` is **not passed as a parameter**.

**Do not modify** the linked list, and solve it using **O(1) memory**.

Unlike the simpler "does a cycle exist" question, here you must return the exact
node at which the loop starts — which is the classic second phase of Floyd's
algorithm.

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list.

## Examples

### Example 1

```
Input: head = [3, 2, 0, -4], pos = 1
Output: node at index 1 (value 2)
Explanation: The tail (-4) links back to index 1, so the cycle starts at the
node whose value is 2.
```

### Example 2

```
Input: head = [1, 2], pos = 0
Output: node at index 0 (value 1)
Explanation: The tail (2) links back to index 0, so the cycle begins at the
node whose value is 1.
```

### Example 3

```
Input: head = [1], pos = -1
Output: null
Explanation: There is no cycle, so there is no cycle-start node to return.
```

## Hint

Use **Floyd's Cycle Detection (Tortoise & Hare)** in two phases: first advance
slow (1 step) and fast (2 steps) until they meet inside the loop; then reset one
pointer to the head and advance both one step at a time — they reunite exactly
at the cycle's entry node.
