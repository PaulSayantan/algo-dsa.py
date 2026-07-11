# Solution — Build a Suffix Array

## Brute Force

Generate every suffix as a string and sort them with a comparison sort.

```python
def build_suffix_array(s):
    n = len(s)
    return sorted(range(n), key=lambda i: s[i:])
```

Building each suffix key is `O(n)` and comparing two suffixes is `O(n)`, so this
is `O(n^2 log n)` in the worst case (and materializes `O(n^2)` characters). Fine
for tiny inputs, hopeless for `n = 2 * 10^5`.

- **Time:** `O(n^2 log n)`
- **Space:** `O(n^2)`

## Optimal Approach (Prefix Doubling + Radix Sort)

**Key idea:** after we have sorted all suffixes by their first `L` characters
(and assigned each a *rank* reflecting that order), we can sort by their first
`2L` characters cheaply. A suffix's first `2L` characters is its first `L`
characters followed by the first `L` characters of the suffix `L` positions
later. So each suffix `i` is captured by the integer **pair**:

```
key(i) = ( rank[i], rank[i + L]  )      # rank = -1 (or 0) if i + L >= n
```

Sorting suffixes by their first `2L` characters is therefore identical to sorting
these pairs — and sorting pairs of small integers is a textbook **two-pass radix
sort**: first stably sort by the second component, then stably sort by the first
component. Because pair components are ranks in `[0, n)`, each pass is a counting
sort in `O(n)`.

```python
def build_suffix_array(s):
    n = len(s)
    sa = sorted(range(n), key=lambda i: s[i])     # base: rank by first char
    rank = [0] * n
    # initial ranks from single characters
    r = 0
    rank[sa[0]] = 0
    for j in range(1, n):
        if s[sa[j]] != s[sa[j - 1]]:
            r += 1
        rank[sa[j]] = r

    L = 1
    while L < n:
        def second_key(i):
            return rank[i + L] + 1 if i + L < n else 0   # 0 means "shorter/empty"
        def first_key(i):
            return rank[i] + 1

        # --- radix sort pass 1: stable counting sort by second key ---
        sa = _counting_sort(sa, second_key, n + 1)
        # --- radix sort pass 2: stable counting sort by first key ---
        sa = _counting_sort(sa, first_key, n + 1)

        # recompute ranks based on the new (first, second) pair order
        new_rank = [0] * n
        r = 0
        for j in range(1, n):
            prev, cur = sa[j - 1], sa[j]
            if (first_key(prev), second_key(prev)) != (first_key(cur), second_key(cur)):
                r += 1
            new_rank[cur] = r
        rank = new_rank
        if r == n - 1:            # all ranks distinct -> fully sorted
            break
        L *= 2
    return sa


def _counting_sort(order, key, k):
    count = [0] * (k + 1)
    for i in order:
        count[key(i) + 1] += 1
    for c in range(1, k + 1):
        count[c] += count[c - 1]
    output = [0] * len(order)
    for i in order:               # forward scan + start offsets = stable
        c = key(i)
        output[count[c]] = i
        count[c] += 1
    return output
```

### Why it is correct

- **Base case:** ranking by the first character sorts suffixes by their length-1
  prefixes.
- **Inductive step:** assume `rank` correctly orders suffixes by their first `L`
  characters (equal ranks ⇔ equal length-`L` prefixes). The pair
  `(rank[i], rank[i+L])` then encodes the first `2L` characters. Radix-sorting by
  the second key and then (stably) by the first key orders the pairs
  lexicographically — i.e. orders suffixes by their first `2L` characters. The
  sentinel `0` for `i + L >= n` makes a *shorter* suffix compare as smaller,
  which matches lexicographic order ("ab" < "abab").
- After `ceil(log2 n)` doublings, `L >= n`, so prefixes span the entire suffix
  and the array is fully sorted. The early exit `r == n - 1` stops as soon as all
  ranks are unique (order already total).

### Complexity

- **Rounds:** `O(log n)` (doubling `L` each round).
- **Per round:** two counting-sort passes + a rank recompute, each `O(n)`.
- **Time:** `O(n log n)`.
- **Space:** `O(n)` for `sa`, `rank`, `count`, and the output buffer.

## Key Insights & Edge Cases

- **Radix sort is the engine, not the whole algorithm.** The clever part is
  reducing "sort suffixes by `2L` chars" to "sort integer pairs," which radix
  sort then does in linear time per round.
- **Sentinel for out-of-range second key** (`i + L >= n`) must sort *before* any
  real rank so that a suffix that ends is treated as smaller — this is what makes
  prefixes win over longer strings ("aa" before "aaa").
- **Two-pass order matters:** sort by the *less significant* key (second
  component) first, then the *more significant* key (first component), each pass
  stable — the same LSD-first rule as ordinary radix sort.
- **Early termination** when all ranks are distinct avoids unnecessary rounds
  (e.g. strings with all-different characters finish in one round).
- **Single-character / all-equal strings:** `"aaa"` yields `[2, 1, 0]` because
  the shortest suffix is lexicographically smallest; the sentinel handling
  produces this correctly.
- **`+1` offsets** in `_counting_sort` keys keep indices non-negative so the
  sentinel `0` and real ranks share one contiguous count array.
