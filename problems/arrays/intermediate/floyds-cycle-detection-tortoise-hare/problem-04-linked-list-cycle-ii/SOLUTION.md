# Solution — Linked List Cycle II

## Brute Force

Traverse the list, recording each visited node in a hash set. The first node you
encounter that is already in the set is the cycle's entry point. If you reach
`None`, return `None`.

```python
def detectCycle(head):
    seen = set()
    node = head
    while node:
        if node in seen:
            return node
        seen.add(node)
        node = node.next
    return None
```

- **Time:** O(n).
- **Space:** O(n) — violates the O(1) memory constraint.

## Optimal Approach — Floyd's Cycle Detection (Tortoise & Hare)

Two phases. Phase 1 detects the cycle and finds *a* meeting point; phase 2
converts that meeting point into the actual entry node.

```python
def detectCycle(head):
    slow = fast = head
    # Phase 1: find a meeting point (or prove no cycle).
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None            # fast hit the end -> no cycle
    if not (fast and fast.next):
        return None            # safety: loop exited via condition, no cycle

    # Phase 2: find the entrance.
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow
```

A cleaner structure uses an explicit flag:

```python
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:                 # cycle found
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

### Why phase 2 finds the entrance

Let `x` = number of nodes from the head to the cycle entrance, `y` = distance
from the entrance to the meeting point (measured along the cycle in travel
direction), and `C` = cycle length. At the phase-1 meeting, slow has moved
`x + y` steps and fast has moved `2(x + y)`. Fast is an integer number of loops
ahead of slow, so `2(x + y) - (x + y) = x + y` is a multiple of `C`; write
`x + y = kC`, hence `x = kC - y`.

Now reset one pointer to the head and keep the other at the meeting point, and
step both by 1. After exactly `x` steps the head pointer reaches the entrance.
The other pointer, starting `y` past the entrance, moves `x = kC - y` steps —
which brings it `kC` past the entrance, i.e. back to the entrance after `k`
loops. They meet precisely at the cycle's entry node.

### Step-by-step on `[3, 2, 0, -4]`, tail -> index 1

Nodes by index: `0:3 -> 1:2 -> 2:0 -> 3:-4 -> (back to 1)`. Entrance is index 1.

Phase 1 (both start at index 0):

| Step | slow (idx) | fast (idx) |
|------|------------|------------|
| 1    | 1          | 2          |
| 2    | 2          | 1          |
| 3    | 3          | 3          |

Meet at index 3. Phase 2 (`slow` back to index 0):

| Step | slow (idx) | fast (idx) |
|------|------------|------------|
| init | 0          | 3          |
| 1    | 1          | 1          |

They meet at index 1 — the node with value `2`, the correct cycle entrance.

- **Time:** O(n) across both phases.
- **Space:** O(1).

## Key Insights & Edge Cases

- **No cycle:** the `while fast and fast.next` guard fails and we return `None`
  (empty list and single acyclic node are handled the same way).
- **Reset to `head`, not to the meeting point,** at the start of phase 2. The
  distance identity `x = kC - y` is exactly what makes a head-anchored pointer
  and the meeting-point pointer converge at the entrance.
- **Use identity comparison (`is`)** since values may repeat.
- **Self-loop / cycle of length 1** (tail points to itself) works: phase 1 meets
  at that node, and phase 2 immediately agrees there if it is the head, or walks
  down to it otherwise.
