# Sum of Window Max and Min — Solution

## Optimal Approach

Run two monotonic deques of indices in lock-step: a **decreasing** deque whose
front is the current window maximum, and an **increasing** deque whose front is
the current window minimum. For each new index push it into both deques (popping
smaller-or-equal tails from the max-deque and larger-or-equal tails from the
min-deque), evict any front that has slid out of the `[i-k+1, i]` window, and
once the first full window forms append `nums[maxd[0]] + nums[mind[0]]`.

### Reference implementation

```python
class Solution:
    def windowMaxPlusMin(self, nums, k):
        maxd = deque()  # decreasing -> front is window max
        mind = deque()  # increasing -> front is window min
        out = []
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
            if i >= k - 1:
                out.append(nums[maxd[0]] + nums[mind[0]])
        return out
```

### Complexity

O(n) time — each index enters and leaves both deques once — and O(k) space.
