# Longest Continuous Subarray With Absolute Diff <= Limit — Solution

## Optimal Approach

Keep a sliding window `[left, right]`. Two monotonic deques of indices track the
window extremes: a **decreasing** deque whose front is the window maximum, and an
**increasing** deque whose front is the window minimum. After extending `right`,
if `max - min > limit`, advance `left` (popping any front index that falls out of
the window) until the window is valid again. The best window width seen is the
answer. Each index enters and leaves each deque once, so the pass is O(n).

### Reference implementation

```python
class Solution:
    def longestSubarray(self, nums, limit):
        maxd = deque()  # indices, values decreasing front -> back (window max at front)
        mind = deque()  # indices, values increasing front -> back (window min at front)
        left = 0
        best = 0
        for right, x in enumerate(nums):
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(right)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(right)
            while nums[maxd[0]] - nums[mind[0]] > limit:
                left += 1
                if maxd[0] < left:
                    maxd.popleft()
                if mind[0] < left:
                    mind.popleft()
            best = max(best, right - left + 1)
        return best
```

### Complexity

O(n) time, O(n) space — each index is pushed and popped from each deque once.
