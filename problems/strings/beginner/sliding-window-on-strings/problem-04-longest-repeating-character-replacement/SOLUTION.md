# Solution — Longest Repeating Character Replacement

## Brute Force

Consider every substring. For each, count its characters and check whether it
can be made uniform with at most `k` replacements — i.e. whether
`length - max_frequency <= k`. Track the longest length that passes.

```python
def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    best = 0
    for i in range(n):
        count = {}
        for j in range(i, n):
            count[s[j]] = count.get(s[j], 0) + 1
            length = j - i + 1
            if length - max(count.values()) <= k:
                best = max(best, length)
    return best
```

- **Time:** O(n^2) with an incremental count (the `max(count.values())` scan is
  O(alphabet) = O(1) for a fixed alphabet).
- **Space:** O(alphabet) for the count map.

## Optimal Approach (Sliding Window)

A window `[left, right]` is *feasible* if the number of characters that are NOT
the window's most frequent character is at most `k`:

```
window_length - max_freq_in_window <= k
```

Grow `right` one step at a time, updating the count of the entering character
and the running `max_freq`. If the window becomes infeasible
(`window_length - max_freq > k`), slide `left` forward by one, decrementing the
outgoing character's count. Because we only ever want a *longer* answer, a
common and correct simplification is to **never shrink by more than one per
step** — the window never grows unless we find a strictly better `max_freq`, so
its size is non-decreasing and equals the best answer at the end.

```python
def characterReplacement(s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0            # highest count of any single char ever seen in a window
    best = 0
    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])
        # If more than k chars need replacing, shrink from the left by one.
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Why the non-shrinking `max_freq` is OK

`max_freq` is never decreased when `left` advances, so it can become "stale"
(larger than the true max in the current window). That is fine: the answer is
monotonic. If the window size at some point was `W` with `max_freq = f` and
`W - f <= k`, then any later window we accept is at least as large. A stale
`max_freq` can only make the feasibility test *pass* for windows no larger than
one already achieved, so it never lets `best` exceed the true optimum, and the
genuinely-optimal window (where `max_freq` is accurate) is still reached and
recorded. The window length `right - left + 1` therefore ends at the correct
maximum.

### Step-by-step on `s = "AABABBA"`, `k = 1`

| right | ch | window | counts | max_freq | len - max_freq | best |
|---|---|---|---|---|---|---|
| 0 | A | `A` | A:1 | 1 | 0 | 1 |
| 1 | A | `AA` | A:2 | 2 | 0 | 2 |
| 2 | B | `AAB` | A:2,B:1 | 2 | 1 | 3 |
| 3 | A | `AABA` | A:3,B:1 | 3 | 1 | 4 |
| 4 | B | `AABAB` | A:3,B:2 | 3 | 2 > 1 -> shrink, left=1 | 4 |
| 5 | B | `ABABB` | A:2,B:3 | 3 | 2 > 1 -> shrink, left=2 | 4 |
| 6 | A | `BABBA` | A:2,B:3 | 3 | 2 > 1 -> shrink, left=3 | 4 |

Result: `4`.

- **Time:** O(n) — `left` and `right` each move forward at most `n` times.
- **Space:** O(alphabet) — at most 26 counts for uppercase letters, i.e. O(1).

## Key Insights & Edge Cases

- **The feasibility formula is the whole trick:** cost to make a window uniform
  = `length - max_freq` (replace everything except the majority character).
- **`k = 0`:** reduces to the longest run of a single repeated character.
- **`k >= len(s)`:** the entire string is feasible, so the answer is `len(s)`.
- **Why the single `if` (not a `while`):** the window size is monotonically
  non-decreasing; shrinking once per infeasible step preserves the largest
  size found so far without ever needing to shrink more.
- **Fixed alphabet:** with only 26 uppercase letters, `max(count.values())`
  is constant time; if you tracked `max_freq` incrementally you avoid even that.
