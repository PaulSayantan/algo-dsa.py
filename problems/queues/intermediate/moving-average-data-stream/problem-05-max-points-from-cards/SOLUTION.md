# Maximum Points You Can Obtain from Cards — Solution

## Optimal Approach

Taking `k` cards from the two ends is equivalent to leaving a single contiguous block of size `n - k` untouched. To maximize the taken sum, minimize the leftover block's sum. That leftover is a fixed-size sliding window: seed it with the first `n - k` elements, then slide keeping a running sum (add entering, drop leaving) and track the minimum. The answer is `total - minWindow`. When `k == n` the window is empty and the answer is the full total. O(n) time.

### Reference implementation

```python
class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        w = n - k
        total = sum(cardPoints)
        if w == 0:
            return total
        cur = sum(cardPoints[:w])
        min_window = cur
        for i in range(w, n):
            cur += cardPoints[i] - cardPoints[i - w]
            if cur < min_window:
                min_window = cur
        return total - min_window
```
