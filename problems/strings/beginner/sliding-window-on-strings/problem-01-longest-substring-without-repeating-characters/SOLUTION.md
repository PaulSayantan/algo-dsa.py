# Solution — Longest Substring Without Repeating Characters

## Brute Force

Enumerate every substring and check whether it has all distinct characters,
keeping the longest length that passes.

```python
def lengthOfLongestSubstring(s: str) -> int:
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

- **Time:** O(n^2) — a start index `i` and an extend index `j`. (The naive
  "check each of the O(n^2) substrings for uniqueness in O(n)" is O(n^3); the
  early `break` above trims it to O(n^2).)
- **Space:** O(min(n, alphabet)) for the `seen` set.

## Optimal Approach (Sliding Window)

Maintain a window `[left, right]` that is guaranteed to contain only distinct
characters. Move `right` forward one character at a time. Track how many times
each character currently sits inside the window (a count map, or a
last-seen-index map). When the incoming character `s[right]` would create a
duplicate, advance `left` — dropping characters out of the window — until the
duplicate is removed. After each extension the window is valid, so update the
best length.

```python
def lengthOfLongestSubstring(s: str) -> int:
    last_seen = {}          # char -> most recent index
    left = 0
    best = 0
    for right, ch in enumerate(s):
        # If ch was seen inside the current window, jump left past it.
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

An equivalent formulation uses a set and a `while` loop to evict from the left:

```python
def lengthOfLongestSubstring(s: str) -> int:
    window = set()
    left = best = 0
    for right, ch in enumerate(s):
        while ch in window:
            window.remove(s[left])
            left += 1
        window.add(ch)
        best = max(best, right - left + 1)
    return best
```

### Why it is correct

The window invariant is "all characters in `s[left..right]` are distinct." We
only ever add `s[right]` after guaranteeing no copy of it remains in the
window (either by the `while` eviction or by jumping `left` past the previous
occurrence). Because `left` never moves backward, once a candidate window is
maximal for a given `right`, no earlier `left` could give a longer valid
window ending at `right` — a smaller `left` would reintroduce the duplicate.
Taking the max over all `right` therefore finds the global longest.

### Step-by-step on `"pwwkew"`

| right | ch | action | window | best |
|---|---|---|---|---|
| 0 | p | add | `p` | 1 |
| 1 | w | add | `pw` | 2 |
| 2 | w | duplicate -> evict `p`,`w`; left=2; add | `w` | 2 |
| 3 | k | add | `wk` | 2 |
| 4 | e | add | `wke` | 3 |
| 5 | w | duplicate -> evict `w`; left=3; add | `kew` | 3 |

Result: `3`.

- **Time:** O(n) — `left` and `right` each advance at most `n` times total.
- **Space:** O(min(n, alphabet)) for the map/set.

## Key Insights & Edge Cases

- **Empty string** returns `0`; the loop never runs.
- **The `last_seen[ch] >= left` guard is essential.** A character seen *before*
  the current window began is not a real duplicate. Without the guard, `left`
  could jump *backward*, breaking the monotonic-pointer invariant and
  producing wrong (too-large) answers on inputs like `"abba"`.
- **Substring vs subsequence:** the window is contiguous, so `"pwke"` in
  `"pwwkew"` is not a valid answer — only contiguous runs count.
- **Alphabet size bounds space:** for a fixed alphabet (e.g. lowercase ASCII),
  the map holds at most 26/128/256 entries, so space is effectively O(1).
