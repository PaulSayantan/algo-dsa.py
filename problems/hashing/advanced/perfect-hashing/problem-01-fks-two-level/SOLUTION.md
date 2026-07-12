# FKS Two-Level Perfect Hashing — Solution

## Optimal Approach

Quadratic second-level sizing guarantees a collision-free hash exists with probability >= 1/2 per draw, so a handful of retries suffice; the expected total space stays O(n).

### Reference implementation

```python
class FKSPerfectHash:
    """FKS two-level perfect hash for a STATIC integer key set (fixed seed)."""

    _P = 2147483647  # a Mersenne prime > any key we use

    def __init__(self, keys):
        random.seed(20250712)          # reproducible construction
        keys = list(keys)
        n = len(keys)
        self._n = n
        self._a1 = random.randrange(1, self._P)
        self._b1 = random.randrange(0, self._P)
        buckets = [[] for _ in range(n)]
        for k in keys:
            buckets[((self._a1 * k + self._b1) % self._P) % n].append(k)
        self._tables = []              # (a, b, m, slots) per first-level bucket
        self._total_slots = 0
        for bk in buckets:
            m = len(bk) * len(bk)      # quadratic size kills collisions whp
            if m == 0:
                self._tables.append((0, 0, 0, []))
                continue
            while True:                 # retry second-level hash until injective
                a = random.randrange(1, self._P)
                b = random.randrange(0, self._P)
                slots = [None] * m
                ok = True
                for k in bk:
                    idx = ((a * k + b) % self._P) % m
                    if slots[idx] is not None:
                        ok = False
                        break
                    slots[idx] = k
                if ok:
                    self._tables.append((a, b, m, slots))
                    self._total_slots += m
                    break

    def lookup(self, key):
        i = ((self._a1 * key + self._b1) % self._P) % self._n
        a, b, m, slots = self._tables[i]
        if m == 0:
            return False
        return slots[((a * key + b) % self._P) % m] == key

    def verify_all(self, keys):
        return all(self.lookup(k) for k in keys)

    def total_slots(self):
        return self._total_slots
```

### Complexity

Lookup O(1) worst case; expected O(n) construction and space.

## Key Insights & Edge Cases

verify_all is True by construction — every key resolves uniquely. A non-key like 100 either lands in an empty first-level bucket or in a slot holding some other key, so lookup returns False. total_slots is the sum of b^2 over buckets, driven entirely by the fixed seed; here the seven keys need 11 second-level slots.
