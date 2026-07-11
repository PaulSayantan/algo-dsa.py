# Solution — Minimum Window Substring

## Brute Force

Try every pair of indices `(i, j)`, and for each candidate substring `s[i:j]`
check whether it covers all of `t` by comparing frequency counts. Keep the
shortest that covers `t`.

```python
def minWindow(s: str, t: str) -> str:
    from collections import Counter
    need = Counter(t)
    best = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            window = Counter(s[i:j])
            if all(window[c] >= need[c] for c in need):
                if best == "" or (j - i) < len(best):
                    best = s[i:j]
                break  # shortest window starting at i found
    return best
```

- **Time:** O(n^2 * alphabet) — O(n^2) substrings, each checked against the
  need map. Rebuilding counts makes it even worse without the incremental
  trick.
- **Space:** O(alphabet) for the counters.

## Optimal Approach (Expand / Contract Sliding Window)

Keep a window `[left, right]`. Precompute `need`, the required count of each
character in `t`, and the number of distinct characters `required = len(need)`.
Maintain `have`, the number of distinct characters currently satisfied
(window count `>=` need count). The window covers `t` exactly when
`have == required`.

Two phases interleave as you sweep `right` across `s`:

1. **Expand:** add `s[right]` to `window`; if it just reached its needed count,
   increment `have`.
2. **Contract:** while `have == required` (window is valid), record it if it is
   the smallest so far, then try to shrink: remove `s[left]`; if that drops a
   character below its needed count, decrement `have` and stop contracting.

```python
def minWindow(s: str, t: str) -> str:
    if not s or not t or len(t) > len(s):
        return ""

    from collections import Counter
    need = Counter(t)
    required = len(need)      # distinct chars that must be satisfied

    window = {}
    have = 0
    best_len = float("inf")
    best_left = 0
    left = 0

    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1

        # Contract while the window still covers t.
        while have == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                have -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_left:best_left + best_len]
```

### Why it is correct

For each `right`, the inner `while` shrinks `left` as far as possible while the
window still covers `t`; the moment before it stops, `[left, right]` is the
*shortest covering window whose right end is `right`*. Any covering window is
the shortest-for-some-right-endpoint, so taking the minimum over all `right`
finds the global shortest. The `have`/`required` bookkeeping detects coverage
in O(1) per step instead of comparing full maps: `have` counts distinct
characters whose window count meets the need, and it equals `required` iff
every needed character is present in sufficient quantity. Both pointers move
only forward, so the sweep is linear.

### Step-by-step on `s = "ADOBECODEBANC"`, `t = "ABC"`

`need = {A:1, B:1, C:1}`, `required = 3`.

1. Expand to `right = 5`: window `ADOBEC` — first time `have == 3`. Contract:
   `A` is needed, dropping it breaks coverage, so left stops at 1. Best so far
   `ADOBEC` (len 6).
2. Continue expanding; at `right = 10` the window `CODEBA` covers `ABC` again.
   Contract from the left past `C`,`O`,`D`,`E` down to `BA...` — record
   `ODEBANC`/`CODEBANC` style candidates, each longer than or equal to 6 until
   a tighter one appears.
3. At `right = 12` (`...BANC`), contracting yields window `BANC` (len 4), which
   covers `A`,`B`,`C` and beats the previous best.

Result: `"BANC"`.

- **Time:** O(len(s) + len(t)) — building `need` is O(len(t)); the sweep visits
  each character of `s` at most twice (once by `right`, once by `left`).
- **Space:** O(alphabet) for `need` and `window`.

## Key Insights & Edge Cases

- **No covering window exists** (e.g. `t = "aa"`, `s = "a"`): `best_len` stays
  infinite, so return `""`.
- **`len(t) > len(s)`:** short-circuit to `""`.
- **Duplicates in `t` matter:** `need` stores *counts*, so `t = "AABC"`
  requires two `A`s in the window; the `window[ch] == need[ch]` test is what
  correctly counts multiplicities.
- **`have` only changes at the exact threshold:** increment when a count first
  *reaches* its need, decrement when it first drops *below* — using `==` and
  `<` (not `>=`) prevents double counting.
- **Record before shrinking** inside the `while`, so the smallest valid window
  at each right endpoint is captured before it is broken.
- **Extra characters are allowed:** the window may contain characters not in
  `t`; they simply inflate the length, which the contraction phase minimizes.
