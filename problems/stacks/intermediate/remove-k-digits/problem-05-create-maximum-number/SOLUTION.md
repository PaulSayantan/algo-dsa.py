# Create Maximum Number — Solution

## Optimal Approach

For every split `i + j = k`, pick the largest length-`i` subsequence of `nums1`
and length-`j` subsequence of `nums2` using the remove-k-digits maximize trick
(a monotonic decreasing drop-stack), then merge the two picks greedily by
comparing the remaining suffixes lexicographically. Keep the best merge overall.

### Reference implementation

```python
class Solution:
    def maxNumber(self, nums1, nums2, k):
        def pick(nums, t):
            drop = len(nums) - t
            stack = []
            for x in nums:
                while drop and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            return stack[:t]

        def greater(a, i, b, j):
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            return j == len(b) or (i < len(a) and a[i] > b[j])

        def merge(a, b):
            res = []
            i = j = 0
            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            return res

        m, n = len(nums1), len(nums2)
        best = []
        for i in range(max(0, k - n), min(k, m) + 1):
            cand = merge(pick(nums1, i), pick(nums2, k - i))
            if cand > best:
                best = cand
        return best
```
