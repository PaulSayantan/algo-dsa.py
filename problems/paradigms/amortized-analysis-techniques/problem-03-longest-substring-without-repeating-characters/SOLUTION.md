# Solution — Longest Substring Without Repeating Characters

## Brute Force

Check every substring for distinctness and keep the longest valid one.

```python
def lengthOfLongestSubstring(s):
    n = len(s)
    best = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best
```

- **Time:** O(n^2) — for each start index we may scan almost the whole string.
- **Space:** O(min(n, alphabet)) for the `seen` set.

## Optimal Approach (Amortized Analysis with a Sliding Window)

Maintain a window `[left, right]` that always contains **distinct** characters, plus a
dictionary `last` mapping each character to the most recent index where it appeared.
Slide `right` from left to right. When `s[right]` was seen at a position **inside** the
current window, jump `left` to just past that previous occurrence.

```
last = {}                       # char -> last index seen
left = 0
best = 0
for right, c in enumerate(s):
    if c in last and last[c] >= left:
        left = last[c] + 1       # shrink window to drop the duplicate
    last[c] = right
    best = max(best, right - left + 1)
return best
```

Reference implementation:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last: dict[str, int] = {}
        left = 0
        best = 0
        for right, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = right
            best = max(best, right - left + 1)
        return best
```

### Why it is correct

The invariant is that `s[left..right]` has no repeated character. When a duplicate of
`c` is found at old position `p = last[c]` with `p >= left`, the only way to restore the
invariant while still ending at `right` is to move `left` to `p + 1` (removing the old
`c`). We never need to move `left` **backward**: a character removed from the left can
never re-enter a window that only grows on the right. Tracking `best` at every step
captures the maximum valid length.

### Why it is O(n) (the amortized argument)

The `left` pointer looks like it could jump a long distance on a single iteration, which
tempts an O(n^2) estimate. But use the **aggregate / potential** view: `left` only ever
**increases**, from 0 to at most n, across the *entire* run. `right` also advances
exactly n times. So the **combined total movement of both pointers is at most 2n**. Each
character is added to the window once (when `right` passes it) and effectively removed at
most once (when `left` passes it) ⇒ **O(n) total**, **O(1) amortized per character**.

Formally, take potential Φ = `left`. Each outer step does O(1) real work plus possibly
advancing `left` by k; the k advance is "prepaid" because Φ rose by k earlier. Summed
over the run, ΔΦ telescopes to at most n.

- **Time:** O(n) total.
- **Space:** O(min(n, |alphabet|)) for the last-seen map.

## Key Insights & Edge Cases

- **Never move `left` backward.** The guard `last[c] >= left` ensures a duplicate seen
  *before* the current window (already evicted) does not wrongly shrink it. Without this
  guard, `"abba"` returns the wrong answer.
- Empty string returns 0; `best` initialized to 0 handles it with no special case.
- All-same input like `"bbbbb"` → the window never exceeds size 1, so answer 1.
- A fixed-size `int[128]` array of last-seen indices can replace the dict for ASCII
  input, giving O(1) lookups and a tiny constant.
- This monotone-pointer pattern is the sliding-window sibling of the monotonic-stack
  problems: forward-only pointers are what make the amortized O(n) bound hold.
