# Compare Two Strings via Double Hash — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    BASE1 = 911382323
    MOD1 = 972663749
    BASE2 = 998244353
    MOD2 = 1000000007

    def _prefix(self, s, base, mod):
        n = len(s)
        H = [0] * (n + 1)
        PW = [1] * (n + 1)
        for i in range(1, n + 1):
            H[i] = (H[i - 1] * base + ord(s[i - 1])) % mod
            PW[i] = (PW[i - 1] * base) % mod
        return H, PW

    def _channels(self, s):
        h1 = self._prefix(s, self.BASE1, self.MOD1)
        h2 = self._prefix(s, self.BASE2, self.MOD2)
        return h1, h2

    @staticmethod
    def _sub(pref, mod, l, r):
        H, PW = pref
        return (H[r + 1] - H[l] * PW[r - l + 1]) % mod

    def _key(self, ch1, ch2, l, r):
        return (self._sub(ch1, self.MOD1, l, r), self._sub(ch2, self.MOD2, l, r))

    def countDistinctOfLength(self, s, L):
        n = len(s)
        if L <= 0 or L > n:
            return 0
        ch1, ch2 = self._channels(s)
        seen = set()
        for i in range(n - L + 1):
            seen.add(self._key(ch1, ch2, i, i + L - 1))
        return len(seen)

    def hasRepeatOfLength(self, s, L):
        n = len(s)
        if L <= 0 or L > n:
            return False
        ch1, ch2 = self._channels(s)
        seen = set()
        for i in range(n - L + 1):
            k = self._key(ch1, ch2, i, i + L - 1)
            if k in seen:
                return True
            seen.add(k)
        return False

    def stringsEqual(self, a, b):
        if len(a) != len(b):
            return False
        if not a:
            return True
        ca1, ca2 = self._channels(a)
        cb1, cb2 = self._channels(b)
        n = len(a)
        return self._key(ca1, ca2, 0, n - 1) == self._key(cb1, cb2, 0, n - 1)
```
