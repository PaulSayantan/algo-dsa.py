# Group Anagrams — Solution

## Brute Force

Compare every string to every other string with a pairwise anagram check, using a
union-find or "already grouped" flags to assemble the buckets.

- **Time:** `O(n^2 * L log L)` (or `O(n^2 * L)` with counting) — `n^2` pairs, each
  anagram test costing `O(L)`–`O(L log L)` for length `L`.
- **Space:** `O(n * L)` for the groups.

Quadratic in the number of strings, which is far too slow for `n` up to `10^4`.

## Optimal Approach (Anagram Check — sort or count)

The key idea: give each string a **canonical signature** that is identical for all
anagrams and different for non-anagrams. Then a single hash map keyed by signature
buckets the strings in one pass — no pairwise comparisons.

Two standard signatures:

- **Sorted string** — `"".join(sorted(word))`. All anagrams share the same sorted
  form (`"eat"`, `"tea"`, `"ate"` -> `"aet"`).
- **Count tuple** — a 26-length tuple of letter frequencies, e.g.
  `tuple(count[0..25])`. All anagrams share the same counts. Tuples are hashable, so
  they can be dictionary keys.

Algorithm (sorted-key version):

1. Create `groups = defaultdict(list)`.
2. For each `word`, compute `key = "".join(sorted(word))` and append `word` to
   `groups[key]`.
3. Return `list(groups.values())`.

```python
def groupAnagrams(self, strs):
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))   # canonical signature shared by all anagrams
        groups[key].append(word)
    return list(groups.values())
```

Count-key version (avoids the `log L` sort factor):

```python
def groupAnagrams(self, strs):
    groups = defaultdict(list)
    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord('a')] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())
```

**Why it is correct:** the signature is a canonical form — a function that maps every
member of an anagram class to the same value and members of different classes to
different values. Grouping by an exact-equality key therefore places two strings in the
same bucket **iff** they are anagrams, which is exactly the required partition.

- **Time:** sorted keys -> `O(n * L log L)`; count keys -> `O(n * L)` where `n` is the
  number of strings and `L` the maximum length.
- **Space:** `O(n * L)` to store all strings across the groups.

## Key Insights & Edge Cases

- **Signature = canonical form.** This is the reusable trick: anytime you need to
  group/dedupe by "same multiset of characters," hash the sorted string or count tuple.
- **Sorted string vs. count tuple.** Sorting is shorter to write; the count tuple is
  asymptotically faster (no `log L`) and shines when `L` is large or the alphabet is
  small and fixed. Both are valid keys because both are canonical and hashable.
- **Empty string** is its own valid group (Example 2): its signature is `""` or an
  all-zero count tuple.
- **Single string / all-unique inputs** each land in their own singleton group.
- **Do not use a raw count *list* as a dict key** — lists are unhashable. Convert to a
  `tuple` (or a string) first.
- **Output order is unspecified**, so returning `groups.values()` in insertion order is
  fine; no sorting of the result is required.
