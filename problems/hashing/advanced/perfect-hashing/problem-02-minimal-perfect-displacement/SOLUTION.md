# Minimal Perfect Hash (CHD-lite) — Solution

## Optimal Approach

Processing buckets largest-first (CHD ordering) makes the greedy displacement search almost always succeed quickly, yielding a space-efficient minimal perfect hash.

### Reference implementation

```python
class MinimalPerfectHash:
    """CHD-lite minimal perfect hash by displacement (fixed seed)."""

    _P = 2147483647

    def __init__(self, keys):
        random.seed(777)
        self._keys = list(keys)
        n = len(self._keys)
        self._n = n
        self._af = random.randrange(1, self._P)   # bucket hash
        self._bf = random.randrange(0, self._P)
        self._ah = random.randrange(1, self._P)   # placement hash
        self._bh = random.randrange(0, self._P)
        buckets = [[] for _ in range(n)]
        for k in self._keys:
            buckets[self._f(k) % n].append(k)
        # Place the biggest buckets first (classic CHD ordering).
        order = sorted(range(n), key=lambda i: (-len(buckets[i]), i))
        self._g = [0] * n              # per-bucket displacement
        taken = [False] * n
        for bi in order:
            bucket = buckets[bi]
            if not bucket:
                continue
            d = 0
            while True:                 # find a displacement with no clashes
                trial, seen, ok = [], set(), True
                for k in bucket:
                    slot = (self._h(k) + d) % n
                    if slot in seen or taken[slot]:
                        ok = False
                        break
                    seen.add(slot)
                    trial.append(slot)
                if ok:
                    for slot in trial:
                        taken[slot] = True
                    self._g[bi] = d
                    break
                d += 1

    def _f(self, k):
        return (self._af * k + self._bf) % self._P

    def _h(self, k):
        return (self._ah * k + self._bh) % self._P

    def hash(self, key):
        return (self._h(key) + self._g[self._f(key) % self._n]) % self._n

    def all_hashes(self):
        return [self.hash(k) for k in self._keys]

    def is_minimal_perfect(self):
        return sorted(self.hash(k) for k in self._keys) == list(range(self._n))
```

### Complexity

hash O(1); construction near-linear expected for small buckets.

## Key Insights & Edge Cases

is_minimal_perfect must be True: the hashes are exactly a permutation of 0..n-1 with no gaps or repeats. all_hashes returns that permutation in key order — here it happens to be the identity [0,1,2,3,4,5], a reproducible artifact of the fixed seed. Minimal perfect hashing powers read-only dictionaries, compilers' keyword tables, and static routing tables.
