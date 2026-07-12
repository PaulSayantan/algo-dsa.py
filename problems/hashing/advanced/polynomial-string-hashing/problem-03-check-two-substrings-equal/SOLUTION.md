# Check If Two Substrings Are Equal — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    BASE = 911382323
    MOD = 972663749

    def _prefix(self, s):
        n = len(s)
        H = [0] * (n + 1)
        PW = [1] * (n + 1)
        for i in range(1, n + 1):
            H[i] = (H[i - 1] * self.BASE + ord(s[i - 1])) % self.MOD
            PW[i] = (PW[i - 1] * self.BASE) % self.MOD
        return H, PW

    def _sub(self, H, PW, l, r):
        # hash of s[l..r] inclusive
        return (H[r + 1] - H[l] * PW[r - l + 1]) % self.MOD

    def equalSubstrings(self, s, queries):
        H, PW = self._prefix(s)
        out = []
        for a, b, L in queries:
            out.append(self._sub(H, PW, a, a + L - 1) == self._sub(H, PW, b, b + L - 1))
        return out

    def countDistinctOfLength(self, s, L):
        n = len(s)
        if L <= 0 or L > n:
            return 0
        H, PW = self._prefix(s)
        seen = set()
        for i in range(n - L + 1):
            seen.add(self._sub(H, PW, i, i + L - 1))
        return len(seen)

    def substringsEqual(self, s, a, b, L):
        H, PW = self._prefix(s)
        return self._sub(H, PW, a, a + L - 1) == self._sub(H, PW, b, b + L - 1)
```
