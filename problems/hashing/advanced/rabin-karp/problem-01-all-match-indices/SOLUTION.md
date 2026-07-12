# All Pattern Match Indices (Rabin-Karp) — Solution

## Optimal Approach

Hash the pattern once, hash the first window, then roll the window hash across the text in O(1) per shift. On a hash match, confirm with a slice comparison so a collision never produces a false positive.

### Reference implementation

```python
class Solution:
    BASE = 911382323
    MOD = 972663749

    def matchIndices(self, text, pattern):
        n, m = len(text), len(pattern)
        if m == 0:
            return list(range(n + 1))
        if m > n:
            return []
        high = pow(self.BASE, m - 1, self.MOD)
        phash = 0
        whash = 0
        for i in range(m):
            phash = (phash * self.BASE + ord(pattern[i])) % self.MOD
            whash = (whash * self.BASE + ord(text[i])) % self.MOD
        res = []
        for i in range(n - m + 1):
            if whash == phash and text[i:i + m] == pattern:
                res.append(i)
            if i < n - m:
                whash = ((whash - ord(text[i]) * high) * self.BASE + ord(text[i + m])) % self.MOD
        return res

    def countOccurrences(self, text, pattern):
        return len(self.matchIndices(text, pattern))

    def strStr(self, haystack, needle):
        hits = self.matchIndices(haystack, needle)
        return hits[0] if hits else -1
```

### Complexity

Expected O(n + m) time, O(1) extra space (plus the output list).

## Key Insights & Edge Cases

A large prime modulus keeps collisions rare so verification seldom runs. Never skip verification — that turns the method Monte-Carlo and can report a spurious index on a collision.
