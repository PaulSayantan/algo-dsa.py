# Longest Substring With Equal Vowels and Consonants — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestEqualVowelConsonant(self, s):
        vowels = set('aeiou')
        first = {0: -1}
        balance = 0
        best = 0
        for i, c in enumerate(s):
            balance += 1 if c in vowels else -1
            if balance in first:
                best = max(best, i - first[balance])
            else:
                first[balance] = i
        return best
```

### Complexity

O(n) time, O(n) space.
