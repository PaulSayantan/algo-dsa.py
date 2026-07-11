# Reverse Linked List — Solution

## Brute Force

The straightforward iterative approach walks the list once, re-pointing each node's
`next` to its predecessor using three pointers (`prev`, `curr`, `nxt`).

```python
def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

- **Time:** `O(n)` — one pass over the list.
- **Space:** `O(1)` — only three pointers.

This is optimal in space and is what you would ship in production. But the problem is a
classic vehicle for practicing recursion on a recursively defined data structure, so
the recursive version below is the instructive one.

## Optimal Approach (Recursion)

Think of the list as `head -> (rest)`. If you *trust* the recursive call to fully
reverse `rest`, you get back the new head of the reversed tail — and crucially,
`head.next` is now the **last** node of that reversed portion. So you only need to make
that last node point back at `head`, and cut `head`'s old forward link.

```python
class Solution:
    def reverseList(self, head):
        # Base case: empty list or single node reverses to itself.
        if head is None or head.next is None:
            return head

        # Recurse on the rest of the list; new_head is the head of the
        # fully reversed tail. head.next is still the *old* second node,
        # which is now the tail of the reversed portion.
        new_head = self.reverseList(head.next)

        head.next.next = head   # make the reversed tail point back at head
        head.next = None        # head becomes the new last node

        return new_head          # propagate the new head unchanged up the stack
```

**Why it is correct (induction on list length):**

- *Base case:* a list of length 0 or 1 is its own reverse — returned directly.
- *Inductive step:* assume `reverseList(head.next)` correctly reverses the tail of
  length `k`. The returned `new_head` is the correct new head. The old node `head.next`
  is the tail's last node; setting `head.next.next = head` appends `head` after it, and
  `head.next = None` terminates the list. The result is the tail reversed, followed by
  `head` — exactly the whole list reversed. `new_head` is passed up unchanged.

**Step by step for `1 -> 2 -> 3`:**

1. `reverseList(1)` calls `reverseList(2)` calls `reverseList(3)`.
2. `reverseList(3)` hits the base case and returns node `3` as `new_head`.
3. Back in `reverseList(2)`: `head=2`, `head.next=3`. Do `3.next = 2`, `2.next = None`.
   List tail is now `3 -> 2`. Return `new_head = 3`.
4. Back in `reverseList(1)`: `head=1`, `head.next=2`. Do `2.next = 1`, `1.next = None`.
   List is now `3 -> 2 -> 1`. Return `new_head = 3`.

- **Time:** `O(n)` — one recursive call per node.
- **Space:** `O(n)` — the recursion stack holds one frame per node (unlike the `O(1)`
  iterative version).

## Key Insights & Edge Cases

- **The base case guards both empty and single-node lists** (`head is None or
  head.next is None`). Forgetting the `head is None` check crashes on an empty list.
- **`new_head` is threaded up unchanged** through every frame — it is decided once at
  the deepest call (the original last node) and never reassigned as the stack unwinds.
- **The relink is a two-liner** and order matters conceptually: `head.next.next = head`
  uses `head.next` before you overwrite `head.next = None`.
- **Stack depth is `O(n)`** — for the constraint's max of 5000 nodes this is fine, but
  on a list of millions of nodes the recursive version risks a stack overflow while the
  iterative version does not. This tradeoff is the key lesson: recursion trades stack
  space for structural clarity.
