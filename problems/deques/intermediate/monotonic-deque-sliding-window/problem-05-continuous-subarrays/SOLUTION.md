# Continuous Subarrays — Solution

## Optimal Approach

For each right endpoint, find the smallest `left` such that the window
`[left, right]` still satisfies `max - min <= 2`. Every subarray that ends at
`right` and starts at any index in `[left, right]` is then continuous, so it
contributes `right - left + 1` to the total. Maintain the window max with a
**decreasing** monotonic deque and the window min with an **increasing** one; when
`max - min > 2`, advance `left`, evicting any deque-front index that leaves the
window. The `left` pointer only moves forward, so the whole scan is O(n).

### Reference implementation

```python
class Solution:
    def continuousSubarrays(self, nums):
        maxd = deque()  # indices, values decreasing front -> back (window max at front)
        mind = deque()  # indices, values increasing front -> back (window min at front)
        left = 0
        total = 0
        for right, x in enumerate(nums):
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(right)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(right)
            while nums[maxd[0]] - nums[mind[0]] > 2:
                left += 1
                if maxd[0] < left:
                    maxd.popleft()
                if mind[0] < left:
                    mind.popleft()
            total += right - left + 1
        return total
```

### Complexity

O(n) time, O(n) space — each index is pushed and popped from each deque once.
