# Solution — Permutation in String

## Brute Force

For every start index `i` in `s2`, take the length-`len(s1)` slice and test
whether it is an anagram of `s1` by sorting or by comparing frequency counts.

```python
def checkInclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    target = sorted(s1)
    for i in range(m - n + 1):
        if sorted(s2[i:i + n]) == target:
            return True
    return False
```

- **Time:** O((m - n) * n log n) with sorting, or O((m - n) * n) if you rebuild
  a fresh count map per window. Either way it re-scans each window from scratch.
- **Space:** O(n) for the slice / counts.

## Optimal Approach (Fixed-Size Sliding Window)

A permutation of `s1` has exactly `len(s1)` characters, so only windows of that
length can match. Build a frequency count `need` for `s1` and a running count
`window` for the current length-`n` slice of `s2`. Slide the window one step at
a time: add the entering character on the right and remove the leaving
character on the left. The window is a permutation of `s1` exactly when
`window == need`.

To avoid comparing whole maps every step (O(alphabet) per step), track a single
integer `matches` = how many distinct characters currently have the *exact*
required count. When it equals the number of distinct characters in `s1`, the
window matches.

```python
def checkInclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n > m:
        return False

    need = [0] * 26
    window = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1

    def idx(c):
        return ord(c) - 97

    # Prime the first window of size n.
    for i in range(n):
        window[idx(s2[i])] += 1
    if window == need:
        return True

    # Slide: add s2[right], drop s2[right - n].
    for right in range(n, m):
        window[idx(s2[right])] += 1
        window[idx(s2[right - n])] -= 1
        if window == need:
            return True
    return False
```

Comparing two 26-length arrays is O(26) = O(1), so the whole scan is linear.
(The `matches`-counter variant makes each step strictly O(1) without the array
compare, but the fixed 26-size compare is already constant-time.)

### Why it is correct

Two strings are permutations of each other iff they have identical character
frequency vectors. The window always holds exactly the last `n` characters
ending at `right`, and `window` is its exact frequency vector maintained
incrementally (add one, remove one per slide). Checking `window == need` after
each slide therefore tests every length-`n` substring of `s2` for the
anagram property. If any matches we return `True`; if none do across all
`m - n + 1` positions, no permutation exists and we return `False`.

### Step-by-step on `s1 = "ab"`, `s2 = "eidbaooo"`

`need = {a:1, b:1}`, window size 2.

| window slice | counts | equals need? |
|---|---|---|
| `ei` | `{e:1,i:1}` | no |
| `id` | `{i:1,d:1}` | no |
| `db` | `{d:1,b:1}` | no |
| `ba` | `{b:1,a:1}` | **yes** -> return True |

- **Time:** O(m) — one pass, constant work per position.
- **Space:** O(1) — two fixed 26-slot arrays (O(alphabet)).

## Key Insights & Edge Cases

- **`len(s1) > len(s2)`:** no window can be large enough; return `False`
  immediately.
- **Fixed vs variable window:** because the answer length is known
  (`len(s1)`), this is a *fixed-size* window — you add and remove exactly one
  character per step, keeping the window length constant.
- **Prime the first window before sliding**, otherwise you miss the match that
  occurs at the very first `n` characters.
- **Incremental counts beat recomputing.** Rebuilding the count map each step
  reintroduces the O(n) factor and loses the speedup.
- **Anagram, not equality:** `"ba"` matches `"ab"` — order inside the window
  does not matter, only multiplicities do.
