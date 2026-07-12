# Count Windows With Range Equal to Target — Solution

## Optimal Approach

The exact-match twist does not change the machinery: you still need the true
range of every fixed-size window, which two monotonic deques give in O(n). Run a
**decreasing** deque (front = window max) and an **increasing** deque
(front = window min) together. Push each index into both, evict any front that
has slid past `i - k`, and once a full window exists compare
`nums[maxd[0]] - nums[mind[0]]` to `target` for equality, incrementing the count
on a hit.

### Reference implementation

```python
class Solution:
    def countExactRangeWindows(self, nums, k, target):
        maxd = deque()  # decreasing -> front is window max
        mind = deque()  # increasing -> front is window min
        count = 0
        for i, x in enumerate(nums):
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(i)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(i)
            if maxd[0] <= i - k:
                maxd.popleft()
            if mind[0] <= i - k:
                mind.popleft()
            if i >= k - 1 and nums[maxd[0]] - nums[mind[0]] == target:
                count += 1
        return count
```

### Complexity

O(n) time, O(k) space.
