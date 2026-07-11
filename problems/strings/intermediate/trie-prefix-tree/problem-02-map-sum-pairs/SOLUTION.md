# Solution — Map Sum Pairs

## Brute Force

Keep a plain dictionary `store: dict[str, int]`.

- `insert(key, val)`: `store[key] = val` — O(L), and overwrite comes for free because dict
  assignment replaces the old value.
- `sum(prefix)`: iterate over every stored key, test `key.startswith(prefix)`, and add the
  matching values — **O(N · L)** per query where `N` is the number of keys.

This is perfectly acceptable for the tiny given limits (≤ 50 calls), but it does not scale
and does not use prefix structure. The Trie approach makes `sum` proportional only to the
prefix length.

## Optimal Approach (Trie with node totals)

Store each key along a Trie path, and on **every node along that path** keep a running
`total` equal to the sum of values of all keys passing through it. Then `sum(prefix)` is a
single O(L) walk to the prefix node, returning its `total`.

The subtlety is **overwrites**. If `"apple"` was inserted with 3 and is re-inserted with 7,
we must not double count. The clean trick is to track the delta:

```
delta = new_val - old_val_of_key   (old = 0 if the key is new)
```

Then add `delta` to the `total` of every node on the path. Adding the delta (rather than the
raw value) automatically corrects previously-stored contributions.

### Reference implementation

```python
class Node:
    __slots__ = ("children", "total")
    def __init__(self) -> None:
        self.children: dict[str, "Node"] = {}
        self.total = 0

class MapSum:
    def __init__(self) -> None:
        self.root = Node()
        self.vals: dict[str, int] = {}   # remembers each key's current value

    def insert(self, key: str, val: int) -> None:
        delta = val - self.vals.get(key, 0)
        self.vals[key] = val
        node = self.root
        for ch in key:
            node = node.children.setdefault(ch, Node())
            node.total += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return 0
            # (root.total is not used; we only ever read the prefix node's total)
        return node.total
```

**Why it is correct.** Node `total` is maintained as an invariant: it equals the sum of the
*current* values of every key whose path includes that node. On insert we shift each affected
node by exactly `new − old`, so keys inserted once contribute their value once and re-inserted
keys have their old contribution cancelled. The prefix node's `total` therefore equals the sum
over all keys sharing that prefix.

**Complexity.**
- `insert`: O(L) time, O(L) new nodes worst case.
- `sum`: O(P) time where `P = len(prefix)`, O(1) extra space.

## Key Insights & Edge Cases

- **Overwrite is the trap.** Naively adding `val` to node totals double counts on re-insert.
  Store the previous value per key and propagate the **delta**.
- **Storing sums on nodes** turns an O(N·L) prefix aggregation into an O(L) lookup — this is
  the core Trie augmentation idea (attach aggregate data to nodes).
- **Missing prefix** returns 0 (walk falls off the tree), which is the correct empty sum.
- **Alternative without a side dict:** you can subtract along the path using a per-key lookup
  during a second traversal, but the `vals` dict is the simplest way to recover the old value
  in O(L).
- Because values are positive here, totals never go negative, but the delta method also works
  correctly if values could be zero or negative.
