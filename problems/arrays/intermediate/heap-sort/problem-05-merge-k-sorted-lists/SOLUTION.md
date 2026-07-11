# Solution — Merge k Sorted Lists

## Brute Force

Collect all node values into one array, sort it, and rebuild a linked list.

```python
vals = []
for head in lists:
    while head:
        vals.append(head.val); head = head.next
vals.sort()
dummy = tail = ListNode()
for v in vals:
    tail.next = ListNode(v); tail = tail.next
return dummy.next
```

- **Time:** `O(N log N)` for `N` total nodes — the sort ignores that each list is
  already ordered.
- **Space:** `O(N)` for the value array.

It works but throws away the sortedness of the inputs. A heap exploits it.

## Optimal Approach (Min-heap over the current fronts)

At any moment the next node of the merged output is the **minimum among the
current front nodes** of the `k` lists — exactly the query a min-heap answers in
`O(log k)`. This is the "repeatedly extract the minimum" phase of heap sort,
generalized from one array to `k` streams.

1. Seed the heap with the head of every non-empty list.
2. Pop the smallest node, append it to the output list.
3. If that node has a `next`, push `next` into the heap.
4. Repeat until the heap is empty.

Because `ListNode` objects are not orderable, push a tuple whose first component
is `node.val` and add a strictly increasing counter as a tiebreaker so Python
never has to compare two nodes when their values are equal.

```python
import heapq

def mergeKLists(self, lists):
    heap = []
    counter = 0                              # unique tiebreaker
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, counter, head))
            counter += 1

    dummy = tail = ListNode()
    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1
    return dummy.next
```

- **Time:** `O(N log k)` — every one of the `N` nodes is pushed and popped once,
  and the heap never holds more than `k` items.
- **Space:** `O(k)` for the heap (the output reuses the existing nodes, so no
  extra node allocation).

**Why it is correct.** Invariant: the heap always holds at most one live front
node per list, and every value not yet output is `>=` the value output so far.
The popped minimum is the smallest among all current fronts, and since each list
is individually sorted, no un-enqueued node in that list is smaller than its
front. Therefore the popped node is the global minimum of all remaining values,
so appending it keeps the output sorted. Pushing its successor maintains the
one-front-per-list invariant.

### Worked trace on `[[1,4,5],[1,3,4],[2,6]]`

```
seed  -> heap fronts {1(A), 1(B), 2(C)}
pop 1(A) out:[1]      push 4(A)  -> {1(B),2(C),4(A)}
pop 1(B) out:[1,1]    push 3(B)  -> {2(C),3(B),4(A)}
pop 2(C) out:[1,1,2]  push 6(C)  -> {3(B),4(A),6(C)}
pop 3(B) out:[..3]    push 4(B)  -> {4(A),4(B),6(C)}
pop 4(A) out:[..4]    push 5(A)  -> {4(B),5(A),6(C)}
pop 4(B) out:[..4]    (B exhausted) -> {5(A),6(C)}
pop 5(A) out:[..5]    (A exhausted) -> {6(C)}
pop 6(C) out:[..6]    -> []
result -> 1,1,2,3,4,4,5,6
```

## Key Insights & Edge Cases

- **Heap size is `k`, not `N`.** Only one front per list lives in the heap at a
  time, so operations cost `O(log k)`, giving `O(N log k)` overall — better than
  the `O(N log N)` collect-and-sort when `k` is small.
- **Make nodes orderable.** Push `(val, counter, node)`; the unique `counter`
  breaks ties so Python never compares two `ListNode`s (which would raise
  `TypeError`).
- **Empty inputs:** `lists == []` and `lists == [None]` both leave the heap empty
  and return `None` (`dummy.next`). Skipping `None` heads at seed time is what
  makes this clean.
- **Divide-and-conquer alternative:** pairwise-merging lists in `log k` rounds
  also achieves `O(N log k)` with `O(1)` extra space and no heap; the heap
  version is more direct and extends naturally to a streaming / online setting.
- **Reuse nodes** rather than allocating new ones — the merged list simply
  re-links the existing `ListNode`s.
