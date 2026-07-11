# Swap Nodes in Pairs — Solution

## Brute Force

Iterate with a dummy node and a `prev` pointer, relinking each adjacent pair as you go.

```python
def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        # relink: prev -> second -> first -> (rest)
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next
```

- **Time:** `O(n)` — each node is touched a constant number of times.
- **Space:** `O(1)` — a few pointers.

This iterative version is optimal in space. The recursive version below trades `O(n)`
stack for a very clean expression of the "swap the front, recurse on the rest"
structure.

## Optimal Approach (Recursion)

Reduce the list to its first pair plus "everything after." Swap the first two nodes,
and let recursion handle the rest of the list; then splice the two results together.

```python
class Solution:
    def swapPairs(self, head):
        # Base case: 0 or 1 node left — nothing to swap.
        if head is None or head.next is None:
            return head

        first = head
        second = head.next

        # Recurse on the list starting after this pair, then relink:
        # second becomes the new front, first follows, and first points
        # at whatever the recursion returns for the remaining nodes.
        first.next = self.swapPairs(second.next)
        second.next = first

        return second   # new head of this swapped pair
```

**Why it is correct (induction on list length):**

- *Base case:* a list of length 0 or 1 has no pair to swap — return it unchanged.
- *Inductive step:* assume `swapPairs(second.next)` correctly swaps all pairs in the
  list of length `n - 2` that follows the first pair. We set `first.next` to that
  correct sublist and `second.next = first`, producing `second -> first -> (correctly
  swapped rest)`. Returning `second` makes it the head of this segment. Thus all pairs
  from the front onward are swapped.

**Step by step for `1 -> 2 -> 3 -> 4`:**

1. `swapPairs(1)`: `first=1`, `second=2`. `first.next = swapPairs(3)`.
2. `swapPairs(3)`: `first=3`, `second=4`. `first.next = swapPairs(None)`.
3. `swapPairs(None)` hits the base case → returns `None`.
4. Unwind step 2: `3.next = None`, `4.next = 3`, return `4`. Sublist: `4 -> 3`.
5. Unwind step 1: `1.next = 4` (the returned sublist head), `2.next = 1`, return `2`.
   Final list: `2 -> 1 -> 4 -> 3`. ✓

- **Time:** `O(n)` — one recursive call per pair, constant work each.
- **Space:** `O(n)` — recursion depth is `n/2` frames.

## Key Insights & Edge Cases

- **Two base cases in one check:** `head is None` (even length exhausted) and
  `head.next is None` (a lone trailing node). The lone node is *kept in place*, which
  is exactly why odd-length lists like `[1, 2, 3]` end with `3` unmoved.
- **The return value is `second`,** not `first` — after swapping, the second original
  node is the new head of the segment, and this new head is threaded up the call stack.
- **Order of relinking matters:** compute `first.next = swapPairs(second.next)` before
  `second.next = first`. If you set `second.next = first` first, you would lose the
  reference to `second.next` (the rest of the list).
- **Values are never touched** — only pointers are rearranged, satisfying the "do not
  modify values" constraint (important because in some variants the nodes carry more
  than a plain integer).
- Recursion depth is `n/2`; within the constraint (≤ 100 nodes) this is trivial, but as
  always the iterative form avoids the stack for very long lists.
