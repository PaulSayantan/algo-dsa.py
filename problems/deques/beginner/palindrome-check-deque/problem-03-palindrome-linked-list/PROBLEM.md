# Palindrome Linked List

**Difficulty:** Easy

**Source:** LeetCode 234 — Palindrome Linked List

## Description

Given the `head` of a singly linked list, return whether the list reads the same forwards and backwards. Because a singly linked list has no backward links, walk it once pushing each node's `val` onto a deque; then compare `popleft()` against `pop()` until at most one element remains. An empty list or a single node is a palindrome.

## Examples

### Example 1

```
Input:  head = [1, 2, 2, 1]
Output: true
```

**Explanation:** The value sequence `1, 2, 2, 1` mirrors itself.

### Example 2

```
Input:  head = [1, 2]
Output: false
```

**Explanation:** `1` and `2` differ, so it is not a palindrome.

## Hint

Copy the node values into a deque in order, then compare `popleft()` vs `pop()` from both ends.
