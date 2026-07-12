# Design HashMap — Solution

## Optimal Approach

Separate chaining: key % capacity picks a bucket, a short list holds colliding [key,value] pairs.

### Reference implementation

```python
class MyHashMap:
    def __init__(self):
        self._size = 1009
        self._buckets = [[] for _ in range(self._size)]

    def _index(self, key):
        return key % self._size

    def put(self, key, value):
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        bucket = self._buckets[self._index(key)]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return
```

### Complexity

O(1) average per operation, O(capacity + n) space.
