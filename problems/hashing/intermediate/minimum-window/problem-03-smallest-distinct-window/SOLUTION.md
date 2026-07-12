# Smallest Subarray Covering All Distinct Elements — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def smallestDistinctWindow(self, arr):
        if not arr:
            return 0
        total = len(set(arr))
        count = defaultdict(int)
        have = 0
        left = 0
        best = len(arr)
        for right, x in enumerate(arr):
            count[x] += 1
            if count[x] == 1:
                have += 1
            while have == total:
                best = min(best, right - left + 1)
                count[arr[left]] -= 1
                if count[arr[left]] == 0:
                    have -= 1
                left += 1
        return best
```

### Complexity

O(n) time, O(d) space (d = number of distinct values).
