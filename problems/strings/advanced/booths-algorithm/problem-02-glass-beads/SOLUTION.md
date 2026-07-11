# Solution — Glass Beads

## Brute Force

Try every cut position, build the rotation, track the smallest string and the
earliest index that produces it.

```python
def cut_position_brute(s: str) -> int:
    n = len(s)
    best = None
    best_idx = 0
    for i in range(n):
        cand = s[i:] + s[:i]
        if best is None or cand < best:   # strict '<' keeps the earliest tie
            best = cand
            best_idx = i
    return best_idx + 1
```

- Each rotation costs `O(n)` to build and `O(n)` to compare, over `n` positions.
- **Time:** `O(n^2)`. **Space:** `O(n)`.

With `n` up to `10^6` and many test cases, `O(n^2)` times out.

## Optimal Approach — Booth's Algorithm

This is the textbook use case: we want the *index* of the least rotation, which is
exactly what Booth's Algorithm computes. Then convert to 1-based.

```python
def least_rotation(s: str) -> int:
    n = len(s)
    ss = s + s
    f = [-1] * len(ss)
    k = 0
    for j in range(1, len(ss)):
        sj = ss[j]
        i = f[j - k - 1]
        while i != -1 and sj != ss[k + i + 1]:
            if sj < ss[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != ss[k + i + 1]:
            if sj < ss[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k % n


def cut_position(s: str) -> int:
    return least_rotation(s) + 1
```

### Why it is correct

- Booth's scans `s + s`, maintaining `k` = the start of the smallest rotation
  consistent with the characters processed so far. The candidate only moves forward
  when a *strictly smaller* rotation is discovered, so among equal (tied) rotations the
  algorithm keeps the earliest start — precisely the "smallest position on tie" rule
  the problem demands.
- Because each character is processed once and failure-link fallbacks are amortized
  `O(1)`, the whole scan is linear.

- **Time:** `O(n)` per necklace. **Space:** `O(n)` for the failure array.

## Key Insights & Edge Cases

- **1-based conversion:** the only difference from the raw algorithm is `+ 1`.
- **Tie-break correctness:** verify your comparison uses strict `<` when updating the
  candidate so periodic inputs like `"abab"` return the *earliest* index (1, not 3).
- **Single character / all-same:** returns 1.
- **Performance across many test files:** UVa/POJ feed many necklaces; keep the failure
  array allocation tight (reuse a buffer) or accept `O(n)` allocation per case — both
  pass since total input is bounded.
- **Alphabet:** only lowercase letters here, but Booth's works for any totally ordered
  alphabet without change.
