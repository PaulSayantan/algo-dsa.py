# Solution — Maximum Length × Occurrences

## Brute Force

Enumerate all substrings, keep the palindromic ones in a hash map from string to
count, then evaluate `len(key) * count` for each key and take the max.

- `O(n^2)` substrings, palindrome test `O(n)` → `O(n^3)` (or `O(n^2)` with a DP
  palindrome table and hashing).
- Space `O(n^2)` to hold distinct palindromes by value.

Infeasible for `n = 10^5`.

## Optimal Approach — Palindromic Tree (Eertree)

### Idea

This problem combines two eertree facts:

1. Each node is a distinct palindrome and stores its **length**.
2. Each palindrome's **number of occurrences** is obtained by counting how often
   the node was the longest palindromic suffix during construction, then
   **propagating those counts up the suffix links** (a longer palindrome's
   occurrences also count as occurrences of all its palindromic suffixes).

With both quantities available per node, the answer is simply

```
max over non-root nodes v of  length[v] * occ[v]
```

### Why propagation gives true occurrence counts

When `add(i)` finishes with `last = v`, palindrome `P_v` is the longest
palindromic suffix ending at `i`, so it occurs there — record `cnt[v] += 1`.
Every palindromic suffix of `P_v` (its suffix-link ancestors) also ends at `i`.
Processing nodes in **decreasing length** and doing `cnt[suffix[v]] += cnt[v]`
credits each of those shorter palindromes with all the occurrences of their
longer super-palindromes. After the pass, `cnt[v] = occ(P_v)` for every node.

### Reference implementation

```python
class Solution:
    def maxPalindromeValue(self, s: str) -> int:
        length = [-1, 0]
        suffix = [0, 0]
        edges = [dict(), dict()]
        cnt = [0, 0]
        last = 1

        def get_link(v: int, i: int) -> int:
            while i - length[v] - 1 < 0 or s[i - length[v] - 1] != s[i]:
                v = suffix[v]
            return v

        for i, c in enumerate(s):
            cur = get_link(last, i)
            if c in edges[cur]:
                last = edges[cur][c]
            else:
                new = len(length)
                length.append(length[cur] + 2)
                edges.append(dict())
                cnt.append(0)
                if length[new] == 1:
                    suffix.append(1)
                else:
                    link = get_link(suffix[cur], i)
                    suffix.append(edges[link][c])
                edges[cur][c] = new
                last = new
            cnt[last] += 1

        for v in sorted(range(2, len(length)), key=lambda x: -length[x]):
            cnt[suffix[v]] += cnt[v]

        return max((length[v] * cnt[v] for v in range(2, len(length))),
                   default=0)
```

- **Time:** `O(n · log |Σ|)` build + `O(n log n)` sort (or `O(n)` with a length
  counting-sort / reverse creation order) + `O(n)` scan.
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Trade-off is real:** the best palindrome is rarely the longest one. In
  `"aaaaa"`, `"aaa"` (3 × 3 = 9) beats both the whole string (5 × 1 = 5) and the
  single char (1 × 5 = 5).
- **Occurrences overlap.** `occ` counts overlapping occurrences (e.g. `"aa"`
  occurs 4 times in `"aaaaa"`), which is exactly what suffix-link propagation
  produces — do not try to de-overlap.
- **Use 64-bit integers.** For `n = 10^5`, `length * occ` can reach ~`10^{10}`.
  Python is safe; in C++/Java use `long long` / `long`.
- **Single character** (`"a"`): only node `"a"`, value `1 * 1 = 1`.
- **All distinct** (`"abc"`): each single char has value `1`, answer `1`.
- Remember to start the max at the sentinel-free range (node index `2`) and use
  a `default` for the degenerate empty input.
