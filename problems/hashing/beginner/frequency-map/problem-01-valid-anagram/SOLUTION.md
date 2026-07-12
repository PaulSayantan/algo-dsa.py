# Valid Anagram — Solution

## Optimal Approach

`Counter(s) == Counter(t)` compares the two frequency maps directly; unequal lengths or any differing count makes them non-equal.

### Reference implementation

```python
class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
```

### Complexity

Time O(n), space O(k) over the alphabet.
