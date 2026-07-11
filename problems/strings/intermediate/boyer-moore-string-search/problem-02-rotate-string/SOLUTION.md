# Solution — Rotate String

## Brute Force

Try all `n` possible rotations of `s` and compare each to `goal`.

```python
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return any(s[i:] + s[:i] == goal for i in range(len(s)))
```

- **Time:** `O(n^2)` — `n` rotations, each an `O(n)` string build/compare.
- **Space:** `O(n)` for each rotated candidate.

## Optimal Approach — Boyer–Moore (string search)

### The reduction

Every rotation of `s` is a length-`n` window of `s + s`:

```
s = "abcde"
s + s = "abcdeabcde"
windows: abcde | bcdea | cdeab | deabc | eabcd
```

So `goal` is a rotation of `s` **iff** `len(s) == len(goal)` **and** `goal` is a
substring of `s + s`. The length guard is essential: without it, a short `goal`
(like `"a"` vs `s = "aa"`) could match as a substring while not being a
rotation.

### Algorithm

1. If `len(s) != len(goal)`, return `False`.
2. If `s == ""` (and lengths equal, so `goal == ""`), return `True`.
3. Build the text `t = s + s` and run Boyer–Moore to find `goal` in `t`.
4. Return `True` iff an occurrence is found.

```python
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    if s == "":
        return True
    return boyer_moore_search(s + s, goal) != -1
```

`boyer_moore_search` is the standard right-to-left matcher with the
bad-character and good-suffix rules (see Problem 1's answer key). Because we only
need existence, we stop at the first match.

### Why it is correct

- **(⇒)** If `goal` is a rotation `s[i:] + s[:i]`, then it equals the window of
  `s + s` starting at index `i`, so Boyer–Moore finds it.
- **(⇐)** If Boyer–Moore finds `goal` at index `i` of `s + s` with `0 <= i < n`
  (guaranteed since `len(goal) == n` and `t` has length `2n`), then
  `goal = t[i:i+n] = s[i:] + s[:i]`, exactly the rotation by `i`.

Boyer–Moore itself is correct because its shift rules never skip a valid
alignment (see Problem 1).

### Complexity

- **Preprocess `goal`:** `O(n + |Σ|)`.
- **Search over `s + s` (length `2n`):** `O(n · m) = O(n^2)` worst case but
  typically sublinear; best case `O(n / m)`. In practice far faster than the
  brute force for larger inputs.
- **Space:** `O(n)` for the concatenation plus `O(n + |Σ|)` for the tables.

## Key Insights & Edge Cases

- **Length check first** — it is both a fast reject and required for
  correctness. `s = "aa", goal = "a"` returns `False` even though `"a"` is a
  substring of `"aaaa"`.
- **Empty strings**: two empty strings are trivially rotations → `True`.
- Searching `s + s` (not the whole `s + s` plus wraparound tricks) is enough
  because any rotation begins at some index `0 <= i < n`, all of which are valid
  start positions inside a `2n`-length text for a length-`n` pattern.
- The same "search in the doubled string" reduction reappears often (necklace /
  cyclic-string problems); pairing it with a fast matcher like Boyer–Moore is a
  common competitive-programming idiom.
