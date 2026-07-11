# Sort Characters By Frequency — Solution

## Brute Force

Count the frequency of every character, then sort the distinct characters by
their count in descending order, and finally emit each character repeated by its
count.

```python
from collections import Counter

def frequencySort(s: str) -> str:
    counts = Counter(s)
    ordered = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    return "".join(ch * cnt for ch, cnt in ordered)
```

- **Time:** `O(n + d log d)` where `n = len(s)` and `d` is the number of
  distinct characters. The `sorted` call is the bottleneck.
- **Space:** `O(n)` for the counter and output string.

Since `d` is at most 62 here (letters + digits), this is already fast in
practice — but it still relies on a comparison sort. We can remove the `log`
factor entirely.

## Optimal Approach (Bucket Sort)

The key observation: **a character's frequency is an integer in the range
`[1, n]`.** That bounded integer is a perfect bucket index. Instead of sorting
by frequency, we *place* each character into the bucket whose index equals its
frequency, then read the buckets from high index to low.

### Steps

1. Count every character's frequency with a hash map (`Counter`).
2. Create `n + 1` buckets, where `buckets[f]` holds the list of characters that
   occur exactly `f` times. (Index `0` is unused but keeps the math clean.)
3. For each `(char, freq)` pair, append `char` to `buckets[freq]`.
4. Walk the buckets from index `n` down to `1`. For each character in a bucket,
   append `char * freq` to the output.

```python
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        n = len(s)
        buckets = [[] for _ in range(n + 1)]  # buckets[f] -> chars with freq f
        for ch, freq in counts.items():
            buckets[freq].append(ch)

        out = []
        for freq in range(n, 0, -1):
            for ch in buckets[freq]:
                out.append(ch * freq)
        return "".join(out)
```

### Why It Is Correct

Every character lands in exactly one bucket, indexed by its true frequency.
Iterating the buckets from index `n` down to `1` visits characters strictly in
non-increasing frequency order, which is exactly the required ordering. Repeating
each character `freq` times reproduces every occurrence, so the multiset of
characters in the output equals that of the input. Ties (equal frequency) share a
bucket and may be emitted in any order — which the problem explicitly allows.

### Complexity

- **Time:** `O(n)`. Counting is `O(n)`, allocating and scanning `n + 1` buckets
  is `O(n)`, and building the output writes exactly `n` characters.
- **Space:** `O(n)` for the buckets and the output string.

## Key Insights & Edge Cases

- **Frequency as an index** is the reusable trick: any time your sort key is a
  small integer bounded by `n`, bucket sort turns an `O(n log n)` sort into
  `O(n)`.
- **`n + 1` buckets, not `n`:** the maximum frequency is `n` (all characters
  identical), so you need index `n` to exist.
- **Case and digits matter:** `'A'`, `'a'`, and `'0'` are distinct keys. Do not
  normalize case.
- **Single distinct character** (e.g. `"aaaa"`) all lands in `buckets[4]` and is
  emitted once as `"aaaa"`.
- **Length-1 string** produces itself — `buckets[1]` holds the sole character.
- Using a plain list of buckets keeps this simpler and faster than a heap-based
  Top-K approach, which would reintroduce a `log` factor.
