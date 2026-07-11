# Solution — Maximum Number of Non-overlapping Palindrome Substrings

## Brute Force

Enumerate every substring, keep those that are palindromes of length `>= k`,
then search for the largest set of non-overlapping intervals (interval
scheduling). Even just generating and palindrome-checking all substrings is
`O(n³)`, and reasoning over subsets on top of that is worse.

```python
def maxPalindromes(s, k):
    n = len(s)
    intervals = []
    for i in range(n):
        for j in range(i, n):
            if j - i + 1 >= k:
                sub = s[i:j + 1]
                if sub == sub[::-1]:
                    intervals.append((j, i))  # (end, start)
    # classic weighted-by-1 interval scheduling: sort by end, greedily pick
    intervals.sort()
    count, last_end = 0, -1
    for end, start in intervals:
        if start > last_end:
            count += 1
            last_end = end
    return count
```

- **Time:** `O(n³)` just to build the palindrome list (dominant term).
- **Space:** `O(n²)` for the interval list.

## Optimal Approach — Greedy Sweep with Expand Around Center

**Two ideas combine here.**

1. **Interval-scheduling greedy:** to maximize the count of non-overlapping
   intervals, repeatedly pick the interval that *ends earliest*, then discard
   everything overlapping it. Fewer characters consumed leaves more room for
   future picks.

2. **Shortest qualifying palindrome per center:** when expanding around a center,
   the *first* time the window reaches length `>= k` gives the **shortest**
   palindrome centered there. That is exactly the earliest-ending candidate we
   want for the greedy — a length-`k` palindrome is as good as any longer one
   centered at the same spot, and it frees up more of the string.

So we sweep centers left to right; the moment expansion (bounded so it can't
reach into already-consumed territory) yields a palindrome of length `>= k`, we
take it, advance a `start` boundary past its end, and keep going.

```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        start = 0  # left boundary: don't reuse characters before this index

        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)  # +0 for odd centers, +1 for even
            # Expand, but never cross into already-taken region (left >= start).
            while left >= start and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    ans += 1
                    start = right + 1  # consume up to `right`
                    break              # shortest qualifying palindrome taken
                left -= 1
                right += 1

        return ans
```

**Why it is correct.** Processing centers left to right, the first palindrome of
length `>= k` we encounter is the one that ends earliest among all still-eligible
palindromes (its center is leftmost and we take its shortest qualifying width).
By the interval-scheduling exchange argument, always picking the earliest-ending
compatible interval is optimal for maximizing the count. The `left >= start`
guard enforces non-overlap: expansions cannot pull in characters already claimed
by a previously selected palindrome.

**Step by step on `s = "abaccdbbd"`, `k = 3`:**

- Centers sweep from the left. At the center on index 1 (`b`), expansion gives
  `"aba"` (indices 0-2), length `3 >= k`. Take it, set `start = 3`, `ans = 1`.
- Continue sweeping. Around the `bb` region, the even center between indices 6
  and 7 expands to `"dbbd"` (indices 5-8), length `4 >= k`. Take it,
  `start = 9`, `ans = 2`.
- No further qualifying palindrome fits. Answer = `2`. ✅

For `s = "aabbaa"`, `k = 2`: greedily take `"aa"` (0-1), then `"bb"` (2-3), then
`"aa"` (4-5) → `3`. For `s = "adbcda"`, `k = 2`: no palindrome of length `>= 2`
exists → `0`.

- **Time:** `O(n²)` — `2n - 1` centers, each expansion `O(n)`. (In practice the
  `break` after the first qualifying hit and the `start` boundary make it fast.)
- **Space:** `O(1)` extra.

## Key Insights & Edge Cases

- **Greedy beats DP in simplicity here.** A DP over prefixes
  (`dp[i] = max(dp[i-1], dp[j] + 1)` for a length-`>=k` palindrome ending at
  `i`) also works in `O(n²)`, but the greedy sweep is shorter and uses `O(1)`
  space. Both rely on expand-around-center to identify palindromes.
- **Take the shortest, not the longest.** Grabbing a longer palindrome than
  necessary consumes extra characters and can only hurt the count — this is the
  crux of correctness.
- **The `left >= start` bound is what enforces non-overlap** during expansion; it
  prevents a new palindrome from stealing characters already assigned.
- **`k = 1`** turns every single character into a valid pick, so the answer is
  `n` (each character taken).
- **No qualifying palindrome** (`"adbcda", k=2`) correctly returns `0`.
- **Center indexing trick:** iterating `center` in `[0, 2n-2)` with
  `left = center // 2`, `right = left + center % 2` enumerates all odd and even
  centers in strict left-to-right order, which the greedy relies on.
