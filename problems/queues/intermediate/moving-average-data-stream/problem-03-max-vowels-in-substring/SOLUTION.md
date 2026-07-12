# Maximum Number of Vowels in a Substring of Given Length — Solution

## Optimal Approach

Maintain the vowel count of the current size-`k` window as a running sum. Seed it from the first `k` characters, then slide one position at a time: the entering character adds 1 if it is a vowel and the leaving character subtracts 1 if it was. Track the running maximum. O(n) time, O(1) extra space.

### Reference implementation

```python
class Solution:
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        cur = sum(1 for c in s[:k] if c in vowels)
        best = cur
        for i in range(k, len(s)):
            cur += (s[i] in vowels) - (s[i - k] in vowels)
            if cur > best:
                best = cur
        return best
```
