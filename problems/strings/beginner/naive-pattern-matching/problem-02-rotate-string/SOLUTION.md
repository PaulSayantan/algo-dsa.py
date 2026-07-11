# Solution — Rotate String

## Brute Force

Generate every rotation of `s` and check whether any equals `goal`. There are `len(s)`
rotations; produce each by moving the front character to the back.

```python
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    cur = s
    for _ in range(len(s)):
        if cur == goal:
            return True
        cur = cur[1:] + cur[:1]   # one left shift
    return False
```

- **Time:** `O(n^2)` — `n` rotations, and each rotation build + comparison is `O(n)`.
- **Space:** `O(n)` for the rotated string built each iteration.

## Optimal Approach (Naive Pattern Matching)

**Key reduction.** Every rotation of `s` appears as a length-`n` window of `s + s`.
Writing `s = "abcde"`, the doubled string `"abcdeabcde"` contains `"abcde"`,
`"bcdea"`, `"cdeab"`, `"deabc"`, `"eabcd"` as consecutive windows — exactly the set of
all rotations. So `goal` is a rotation of `s` **iff** `len(s) == len(goal)` **and**
`goal` is a substring of `s + s`. We locate that substring with naive matching.

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        text = s + s
        n, m = len(text), len(goal)
        for start in range(n - m + 1):
            j = 0
            while j < m and text[start + j] == goal[j]:
                j += 1
            if j == m:
                return True
        return False
```

**Why it is correct.**
- The length check is necessary: rotation preserves length, so unequal lengths mean
  `False` immediately. It also handles the tricky case `s = ""`, `goal = "x"`.
- If `goal` starts at index `start` in `s + s` with `0 <= start < n`, then it equals the
  rotation of `s` by `start` positions, so `True` is correct.
- Conversely, if `goal` is a rotation by `k`, it appears at index `k` of `s + s`, so the
  search finds it. Because both strings have equal length, no match can start beyond
  index `len(s)` that isn't already a duplicate of an earlier rotation, so scanning
  `start` up to `n - m` suffices.

**Step-by-step** on `s = "abcde"`, `goal = "cdeab"`: build `text = "abcdeabcde"`. Sliding
`goal` over `text`, the alignment at `start = 2` gives `text[2:7] = "cdeab"`, which
matches all 5 characters -> return `True`.

- **Time:** `O(n · m) = O(n^2)` worst case where `n = m = len(s)`; linear on typical
  inputs thanks to the early mismatch exit.
- **Space:** `O(n)` for the doubled string `s + s`; the search itself is `O(1)`.

## Key Insights & Edge Cases

- **The `s + s` trick** is the whole problem. Once you see it, rotation-detection becomes
  a plain substring search.
- **Always check lengths first.** `goal` could be a substring of `s + s` while being
  shorter than `s` (e.g. `s = "ab"`, `goal = "a"`); the length guard rejects that.
- **Equal strings / zero shift.** `s == goal` matches at `start = 0`, returning `True`.
- **All-identical characters.** `s = "aaaa"`, `goal = "aaaa"` triggers the naive
  worst case (many full-length comparisons) but is still correct.
- You can swap the naive search for KMP to get `O(n)`; the reduction to substring search
  stays identical.
