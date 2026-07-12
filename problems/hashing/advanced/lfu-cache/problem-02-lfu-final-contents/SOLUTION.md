# LFU Cache — Final Contents — Solution

## Optimal Approach

Report keys sorted so the assertion is independent of internal bucket ordering.

### Reference implementation

```python
class LFUCacheKeys:
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

    def keys_sorted(self):
        return sorted(self.val.keys())
```

### Complexity

O(1) per op; keys_sorted is O(k log k) for k resident keys.

## Key Insights & Edge Cases

Trace (cap=2): put1,put2 (freqs 1,1); get(1)=1 -> freq(1)=2; put(3) evicts LFU 2 -> {1,3}; get(3)=3 -> freq(3)=2; put(4): 1 and 3 both at freq 2, key 1 is the LRU of the tie, so it is evicted -> {3,4}. Sorting the resident set gives a deterministic [3,4].
