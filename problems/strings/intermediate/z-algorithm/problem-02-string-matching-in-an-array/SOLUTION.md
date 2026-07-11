# Solution — String Matching in an Array

## Brute Force

For every ordered pair `(a, b)` with `a != b`, test whether `a` is a substring
of `b` using the built-in operator.

```python
def stringMatching(words):
    res = []
    for a in words:
        if any(a != b and a in b for b in words):
            res.append(a)
    return res
```

- **Time:** `O(k^2 * L^2)` worst case, where `k = len(words)` and `L` is the max
  word length: there are `O(k^2)` pairs and each `a in b` test is `O(L^2)` in the
  naive substring engine (Python's `in` is actually better, but the plain
  character-by-character mental model is quadratic per pair).
- **Space:** `O(1)` extra beyond the output.

## Optimal Approach (Z-Algorithm)

Replace the substring test with a linear-time Z check. For a candidate
`pattern` and a target `text`:

1. Skip the case `pattern is text` / equal strings — a word cannot be a
   substring of itself here.
2. If `len(pattern) > len(text)`, it cannot fit; skip.
3. Build `combined = pattern + '#' + text` where `'#'` is absent from both.
4. Compute the Z-array of `combined`. If any index `i` in the text region has
   `z[i] == len(pattern)`, then `pattern` occurs inside `text`.

A word belongs in the answer as soon as *one* other word contains it.

### Why it is correct

`z[i]` is the length of the longest prefix of `combined` (which begins with the
whole `pattern`) that matches starting at `i`. Because of the foreign separator,
`z[i]` never exceeds `len(pattern)` and never straddles the boundary. Hence
`z[i] == len(pattern)` at a text-region index is exactly the statement that
`pattern` appears in `text` at that spot.

### Step-by-step

- Loop over each `a` in `words`.
- For each other `b`, run `is_substring(a, b)` via Z; break and record `a` on the
  first hit.
- Collect all matched words.

### Reference implementation

```python
from typing import List


def z_array(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


class Solution:
    def _is_substring(self, pattern: str, text: str) -> bool:
        if len(pattern) > len(text):
            return False
        z = z_array(pattern + "#" + text)
        m = len(pattern)
        return any(z[i] == m for i in range(m + 1, len(z)))

    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, a in enumerate(words):
            for j, b in enumerate(words):
                if i != j and self._is_substring(a, b):
                    res.append(a)
                    break
        return res
```

- **Time:** `O(k^2 * L)` — `O(k^2)` pairs, each Z build linear in the combined
  length `O(L)`.
- **Space:** `O(L)` for the combined string and its Z-array per test.

## Key Insights & Edge Cases

- **Exclude self-matches.** Comparing a word against itself would always
  "match"; guard with an index or identity check. Because the problem promises
  unique words, comparing by index `i != j` is sufficient.
- **Length short-circuit:** a longer pattern can never sit inside a shorter
  text — skipping saves the Z build.
- **Duplicates:** not a concern here (words are unique), but if duplicates were
  allowed you would compare by index, not by value.
- **Small inputs:** the constraints are tiny, so even brute force passes; the
  Z-based version is the transferable pattern that scales to large single-query
  matching problems.
- **A neat alternative:** sort words by length, then for each word test only
  against the longer words — but that is an optimization on top of the same Z
  membership test.
