# Solution — Longest Substring Without Repeating Characters

## Brute Force

Check every substring `s[l..r]` and test whether all its characters are unique
(e.g. by putting them in a set); track the longest that passes.

```python
def lengthOfLongestSubstring(s):
    n = len(s)
    best = 0
    for l in range(n):
        seen = set()
        for r in range(l, n):
            if s[r] in seen:
                break
            seen.add(s[r])
            best = max(best, r - l + 1)
    return best
```

- **Time:** `O(n^2)` substrings-ish (the early `break` helps but the worst case is
  still quadratic).
- **Space:** `O(min(n, alphabet))` for the set.

## Optimal Approach (Sliding Window, variable size)

Maintain a window `[left, right]` that always contains **distinct** characters,
using a hash map / set (or a count map) to know what is inside.

**Algorithm (longest-window flavor):**

1. Keep `left = 0` and a set `in_window` of the characters currently in the window.
2. For each `right`, look at `c = s[right]`.
3. **While** `c` is already in the window, remove `s[left]` from the set and
   advance `left` — this evicts characters until the earlier copy of `c` is gone.
4. Add `c` to the set. The window `[left, right]` is now all-distinct; update
   `best = max(best, right - left + 1)`.

```python
def lengthOfLongestSubstring(s):
    in_window = set()
    left = 0
    best = 0
    for right, c in enumerate(s):
        while c in in_window:
            in_window.discard(s[left])
            left += 1
        in_window.add(c)
        best = max(best, right - left + 1)
    return best
```

A common optimization stores each character's **last index** in a map and jumps
`left` directly to `last[c] + 1` instead of stepping one at a time — still `O(n)`,
just fewer operations:

```python
def lengthOfLongestSubstring(s):
    last = {}
    left = 0
    best = 0
    for right, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = right
        best = max(best, right - left + 1)
    return best
```

**Why it is correct.** The invariant is "`s[left..right]` has no repeats". When a
new character `c` would break the invariant, the *only* offending element is the
prior occurrence of `c`, and it sits at some index `< right` but `>= left`.
Advancing `left` past that occurrence (and no further than necessary) restores the
invariant while keeping the window as large as possible, so every position `right`
contributes the longest valid window ending there.

**Trace of Example 3** (`s = "pwwkew"`):

| right | c | window before | action | window after | best |
|------:|---|---------------|--------|--------------|-----:|
| 0 | p | "" | add p | "p" | 1 |
| 1 | w | "p" | add w | "pw" | 2 |
| 2 | w | "pw" | evict p, evict w, add w | "w" | 2 |
| 3 | k | "w" | add k | "wk" | 2 |
| 4 | e | "wk" | add e | "wke" | 3 |
| 5 | w | "wke" | evict w, add w | "kew" | 3 |

Result: `3`.

- **Time:** `O(n)` — each character is added once and removed at most once.
- **Space:** `O(min(n, alphabet))` for the map/set.

## Key Insights & Edge Cases

- **Empty string** returns `0` — the loop never runs and `best` stays `0`.
- **All identical characters** (`"bbbbb"`) collapse the window to length `1` each
  step; the answer is `1`.
- With the last-index optimization, guard with `last[c] >= left`; otherwise a
  duplicate that lies *before* the current window would wrongly pull `left`
  backward.
- The window never needs to move `left` backward; both pointers only advance,
  which is what guarantees linear time.
