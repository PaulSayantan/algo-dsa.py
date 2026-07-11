# Solution — Check if a String is a Lyndon Word

## Brute Force

Directly apply the definition: a Lyndon word is strictly smaller than every proper
suffix.

```python
def is_lyndon_brute(s: str) -> bool:
    return len(s) > 0 and all(s < s[k:] for k in range(1, len(s)))
```

Each comparison `s < s[k:]` builds an `O(n)` suffix slice and compares in up to `O(n)`,
and we do it for `n - 1` suffixes.

- **Time:** `O(n^2)` (worst case, e.g. `"aaaa...ab"`).
- **Space:** `O(n)` for the slices (or `O(1)` if you compare in place with indices).

## Optimal Approach (Duval's Algorithm)

By the Chen–Fox–Lyndon theorem, every string factors uniquely into non-increasing
Lyndon words `w1 >= w2 >= ... >= wk`. A string is *itself* a Lyndon word **iff** that
factorization has exactly one factor and it equals the whole string, i.e. `k == 1`.

So we don't even need to store factors — we just check that the **first** Lyndon factor
Duval discovers has length `n`.

### Why it's correct

Duval always peels off the *longest* Lyndon prefix that starts the current non-increasing
tail... more precisely, it emits the leftmost Lyndon factor `w1` first. If `w1 == s`,
then the unique factorization is `[s]`, so `s` is Lyndon. If `w1` is shorter than `s`,
the factorization has at least two factors, so `s` cannot be Lyndon (a Lyndon word's
factorization is itself).

### Step by step

Maintain `i = 0` (factor start), `j = 1` (scan), `k = 0` (matched-prefix pointer):

1. If `s[k] < s[j]`: still a valid Lyndon prefix, reset `k = i`, advance `j`.
2. If `s[k] == s[j]`: possible periodic prefix, advance both `k` and `j`.
3. If `s[k] > s[j]` or `j == n`: the current Lyndon word has period `p = j - k`. The
   first factor has length `p`. If `p == n`, the whole string is one Lyndon word.

```python
def is_lyndon(s: str) -> bool:
    n = len(s)
    if n == 0:
        return False
    i, j, k = 0, 1, 0
    while j < n and s[k] <= s[j]:
        k = i if s[k] < s[j] else k + 1
        j += 1
    # First Lyndon factor length is (j - k); it equals n iff s is Lyndon.
    return (j - k) == n
```

- **Time:** `O(n)` — `j` advances monotonically to `n`.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- A single character is always a Lyndon word (no proper suffix). The loop body doesn't
  even run; `j - k = 1 - 0 = 1 = n`, returns `True`.
- Any string with a repeated block, like `"abab"` or `"aa"`, fails: the first factor is
  shorter than `n` (`"ab"` and `"a"` respectively).
- A Lyndon word never has equal adjacent... it can have repeats internally (`"aab"`,
  `"aabb"` are Lyndon) — the key is strict comparison against *suffixes*, not adjacency.
- The last character of a Lyndon word of length `>= 2` is strictly greater than its first
  character; a useful sanity check but not sufficient on its own.
