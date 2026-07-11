# Solution — Count Distinct Necklaces

## Brute Force

For each pair of equal-length strings, test whether one is a rotation of the other
(`b in a + a`) and union them, or generate every rotation of each string and use the
minimum as a key.

A naive all-pairs comparison is:

```python
def count_brute(words):
    reps = []
    for w in words:
        rots = {w[i:] + w[:i] for i in range(len(w))}
        # is w a rotation of any already-seen representative?
        if not any(r in rots for r in reps):
            reps.append(w)
    return len(reps)
```

- Generating all rotations of one word is `O(L^2)`, and comparing against all
  representatives multiplies further.
- **Time:** up to `O(N * L^2)` or worse for `N` words of length `L`. **Space:** `O(L)`
  per rotation set.

This blows up when total length approaches `10^6`.

## Optimal Approach — Booth's Canonicalization

Give every necklace a single **canonical name**: its lexicographically smallest
rotation. Two strings are the same necklace **iff** their canonical names are equal
(rotation is an equivalence relation, and the smallest rotation is invariant under
rotation). So:

1. For each word `w`, compute `canon(w) = smallest_rotation(w)` with Booth's Algorithm
   in `O(len(w))`.
2. Insert each `canon(w)` into a hash set.
3. The answer is the size of the set.

```python
def least_rotation(s: str) -> int:
    n = len(s)
    ss = s + s
    f = [-1] * len(ss)
    k = 0
    for j in range(1, len(ss)):
        sj = ss[j]
        i = f[j - k - 1]
        while i != -1 and sj != ss[k + i + 1]:
            if sj < ss[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != ss[k + i + 1]:
            if sj < ss[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k % n


def canonical(s: str) -> str:
    if not s:
        return s
    k = least_rotation(s)
    return s[k:] + s[:k]


def count_distinct_necklaces(words):
    return len({canonical(w) for w in words})
```

### Why it is correct

- **Rotation is an equivalence relation** (reflexive, symmetric, transitive) on strings
  of a given length; its classes are exactly "necklaces."
- The lexicographically smallest rotation is the **same** for every member of a class
  (rotating a string does not change the *set* of its rotations, hence not their
  minimum). It is therefore a well-defined canonical representative.
- Strings of different lengths land in different classes automatically because their
  canonical forms differ in length.
- Counting distinct canonical strings counts distinct classes.

- **Time:** `O(total length)` — Booth's is linear per word; hashing a length-`L` string
  is `O(L)`. **Space:** `O(total length)` for the set of canonical strings.

## Key Insights & Edge Cases

- **Different lengths never collide:** no special handling needed; canonical forms keep
  their length.
- **Periodic strings** (`"abab"`, `"aaaa"`): canonicalization still returns a single
  well-defined string, so all rotations of a periodic word collapse to one entry.
- **Duplicate words:** identical strings share a canonical form and count once — correct.
- **Hashing cost:** if you worry about hashing long strings, you can store a rolling hash
  of the canonical form, but plain string hashing is `O(total length)` overall.
- **This canonicalization pattern** (map to least rotation, then dedupe/compare) is the
  workhorse for any problem about cyclic-string equality: deduping circular DNA reads,
  grouping cyclic permutations, etc.
