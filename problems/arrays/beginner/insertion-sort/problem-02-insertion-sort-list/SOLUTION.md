# Solution — Insertion Sort List

## Brute Force

Copy every node's value into an array, sort the array with any method, then overwrite the
node values in order. This ignores the spirit of the exercise (and of insertion sort) but
does produce a correct result.

- Time: `O(n log n)` if you use a library sort, or `O(n^2)` if you insertion-sort the array.
- Space: `O(n)` for the value array.

## Optimal Approach (Insertion Sort on the list)

We build a **separate sorted list** in place using the original nodes, fronted by a `dummy`
node so that inserting before the current head needs no special case.

Walk the input list one node at a time. For each `curr`:

1. Save `next_node = curr.next` (we are about to detach `curr`).
2. Find the insertion point in the sorted list: start at `dummy` and advance a pointer `prev`
   while `prev.next` exists and `prev.next.val < curr.val`. Stop when `prev.next` is the first
   node whose value is `>=` `curr.val` (or `None`).
3. Splice `curr` in: `curr.next = prev.next; prev.next = curr`.
4. Move on to `next_node`.

Return `dummy.next`.

**Why it is correct.** Invariant: the chain hanging off `dummy` is always sorted and contains
exactly the nodes processed so far. Step 2 locates the unique gap where `curr` keeps the list
sorted (the first spot where the following value is not smaller), and step 3 links it there.
After every input node has been consumed, `dummy.next` is the full sorted list.

**Stability.** The scan advances only while `prev.next.val < curr.val` (strict `<`), so `curr`
is inserted *after* any node with an equal value that was processed earlier — original order
of equal keys is preserved.

**Small optimization.** If `curr.val >= tail.val` (the last sorted node), you can append
without rescanning from `dummy`. Tracking a `tail`/`prev` cursor helps on nearly-sorted input.

```python
def insertionSortList(self, head):
    dummy = ListNode()
    curr = head
    while curr:
        next_node = curr.next
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        curr.next = prev.next
        prev.next = curr
        curr = next_node
    return dummy.next
```

- Time: `O(n^2)` worst case (reverse-sorted forces a full scan each time); `O(n)` best case
  when already sorted *if* you keep a tail pointer and append.
- Space: `O(1)` — no new nodes are allocated; only pointers are rewired.

## Key Insights & Edge Cases

- **Dummy head removes edge cases.** Inserting a new minimum at the front is handled by the
  same code as any other insertion, because `prev` can be `dummy`.
- **Detach before searching.** Save `curr.next` before rewiring `curr.next`, or you will lose
  the rest of the unsorted list.
- **Restart the scan from `dummy`.** Each new element may belong anywhere, including before
  the current sorted head, so the search pointer must start at `dummy` unless you add the
  tail-append shortcut.
- **Single node / empty list.** `head` with 0 or 1 nodes returns immediately correct;
  `dummy.next` yields the same list.
- **Do not compare against a stale pointer.** Reassign `prev` fresh inside the outer loop.
