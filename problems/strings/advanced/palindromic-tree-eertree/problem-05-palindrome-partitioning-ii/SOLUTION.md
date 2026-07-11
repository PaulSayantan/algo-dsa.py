# Solution — Palindrome Partitioning II

## Brute Force

Try every way to cut `s` and check that each piece is a palindrome, keeping the
minimum number of cuts. There are `2^(n-1)` cut placements, so this is
exponential and only works for tiny inputs.

A first improvement is the **classic `O(n^2)` DP**: precompute `is_pal[j][i]`
(whether `s[j..i]` is a palindrome) in `O(n^2)`, then

```
dp[i] = min number of palindromic pieces for prefix of length i
dp[0] = 0
dp[i] = min over j < i with s[j..i-1] palindrome of dp[j] + 1
answer  = dp[n] - 1        # pieces minus one = cuts
```

This is `O(n^2)` time / `O(n^2)` space (or `O(n)` space with careful ordering)
and is the standard accepted LeetCode 132 solution. The eertree method below
brings this to near-linear and works **online** (character by character).

## Optimal Approach — Eertree with Series Links

### Why the naive eertree DP is not enough

At position `i`, the palindromic suffixes ending at `i` are exactly the nodes on
the suffix-link chain from `last`. A DP transition
`dp[i] = min(dp[i - len[v]] + 1)` over that whole chain is correct, but the
chain can have `O(i)` nodes, giving `O(n^2)` again.

### Series links: the key structural fact

Define for each node `v`:

- `diff[v] = length[v] - length[suffix_link[v]]` (gap to the next shorter
  palindromic suffix), and
- `slink[v]` (**series link**) = the highest suffix-link ancestor of `v` that has
  the **same `diff`** value. Concretely, when creating `v`, set
  `slink[v] = slink[suffix_link[v]]` if `diff[v] == diff[suffix_link[v]]`, else
  `slink[v] = suffix_link[v]`.

**Theorem (Rubinchik–Shur / "palindromic series"):** the suffix palindromes of
any prefix partition into `O(log i)` maximal *series*, where inside one series
the palindrome lengths form an arithmetic progression (all consecutive `diff`s
equal). So walking series links from `last` visits only `O(log i)` groups.

Each series can be summarized by a single aggregate, so we spend `O(1)` per
series and `O(log i)` per character — `O(n log n)` overall.

### The DP with an auxiliary array `g`

Let `dp[i]` be the minimum number of palindromic pieces for the first `i`
characters, `dp[0] = 0`. Maintain `g[v]` = the best `dp[j]` over the *tail* of
the series headed by `v`, i.e. over the arithmetic run of palindromic suffixes in
that series. After appending `s[i-1]` (so the current prefix has length `i`),
walk `v = last, slink[v], slink[...], ...`:

```
g[v] = dp[i - (length[slink[v]] + diff[v])]
if diff[v] == diff[suffix_link[v]]:
    g[v] = min(g[v], g[suffix_link[v]])   # fold in the rest of this series
dp[i] = min(dp[i], g[v] + 1)
```

The term `length[slink[v]] + diff[v]` is the length of the **shortest** palindrome
in `v`'s series; subtracting it from `i` indexes the DP just before that
shortest palindrome. Folding `g[suffix_link[v]]` in when the `diff` matches lets
one `g` value stand for the entire arithmetic run, which is what makes each
series `O(1)`.

### Reference implementation

```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        INF = float("inf")

        length = [-1, 0]
        suffix = [0, 0]
        edges = [dict(), dict()]
        diff = [0, 0]
        slink = [0, 0]
        last = 1
        g = [0, 0]

        dp = [INF] * (n + 1)
        dp[0] = 0

        def get_link(v: int, i: int) -> int:
            while i - length[v] - 1 < 0 or s[i - length[v] - 1] != s[i]:
                v = suffix[v]
            return v

        for i in range(1, n + 1):
            c = s[i - 1]
            cur = get_link(last, i - 1)
            if c in edges[cur]:
                last = edges[cur][c]
            else:
                new = len(length)
                length.append(length[cur] + 2)
                edges.append(dict())
                diff.append(0)
                slink.append(0)
                g.append(0)
                if length[new] == 1:
                    suffix.append(1)
                else:
                    link = get_link(suffix[cur], i - 1)
                    suffix.append(edges[link][c])
                edges[cur][c] = new
                diff[new] = length[new] - length[suffix[new]]
                slink[new] = (slink[suffix[new]]
                              if diff[new] == diff[suffix[new]]
                              else suffix[new])
                last = new

            v = last
            while length[v] > 0:
                g[v] = dp[i - (length[slink[v]] + diff[v])]
                if diff[v] == diff[suffix[v]]:
                    g[v] = min(g[v], g[suffix[v]])
                dp[i] = min(dp[i], g[v] + 1)
                v = slink[v]

        return dp[n] - 1
```

- **Time:** `O(n log n)` — linear eertree construction plus `O(log i)` series
  links processed per character.
- **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Cuts = pieces − 1.** The DP tracks the minimum number of palindromic
  *pieces*; subtract one at the end to get cuts. `dp[0] = 0` seeds the empty
  prefix.
- **Series links are what make it near-linear.** Without them, iterating the full
  suffix-link chain is `O(n^2)`. The `O(log n)` bound on the number of series is
  the crucial theorem; `slink`/`diff` must be set at node-creation time.
- **`length[slink[v]] + diff[v]`** is the length of the shortest palindrome in
  the current series — the correct offset into `dp`. A common bug is using
  `length[suffix[v]]` here, which only covers the immediate next palindrome, not
  the whole series.
- **Already a palindrome** (`"a"`, `"aba"`): `dp[n] = 1`, answer `0` cuts.
- **No long palindromes** (`"abc"`): every piece is a single char, `dp[n] = 3`,
  answer `2` cuts.
- **Variant — counting factorizations:** replace `min(..., g+1)` with modular
  addition of `dp` values to count the number of palindromic factorizations; the
  same series-link machinery applies.
- For LeetCode 132's small bound (`n <= 2000`) the `O(n^2)` DP is simpler and
  fully sufficient; use the eertree method when `n` is large or the input must be
  processed online.
