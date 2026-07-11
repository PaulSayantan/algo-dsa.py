# Solution — Repeated String Match

## The bound (why we never repeat forever)

The crucial observation is: **how many copies could possibly be needed?**

Let `t = ceil(len(b) / len(a))`. With `t` copies, the concatenation is at least
as long as `b`. If `b` starts inside the first copy, `t` copies span it — but if
`b` starts partway through a copy, it might spill just past the end and need
**one more** copy. It can never need more than that: after enough copies to fully
contain `b` plus one spillover copy, any additional copy is pure prefix/suffix
padding that a shift of at most `len(a)` already covers.

So the only candidates are `t` and `t + 1`. If neither works, the answer is
`-1`.

## Brute Force

Build `a` repeated `t` times, then keep appending single copies of `a` and
checking `b in ...` until the string is longer than `len(b) + len(a)`.

```python
def repeatedStringMatch(a, b):
    import math
    t = math.ceil(len(b) / len(a))
    for k in (t, t + 1):
        if b in a * k:
            return k
    return -1
```

- **Time:** each `b in a * k` uses Python's built-in search; naive substring
  search is `O(len(a) * k * len(b))` in the worst case = `O((n + m) * m)` where
  `n = len(a)`, `m = len(b)`.
- **Space:** `O(n + m)` for the concatenation.

## Optimal Approach — KMP

Keep the same two-candidate bound, but replace the substring test with an
explicit KMP search so the matching itself is linear.

```python
def build_lps(p):
    m = len(p)
    lps = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and p[i] != p[k]:
            k = lps[k - 1]
        if p[i] == p[k]:
            k += 1
        lps[i] = k
    return lps

def kmp_contains(text, pattern):
    if pattern == "":
        return True
    lps = build_lps(pattern)
    j = 0
    for c in text:
        while j > 0 and c != pattern[j]:
            j = lps[j - 1]
        if c == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
    return False

def repeatedStringMatch(a, b):
    import math
    t = math.ceil(len(b) / len(a))
    for k in (t, t + 1):
        if kmp_contains(a * k, b):
            return k
    return -1
```

### Why it is correct

- **Lower bound:** we start at `t = ceil(m / n)`; fewer copies are literally too
  short to contain `b`, so we never miss a smaller valid answer.
- **Upper bound:** if `b` is a substring of `a` repeated *any* number of times,
  it must appear within a window of length `m` inside the infinite repetition
  `aaaa...`. Aligning that window against copy boundaries shows it fits inside at
  most `t + 1` copies; if it does not appear in `a * (t+1)` it never will.
- **KMP** correctly reports whether `b` occurs, in linear time in the text
  length.

### Complexity

Let `n = len(a)`, `m = len(b)`. The concatenation has length `O(n + m)` (since
`t * n <= m + n`). Building the LPS of `b` is `O(m)`; scanning the concatenation
is `O(n + m)`. Done for two candidates:

- **Time:** **O(n + m)**.
- **Space:** **O(n + m)** for the concatenation and `O(m)` for the LPS array.

## Key Insights & Edge Cases

- **Only two candidates matter.** The `t`/`t+1` bound is the whole trick;
  everything else is a standard KMP `contains` check.
- **`b` longer than a single copy is normal** — that is exactly why we repeat.
  Do not stop at one copy.
- **Impossible case:** if `b` contains a character absent from `a`, or the
  cyclic structure never lines up, both candidates fail and we return `-1`
  (e.g. `a = "abc"`, `b = "wxyz"`).
- **Off-by-one on the ceiling:** use `ceil(m / n)`, not integer floor, or you
  may start one copy short. Example 3 (`a="abc"`, `b="cabcabca"`, `m=8`,
  `n=3`) has `t = ceil(8/3) = 3`, and the real answer is `t + 1 = 4`, showing
  the `+1` candidate is genuinely necessary.
