# Longest Substring Without Repeating Characters — Solution

## Brute Force

Enumerate every substring `s[i .. j]` and check whether it has all-distinct
characters (e.g. by inserting into a set and detecting a collision). Track the longest
one that passes.

```python
best = 0
for i in range(len(s)):
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        best = max(best, j - i + 1)
return best
```

- **Time:** O(n^2) — O(n) starting points, each extended up to O(n).
- **Space:** O(min(n, Σ)) for the `seen` set, where Σ is the alphabet size.

## Optimal Approach (Sliding Window)

Maintain a window `[left, right]` that always contains **only distinct** characters,
plus a map `last_seen[c]` giving the most recent index at which character `c` appeared.

1. Initialize `left = 0`, `best = 0`, and an empty `last_seen` map.
2. Move `right` across the string. For the character `c = s[right]`:
   - If `c` is already in the window — that is, `c` is in `last_seen` **and**
     `last_seen[c] >= left` — then jump `left` to `last_seen[c] + 1`. This discards
     the earlier copy of `c` (and everything before it) in one step.
   - Record `last_seen[c] = right`.
   - Update `best = max(best, right - left + 1)`.
3. Return `best`.

**Why it is correct:** The guard `last_seen[c] >= left` ensures we only jump `left`
forward when the previous occurrence of `c` is *inside* the current window; a stale
occurrence that already fell out of the window is ignored, so `left` never moves
backward. Because `left` is monotonically non-decreasing and `right` advances every
step, each index is processed a constant number of times.

```python
last_seen = {}
left = 0
best = 0
for right, c in enumerate(s):
    if c in last_seen and last_seen[c] >= left:
        left = last_seen[c] + 1
    last_seen[c] = right
    best = max(best, right - left + 1)
return best
```

## Key Insights & Edge Cases

- **`left` must never move backward.** The `last_seen[c] >= left` check is the crux;
  omitting it breaks inputs like `"abba"` (the stale `'a'` at index 0 would wrongly
  pull `left` back to 1 after `left` had already advanced to 2).
- **Jump vs. one-step shrink.** Using `last_seen` lets `left` leap directly past the
  duplicate. An alternative is to keep a `set` and shrink `left` one character at a
  time in a `while` loop; both are O(n) amortized.
- **Empty string:** `best` stays `0`, which is correct.
- **All identical characters (`"bbbbb"`):** every step sets `left = right`, so the
  window length is always 1.
- **Space:** O(min(n, Σ)) for the map — bounded by the alphabet size, not `n`.
