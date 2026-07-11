# Merge k Sorted Lists — Solution

Let `k` be the number of lists and `N` the total number of nodes across all of them.

## Brute Force

Collect every value into an array, sort it, and rebuild one linked list.

```python
def mergeKLists(lists):
    vals = []
    for head in lists:
        while head:
            vals.append(head.val)
            head = head.next
    vals.sort()
    dummy = tail = ListNode()
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
```

- **Time:** `O(N log N)`.
- **Space:** `O(N)`.

A second, still-suboptimal idea is to fold the lists one at a time into an accumulator
using the two-list merge from Problem 2. That is `O(k * N)`: the accumulator is re-walked
on every merge, so early nodes are touched up to `k` times.

## Optimal Approach (Divide-and-Conquer Two-Pointer Merge)

Reuse the linear two-list merge as a subroutine, but combine the lists **pairwise in
rounds** instead of one at a time. Round 1 merges lists `(0,1), (2,3), ...`; round 2
merges those results pairwise; and so on. After `ceil(log2 k)` rounds a single list
remains.

```python
def mergeTwoLists(a, b):
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a if a else b
    return dummy.next

def mergeKLists(lists):
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            a = lists[i]
            b = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwoLists(a, b))
        lists = merged
    return lists[0]
```

**Why it is correct.** `mergeTwoLists` correctly merges any two sorted lists (Problem 2).
Merging is associative on sorted lists, so combining them in any binary-tree order yields
the same fully sorted list. Each round halves the number of lists, so the process
terminates with exactly one sorted list.

**Why it is faster.** Every node participates in one merge per round, and there are
`log k` rounds, giving `O(N log k)` total — a node is touched `log k` times instead of up
to `k` times.

**Step-by-step** on `lists = [1->4->5, 1->3->4, 2->6]`:

- Round 1: merge `1->4->5` with `1->3->4` -> `1->1->3->4->4->5`; the lone `2->6` carries
  over. Now `lists = [1->1->3->4->4->5, 2->6]`.
- Round 2: merge those two -> `1->1->2->3->4->4->5->6`.
- One list left -> return it.

### Alternative: min-heap

Push the head of each list into a min-heap keyed by value; repeatedly pop the smallest,
append it to the output, and push that node's successor. This also runs in `O(N log k)`
time (heap holds at most `k` nodes) with `O(k)` extra space. Use a tie-breaker (e.g. a
counter) so nodes with equal values never get compared directly.

- **Time:** `O(N log k)` for both the divide-and-conquer and heap variants.
- **Space:** `O(1)` extra for divide-and-conquer (ignoring recursion/round bookkeeping);
  `O(k)` for the heap.

## Key Insights & Edge Cases

- The two-list Two-Pointer Merge is the reusable primitive; the "k" version is just how
  you *schedule* those merges.
- Pairwise/divide-and-conquer beats sequential folding: `O(N log k)` vs `O(N k)` because
  each node is re-merged `log k` times rather than `k` times.
- `lists == []`: return `None` immediately.
- `lists == [[]]` or any `None` heads: `mergeTwoLists` treats `None` as an empty list, so
  they contribute nothing and the result is `None`/empty.
- Odd list count in a round: the unpaired list is carried into the next round unchanged
  (the `b = None` branch merges it with nothing).
- Keep the merge **stable** (`a.val <= b.val`) if you need to preserve relative order of
  equal elements across lists.
