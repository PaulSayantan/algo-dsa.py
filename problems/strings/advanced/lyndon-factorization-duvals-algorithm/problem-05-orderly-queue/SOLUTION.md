# Solution — Orderly Queue (LeetCode 899)

## Brute Force

For `k == 1` there are only `n` reachable strings (the rotations); take the min. For
`k >= 2` you can reach every permutation, so sort.

```python
def orderlyQueue_brute(s, k):
    if k >= 2:
        return "".join(sorted(s))
    return min(s[i:] + s[:i] for i in range(len(s)))  # smallest rotation
```

- **Time:** `O(n^2)` for the `k == 1` branch (build/compare `n` rotations); `O(n log n)`
  to sort.
- **Space:** `O(n)`.

With `n <= 1000` this already passes on LeetCode, but the rotation part is the natural
place to plug in Duval for a clean `O(n)`.

## Optimal Approach (Duval for the k == 1 Rotation)

### Why the two regimes

- **`k >= 2`:** Having two "free" front slots lets you simulate an adjacent transposition
  (move the 2nd char, then the 1st, in the right order), and adjacent transpositions
  generate **all permutations**. Hence the best reachable string is simply the characters
  sorted ascending: `"".join(sorted(s))`.
- **`k == 1`:** Each move takes `s[0]` to the back — that is a left rotation by one. The
  reachable set is exactly the `n` rotations of `s`, so the answer is the
  **lexicographically smallest rotation**.

### Smallest rotation via Duval

Run Duval's scan on `t = s + s`, tracking the start of the last Lyndon factor that begins
before index `n`; that start `d` gives the minimal rotation `t[d:d+n]`.

```python
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))
        # k == 1: lexicographically smallest rotation via Duval on s + s
        n = len(s)
        t = s + s
        i = 0
        ans = 0
        while i < n:
            ans = i
            j = i + 1
            m = i               # 'm' plays Duval's k-pointer (renamed to avoid clashing with arg k)
            while j < len(t) and t[m] <= t[j]:
                m = i if t[m] < t[j] else m + 1
                j += 1
            while i <= m:
                i += (j - m)
        return t[ans:ans + n]
```

### Why it's correct

The `k >= 2` branch is a permutation-reachability argument (bubble-sort style). The
`k == 1` branch reduces to the previous problem: the last Lyndon factor of `s + s` that
starts before position `n` is the smallest length-`>= n` suffix of the doubled string,
which is exactly the smallest rotation of `s`.

- **Time:** `O(n log n)` overall (dominated by the sort in the `k >= 2` case); the Duval
  rotation scan is `O(n)`.
- **Space:** `O(n)` for the doubled string / sorted copy.

## Key Insights & Edge Cases

- **Naming clash:** the problem's `k` is the number of free front slots; Duval's internal
  pointer is traditionally also called `k`. Rename one (here Duval's becomes `m`) to avoid
  bugs.
- **`k == 1` on an already-minimal string** like `"abc"`: the smallest rotation is
  `"abc"` itself (`ans = 0`).
- **All-equal string** `"aaaa"`, any `k`: sorting and the smallest rotation both give
  `"aaaa"`.
- **Single character:** returns that character for any `k`.
- Don't over-think `k >= 2` — no rotation logic is needed; sorting always wins because any
  arrangement is reachable.
