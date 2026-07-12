# Sort Characters By Frequency — Solution

## Optimal Approach

`Counter.most_common()` returns (char, count) pairs already ordered by descending count; concatenating `char * count` builds the answer. With distinct frequencies the order is fully determined.

### Reference implementation

```python
class Solution:
    def frequencySort(self, s):
        counts = Counter(s)
        parts = []
        for ch, cnt in counts.most_common():
            parts.append(ch * cnt)
        return "".join(parts)
```

### Complexity

Time O(n + k log k), space O(k).
