# Longest Repeated Substring Length — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    BASE = 911382323
    MOD = 972663749

    def longestDupLength(self, s):
        n = len(s)
        nums = [ord(c) for c in s]

        def has_dup(L):
            if L == 0:
                return True
            high = pow(self.BASE, L - 1, self.MOD)
            h = 0
            for i in range(L):
                h = (h * self.BASE + nums[i]) % self.MOD
            seen = {h: [0]}
            for i in range(1, n - L + 1):
                h = ((h - nums[i - 1] * high) * self.BASE + nums[i + L - 1]) % self.MOD
                if h in seen:
                    if any(s[j:j + L] == s[i:i + L] for j in seen[h]):
                        return True
                    seen[h].append(i)
                else:
                    seen[h] = [i]
            return False

        lo, hi, best = 1, n - 1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_dup(mid):
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best

    def longestRepeatedSubstringLength(self, s):
        return self.longestDupLength(s)

    def findRepeatedDnaSequences(self, s):
        L = 10
        n = len(s)
        if n < L:
            return []
        count = {}
        res = set()
        for i in range(n - L + 1):
            sub = s[i:i + L]
            count[sub] = count.get(sub, 0) + 1
            if count[sub] == 2:
                res.add(sub)
        return sorted(res)
```

### Complexity

O(n log n) expected time.
