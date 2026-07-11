# Solution — Maximum Number of Vowels in a Substring of Given Length

## Brute Force

For each start index `i`, look at the substring `s[i..i+k-1]` and count its vowels,
keeping the maximum.

```python
vowels = set("aeiou")
best = 0
for i in range(len(s) - k + 1):
    best = max(best, sum(c in vowels for c in s[i:i + k]))
return best
```

- **Time:** O(n·k) — each window re-scans `k` characters.
- **Space:** O(1)

## Optimal Approach (Sliding Window, Fixed Size)

The vowel count of adjacent windows differs by at most the one character entering and
the one leaving. Maintain a running `count` and update it in O(1) per slide.

1. Let `vowels = {'a','e','i','o','u'}`.
2. Count vowels in the first window `s[0..k-1]` → `count`; set `best = count`.
3. For `right` from `k` to `n - 1`:
   - If `s[right]` is a vowel, `count += 1` (character entering on the right).
   - If `s[right - k]` was a vowel, `count -= 1` (character leaving on the left).
   - `best = max(best, count)`.
   - **Early exit:** if `best == k`, no window can do better — return `k`.
4. Return `best`.

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(1 for c in s[:k] if c in vowels)
        best = count
        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1
            if s[right - k] in vowels:
                count -= 1
            best = max(best, count)
            if best == k:
                return k
        return best
```

**Why it is correct:** After the update at index `right`, `count` equals the number of
vowels in `s[right-k+1 .. right]`, because we added exactly the entering character's
contribution and removed exactly the leaving character's contribution. Every length-`k`
window is visited once, so the tracked maximum is the true answer.

**Step by step** on `s = "abciiidef", k = 3`:

1. First window `"abc"` → vowels: `a` → `count = 1`, `best = 1`.
2. `right=3` (`i`): enter `i` (+1 → 2), leave `a` (−1 → 1) — window `"bci"`, `best = 1`.
3. `right=4` (`i`): enter `i` (+1 → 2), leave `b` (0 → 2) — window `"cii"`, `best = 2`.
4. `right=5` (`i`): enter `i` (+1 → 3), leave `c` (0 → 3) — window `"iii"`, `best = 3` → equals `k`, return `3`.

Answer: `3`.

## Key Insights & Edge Cases

- **O(1) vowel test:** using a `set` (or checking membership in the string
  `"aeiou"`) keeps each entering/leaving check constant time.
- **Early termination** at `best == k` is a genuine optimization: `k` is the largest a
  window can possibly reach, so once hit you can stop immediately.
- **`k == 1`:** answer is `1` if any vowel exists, else `0` — handled naturally.
- **No vowels at all:** `count` stays `0` throughout and `0` is returned.
- Do not rebuild a substring on every step (e.g. `s[i:i+k]`) — that reintroduces the
  O(n·k) cost the window is meant to eliminate.
