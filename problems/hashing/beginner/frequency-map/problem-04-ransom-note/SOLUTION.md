# Ransom Note — Solution

## Optimal Approach

Build the magazine's frequency map, then verify each letter the note requires is available in at least that quantity. A single deficient letter fails the whole note.

### Reference implementation

```python
class Solution:
    def canConstruct(self, ransomNote, magazine):
        need = Counter(ransomNote)
        have = Counter(magazine)
        for ch, cnt in need.items():
            if have[ch] < cnt:
                return False
        return True
```

### Complexity

Time O(m + r), space O(k).
