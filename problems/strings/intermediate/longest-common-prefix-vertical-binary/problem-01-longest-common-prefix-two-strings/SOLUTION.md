# Solution — Longest Common Prefix of Two Strings

## Brute Force

Generate every prefix of `a` (there are `len(a) + 1` of them, from `""` up to all of
`a`), and for each check whether it is also a prefix of `b`. Return the longest one that
passes.

- Building a prefix of length `k` and testing `b.startswith(prefix)` costs `O(k)`.
- Summing over `k = 0..len(a)` gives `O(len(a)^2)` in the worst case.

**Time:** `O(len(a)^2)` (or `O(len(a) * len(b))` if you test against `b` naively).
**Space:** `O(len(a))` for the prefix strings.

## Optimal Approach (Vertical Scan)

A prefix of both strings can never be longer than the shorter string. Walk the two
strings **column by column** and stop the instant they disagree.

```python
def longest_common_prefix_pair(a: str, b: str) -> str:
    limit = min(len(a), len(b))
    i = 0
    while i < limit and a[i] == b[i]:
        i += 1
    return a[:i]
```

**Why it is correct.** The loop maintains the invariant *"`a[:i] == b[:i]`"*. It advances
`i` only when the next column matches, and halts either when a column mismatches (so no
longer common prefix can exist — any longer prefix would have to include this differing
character) or when `i` reaches `limit` (a prefix cannot exceed the shorter string). Thus
`a[:i]` is exactly the longest common prefix.

**Step by step for `a = "flower"`, `b = "flight"`:**

| i | a[i] | b[i] | match? |
|---|------|------|--------|
| 0 | f    | f    | yes    |
| 1 | l    | l    | yes    |
| 2 | o    | i    | no -> stop |

Result: `a[:2] = "fl"`.

**Time:** `O(min(len(a), len(b)))` — each shared character is examined once, and scanning
stops early at the first mismatch. **Space:** `O(1)` extra (the slice is the output).

## Binary Search Alternative

The predicate `match(L) = (a[:L] == b[:L])` is monotonic: if a prefix of length `L`
matches, so does every shorter prefix. Binary search the largest `L` in
`[0, min(len(a), len(b))]` for which `match(L)` holds.

```python
def longest_common_prefix_pair(a: str, b: str) -> str:
    lo, hi = 0, min(len(a), len(b))
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if a[:mid] == b[:mid]:
            lo = mid
        else:
            hi = mid - 1
    return a[:lo]
```

This performs `O(log min_len)` guesses, each an `O(L)` prefix comparison, i.e.
`O(min_len * log min_len)` — asymptotically worse than the linear scan for a plain pair,
but the same idea generalizes to arrays and to `O(1)` hashed comparisons.

## Key Insights & Edge Cases

- **Empty input:** if `a` or `b` is `""`, `limit = 0`, the loop never runs, and the
  answer is `""` — handled without special-casing.
- **One string is a prefix of the other:** e.g. `"abc"` / `"abcde"` returns `"abc"`; the
  `i < limit` guard stops at the shorter length.
- **Immediate mismatch:** `"dog"` / `"cat"` returns `""`.
- **Case sensitivity:** `'A'` and `'a'` are different characters; lowercase first if a
  case-insensitive prefix is desired.
- Returning a *slice* `a[:i]` (rather than accumulating characters) keeps the code
  `O(1)` in auxiliary space and avoids per-character string concatenation.
