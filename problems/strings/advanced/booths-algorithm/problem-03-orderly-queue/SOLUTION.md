# Solution — Orderly Queue

## The critical observation

Everything hinges on `k`:

- **`k >= 2`:** With two movable front slots you can perform an adjacent swap of the
  first two characters (move the 1st to the back, do work, move things around) and, more
  generally, realize *any* permutation of the string. Therefore the smallest reachable
  string is the **sorted** string. Proof sketch: with `k = 2` you can bubble any
  character to any position, so all permutations are reachable; more freedom (`k > 2`)
  cannot make the optimum worse.
- **`k == 1`:** The only move is "first char to the back," which cycles the string.
  After `t` moves you get rotation `t`. So the reachable set is *exactly* the `n`
  rotations, and the answer is the **lexicographically smallest rotation**.

## Brute Force (k == 1 case)

Enumerate all rotations and take the min.

```python
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))
        return min(s[i:] + s[:i] for i in range(len(s)))
```

- Sorting is `O(n log n)`. The rotation scan is `O(n^2)` (n rotations, each an
  `O(n)` build + compare).
- **Time:** `O(n^2)` for `k == 1`. **Space:** `O(n)`.
- At `n <= 1000` this is fully acceptable and is the common accepted LeetCode solution.

## Optimal Approach — Booth's Algorithm for the k == 1 branch

Replace the `O(n^2)` rotation scan with Booth's `O(n)` least-rotation routine. This is
the principled linear-time solution and generalizes to much larger `n`.

```python
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))
        # k == 1: lexicographically smallest rotation via Booth's Algorithm
        n = len(s)
        ss = s + s
        f = [-1] * len(ss)
        idx = 0
        for j in range(1, len(ss)):
            sj = ss[j]
            i = f[j - idx - 1]
            while i != -1 and sj != ss[idx + i + 1]:
                if sj < ss[idx + i + 1]:
                    idx = j - i - 1
                i = f[i]
            if sj != ss[idx + i + 1]:
                if sj < ss[idx]:
                    idx = j
                f[j - idx] = -1
            else:
                f[j - idx] = i + 1
        idx %= n
        return s[idx:] + s[:idx]
```

### Why it is correct

- The `k >= 2` branch is justified by the permutation-reachability argument above; the
  sorted string is the global minimum over all permutations.
- The `k == 1` branch returns the least rotation, and Booth's Algorithm computes that
  correctly in `O(n)` (see the least-rotation write-ups in the sibling problems).

- **Time:** `O(n log n)` for `k >= 2` (sorting), `O(n)` for `k == 1` (Booth's).
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Do not overthink `k >= 2`:** many first attempts try to simulate moves; the sorted
  string is provably optimal and `O(n log n)`.
- **`k == 1` with a periodic string** (e.g. `"aaaa"`): all rotations equal, Booth's
  returns the string itself.
- **Length 1:** both branches return `s` unchanged.
- **Zero moves allowed:** returning `s` itself is a valid candidate; for `k == 1` the
  least rotation may well *be* `s` (rotation index 0), which Booth's reports naturally.
