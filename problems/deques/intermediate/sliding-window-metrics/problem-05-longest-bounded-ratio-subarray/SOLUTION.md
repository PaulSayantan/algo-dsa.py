# Longest Bounded-Ratio Subarray — Solution

## Optimal Approach

The window is valid exactly when its max is within `multiplier` times its min,
so we need both extremes cheaply. Keep a **decreasing** deque (front = window
max) and an **increasing** deque (front = window min). Expand `right` one step at
a time, pushing the index into both deques. Whenever the invariant
`nums[maxd[0]] <= multiplier * nums[mind[0]]` is violated, advance `left`,
popping any deque front whose index has dropped below `left`. After each step the
window `[left, right]` is valid, so update the best length with
`right - left + 1`.

### Reference implementation

```python
class Solution:
    def longestBoundedRatio(self, nums, multiplier):
        maxd = deque()  # decreasing -> front is window max
        mind = deque()  # increasing -> front is window min
        left = 0
        best = 0
        for right, x in enumerate(nums):
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(right)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(right)
            while nums[maxd[0]] > multiplier * nums[mind[0]]:
                left += 1
                if maxd[0] < left:
                    maxd.popleft()
                if mind[0] < left:
                    mind.popleft()
            best = max(best, right - left + 1)
        return best
```

### Complexity

O(n) time — each index enters and leaves both deques at most once and `left`
only advances — and O(n) space in the worst case for the deques.
