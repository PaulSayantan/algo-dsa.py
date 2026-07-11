# Solution — Sort List

## Brute Force

Walk the list, collect all values into an array, sort the array with any
`O(n log n)` sort, then overwrite each node's `val` in order (or rebuild the
list).

- **Time:** `O(n log n)` for the array sort.
- **Space:** `O(n)` for the array — violates the `O(1)` follow-up.

## Optimal Approach (Merge Sort on the list)

Merge sort maps beautifully onto linked lists because it needs only sequential
access and node splicing, not indexing.

**1. Split into halves.** Use slow/fast pointers to find the middle, then cut the
list into two independent lists.

```python
def _split(self, head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None      # terminate the first half
    return head, mid
```

Starting `fast` at `head.next` ensures that for a 2-node list the split is
`1 | 1`, which guarantees progress and avoids infinite recursion.

**2. Recurse** on each half.

**3. Merge two sorted lists** by splicing nodes onto a dummy tail.

```python
def _merge(self, a, b):
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:        # <= keeps it stable
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b            # attach the remaining nodes
    return dummy.next

def sortList(self, head):
    if not head or not head.next:
        return head
    left, right = self._split(head)
    return self._merge(self.sortList(left), self.sortList(right))
```

**Why it is correct.** Base case: a list of length 0 or 1 is sorted. Inductive
step: `_split` produces two strictly smaller lists whose recursive sorts are
correct, and `_merge` interleaves two sorted lists into one sorted list (it always
splices the smaller current head). Because we relink existing nodes rather than
create new ones, no data is lost or duplicated.

**Complexity.**

- **Time:** `O(n log n)` — `log n` levels of splitting, `O(n)` merge work per
  level.
- **Space:** `O(1)` auxiliary for pointers (the merge reuses existing nodes),
  plus `O(log n)` recursion stack. A fully iterative bottom-up version reaches
  true `O(1)` including the stack.

## Key Insights & Edge Cases

- **Slow/fast split:** initialise `fast = head.next` (not `head`) so the left half
  is never empty for a 2-node list; otherwise you recurse forever.
- **Cut the list:** you must set `slow.next = None` to detach the first half.
  Forgetting this leaves the two halves still linked and corrupts the merge.
- **Merge by splicing**, not by copying values, to keep `O(1)` space.
- **Empty list / single node:** handled by the `not head or not head.next` base
  case — return `head` as is (Example 3).
- Stability via `a.val <= b.val` matters when nodes carry satellite data beyond
  `val`.
- For genuine `O(1)` total space, implement the **bottom-up** variant: merge runs
  of size 1, then 2, then 4, ... using a dummy head to stitch merged runs, which
  removes the recursion stack entirely.
