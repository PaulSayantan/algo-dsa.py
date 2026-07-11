# Merge Two Sorted Lists — Solution

## Brute Force

Walk both lists, collect all values into an array, sort the array, and rebuild a linked
list.

```python
def mergeTwoLists(list1, list2):
    vals = []
    for head in (list1, list2):
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

- **Time:** `O(N log N)` where `N = len(list1) + len(list2)`.
- **Space:** `O(N)` for the array and the new nodes.

It ignores the sorted structure and allocates brand-new nodes instead of splicing.

## Optimal Approach (Two-Pointer Merge)

Use a **dummy head** so we never special-case the first append, plus a `tail` pointer
that always points at the last node of the result so far. Advance a pointer along each
input list; each step, splice on the node with the smaller value.

```python
def mergeTwoLists(list1, list2):
    dummy = tail = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2   # attach the remaining tail
    return dummy.next
```

**Why it is correct.** The invariant is that everything already linked after `dummy` is
sorted and every value in it is `<=` the current `list1.val` and `list2.val`. Each step
appends the smallest unused node, preserving the invariant. When one list runs out, the
other list's remaining nodes are all `>=` everything appended and are themselves sorted,
so we can attach the whole remainder in `O(1)`.

**Step-by-step** on `list1 = 1->2->4`, `list2 = 1->3->4`:

| Compare | Append | Result so far |
| --- | --- | --- |
| `1` vs `1` -> take list1 (`<=`) | 1 | `1` |
| `2` vs `1` -> take list2 | 1 | `1->1` |
| `2` vs `3` -> take list1 | 2 | `1->1->2` |
| `4` vs `3` -> take list2 | 3 | `1->1->2->3` |
| `4` vs `4` -> take list1 | 4 | `1->1->2->3->4` |
| list1 empty -> attach list2 remainder `4` | | `1->1->2->3->4->4` |

- **Time:** `O(m + n)` — each node visited once.
- **Space:** `O(1)` — only the dummy node is allocated; existing nodes are reused.

## Key Insights & Edge Cases

- The **dummy head** removes the "is this the first node?" branch and gives a stable
  handle (`dummy.next`) to return.
- Using `<=` (not `<`) keeps the merge **stable** — equal values from `list1` come
  first — which matches the merge step of a stable merge sort.
- Attach the non-empty remainder in one assignment; do not keep looping node by node.
- Either or both lists empty: the `while` never runs and `tail.next` gets the non-empty
  list (or `None`), returning the correct head.
- No new value-carrying nodes are created — the problem asks you to splice existing
  nodes.
