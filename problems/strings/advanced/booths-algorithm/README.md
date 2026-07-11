# Booth's Algorithm — Least Rotation of a String

**Booth's Algorithm** finds the starting index of the **lexicographically smallest
rotation** of a string in **O(n) time** and **O(n) extra space** (the classic
formulation appends `S + S` and runs a modified Knuth–Morris–Pratt failure-function
scan over it).

A *rotation* of `S = s0 s1 ... s(n-1)` is any string `s_i s_{i+1} ... s_{n-1} s_0 ... s_{i-1}`.
There are `n` rotations, and the "least rotation" is the rotation that comes first in
dictionary order. The naive way — generate all `n` rotations and take the minimum — is
`O(n^2)` (or `O(n^2)` comparisons even with clever tricks). Booth's algorithm reaches
the same answer in a single linear scan.

## When to reach for it

- You need the **canonical form** of a cyclic string so that all rotations of the same
  string map to one representative (necklace canonicalization, hashing cyclic sequences,
  deduplicating circular DNA/genome fragments).
- You need the **index** at which the smallest (or, by negating the comparison, largest)
  rotation begins.
- A problem lets you rotate a string one character at a time an unlimited number of times
  and asks for the smallest reachable string.
- You are comparing/counting cyclic strings and `O(n^2)` per string is too slow.

Booth's algorithm is the specialized, constant-factor-friendly choice for *least rotation*.
The more general **Lyndon-word / Duval "least rotation via Lyndon factorization"** and
**suffix-automaton / suffix-array on `S+S`** approaches solve the same problem, also in
`O(n)`, and are worth knowing as alternatives.

## Complexity

| Metric | Cost |
|---|---|
| Time  | `O(n)` |
| Extra space | `O(n)` for the failure array `f` over `S+S` |

## Core routine (reference)

```python
def least_rotation(s: str) -> int:
    """Return the index in s where the lexicographically smallest rotation begins."""
    n = len(s)
    ss = s + s                      # concatenate so rotations are substrings of length n
    f = [-1] * len(ss)              # failure function over ss
    k = 0                           # candidate start of the least rotation
    for j in range(1, len(ss)):
        sj = ss[j]
        i = f[j - k - 1]
        while i != -1 and sj != ss[k + i + 1]:
            if sj < ss[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != ss[k + i + 1]:
            if sj < ss[k]:          # sj < ss[k + i + 1] with i == -1
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k % n
```

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Lexicographically Smallest Rotation](problem-01-lexicographically-smallest-rotation/PROBLEM.md) | Direct application: return the least rotation string | Easy |
| 2 | [Glass Beads](problem-02-glass-beads/PROBLEM.md) | Return the 1-based index where the least rotation starts (UVa 719) | Easy–Medium |
| 3 | [Orderly Queue](problem-03-orderly-queue/PROBLEM.md) | `k == 1` reduces to least rotation; `k >= 2` sorts (LeetCode 899) | Medium–Hard |
| 4 | [Count Distinct Necklaces](problem-04-count-distinct-necklaces/PROBLEM.md) | Canonicalize each string by its least rotation, then dedupe | Medium |
| 5 | [Count Distinct Bracelets](problem-05-count-distinct-bracelets/PROBLEM.md) | Canonicalize under rotation **and** reflection | Hard |
