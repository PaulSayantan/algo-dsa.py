# Solution: Valid Anagram

## Brute Force

Sort both strings and compare them character by character. Two strings are
anagrams if and only if their sorted forms are equal.

```python
def isAnagram(s, t):
    return sorted(s) == sorted(t)
```

- **Time:** `O(n log n)` — dominated by sorting each string of length `n`.
- **Space:** `O(n)` — sorting produces new sorted sequences (Python's `sorted`
  returns a list of length `n`).

This is simple and correct, but sorting is more work than necessary.

## Optimal Approach

Count the frequency of each character. Build a frequency map from `s`, then walk
`t`, decrementing counts. If any count goes negative or a character in `t` is
missing, they are not anagrams. Finally, all counts must be zero.

**Why it is correct:** Anagrams are exactly the strings whose character
multisets are equal. A frequency table is a canonical representation of a
multiset, so equal tables imply equal multisets and vice versa. Because we first
check lengths, a fully-zeroed table after processing `t` guarantees a match.

**Step by step:**
1. If `len(s) != len(t)`, return `False` immediately.
2. Build `counts`, a map from character to how many times it appears in `s`.
3. For each character `c` in `t`: decrement `counts[c]`. If `c` is absent or its
   count drops below zero, return `False`.
4. Return `True` (all counts balanced out).

```python
from collections import Counter

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    counts = Counter(s)
    for c in t:
        counts[c] -= 1
        if counts[c] < 0:
            return False
    return True

# Even shorter using Counter equality:
def isAnagram_short(s, t):
    return Counter(s) == Counter(t)
```

Because the alphabet is fixed (26 lowercase letters), a length-26 array indexed
by `ord(c) - ord('a')` works too and avoids hashing overhead.

- **Time:** `O(n)` — a constant number of passes over the strings.
- **Space:** `O(k)` where `k` is the alphabet size (`O(1)` for a fixed 26-letter
  alphabet).

## Key Insights & Edge Cases

- **Length check first:** Different lengths can never be anagrams; this cheap
  test also guarantees the "decrement to zero" logic is complete.
- **Array vs. hash map:** For a small fixed alphabet, a count array is faster and
  uses constant space. For Unicode or unknown alphabets, prefer a hash map.
- **Empty strings:** Two empty strings are anagrams of each other (returns
  `True`); the constraints here start at length 1, but the logic still holds.
- **Unicode follow-up:** LeetCode notes a follow-up where inputs may contain
  Unicode — a hash map handles this without change, while a fixed 26-slot array
  would not.
