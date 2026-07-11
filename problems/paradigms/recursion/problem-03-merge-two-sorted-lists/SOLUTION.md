# Merge Two Sorted Lists — Solution

## Brute Force

Iteratively build the result with a dummy head and a `tail` pointer, repeatedly
appending the smaller of the two current heads.

```python
def mergeTwoLists(list1, list2):
    dummy = tail = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    tail.next = list1 or list2   # attach whatever remains
    return dummy.next
```

- **Time:** `O(m + n)` where `m`, `n` are the two list lengths.
- **Space:** `O(1)` — nodes are spliced in place, only a dummy and a tail pointer used.

This iterative version is optimal in space. The recursive version below has the same
time but uses `O(m + n)` stack space; it is included because it expresses the merge's
self-similar structure especially cleanly.

## Optimal Approach (Recursion)

Observe the self-similar structure: the merged list's first node is whichever of the
two heads is smaller. After choosing it, the *rest* of the merged list is exactly the
merge of that list's tail with the other list — a strictly smaller instance of the
same problem.

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        # Base cases: if one list is empty, the merge is the other list.
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Recursive case: pick the smaller head, then merge the remainder.
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

**Why it is correct:** Each call outputs the globally smallest remaining node (both
lists are sorted, so the smaller of the two heads is `<=` every other remaining
element). By induction, the recursive call correctly merges everything after that node,
so linking it as `chosen.next` produces a fully sorted merge. Every call consumes one
node, so the combined length strictly decreases toward a base case.

**Step by step for `list1 = 1 -> 2`, `list2 = 1 -> 3`:**

1. `1 <= 1`, so take `list1`'s `1`; its next = merge(`2`, `1 -> 3`).
2. `2 > 1`, so take `list2`'s `1`; its next = merge(`2`, `3`).
3. `2 <= 3`, so take `2`; its next = merge(`None`, `3`).
4. Base case: `list1 is None` → return `3`. Unwinding gives `2 -> 3`, then
   `1 -> 2 -> 3`, then `1 -> 1 -> 2 -> 3`.

- **Time:** `O(m + n)` — one call consumes one node; total calls = total nodes.
- **Space:** `O(m + n)` recursion stack (vs. `O(1)` for the iterative form).

## Key Insights & Edge Cases

- **Two base cases**, one per list, handle exhaustion *and* the both-empty case: if
  `list1` is `None` return `list2` (which may itself be `None`), and vice versa.
- **Use `<=`, not `<`,** when comparing heads to keep the merge **stable** and to
  handle equal values without dropping either — either choice is sorted, but `<=`
  preserves the relative order of equal elements from `list1`.
- **Nodes are reused, not copied** — the result splices the existing nodes, matching
  the problem's requirement.
- **Stack depth is `m + n`** in the worst case (fully interleaved lists). Within the
  constraint (≤ 50 + 50 nodes) this is trivial, but for very long lists the iterative
  version avoids the deep stack.
- This recursive merge is precisely the **combine step** reused inside merge sort,
  which is why it doubles as great recursion practice.
