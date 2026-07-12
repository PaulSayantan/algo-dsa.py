# Design Authentication Manager — Solution

## Optimal Approach

A single expiry map; renew guarded by the unexpired check.

### Reference implementation

```python
class AuthenticationManager:
    def __init__(self, timeToLive):
        self._ttl = timeToLive
        self._exp = {}

    def generate(self, tokenId, currentTime):
        self._exp[tokenId] = currentTime + self._ttl

    def renew(self, tokenId, currentTime):
        if tokenId in self._exp and self._exp[tokenId] > currentTime:
            self._exp[tokenId] = currentTime + self._ttl

    def countUnexpiredTokens(self, currentTime):
        return sum(1 for e in self._exp.values() if e > currentTime)
```

### Complexity

generate/renew O(1); count O(n).

## Key Insights & Edge Cases

aaa exp=6, bbb exp=7. renew(aaa,4) succeeds (6>4) → exp 9. renew(bbb,8) is a no-op (bbb expired at 7 ≤ 8). At t=8 only aaa (exp 9) survives → 1.
