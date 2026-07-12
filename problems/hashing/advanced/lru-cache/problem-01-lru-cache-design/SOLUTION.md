# LRU Cache — Solution

## Optimal Approach

Keep entries in recency order. `get`/`put` move the touched key to the most-recent end; overflow pops the least-recent end. OrderedDict makes each step O(1).

### Reference implementation

```python
class LRUCache:
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
```

### Complexity

O(1) time per get/put; O(capacity) space.

## Key Insights & Edge Cases

Trace (cap=2): put1,put2 -> {1,2}; get(1)=1, order becomes [2,1]; put(3) evicts LRU 2 -> {1,3}; get(2)=-1; put(4) evicts LRU 1 -> {3,4}; get(1)=-1; get(3)=3; get(4)=4. The subtle part is that get() itself refreshes recency — which is why 1 survived the first eviction.
