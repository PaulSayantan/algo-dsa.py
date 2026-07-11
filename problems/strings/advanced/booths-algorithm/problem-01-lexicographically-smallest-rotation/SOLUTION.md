# Solution — Lexicographically Smallest Rotation

## Brute Force

Generate every rotation and keep the minimum.

```python
def smallest_rotation_brute(s: str) -> str:
    n = len(s)
    best = s
    for i in range(1, n):
        cand = s[i:] + s[:i]
        if cand < best:
            best = cand
    return best
```

- Building each rotation is `O(n)` and comparing two length-`n` strings is `O(n)`,
  and we do this `n` times.
- **Time:** `O(n^2)` (worst case, e.g. `"aaaa...ab"`). **Space:** `O(n)` per candidate.

For `n` up to `10^6` this is far too slow.

## Optimal Approach — Booth's Algorithm

Booth's Algorithm computes the index `k` of the least rotation in a single `O(n)`
pass. The key ideas:

1. **Double the string.** Every rotation of `s` (length `n`) appears as a length-`n`
   substring of `ss = s + s` starting at some index in `[0, n)`. So finding the least
   rotation becomes: find the start index `k` in `[0, n)` such that
   `ss[k : k + n]` is minimal.

2. **Failure-function scan (a KMP variant).** We build a failure array `f` over `ss`
   while maintaining the best candidate start `k` seen so far. As we extend a match
   between the candidate rotation and a later position, we compare characters:
   - If the new character continues to *match* the current best, we extend `f`.
   - If it is *smaller*, we have found a lexicographically better rotation and jump
     the candidate `k` forward to a new start.
   - If it is *larger*, the current candidate stays; we fall back through `f` (exactly
     like KMP failure links) to realign.

   Each of these three outcomes advances progress so that the total work is linear.

3. **Answer.** `k % n` is the start index; the least rotation is `s[k:] + s[:k]`.

### Reference implementation

```python
def least_rotation(s: str) -> int:
    n = len(s)
    ss = s + s
    f = [-1] * len(ss)          # failure function
    k = 0                       # least-rotation candidate start
    for j in range(1, len(ss)):
        sj = ss[j]
        i = f[j - k - 1]
        while i != -1 and sj != ss[k + i + 1]:
            if sj < ss[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != ss[k + i + 1]:
            if sj < ss[k]:      # here i == -1
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k % n


def smallest_rotation(s: str) -> str:
    if not s:
        return s
    k = least_rotation(s)
    return s[k:] + s[:k]
```

### Why it is correct

The invariant is that after processing prefix `ss[0..j]`, `k` is the start of the
lexicographically smallest rotation *begin position* consistent with the characters
seen so far. The failure links guarantee that when a mismatch that is *larger* occurs,
the next viable candidate start is reached without rescanning already-matched
characters — giving amortized `O(1)` work per position, hence `O(n)` total.

- **Time:** `O(n)` — one pass over `ss` of length `2n`; the inner `while` follows
  failure links whose total traversal is amortized linear.
- **Space:** `O(n)` for `f`. (You can trim the doubled string to length `2n - 1` or
  compare indices modulo `n` to save memory; the asymptotics are unchanged.)

## Key Insights & Edge Cases

- **Ties / periodic strings** (`"abab"`, `"aaaa"`): several rotations are equal
  strings. Booth's returns one valid start index; the returned *string* is unique, so
  any tie-break is fine for this problem.
- **All-equal strings** (`"aaaa"`): the answer is the string itself; Booth's returns
  `k = 0`.
- **Length 1 or empty:** trivially the string itself. Guard the empty case before
  indexing `ss[k]`.
- **Largest rotation instead of smallest:** flip every `<` to `>` in the comparisons.
- **Alternative linear-time methods:** Duval's Lyndon factorization also yields the
  least rotation in `O(n)`, and a suffix array / suffix automaton on `s + s` works too.
  Booth's is the leanest and most cache-friendly for this exact task.
