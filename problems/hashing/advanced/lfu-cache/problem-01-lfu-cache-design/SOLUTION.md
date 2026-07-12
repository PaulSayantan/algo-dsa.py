# LFU Cache — Solution

## Optimal Approach

Buckets keyed by frequency, each an OrderedDict for LRU ordering within a frequency. `minfreq` points at the eviction bucket; touching a key moves it from bucket f to f+1.

### Reference implementation

```python
class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.val = {}
        self.freq = {}
        self.buckets = defaultdict(OrderedDict)
        self.minfreq = 0

    def _touch(self, key):
        f = self.freq[key]
        del self.buckets[f][key]
        if not self.buckets[f]:
            del self.buckets[f]
            if self.minfreq == f:
                self.minfreq = f + 1
        self.freq[key] = f + 1
        self.buckets[f + 1][key] = None

    def get(self, key):
        if key not in self.val:
            return -1
        self._touch(key)
        return self.val[key]

    def put(self, key, value):
        if self.cap <= 0:
            return
        if key in self.val:
            self.val[key] = value
            self._touch(key)
            return
        if len(self.val) >= self.cap:
            evict, _ = self.buckets[self.minfreq].popitem(last=False)
            del self.val[evict]
            del self.freq[evict]
        self.val[key] = value
        self.freq[key] = 1
        self.buckets[1][key] = None
        self.minfreq = 1
```

### Complexity

O(1) time per get/put; O(capacity) space.

## Key Insights & Edge Cases

Trace (cap=2): put1,put2 (freqs 1,1). get(1)=1 -> freq(1)=2. put(3) evicts LFU key 2 (freq 1) -> resident {1,3}. get(2)=-1. get(3)=3 -> freq(3)=2. Now put(4): keys 1 and 3 both have freq 2, tie broken by LRU — key 1 was touched before key 3, so 1 is evicted -> {3,4}. get(1)=-1, get(3)=3, get(4)=4. The freq-then-recency tie-break is the crux.
