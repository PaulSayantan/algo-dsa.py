# Sort Characters By Frequency — Solution

## Brute Force

Sort the individual characters using a comparator based on how many times each one
occurs in the string, recomputing `s.count(ch)` for comparisons.

```python
def frequencySort(s: str) -> str:
    return "".join(sorted(s, key=lambda ch: -s.count(ch)))
```

- **Time:** O(n^2) in the worst case — `s.count(ch)` is O(n) and may be evaluated
  many times during the O(n log n) sort.
- **Space:** O(n) for the character list.

Simple, but the repeated `count` calls make it quadratic and needlessly slow.

## Optimal Approach (Character Frequency Count)

Count each character **once**, then sort the *distinct* characters (at most a
constant 62 of them) by their tallies, and finally build the output by repeating
each character by its count.

Steps:

1. Build a frequency map with a single pass. A size-128 ASCII array works, or use
   `collections.Counter(s)`.
2. Take the `(char, count)` pairs and sort them by `count` **descending**. There
   are at most 62 distinct characters here, so this sort is effectively constant
   work.
3. For each pair, append `char * count` to the result, and join.

```python
from collections import Counter

def frequencySort(s: str) -> str:
    counts = Counter(s)                       # O(n) tally
    ordered = sorted(counts.items(),
                     key=lambda kv: kv[1],
                     reverse=True)             # sort distinct chars by count
    return "".join(ch * cnt for ch, cnt in ordered)
```

**Why it is correct:** `counts[ch]` is exactly how many times `ch` occurs. Emitting
`ch * counts[ch]` reproduces the right multiplicity for every character, so the
output is a permutation of `s`. Sorting the distinct characters by descending count
guarantees the "most frequent first" ordering; characters with equal counts may be
emitted in any order, which the problem explicitly allows.

- **Time:** O(n + k log k) where `k` is the number of distinct characters
  (bounded by 62, so this is effectively O(n)).
- **Space:** O(n) for the output string plus O(k) for the counts.

### Bucket-sort variant (no comparison sort)

Because counts range from 1 to `n`, you can bucket characters by count and read
buckets from high to low, giving strict O(n) time:

```python
def frequencySort(s: str) -> str:
    counts = Counter(s)
    buckets = [[] for _ in range(len(s) + 1)]   # index = frequency
    for ch, cnt in counts.items():
        buckets[cnt].append(ch)
    out = []
    for freq in range(len(s), 0, -1):
        for ch in buckets[freq]:
            out.append(ch * freq)
    return "".join(out)
```

## Key Insights & Edge Cases

- **Group, then order:** the answer requires identical characters to be contiguous,
  which falls out naturally from emitting `ch * count`.
- **Case sensitivity:** `'A'` and `'a'` are distinct characters, so do not
  lowercase the input. The digit and mixed-case alphabet means a size-128 array (or
  a `Counter`) rather than size-26.
- **Ties are free choices:** any ordering among equal-frequency characters is
  accepted, so no stable-sort requirement exists.
- **Single distinct character** (e.g. `"aaaa"`) trivially returns itself.
- **Efficiency note:** the win over brute force is counting each character exactly
  once instead of recomputing `count` inside a comparator.
