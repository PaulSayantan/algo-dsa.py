# Minimum Window Substring — Solution

## Brute Force

Enumerate every substring `s[i .. j]` and check whether it covers `t` (its character
counts dominate `t`'s counts). Keep the shortest one that does.

```python
from collections import Counter
need = Counter(t)
best = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        window = Counter(s[i:j + 1])
        if all(window[c] >= need[c] for c in need):
            if best == "" or (j - i + 1) < len(best):
                best = s[i:j + 1]
return best
```

- **Time:** O(m^2 · Σ) — O(m^2) substrings, each coverage check O(Σ).
- **Space:** O(Σ).

Far too slow for `m` up to `10^5`.

## Optimal Approach (Sliding Window)

Maintain a window `[left, right]` and two ideas:

- `need[c]` — how many of character `c` the window still requires (built from `t`).
- `required` — the number of **distinct** characters in `t` whose full quota is not
  yet met inside the window. When `required == 0`, the window covers `t`.

We use a `formed` counter of how many distinct requirements are currently satisfied,
and grow/shrink to find the minimum window.

1. Build `need = Counter(t)`; let `required = len(need)`.
2. Keep `window` counts, `formed = 0`, `left = 0`, and a best answer `(length, l, r)`
   initialized to "infinite length".
3. Move `right` across `s`. For `c = s[right]`:
   - `window[c] += 1`.
   - If `c` is in `need` and `window[c] == need[c]`, one more requirement is fully
     met: `formed += 1`.
   - **While `formed == required`** (the window is valid), try to shrink:
     - Record the window if `right - left + 1` beats the best.
     - Let `d = s[left]`; do `window[d] -= 1`. If `d` is in `need` and
       `window[d] < need[d]`, that requirement is broken again: `formed -= 1`.
     - Advance `left`.
4. Return the best substring recorded, or `""` if none was ever valid.

**Why it is correct:** `formed == required` holds exactly when every character of `t`
is present in the window with at least its required multiplicity — a valid covering
window. For each `right` we shrink from the left as far as possible while still valid,
which yields the shortest valid window *ending at or before* `right`. Taking the
minimum over all `right` gives the global minimum. `left` and `right` only ever move
forward, so it is a single linear sweep.

```python
from collections import Counter

if not t or not s:
    return ""
need = Counter(t)
required = len(need)
window = {}
formed = 0
left = 0
best_len = float("inf")
best_l = 0
for right, c in enumerate(s):
    window[c] = window.get(c, 0) + 1
    if c in need and window[c] == need[c]:
        formed += 1
    while formed == required:
        if right - left + 1 < best_len:
            best_len = right - left + 1
            best_l = left
        d = s[left]
        window[d] -= 1
        if d in need and window[d] < need[d]:
            formed -= 1
        left += 1
return "" if best_len == float("inf") else s[best_l:best_l + best_len]
```

- **Time:** O(m + n) — each character of `s` enters and leaves the window at most once;
  count comparisons are O(1).
- **Space:** O(Σ) for the `need` and `window` maps (bounded by the alphabet, ~52).

## Key Insights & Edge Cases

- **Track `formed` vs `required`, not full map equality.** Incrementing `formed` only
  when a count reaches (not exceeds) its requirement makes coverage testing O(1) and
  correctly handles duplicate demands like `t = "aa"`.
- **Coverage means `>=`, not `==`.** The window may hold extra copies of a character;
  that is fine as long as each required quota is met. Note the shrink test uses
  `window[d] < need[d]` (strictly less) so surplus copies are dropped for free.
- **Duplicates in `t`:** using counts (a multiset) rather than a set is essential —
  `t = "aa"` needs two `a`s (Example 3 returns `""` when only one exists).
- **No valid window:** the `best_len == infinity` sentinel yields `""`.
- **Shrink with `while`, not `if`:** unlike the character-replacement problem, here we
  want the *minimum* length, so we must contract fully while the window stays valid.
- **`t` longer than `s`, or characters missing:** `formed` never reaches `required`,
  so the answer is `""`.
