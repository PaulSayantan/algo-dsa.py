# Solution — Kth Largest Element in a Stream

## Brute Force

Keep every element in a list. On each `add`, append the value and sort (or scan for
the k-th largest).

- Sort each time: `O(n log n)` per `add`, so `O(m * n log n)` overall for `m` calls.
- Keeping the list sorted with `bisect.insort` and indexing `arr[-k]`: the index is
  `O(1)` but the insertion shifts elements, costing `O(n)` per `add`, i.e. `O(m*n)`.

Both are too slow for `10^4` adds against a stream that also grows to `10^4`.

A cleaner classic answer for *this exact problem* is a **min-heap of size k**: keep
only the k largest seen so far, and the root is the answer in `O(log k)` per add.
That is optimal for k-th largest specifically. We use an order-statistics tree
instead because it generalizes: it can answer *any* order statistic, supports
arbitrary deletes, and directly demonstrates the `select` operation the rest of this
folder builds on.

## Optimal Approach (Order-Statistics Tree)

Maintain the whole stream as a **dynamic multiset** in a balanced BST where each
node stores `size` = number of stored keys in its subtree (duplicates counted). A
treap (BST + random priorities) is the easiest self-balancing choice to code.

Node fields: `key`, random `pr`iority, `left`, `right`, `count` (how many copies of
this exact key), and `size` = `count + size(left) + size(right)`.

**Why the answer is a select.** If the multiset currently holds `n` keys, the k-th
**largest** is the `(n - k + 1)`-th **smallest**. `select(t)` descends the tree
using subtree sizes:

```
select(node, t):            # 1-indexed
    ls = size(node.left)
    if t <= ls:                 return select(node.left, t)
    if t <= ls + node.count:    return node.key      # t falls inside this key
    return select(node.right, t - ls - node.count)
```

`insert` walks down comparing keys, bumps `count` if the key already exists, creates
a leaf otherwise, and bubbles the new node up with rotations while its priority
exceeds its parent's. Every rotation and every return recomputes `size` from the
children in `O(1)`, so sizes stay correct automatically.

**Correctness.** The BST ordering guarantees that for any node, everything in the
left subtree is smaller and everything in the right subtree is larger. Therefore
`size(left)` keys precede the node in sorted order; `select` uses this to route to
the unique key at position `t`. Treap rotations preserve the BST ordering and only
change shape, and the size field is a pure function of the (post-rotation) children,
so it is always consistent. Because priorities are random, the expected tree height
is `O(log n)`, making insert and select `O(log n)` expected.

**Per `add`:**
1. `insert(val)` — `O(log n)`.
2. `n = root.size`; return `select(root, n - k + 1)` — `O(log n)`.

Total: `O((n_0 + m) log(n_0 + m))` time, `O(n_0 + m)` space, where `n_0` is the
initial size and `m` the number of adds.

Reference core (treap):

```python
import random

class Node:
    __slots__ = ("key", "pr", "left", "right", "size", "count")
    def __init__(self, key):
        self.key = key; self.pr = random.random()
        self.left = self.right = None
        self.size = 1; self.count = 1

def _sz(n): return n.size if n else 0
def _upd(n): n.size = n.count + _sz(n.left) + _sz(n.right)
def _rot_r(n):
    l = n.left; n.left = l.right; l.right = n; _upd(n); _upd(l); return l
def _rot_l(n):
    r = n.right; n.right = r.left; r.left = n; _upd(n); _upd(r); return r

def insert(n, key):
    if n is None: return Node(key)
    if key == n.key:
        n.count += 1; n.size += 1; return n
    if key < n.key:
        n.left = insert(n.left, key)
        if n.left.pr > n.pr: n = _rot_r(n)
    else:
        n.right = insert(n.right, key)
        if n.right.pr > n.pr: n = _rot_l(n)
    _upd(n); return n

def select(n, t):                      # t is 1-indexed
    ls = _sz(n.left)
    if t <= ls: return select(n.left, t)
    if t <= ls + n.count: return n.key
    return select(n.right, t - ls - n.count)

class KthLargest:
    def __init__(self, k, nums):
        self.k = k; self.root = None
        for v in nums: self.root = insert(self.root, v)
    def add(self, val):
        self.root = insert(self.root, val)
        return select(self.root, self.root.size - self.k + 1)
```

## Key Insights & Edge Cases

- **k-th largest = (n - k + 1)-th smallest.** Do the index arithmetic on the live
  size after each insert, not on the initial size.
- **Duplicates matter.** This is a multiset, not a set. Store a `count` per key (or
  allow equal keys to route right consistently); example 1 relies on the second `5`
  and the extra `4` being counted.
- **Empty initial `nums`.** With `k = 1` and no initial elements (example 2), the
  first `add` produces a size-1 tree and `select(1)` returns that lone value.
- **The problem guarantees `size >= k` at query time**, so `n - k + 1 >= 1` always;
  no need to guard against an out-of-range select.
- If the problem only ever asked for k-th largest (no deletes, fixed k), a size-k
  min-heap is simpler and faster (`O(log k)`); reach for the OST when you need
  arbitrary order statistics, deletions, or the actual ranks.
