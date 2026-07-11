# Permutation in String — Solution

## Brute Force

Let `k = len(s1)`. For every length-`k` window of `s2`, sort the window (or build a
fresh frequency count) and compare it against the sorted `s1` (or its count).

```python
from collections import Counter
target = Counter(s1)
k = len(s1)
for i in range(len(s2) - k + 1):
    if Counter(s2[i:i + k]) == target:
        return True
return False
```

- **Time:** O(n · k) for count-per-window, or O(n · k log k) if you sort each window,
  where `n = len(s2)`.
- **Space:** O(Σ) for the counts.

Rebuilding the count for every window ignores the huge overlap between adjacent
windows.

## Optimal Approach (Sliding Window)

A substring is a permutation of `s1` iff it has **exactly the same character
frequencies** as `s1`. Slide a fixed window of width `k = len(s1)` across `s2` and
maintain the window's frequency table incrementally.

1. If `len(s1) > len(s2)`, return `False` immediately.
2. Build `need`, a size-26 count array for `s1`, and `window`, a size-26 count array
   for the first `k` characters of `s2`.
3. If `window == need`, return `True`.
4. Slide from index `k` to `len(s2) - 1`. At each step:
   - Add the incoming character: `window[s2[right]] += 1`.
   - Remove the outgoing character: `window[s2[right - k]] -= 1`.
   - If `window == need`, return `True`.
5. If no window matched, return `False`.

**Why it is correct:** After each slide, `window` holds the exact letter counts of the
contiguous block `s2[right - k + 1 .. right]`. Equal count vectors mean the two
multisets of letters are identical, i.e. one is a permutation of the other. Every
length-`k` window is examined once.

```python
if len(s1) > len(s2):
    return False
need = [0] * 26
window = [0] * 26
for c in s1:
    need[ord(c) - 97] += 1
k = len(s1)
for i in range(k):
    window[ord(s2[i]) - 97] += 1
if window == need:
    return True
for right in range(k, len(s2)):
    window[ord(s2[right]) - 97] += 1
    window[ord(s2[right - k]) - 97] -= 1
    if window == need:
        return True
return False
```

- **Time:** O(n) with a fixed alphabet — each of O(n) slides does O(1) count updates
  plus an O(26) = O(1) array comparison.
- **Space:** O(Σ) = O(1) for the two fixed-size (26) count arrays.

## Key Insights & Edge Cases

- **Permutation ⇔ equal frequency counts.** Order inside the window never matters.
- **Fixed-size window** again uses the "add one, remove one" update — the workhorse of
  fixed-window problems.
- **Comparing count arrays is O(1)** because the alphabet has a constant size (26).
  A refinement tracks a single `matches` counter (how many of the 26 letters already
  have the right count) to avoid even the 26-element comparison.
- **`len(s1) > len(s2)`:** must be handled first, otherwise the initial window build
  reads out of bounds.
- **Repeated letters in `s1` (e.g. `"aab"`):** frequency counts (not a set) handle
  multiplicity correctly — `"ab"` would not match `"aab"`.
