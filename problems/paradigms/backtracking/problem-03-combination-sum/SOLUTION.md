# Combination Sum — Solution

## Brute Force

Because a value can repeat, the naive idea is to try every count of every
candidate. For candidate `c`, it can appear `0, 1, 2, ...` up to `target // c`
times; take the Cartesian product over all candidates and keep tuples whose
weighted sum equals `target`. The number of `(count)` tuples is
`∏ (target // c_i + 1)`, which explodes quickly and wastes work on combinations
that overshoot early.

- **Time:** roughly `O(∏_i (target/c_i))` — exponential in the number of
  candidates.
- **Space:** `O(target / min(candidates))` for one candidate tuple.

It is correct but does no early pruning, so it evaluates enormous numbers of
dead combinations.

## Optimal Approach (Backtracking)

Grow one combination, always choosing candidates at index `start` or later. To
allow reuse of a value, recurse with the **same** index `i` (not `i + 1`); using
`start`-or-later ordering is what prevents permutation-style duplicates like
`[2,3,2]`. Prune whenever the remaining amount goes negative.

```python
def combinationSum(candidates, target):
    result = []
    path = []
    candidates.sort()               # enables the early break below

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])  # exact hit -> record a copy
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break               # sorted: all later candidates too big -> prune
            path.append(candidates[i])         # choose
            backtrack(i, remaining - candidates[i])  # i (not i+1): reuse allowed
            path.pop()                          # undo

    backtrack(0, target)
    return result
```

**Why it is correct.**

- *No missed solutions:* at each level we consider every candidate from `start`
  onward, and recursing with `i` lets a value be taken again, so any multiset
  can be assembled in non-decreasing index order.
- *No duplicate multisets:* by never going back to indices before `start`, each
  distinct multiset is generated in exactly one canonical (index-sorted) order.
- *Termination / pruning:* every recursive call strictly decreases `remaining`
  by at least `min(candidates) >= 2 > 0`, so depth is bounded by
  `target / min(candidates)`; the sorted `break` skips branches that can only
  overshoot.

**Step by step for `candidates = [2,3,6,7]`, `target = 7`:**

- Take `2` (rem 5) → take `2` (rem 3) → take `2` (rem 1) → next candidate `2>1`,
  break. Back up. Take `3` (rem 0) → record `[2,2,3]`.
- Unwind the 2's. Try `3` first (rem 4) → `3` again (rem 1) → break; `6>1`… dead.
- Try `6` (rem 1) → break. Try `7` (rem 0) → record `[7]`.

Result: `[[2,2,3], [7]]`.

- **Time:** `O(N^(target / min)) ` in the worst case — bounded by the size of the
  pruned decision tree; each recorded combination costs `O(target/min)` to copy.
- **Space:** `O(target / min(candidates))` recursion depth + current path.

## Key Insights & Edge Cases

- **`i` vs. `i + 1`.** Recursing with `i` permits repeats (this problem);
  recursing with `i + 1` gives *without-repetition* combinations (LeetCode 40,
  "Combination Sum II", where you also skip equal neighbors to dedup).
- **Sorting + `break`** turns an O(len) scan-and-skip into an early cutoff and is
  the main practical speedup; it does not change correctness.
- **Distinct candidates** are guaranteed, so no per-level dedup is required.
- **No solution** (e.g., `target` smaller than every candidate) correctly returns
  `[]` — the loop body prunes everything and nothing is recorded.
- **Copy on record** (`path[:]`) as always, to avoid aliasing the mutable path.
