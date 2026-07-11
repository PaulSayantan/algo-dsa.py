# Linked List Random Node

**Difficulty:** Medium

**Source:** LeetCode 382 — Linked List Random Node

## Description

Given a singly linked list, return the value of a **random node** from the list. Each
node must be chosen with **equal probability**.

Implement the `Solution` class:

- `Solution(ListNode head)` — initializes the object with the head of the list.
- `int getRandom()` — returns the value of a random node, chosen uniformly at random
  from the list.

**Follow-up:** What if the linked list is extremely large and its length is unknown to
you? Could you solve this **without** first counting the nodes, and using only constant
extra space?

## Constraints

- The number of nodes in the list is in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- At most `10^4` calls will be made to `getRandom`.

## Examples

### Example 1

```
Input:
["Solution", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], []]

Output (one possible run):
[null, 1, 3, 2]
```

**Explanation:** The list is `1 -> 2 -> 3`. Each call to `getRandom()` returns one of
`1`, `2`, or `3`, each with probability `1/3`. The specific values above are just one
random outcome; a different run may return `[null, 2, 2, 1]`, etc.

### Example 2

```
Input:
["Solution", "getRandom", "getRandom"]
[[[7]], [], []]

Output:
[null, 7, 7]
```

**Explanation:** The list has a single node `7`. Every call must return `7` because it
is the only node (probability `1`).

## Hint

You do not need to know the list length in advance. Walk the list once and, at the
i-th node (1-indexed), keep it as your candidate answer with probability `1/i`. This is
**Reservoir Sampling** with `k = 1`.
