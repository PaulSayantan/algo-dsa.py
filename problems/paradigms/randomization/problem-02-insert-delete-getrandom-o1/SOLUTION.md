# Insert Delete GetRandom O(1) — Solution

## Brute Force

Store the elements in a plain list:

- `insert` — scan the list for `val` (O(n)); append if absent.
- `remove` — scan for `val` (O(n)); delete it with `list.remove`, which shifts the tail
  (another O(n)).
- `getRandom` — pick `list[random(0, len-1)]` in O(1).

Sampling is already uniform and O(1), but `insert` and `remove` are **O(n)** because of the
linear scan and the shifting on deletion. Over `2 * 10^5` operations this is too slow.

Alternatively, a hash set gives O(1) `insert`/`remove` but there is **no O(1) uniform random
access** into a Python `set` (you cannot index it; converting to a list is O(n) per call).
So neither structure alone gives all three operations in O(1).

## Optimal Approach (Randomization + array/hashmap swap-delete)

The insight: uniform random selection in O(1) needs contiguous integer indices (an array),
while membership and O(1) deletion need a hash map. Combine both.

Maintain:
- `vals` — a dynamic array (Python list) holding the current elements in arbitrary order.
- `idx` — a dict mapping each value to its position in `vals`.

```python
class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.idx = {}

    def insert(self, val):
        if val in self.idx:
            return False
        self.idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        if val not in self.idx:
            return False
        i = self.idx[val]
        last = self.vals[-1]
        # Move the last element into the hole at index i.
        self.vals[i] = last
        self.idx[last] = i
        # Pop the (now duplicated) last slot and drop val from the map.
        self.vals.pop()
        del self.idx[val]
        return True

    def getRandom(self):
        return self.vals[random.randint(0, len(self.vals) - 1)]
```

### Why deletion is O(1)

The trick is the **swap-with-last** removal. Deleting from the middle of an array normally
costs O(n) because everything after the hole shifts left. Instead, we overwrite the hole
with the array's *last* element, update that element's stored index, and then `pop()` the
last slot — `list.pop()` with no argument is O(1). Order does not matter for a set, so this
reshuffling is harmless.

### Why getRandom is uniform and O(1)

At all times `vals` holds exactly the current elements packed into indices `0..n-1` with no
gaps. Choosing `random.randint(0, n-1)` picks each index with probability `1/n`, and each
index holds a distinct element, so every element is returned with probability `1/n` — exactly
uniform. Indexing a list is O(1).

### Complexity

- `insert`: **average O(1)** (dict lookup/insert + amortized O(1) append).
- `remove`: **average O(1)** (dict lookup, one overwrite, O(1) `pop`, dict delete).
- `getRandom`: **O(1)** (one RNG draw + one index).
- Space: **O(n)** for the array plus the map.

("Average" reflects hash-map expected-O(1) operations and amortized list growth.)

## Key Insights & Edge Cases

- **Two structures, each covering the other's weakness:** the array gives O(1) uniform
  sampling; the map gives O(1) membership and locates the element to delete.
- **Update the moved element's index.** The most common bug is forgetting
  `self.idx[last] = i` after moving `last` into the hole — the map then points to a stale
  slot and later removals corrupt the structure.
- **Removing the last element / single element.** When `val` is already the last element,
  `i == len-1`; the overwrite is a self-assignment and `pop()` removes it correctly. Handle
  this uniformly (no special case needed) as long as you `del self.idx[val]` after, or delete
  before checking — just be careful the map ends consistent.
- **Duplicates are not allowed** in this problem, so the value -> index map is well defined.
  (LeetCode 381, "…allow duplicates", stores a *set of indices* per value instead.)
- **getRandom precondition:** guaranteed non-empty, so no empty-array guard is required, but
  a defensive check avoids an out-of-range RNG call if the invariant is ever broken.
