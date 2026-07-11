# Linked List Random Node

**Difficulty:** Medium

**Source:** LeetCode 382 — Linked List Random Node

## Description

Given a singly linked list, return the value of a **random node** from the list. Each node
must have the **same probability** of being chosen.

Implement the `Solution` class:

- `Solution(head)` — Initializes the object with the head of the singly linked list.
- `getRandom()` — Chooses a node uniformly at random from the list and returns its value.
  All nodes must be equally likely to be chosen.

**Follow-up:** What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space (i.e., without first copying the
list into an array and without precomputing or storing the length)?

## Constraints

- The number of nodes in the linked list is in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- At most `10^4` calls will be made to `getRandom`.

## Examples

### Example 1

```
Input:
["Solution", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], []]

Output:
[null, 1, 3, 2]
```

**Explanation:**
- `Solution([1, 2, 3])` builds the object over the list `1 -> 2 -> 3`.
- `getRandom()` returns one of `1`, `2`, `3`, each with probability `1/3`; shown returning `1`.
- `getRandom()` again returns a uniform choice, e.g. `3`.
- `getRandom()` again returns a uniform choice, e.g. `2`.

The specific values vary between runs; the requirement is only that each of the three
values appears with probability `1/3`.

### Example 2

```
Input:
["Solution", "getRandom", "getRandom"]
[[[9]], [], []]

Output:
[null, 9, 9]
```

**Explanation:** With a single node, every `getRandom()` must return `9` (probability 1).

## Hint

Use **Randomization** via *reservoir sampling* with reservoir size 1: stream through the
nodes once and, at the i-th node (1-indexed), replace the current pick with this node's
value with probability `1/i`. This needs only one pass and O(1) extra memory — perfect when
the length is unknown.
