# Find All Anagrams in a String — Solution

## Brute Force

For every start index `i` in `0 .. len(s) - len(p)`, take the substring
`s[i : i + len(p)]` and run a full anagram check against `p` (sort both and compare, or
build a fresh count table each time).

- **Time:** `O((n - m + 1) * m)` for counting, or `O((n - m + 1) * m log m)` for
  sorting, where `n = len(s)`, `m = len(p)`. Rebuilding the window's table from scratch
  at every position is the waste.
- **Space:** `O(m)` (or `O(1)` for a fixed 26-letter alphabet).

Correct but does redundant work: consecutive windows overlap in `m - 1` characters.

## Optimal Approach (Anagram Check — sort or count, on a sliding window)

A window of length `m` is an anagram of `p` **iff** its character-frequency table
equals `p`'s table. Instead of recomputing the window table each step, **slide** it:
add the entering character and remove the leaving character in `O(1)`.

Algorithm (fixed-size sliding window):

1. If `len(p) > len(s)`, return `[]` (no window can fit).
2. Build `need = Counter(p)` and `window = Counter(s[:m])` for the first window.
3. `result = [0] if window == need else []`.
4. For each right end `r` from `m` to `n - 1`:
   - Add `s[r]` to `window`.
   - Remove `s[r - m]` from `window` (decrement; delete the key when it hits 0 so the
     `Counter` comparison stays exact).
   - The window now covers `s[r - m + 1 : r + 1]`, starting at `l = r - m + 1`. If
     `window == need`, append `l` to `result`.
5. Return `result`.

```python
def findAnagrams(self, s, p):
    m, n = len(p), len(s)
    if m > n:
        return []
    need = Counter(p)
    window = Counter(s[:m])
    res = [0] if window == need else []
    for r in range(m, n):
        window[s[r]] += 1
        left_char = s[r - m]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]          # keep Counter clean for == comparison
        if window == need:
            res.append(r - m + 1)
    return res
```

A common optimization avoids comparing whole tables each step by tracking a single
`matches` counter (how many of the 26 letters currently have the exact required count),
updating it as characters enter/leave, and recording an index whenever `matches == 26`.
That makes each step truly `O(1)` instead of `O(alphabet)`.

**Why it is correct:** the window always holds exactly the multiset of the current
length-`m` substring. Comparing that multiset to `p`'s multiset is precisely the anagram
test, so an index is recorded exactly when the substring starting there is an anagram of
`p`. Sliding maintains the invariant "window == frequency table of `s[l..r]`" after each
add/remove pair.

- **Time:** `O(n)` — each character enters and leaves the window once; comparisons are
  `O(1)` (26-letter alphabet) or `O(1)` amortized with the `matches` trick.
- **Space:** `O(1)` for the fixed lowercase alphabet (two 26-slot tables).

## Key Insights & Edge Cases

- **Fixed-size window.** Unlike variable-length sliding-window problems, here the window
  length is always `len(p)`; you add one char and drop one char in lockstep.
- **Keep the count table clean.** When decrementing a `Counter`, delete keys that reach
  0; otherwise a lingering `{'x': 0}` entry breaks `window == need` equality. (A fixed
  26-length array sidesteps this since you compare arrays element-wise.)
- **`len(p) > len(s)`** -> return `[]` up front.
- **Empty result** when no window matches (Example 3, `s="aa", p="bb"`).
- **Overlapping matches are allowed and expected** (Example 2 returns `[0, 1, 2]`); the
  window naturally reports every valid start index.
- **Array vs. Counter.** For guaranteed lowercase input, two `int[26]` arrays plus the
  `matches` counter give the cleanest `O(n)` solution and avoid hashing overhead.
