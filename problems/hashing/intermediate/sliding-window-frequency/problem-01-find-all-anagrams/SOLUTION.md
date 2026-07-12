# Find All Anagrams in a String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findAnagrams(self, s, p):
        np, ns = len(p), len(s)
        if ns < np:
            return []
        need = Counter(p)
        window = Counter()
        res = []
        for i in range(ns):
            window[s[i]] += 1
            if i >= np:
                left = s[i - np]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
            if window == need:
                res.append(i - np + 1)
        return res
```

### Complexity

O(n) time (each char enters/leaves once), O(1) extra space (alphabet-bounded map).
