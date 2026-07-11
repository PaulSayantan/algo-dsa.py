# EquiLeader — Solution

## Brute Force

For every split point `S`, compute the leader of the left half and the leader of the right
half independently and check whether they exist and match.

```python
def equiLeaders(A):
    n = len(A)
    def leader(sub):
        from collections import Counter
        c = Counter(sub)
        v, cnt = c.most_common(1)[0]
        return v if cnt * 2 > len(sub) else None
    ans = 0
    for s in range(n - 1):
        L = leader(A[:s + 1])
        R = leader(A[s + 1:])
        if L is not None and L == R:
            ans += 1
    return ans
```

- **Time:** O(n^2) — each of the n split points recomputes counts over O(n) elements.
- **Space:** O(n) for the sub-array copies / counters.

Too slow for n up to 100000.

## Optimal Approach — Global Leader via Boyer–Moore + Prefix Sweep

**Crucial observation.** If a value `x` is the strict majority of *both* halves, then it is a
strict majority of their union — the whole array. Formally, if `left_count > len(left)/2` and
`right_count > len(right)/2`, then `left_count + right_count > (len(left)+len(right))/2 = n/2`.
So **the only value that can ever be an equi leader's shared leader is the global leader** of
the entire array. There is at most one.

Algorithm:

1. **Find the global leader candidate** with a Boyer–Moore voting pass, then **verify** it is
   an actual majority (`total_count * 2 > n`). If not, there are zero equi leaders.
2. **Sweep split points.** Walk `S` from `0` to `n − 2`, maintaining `prefix_count` = number
   of leader occurrences in `A[0 .. S]`. At each `S`:
   - left size = `S + 1`, left has the leader as majority iff `prefix_count * 2 > (S + 1)`.
   - right count = `total_count − prefix_count`, right size = `n − (S + 1)`, right has it as
     majority iff `(total_count − prefix_count) * 2 > (n − S − 1)`.
   - If both hold, increment the answer.

```python
def equiLeaders(A):
    n = len(A)

    # Phase 1: Boyer–Moore candidate.
    candidate, count = None, 0
    for x in A:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1

    # Phase 2: verify it is a real leader.
    total = sum(1 for x in A if x == candidate)
    if total * 2 <= n:
        return 0

    # Phase 3: sweep split points.
    ans = 0
    prefix = 0
    for s in range(n - 1):              # s is the last index of the left half
        if A[s] == candidate:
            prefix += 1
        left_size = s + 1
        right_size = n - left_size
        if prefix * 2 > left_size and (total - prefix) * 2 > right_size:
            ans += 1
    return ans
```

### Why it is correct

By the observation above, we never need to consider any value other than the global leader,
so counting only the leader's occurrences suffices. `prefix` is the exact count of the leader
in `A[0..s]`; `total - prefix` is therefore its count in the suffix. The two strict-majority
tests directly encode "leader of the left half" and "leader of the right half," and equality
of the two leaders is automatic because we test the *same* value on both sides.

### Worked trace on `[4, 3, 4, 4, 4, 2]`

Voting → candidate `4`. Verify: `total = 4`, `4 * 2 = 8 > 6`, so `4` is the leader (n = 6).

| S | A[S] | prefix | left_size | left maj? (2·prefix > size) | right count | right_size | right maj? | equi? |
|---|------|--------|-----------|------------------------------|-------------|------------|------------|-------|
| 0 | 4 | 1 | 1 | 2 > 1 ✓ | 3 | 5 | 6 > 5 ✓ | yes |
| 1 | 3 | 1 | 2 | 2 > 2 ✗ | 3 | 4 | – | no |
| 2 | 4 | 2 | 3 | 4 > 3 ✓ | 2 | 3 | 4 > 3 ✓ | yes |
| 3 | 4 | 3 | 4 | 6 > 4 ✓ | 1 | 2 | 2 > 2 ✗ | no |
| 4 | 4 | 4 | 5 | 8 > 5 ✓ | 0 | 1 | 0 > 1 ✗ | no |

Two equi leaders. ✓

- **Time:** O(n) — one voting pass, one verification pass, one sweep.
- **Space:** O(1) — a handful of counters.

## Key Insights & Edge Cases

- **The reduction to one value is the whole trick.** Recognizing that an equi leader must be
  the *global* leader collapses an O(n^2) search into three linear scans.
- **Verification is required:** if the array has no leader (e.g. `[1, 2, 3]`), the answer is
  `0` — do not skip the `total * 2 <= n` check.
- **Strict inequality (`> half`, coded as `2 * count > size`)** matters. Using `>=` would
  wrongly count ties (a half split evenly between two values has no leader).
- The split range is `0 <= S < n − 1`, so both halves are non-empty; iterate `s` over
  `range(n - 1)`.
- Edge cases: `n = 1` yields `0` (no valid split), all-equal arrays yield `n − 1`, and arrays
  with a leader but few equi points work without special casing.
