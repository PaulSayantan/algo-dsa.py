# Solution: First Unique Character in a String

## Brute Force

For each character, scan the rest of the string to see whether it appears
anywhere else. Return the index of the first character that appears nowhere
else.

```python
def firstUniqChar(s):
    for i, c in enumerate(s):
        if s.count(c) == 1:   # s.count scans the whole string each time
            return i
    return -1
```

- **Time:** `O(n^2)` — `s.count(c)` is `O(n)` and is called up to `n` times.
- **Space:** `O(1)` — no auxiliary structure (ignoring the input).

Correct but quadratic; too slow when `n` approaches `10^5`.

## Optimal Approach

Count all characters in one pass, then find the first index whose character has
a count of exactly one.

**Why it is correct:** A character is "unique" exactly when its total frequency
is one. After the first pass, `counts[c]` is the true total for every character,
independent of position. Scanning left to right and returning the first index
with `counts[s[i]] == 1` therefore yields the earliest unique character by
definition.

**Step by step:**
1. Build `counts`, mapping each character to its number of occurrences in `s`.
2. Iterate over `s` with indices. For index `i`, if `counts[s[i]] == 1`, return
   `i`.
3. If no such index is found, return `-1`.

```python
from collections import Counter

def firstUniqChar(s):
    counts = Counter(s)
    for i, c in enumerate(s):
        if counts[c] == 1:
            return i
    return -1
```

- **Time:** `O(n)` — two linear passes.
- **Space:** `O(k)` where `k` is the alphabet size (`O(1)` for 26 lowercase
  letters).

## Key Insights & Edge Cases

- **Two passes are required:** You cannot know a character is unique until you
  have seen the whole string, so the count pass must complete before the
  index-search pass.
- **Return index, not character:** The problem asks for the position; keep the
  original order by scanning `s` (not the map) in the second pass.
- **All repeating:** Strings like `"aabb"` return `-1`.
- **Single character:** `"z"` returns `0`.
- **Fixed alphabet optimization:** A length-26 integer array can replace the
  hash map for a small constant-factor speedup and `O(1)` space.
