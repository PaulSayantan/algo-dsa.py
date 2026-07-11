# Solution — Implement strStr()

## Brute Force

The brute force *is* Naive Pattern Matching here, so the two sections are closely
related. The most literal "brute force" is: for every possible starting index, slice
out a substring of the needle's length and compare it to the needle with `==`.

```python
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    for start in range(n - m + 1):
        if haystack[start:start + m] == needle:
            return start
    return -1
```

- **Time:** `O(n · m)` — up to `n - m + 1` alignments, and each slice + `==`
  comparison costs `O(m)`.
- **Space:** `O(m)` because each `haystack[start:start + m]` builds a new substring.

## Optimal Approach (Naive Pattern Matching)

We keep the same `O(n · m)` worst case but drop the extra space by comparing character
by character in place, and we **bail out on the first mismatch** at each alignment so
typical inputs run much faster than the worst case.

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for start in range(n - m + 1):          # every valid alignment
            j = 0
            while j < m and haystack[start + j] == needle[j]:
                j += 1
            if j == m:                          # matched all m characters
                return start
        return -1
```

**Why it is correct.** A match of `needle` can begin at any index `start` in
`0 .. n - m`. Any index beyond `n - m` cannot fit `m` more characters, so we never need
to check it — that is exactly the loop's upper bound `range(n - m + 1)`. For each
`start` we compare `needle[j]` against `haystack[start + j]` for increasing `j`. The
inner loop stops either at the first mismatch (`haystack[start + j] != needle[j]`) or
when `j` reaches `m`. If `j == m`, every one of the `m` characters matched, so `needle`
occurs at `start`, and because we scan `start` in increasing order this is the *first*
occurrence. If no alignment fully matches, we correctly return `-1`.

**Step-by-step** on `haystack = "hello"`, `needle = "ll"` (`n = 5`, `m = 2`, so
`start` ranges over `0..3`):

| start | compare | result |
|-------|---------|--------|
| 0 | `h` vs `l` | mismatch at j=0 |
| 1 | `e` vs `l` | mismatch at j=0 |
| 2 | `l`==`l`, `l`==`l` | j reaches 2 = m -> return 2 |

- **Time:** `O(n · m)` worst case (e.g. `haystack = "aaaaaa"`, `needle = "aaab"`),
  `O(n)` on typical text where mismatches appear quickly.
- **Space:** `O(1)` — only the indices `start` and `j`.

## Key Insights & Edge Cases

- **Loop bound.** The last alignment worth checking is `start = n - m`. Using
  `range(n - m + 1)` includes it and excludes everything past it in one shot.
- **Empty needle.** LeetCode 28 guarantees `needle.length >= 1`, so you need not handle
  `m == 0`. If you ever generalize, note `n - m + 1 = n + 1` alignments and the first
  (index 0) trivially matches, so the convention is to return `0`.
- **Needle longer than haystack.** Then `n - m + 1 <= 0`, the `range` is empty, and the
  function correctly returns `-1` without any special case.
- **Early exit matters.** Breaking on the first mismatch is what makes the average case
  linear; do not compare the whole window unconditionally.
- **Overlap is irrelevant here** because we return on the first match, but the same loop
  is the basis for counting overlapping matches (see Problem 3).
