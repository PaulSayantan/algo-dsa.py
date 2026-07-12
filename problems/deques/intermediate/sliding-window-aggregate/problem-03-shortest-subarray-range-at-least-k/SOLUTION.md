# Shortest Subarray With Range At Least K — Solution

## Optimal Approach

Keep two monotonic deques of indices over the current window `[left, right]`: a
decreasing one whose front is the window maximum and an increasing one whose
front is the window minimum. Extend `right` one step at a time; the range
`max - min` only grows as the window widens, so once it reaches `k` we greedily
shrink from the left as long as the shortened window still satisfies
`max - min >= k`, recording the width each time and evicting any front index
that slips out of the window. Every index enters and leaves each deque once.

### Reference implementation

```python
class Solution:
    def shortestSubarray(self, nums, k):
        maxd = deque()  # decreasing values -> front is window max
        mind = deque()  # increasing values -> front is window min
        left = 0
        best = float("inf")
        for right, x in enumerate(nums):
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(right)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(right)
            while maxd and mind and nums[maxd[0]] - nums[mind[0]] >= k:
                best = min(best, right - left + 1)
                left += 1
                if maxd[0] < left:
                    maxd.popleft()
                if mind[0] < left:
                    mind.popleft()
        return best if best != float("inf") else -1
```

### Complexity

O(n) time (each index is pushed and popped from each deque at most once), O(n)
space for the deques.
