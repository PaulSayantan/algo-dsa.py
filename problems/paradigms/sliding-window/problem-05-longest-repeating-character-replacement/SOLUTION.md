# Longest Repeating Character Replacement — Solution

## Brute Force

For every substring `s[i .. j]`, count the most frequent character `f` in it. The
substring can be made uniform iff `(j - i + 1) - f <= k` (the other characters get
replaced). Track the longest such substring.

```python
best = 0
for i in range(len(s)):
    count = {}
    for j in range(i, len(s)):
        count[s[j]] = count.get(s[j], 0) + 1
        length = j - i + 1
        if length - max(count.values()) <= k:
            best = max(best, length)
return best
```

- **Time:** O(n^2) (the running `max` keeps the inner work O(Σ) per step).
- **Space:** O(Σ).

## Optimal Approach (Sliding Window)

A window `[left, right]` is **valid** when the number of characters we must replace to
make it uniform is at most `k`:

```
(right - left + 1) - maxFreq <= k
```

where `maxFreq` is the highest single-character frequency inside the window. We keep a
26-element `count` array and expand the window; whenever it becomes invalid, we slide
`left` forward by one.

1. Initialize `left = 0`, `max_freq = 0`, an empty `count` map, and `best = 0`.
2. For each `right`:
   - Increment `count[s[right]]` and update `max_freq = max(max_freq, count[s[right]])`.
   - If the window is invalid — `(right - left + 1) - max_freq > k` — then decrement
     `count[s[left]]` and advance `left` by one. (Using an `if`, not a `while`, keeps
     the window from ever shrinking below the best length seen so far.)
   - The current window length `right - left + 1` is a candidate answer.
3. Return the largest window length reached, which is `n - left` at the end (or simply
   track `best` explicitly).

**Why it is correct:** The answer we ultimately want is a maximum length. Once we find
a valid window of some length `L`, we never need a *shorter* valid window, so the
window is only ever allowed to grow or shift — never shrink. If adding `s[right]`
makes the window invalid, sliding `left` by exactly one keeps the width unchanged
(it can only grow again later when a longer valid window appears). Therefore the final
window width equals the maximum valid length.

A subtle point: `max_freq` is **not** decreased when characters leave the window. That
is fine — `max_freq` may then be an overestimate, but an overestimate can only make
the validity test *looser*, so it never lets the window grow beyond the true best. The
recorded best length remains correct.

```python
count = {}
left = 0
max_freq = 0
best = 0
for right in range(len(s)):
    count[s[right]] = count.get(s[right], 0) + 1
    max_freq = max(max_freq, count[s[right]])
    if (right - left + 1) - max_freq > k:
        count[s[left]] -= 1
        left += 1
    best = max(best, right - left + 1)
return best
```

- **Time:** O(n) — a single pass; `left` and `right` each move at most `n` times.
- **Space:** O(Σ) = O(1) for the fixed 26-letter count map.

## Key Insights & Edge Cases

- **The validity invariant `windowLen - maxFreq <= k`** is the whole trick: the
  characters to replace are exactly `windowLen - maxFreq`.
- **Never letting `max_freq` shrink is intentional and safe.** This is the most
  commonly misunderstood part; a stale (too-large) `max_freq` cannot cause an invalid
  window to grow, only prevents needless shrinking, and the answer only ever increases.
- **Use `if` to shift, not `while` to shrink.** Because we only care about the maximum
  length, holding the window width steady is what makes this an O(n) one-pass method.
- **k = 0:** reduces to the longest run of a single repeated character.
- **k >= n - maxFreqOverall / whole string uniform-able:** the answer is `n` (e.g.
  `"ABAB", k = 2`).
- **Single character string:** returns 1.
