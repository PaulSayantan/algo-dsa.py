# Sliding Window Median — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        res = []

        def median():
            if k % 2:
                return float(window[k // 2])
            return (window[k // 2 - 1] + window[k // 2]) / 2

        res.append(median())
        for i in range(k, len(nums)):
            out = nums[i - k]
            window.pop(bisect.bisect_left(window, out))
            bisect.insort(window, nums[i])
            res.append(median())
        return res
```
