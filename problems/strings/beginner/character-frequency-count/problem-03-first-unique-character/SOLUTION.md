# First Unique Character in a String — Solution

## Brute Force

For each index `i`, scan the rest of the string to see whether `s[i]` appears
anywhere else. Return the first index whose character has no duplicate.

```python
def firstUniqChar(s: str) -> int:
    for i, ch in enumerate(s):
        if all(ch != s[j] for j in range(len(s)) if j != i):
            return i
    return -1
```

- **Time:** O(n^2) — for each of the `n` characters we may scan all `n` others.
- **Space:** O(1).

Correct but quadratic; for `n` up to 10^5 this is far too slow.

## Optimal Approach (Character Frequency Count)

Uniqueness of a character depends only on its total count in the whole string, so
compute all counts first, then find the earliest index whose count is 1.

Steps:

1. Allocate a size-26 array `counts` and tally every character:
   `counts[ord(ch) - ord('a')] += 1`. (One O(n) pass.)
2. Iterate over the string **in order** with indices. The first index `i` where
   `counts[ord(s[i]) - ord('a')] == 1` is the answer, because it is the earliest
   position holding a character that occurred exactly once.
3. If no such index exists, return `-1`.

```python
def firstUniqChar(s: str) -> int:
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - ord('a')] += 1
    for i, ch in enumerate(s):
        if counts[ord(ch) - ord('a')] == 1:
            return i
    return -1
```

**Why it is correct:** After the first pass, `counts[c]` is the exact number of
occurrences of character `c`. A character is unique iff its count equals 1. The
second pass visits indices in increasing order and returns the first one satisfying
that predicate, which is by definition the first unique character.

- **Time:** O(n) — two linear passes.
- **Space:** O(1) — the fixed 26-slot array (alphabet size is constant).

`collections.Counter` gives the same result: build `cnt = Counter(s)`, then return
the first `i` with `cnt[s[i]] == 1`.

## Key Insights & Edge Cases

- **Two passes are required:** you cannot decide the first unique character on a
  single left-to-right pass, because a character seen once early might repeat
  later. You must know the final counts before scanning for the answer.
- **Order of the answer scan matters:** scan the *original string* (not the count
  array) so that ties are broken by position, returning the smallest index.
- **All-repeating input** (e.g. `"aabb"`) correctly yields `-1` since no bucket
  ends at 1.
- **Single character** `"z"` returns `0` — its count is 1.
- **Streaming variant:** if characters arrive one at a time and you must answer
  repeatedly, a queue of candidate indices plus the count array (a "first unique
  number in a stream" design) keeps each query O(1) amortized.
