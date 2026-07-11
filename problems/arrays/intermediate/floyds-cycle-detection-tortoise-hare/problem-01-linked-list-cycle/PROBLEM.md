# Linked List Cycle

**Difficulty:** Easy

**Source:** LeetCode 141 — Linked List Cycle

## Description

Given the `head` of a singly linked list, determine if the list has a cycle in
it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the `next` pointer. Internally, a
position `pos` is used to denote the index of the node that the tail's `next`
pointer is connected to. Note that `pos` is **not passed as a parameter** — it
only describes how the test input is built.

Return `true` if there is a cycle in the linked list. Otherwise, return
`false`.

You must solve it using **O(1) (constant) memory**.

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list.

## Examples

### Example 1

```
Input: head = [3, 2, 0, -4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail (node -4)
connects back to the node at index 1 (node 2). Following next pointers forever
never terminates.
```

### Example 2

```
Input: head = [1, 2], pos = 0
Output: true
Explanation: The tail (node 2) connects back to the node at index 0 (node 1),
so the list loops: 1 -> 2 -> 1 -> 2 -> ...
```

### Example 3

```
Input: head = [1], pos = -1
Output: false
Explanation: pos = -1 means the tail points to null, so there is no cycle. A
single node whose next is null simply terminates.
```

## Hint

Use **Floyd's Cycle Detection (Tortoise & Hare)**: advance one pointer one step
at a time and another two steps at a time. If they ever land on the same node,
a cycle exists; if the fast pointer reaches the end of the list, it does not.
