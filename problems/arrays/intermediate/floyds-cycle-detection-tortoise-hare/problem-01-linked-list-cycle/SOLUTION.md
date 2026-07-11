# Solution — Linked List Cycle

## Brute Force

Walk the list node by node and remember every node you have seen in a hash set
(store node identities/references, not values, since values may repeat). If you
ever reach a node already in the set, there is a cycle; if you reach `None`,
there is not.

```python
def hasCycle(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False
```

- **Time:** O(n) — each node visited once.
- **Space:** O(n) — the hash set can hold every node.

This is correct and simple, but it violates the O(1) memory requirement.

## Optimal Approach — Floyd's Cycle Detection (Tortoise & Hare)

Use two pointers starting at the head:

- `slow` moves **one** node per step.
- `fast` moves **two** nodes per step.

Advance both until either `fast` (or `fast.next`) becomes `None` — meaning the
list ends, so no cycle — or `slow is fast`, meaning they collided inside a
cycle.

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

### Why it is correct

- **No cycle:** the fast pointer reaches the end (`None`) in about n/2 steps and
  the loop exits returning `False`.
- **Cycle exists:** once both pointers are inside the loop, consider the gap
  between them measured *along the cycle* in the direction of travel. Each step
  the fast pointer gains exactly one position on the slow pointer (fast moves 2,
  slow moves 1, net +1). Since the gap is a non-negative integer less than the
  loop length and it strictly decreases by 1 every step (mod loop length), it
  must eventually hit 0 — i.e. they land on the same node. The fast pointer can
  never "jump over" the slow one without landing on it, precisely because the
  gap shrinks by 1 (not 2) each step.

### Step-by-step on `[3, 2, 0, -4]` with tail linking to index 1

Nodes by index: `0:3 -> 1:2 -> 2:0 -> 3:-4 -> (back to index 1)`.

| Step | slow (index) | fast (index) |
|------|--------------|--------------|
| start| 0            | 0            |
| 1    | 1            | 2            |
| 2    | 2            | 1 (wrapped)  |
| 3    | 3            | 3            |

At step 3 `slow is fast` (both at index 3), so we return `True`.

- **Time:** O(n). Before entering the cycle the fast pointer takes ~n steps to
  reach it; once both are inside, they meet within one loop length. Total work
  is linear.
- **Space:** O(1) — just two pointers.

## Key Insights & Edge Cases

- **Empty list / single node with `next = None`:** the `while fast and
  fast.next` guard is false immediately, so we correctly return `False`.
- **Compare by identity, not value.** Use `slow is fast` (reference equality).
  Node values can repeat even without a cycle.
- **Guard both `fast` and `fast.next`** before doing `fast.next.next`, or you
  risk an `AttributeError` on `None`.
- **Initialize both pointers at `head`.** Starting them together keeps the
  loop's meeting-point math clean (and is required for the follow-up problem
  that finds the cycle's entry node).
