# Solution — Lexicographically Smallest Rotation

## Brute Force

Generate all `n` rotations and take the minimum.

```python
def least_rotation_brute(s):
    return min(s[i:] + s[:i] for i in range(len(s)))
```

Each rotation is built and compared in `O(n)`, and there are `n` of them.

- **Time:** `O(n^2)`.
- **Space:** `O(n)` per candidate.

Fine for small inputs but hopeless for `n = 10^6`.

## Optimal Approach (Duval on the Doubled String)

**Key fact:** the lexicographically smallest rotation of `s` starts at the same index as
the smallest suffix of `s + s` that has length `>= n`. Concretely, run Duval's scan over
`t = s + s` and track the **start index of every Lyndon factor**; the last factor start
that is still `< n` is the answer index `d`. The minimal rotation is `t[d : d + n]`.

Intuitively, appending `s` to itself lets a Lyndon factor "wrap around" the boundary, and
the smallest suffix of the doubled string that is at least `n` long corresponds precisely
to the smallest rotation. We only need to scan while `i < n`, giving `O(n)`.

### Implementation

```python
def least_rotation(s):
    n = len(s)
    t = s + s
    i = 0
    ans = 0
    while i < n:                     # only need factor starts in [0, n)
        ans = i                      # candidate start of the minimal rotation
        j = i + 1
        k = i
        while j < len(t) and t[k] <= t[j]:
            k = i if t[k] < t[j] else k + 1
            j += 1
        while i <= k:                # emit factor(s), each advancing i by (j - k)
            i += (j - k)
    return t[ans:ans + n]
```

`ans` records the start of the last Lyndon factor that began before index `n`. Because
Duval emits factors in non-increasing order and the last factor before `n` is the
smallest length-`>= n` suffix of `t`, `t[ans:ans+n]` is the minimal rotation.

- **Time:** `O(n)` — the scan over `t` of length `2n` is linear and we stop at `i >= n`.
- **Space:** `O(n)` to hold `t = s + s` (or `O(1)` extra if you index into `s` modulo `n`
  instead of materializing `t`).

### Returning only the index

Some judges ask for the 0-based shift `d` (the number of positions to rotate). That is
exactly `ans`; the minimal rotation is `s[ans:] + s[:ans]`.

## Key Insights & Edge Cases

- **Ties / periodic strings:** for `"abab"` the minimal rotation is `"abab"` itself
  (`d = 0`); Duval naturally returns the smallest valid start.
- **All-equal string** `"aaaa"`: every rotation is identical; `ans` stays `0`.
- **Why `s + s` and not just `s`:** a single copy cannot express rotations that wrap the
  end back to the front. Doubling captures all `n` rotations as length-`n` substrings.
- **Stopping condition matters:** scanning the full `2n` would still be `O(n)`, but
  stopping at `i >= n` guarantees `ans < n`, so `t[ans:ans+n]` is a genuine rotation.
- **Comparison-based `O(n log n)` sort of rotations** (via suffix array on `s + s + $`)
  also works but is heavier; Duval is the clean linear-time, low-constant answer.
