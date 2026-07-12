# Palindrome Number — Solution

## Optimal Approach

A negative integer can never be a palindrome: reversing `-121` would place the
sign at the end. For a non-negative `x`, treat its decimal representation as a
sequence of characters, load them into a deque, and check the palindrome
property directly by comparing the front (`popleft()`) with the back (`pop()`)
until zero or one digit remains.

### Reference implementation

```python
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        dq = deque(str(x))
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
```

- **Time:** O(d) — one pass over the `d` digits.
- **Space:** O(d) — the deque holds every digit.
