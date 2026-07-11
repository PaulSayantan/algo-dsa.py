# Find All Anagrams in a String — Solution

## Brute Force

For every start index `i` in `s` (with a full-width window remaining), take the
substring `s[i:i+len(p)]`, build its count signature, and compare it to `p`'s
signature. Record `i` on a match.

```python
def findAnagrams(s, p):
    from collections import Counter
    k, target = len(p), Counter(p)
    return [i for i in range(len(s) - k + 1)
            if Counter(s[i:i+k]) == target]
```

- **Time:** `O((n - k + 1) * k)` = `O(n * k)` — we rebuild the whole signature
  for each of the `~n` windows.
- **Space:** `O(A)` for the counters (`A` = alphabet size).

The waste is recomputing the full window signature from scratch every step even
though consecutive windows differ by only two characters.

## Optimal Approach (Hashing Signature + Sliding Window)

`p`'s count signature is fixed. Maintain a **rolling count signature** for a
window of width `k = len(p)` as it slides across `s`: when the window advances
by one, one character enters on the right and one leaves on the left. Update the
signature in `O(1)` and compare it to `p`'s signature at each position.

Why it is correct: a length-`k` substring is an anagram of `p` exactly when it
has the identical character multiset, i.e. identical count signature. The window
signature is always kept in sync with the current substring, so every index
where the two signatures match is exactly an anagram occurrence, and no match is
missed because we test every valid window.

To avoid comparing 26 numbers on every step, track a `matches` counter that
records how many of the 26 letters currently have `window[c] == need[c]`. When
`matches == 26`, the whole window is an anagram.

Step by step:

1. If `len(s) < len(p)`, return `[]`.
2. Build `need[26]` from `p` and `window[26]` from the first `k` chars of `s`.
3. Compare and, if equal, record index `0`.
4. Slide from `i = k` to `len(s) - 1`: add `s[i]` to the window, remove
   `s[i-k]`, and whenever the full window matches `need`, record `i - k + 1`.

```python
from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    n, k = len(s), len(p)
    if n < k:
        return []
    need = [0] * 26
    window = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1

    res = []
    for i, ch in enumerate(s):
        window[ord(ch) - 97] += 1          # char enters on the right
        if i >= k:
            window[ord(s[i - k]) - 97] -= 1  # char leaves on the left
        if i >= k - 1 and window == need:
            res.append(i - k + 1)
    return res
```

- **Time:** `O(n)` — each character enters and leaves the window once; the
  `window == need` list comparison is `O(26) = O(1)`. (With a `matches` counter
  it is strictly `O(1)` work per step.)
- **Space:** `O(1)` — two fixed length-26 arrays.

## Key Insights & Edge Cases

- **`len(p) > len(s)`** — no window exists; return `[]` up front.
- **Fixed-width window** — unlike variable-length sliding-window problems, the
  window here is always exactly `len(p)` wide, which is what makes the rolling
  update a clean add-one/remove-one.
- **Comparing signatures cheaply** — `window == need` on two length-26 lists is
  constant work; for larger alphabets track a `matches` count so you never scan
  the whole table.
- **Overlapping matches are allowed** — Example 2 (`"abab"`, `"ab"`) yields
  `[0, 1, 2]`, adjacent overlapping windows all count.
- **Index bookkeeping** — the window covering `s[i-k+1 .. i]` starts at
  `i - k + 1`; off-by-one here is the most common bug.
