# First Palindromic String in the Array — Solution

## Optimal Approach

Walk the words left to right. For each word, run the standard deque palindrome
check — compare the front (`popleft()`) with the back (`pop()`) until at most one
character remains. Return the first word that survives the check; if the scan
finishes with none, return the empty string.

### Reference implementation

```python
class Solution:
    def firstPalindrome(self, words):
        def is_pal(w):
            dq = deque(w)
            while len(dq) > 1:
                if dq.popleft() != dq.pop():
                    return False
            return True

        for w in words:
            if is_pal(w):
                return w
        return ""
```

- **Time:** O(n * k) — `n` words each checked in O(k) for length `k`.
- **Space:** O(k) — one deque per word.
