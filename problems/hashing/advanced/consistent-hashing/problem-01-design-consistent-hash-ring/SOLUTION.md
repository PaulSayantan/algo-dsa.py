# Design a Consistent Hash Ring — Solution

## Optimal Approach

Place `vnodes` hashed positions per server in a sorted structure. A lookup binary-searches for the first position >= hash(key), wrapping to the smallest position at the end of the ring.

### Reference implementation

```python
class ConsistentHashRing:
    """A consistent-hash ring with virtual nodes and a FIXED arithmetic hash."""

    _MASK = 0xFFFFFFFFFFFFFFFF

    def __init__(self, vnodes=3):
        self._vnodes = vnodes
        self._ring = {}          # ring position -> server name
        self._sorted = []        # sorted ring positions
        self._nodes = set()

    def _hash(self, s):
        # 64-bit FNV-1a followed by a murmur3-style finalizer for good spread.
        h = 1469598103934665603
        for ch in str(s):
            h ^= ord(ch)
            h = (h * 1099511628211) & self._MASK
        h ^= h >> 33
        h = (h * 0xFF51AFD7ED558CCD) & self._MASK
        h ^= h >> 33
        h = (h * 0xC4CEB9FE1A85EC53) & self._MASK
        h ^= h >> 33
        return h

    def add_node(self, name):
        if name in self._nodes:
            return
        self._nodes.add(name)
        for v in range(self._vnodes):
            pos = self._hash(name + "#" + str(v))
            while pos in self._ring:      # probe on the rare collision
                pos = (pos + 1) & self._MASK
            self._ring[pos] = name
            bisect.insort(self._sorted, pos)

    def remove_node(self, name):
        if name not in self._nodes:
            return
        self._nodes.discard(name)
        for pos in sorted(p for p, nm in self._ring.items() if nm == name):
            del self._ring[pos]
            i = bisect.bisect_left(self._sorted, pos)
            self._sorted.pop(i)

    def get_node(self, key):
        if not self._sorted:
            return None
        i = bisect.bisect_left(self._sorted, self._hash(key))
        if i == len(self._sorted):        # wrap around the ring
            i = 0
        return self._ring[self._sorted[i]]

    def num_vnodes(self):
        return len(self._sorted)

    def analyze_removal(self, keys, node):
        before = {k: self.get_node(k) for k in keys}
        self.remove_node(node)
        moved = 0
        only_its_keys = True
        for k in keys:
            if self.get_node(k) != before[k]:
                moved += 1
                if before[k] != node:
                    only_its_keys = False
        self.add_node(node)               # restore for further queries
        return [moved, only_its_keys]
```

### Complexity

add/remove_node: O(vnodes * log M) to insert/delete positions; get_node: O(log M) binary search, where M = total virtual nodes.

## Key Insights & Edge Cases

num_vnodes() is simply servers x vnodes (here 3 x 3 = 9). Because each key deterministically hashes to one ring position and is served by the next node clockwise, the same key always resolves to the same server across processes — the whole point of a *fixed* hash. Virtual nodes smooth the arc-length distribution so load is balanced.
