# Solution — Sort Characters By Frequency

## Brute Force

Count characters, then hand the `(char, count)` pairs to a library sort keyed by `-count`, and join:

```python
from collections import Counter

def frequencySort(self, s):
    counts = Counter(s)
    return "".join(ch * cnt for ch, cnt in sorted(counts.items(),
                                                   key=lambda p: -p[1]))
```

- **Time:** `O(n + k log k)` where `n = len(s)` and `k` is the number of distinct characters
  (`k <= 62` here, so the sort is effectively negligible).
- **Space:** `O(n)` for the output string plus `O(k)` for the counter.

This is optimal in practice; below we replace the library sort with Selection Sort to practice the
technique. Because `k` is at most 62 (a-z, A-Z, 0-9), the `O(k²)` selection sort is trivially cheap.

## Optimal Approach (Selection Sort on the frequency key)

1. Count every character's frequency into a map.
2. Materialize the distinct `(char, count)` pairs into a list.
3. **Selection-Sort** that list by descending `count`: each pass finds the pair with the maximum
   remaining count and swaps it to the front of the unsorted region.
4. Concatenate `char * count` for each pair in the resulting order.

```python
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        pairs = list(Counter(s).items())          # [(char, count), ...]
        k = len(pairs)
        for i in range(k - 1):
            max_idx = i
            for j in range(i + 1, k):
                if pairs[j][1] > pairs[max_idx][1]:
                    max_idx = j
            if max_idx != i:
                pairs[i], pairs[max_idx] = pairs[max_idx], pairs[i]
        return "".join(ch * cnt for ch, cnt in pairs)
```

### Why it is correct

We are sorting the *distinct characters* by a **derived key** — the frequency count — rather than by
the characters themselves. Selection Sort's invariant guarantees that after pass `i`, the first
`i + 1` pairs are the `i + 1` most frequent characters in non-increasing count order. Emitting each
character repeated `count` times then produces a valid permutation of `s` whose character blocks are
in decreasing frequency. Every character of `s` is emitted exactly `count` times, so the output is a
true permutation of the input.

### Step-by-step on `"tree"`

Counts: `t:1, r:1, e:2`. Pairs (insertion order): `[(t,1), (r,1), (e,2)]`.

| i | max count in suffix | swap indices | pairs                        |
|---|---------------------|--------------|------------------------------|
| 0 | `(e,2)` @2          | swap 0,2     | `[(e,2), (r,1), (t,1)]`      |
| 1 | `(r,1)` @1          | none         | `[(e,2), (r,1), (t,1)]`      |

Emit: `"ee" + "r" + "t"` → `"eert"`.

### Complexity

- **Time:** `O(n + k²)` — `O(n)` to count, `O(k²)` for Selection Sort over `k` distinct characters,
  `O(n)` to build the result. With `k <= 62`, the `k²` term is a small constant.
- **Space:** `O(n)` for the output (plus `O(k)` for the counter and pair list).

## Key Insights & Edge Cases

- **Sort the key, not the value:** the elements being ordered are the distinct characters; the
  ordering criterion is a *separate* number (the count). This "sort by a derived key" pattern is
  exactly how Selection Sort generalizes beyond raw numbers.
- **Ties are free:** the problem accepts any order among equal-frequency characters, so we do not
  need a stable sort or a tiebreaker. Using strict `>` keeps whichever equal-count pair was already
  earlier.
- **Case & digits are distinct symbols:** `'A'` and `'a'` are different keys; `'0'`..`'9'` are
  counted like letters. The counting map handles this automatically.
- **Single distinct character** (e.g. `"aaaa"`): one pair, loop body runs zero times, output equals
  the input.
- **Emit the whole block:** remember to repeat each character by its count (`ch * cnt`), not just
  append the character once — a common mistake that drops duplicates.
