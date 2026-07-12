# Number of Sub-arrays of Size K and Average >= Threshold — Solution

## Optimal Approach

Compare the running window sum against `k * threshold` instead of dividing, so the whole scan stays in integer arithmetic. Seed the first window, then slide: add the entering element and drop the leaving one in O(1) per step, for O(n) total.

### Reference implementation

```python
class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        target = k * threshold
        window = sum(arr[:k])
        count = 1 if window >= target else 0
        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window >= target:
                count += 1
        return count
```
