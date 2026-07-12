# Permutation in String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def checkInclusion(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        need = Counter(s1)
        window = Counter()
        for i in range(n2):
            window[s2[i]] += 1
            if i >= n1:
                left = s2[i - n1]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
            if window == need:
                return True
        return False
```

### Complexity

O(|s2|) time, O(1) space.
