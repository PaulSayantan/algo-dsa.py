# LRU Cache — Final Contents — Solution

## Optimal Approach

Report keys sorted so the assertion doesn't depend on internal ordering.

### Reference implementation

```python
class LRUCacheKeys:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

    def keys_sorted(self):
        return sorted(self.cache.keys())
```

### Complexity

O(1) per op; keys_sorted is O(k log k) for k resident keys.

## Key Insights & Edge Cases

Trace (cap=3): put 1,2,3 -> resident {1,2,3}, order [1,2,3]; put(4) evicts LRU 1 -> {2,3,4}, order [2,3,4]; get(2)=20 refreshes 2 -> order [3,4,2]; put(5) evicts LRU 3 -> {2,4,5}. Sorting hides the recency order but the SET is fully determined by which keys were touched.
