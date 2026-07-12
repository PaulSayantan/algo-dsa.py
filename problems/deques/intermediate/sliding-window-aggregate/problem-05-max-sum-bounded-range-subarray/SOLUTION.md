# Maximum Sum of a Bounded-Range Subarray — Solution

## Optimal Approach

Because all values are positive, among windows ending at a fixed right index the
widest bounded-range window has the largest sum, so we maintain the maximal valid
window with two monotonic deques (decreasing for the max, increasing for the min)
plus a running window sum. Extend `right`, add `nums[right]` to the sum, then
while `max - min > limit` subtract `nums[left]` and advance `left`, evicting any
deque front that leaves the window. After each valid step the running sum is the
best sum for a window ending at `right`; keep the global maximum.

### Reference implementation

```python
class Solution:
    def maxBoundedSum(self, nums, limit):
        maxd = deque()  # decreasing values -> front is window max
        mind = deque()  # increasing values -> front is window min
        left = 0
        window_sum = 0
        best = 0
        for right, x in enumerate(nums):
            window_sum += x
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(right)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(right)
            while nums[maxd[0]] - nums[mind[0]] > limit:
                window_sum -= nums[left]
                left += 1
                if maxd[0] < left:
                    maxd.popleft()
                if mind[0] < left:
                    mind.popleft()
            best = max(best, window_sum)
        return best
```

### Complexity

O(n) time (each index enters and leaves each deque once), O(n) space for the
deques.
