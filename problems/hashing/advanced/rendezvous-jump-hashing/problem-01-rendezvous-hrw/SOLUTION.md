# Rendezvous (HRW) get_node — Solution

## Optimal Approach

Score every (node, key) pair with a fixed hash and take the argmax. No ring, no virtual nodes — membership changes only flip the winner for keys whose top score belonged to the changed node.

### Reference implementation

```python
class RendezvousHash:
    """Highest-Random-Weight (HRW) hashing with a FIXED arithmetic score."""

    _MASK = 0xFFFFFFFFFFFFFFFF

    def __init__(self):
        self._nodes = []

    def add_node(self, name):
        if name not in self._nodes:
            self._nodes.append(name)

    def _score(self, node, key):
        h = 1469598103934665603
        for ch in (node + ":" + str(key)):
            h ^= ord(ch)
            h = (h * 1099511628211) & self._MASK
        h ^= h >> 33
        h = (h * 0xFF51AFD7ED558CCD) & self._MASK
        h ^= h >> 33
        h = (h * 0xC4CEB9FE1A85EC53) & self._MASK
        h ^= h >> 33
        return h

    def get_node(self, key):
        best, best_score = None, -1
        for node in sorted(self._nodes):     # sorted -> deterministic tie handling
            s = self._score(node, key)
            if s > best_score:
                best_score, best = s, node
        return best
```

### Complexity

get_node: O(N) scores for N nodes; O(1) extra memory.

## Key Insights & Edge Cases

HRW gives naturally balanced assignment (each key independently picks a uniformly-random-looking winner) and minimal disruption without maintaining ring state. The catch versus jump hashing is the O(N)-per-lookup cost, which matters only when N is large.
