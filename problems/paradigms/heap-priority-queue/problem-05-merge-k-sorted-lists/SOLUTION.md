# Merge k Sorted Lists — Solution

Let `N` be the **total** number of nodes across all lists and `k` the number of lists.

## Brute Force

Collect every node's value into one array, sort it, and rebuild a linked list.

- **Time:** `O(N log N)` — dominated by the sort of all `N` values.
- **Space:** `O(N)` for the array (plus the output list).

This throws away the fact that each input list is *already sorted*; we re-sort from
scratch. It works but does more comparisons than necessary.

## Optimal Approach (Heap / Priority Queue)

**Idea:** This is a classic **`k`-way merge**. At any moment the next node in the merged
output is the smallest among the current *front* nodes of the `k` lists. A **min-heap of
size `k`** (one entry per non-empty list) exposes that global minimum in `O(log k)`.

Procedure:

1. Push the head of every non-empty list into the heap.
2. Pop the minimum, append it to the output, and push its `next` (if any) back.
3. Repeat until the heap is empty.

Because two `ListNode`s aren't directly comparable, key the heap on `(val, index, node)`
— the unique `index` breaks ties on equal `val` so Python never tries to compare nodes.

```python
import heapq

def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

**Why it is correct:** Invariant — the heap always holds exactly one node per list that
still has unconsumed elements, and each is the smallest *unmerged* value of its list
(since each list is sorted). Therefore the heap's minimum is the smallest unmerged value
*overall*, so appending it and advancing that list preserves both the sortedness of the
output and the invariant. The process consumes every node exactly once.

- **Time:** `O(N log k)` — each of the `N` nodes is pushed and popped once, at `O(log k)`
  per operation since the heap never exceeds `k` entries.
- **Space:** `O(k)` for the heap (we splice existing nodes, so no extra node allocation).

### Alternative — divide & conquer

Pairwise-merge lists (merge `k` lists into `k/2`, then `k/4`, ...) using the standard
two-list merge. Also `O(N log k)` time and `O(1)` extra space (recursion aside), with no
heap needed — a good answer to mention alongside the heap.

## Key Insights & Edge Cases

- **Heap size is `k`, not `N`:** we only ever hold one front node per list, giving the
  `log k` (not `log N`) factor — the whole reason this beats the brute-force sort.
- **Tie-break key:** include a unique counter/index in the tuple (`(val, i, node)`) so
  equal values never force a comparison of `ListNode` objects (which would raise
  `TypeError`).
- **Empty inputs:** `lists == []` or lists full of `None` → the heap starts empty → return
  `None`. Skip `None` heads when seeding.
- **Splice, don't copy:** relink the existing nodes rather than allocating new ones for
  `O(k)` extra space instead of `O(N)`.
- **Single list** passes straight through; **one very long list among many short ones**
  still costs only `O(log k)` per node.
