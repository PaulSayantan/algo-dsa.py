# Minimum Window Substring — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        start, end = 0, 0
        best_len = float("inf")
        for right, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            while missing == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    start, end = left, right + 1
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return s[start:end] if best_len != float("inf") else ""
```

### Complexity

O(|s| + |t|) time, O(|t|) space.
