# Find the Difference — Solution

## Brute Force

Sort both strings and walk them in lockstep. The first index where the sorted
strings disagree exposes the inserted letter; if they agree everywhere, the extra
letter is the last character of the (longer) sorted `t`.

```python
def findTheDifference(s: str, t: str) -> str:
    ss, tt = sorted(s), sorted(t)
    for a, b in zip(ss, tt):
        if a != b:
            return b
    return tt[-1]
```

- **Time:** O(n log n) for the sorts.
- **Space:** O(n) for the sorted lists.

## Optimal Approach (Character Frequency Count)

The added letter is exactly the character whose count in `t` is one greater than
its count in `s`. Compute the element-wise difference of the two frequency vectors
and read off the letter with a positive residual.

Steps:

1. Allocate a size-26 array `counts`.
2. Add for every character in `t`: `counts[ord(ch) - ord('a')] += 1`.
3. Subtract for every character in `s`: `counts[ord(ch) - ord('a')] -= 1`.
4. Every letter shared by both strings nets to `0`; the single inserted letter
   nets to `+1`. Return the character whose bucket is positive.

```python
def findTheDifference(s: str, t: str) -> str:
    counts = [0] * 26
    for ch in t:
        counts[ord(ch) - ord('a')] += 1
    for ch in s:
        counts[ord(ch) - ord('a')] -= 1
    for i in range(26):
        if counts[i] > 0:
            return chr(i + ord('a'))
    return ""  # unreachable given the problem guarantees
```

**Why it is correct:** `counts` is `freq(t) - freq(s)`. Because `t` is `s` plus one
extra letter `x`, the two frequency vectors are identical except that
`freq(t)[x] = freq(s)[x] + 1`. Hence exactly one bucket is `+1` and all others are
`0`, and that bucket's letter is the answer.

- **Time:** O(n) — one pass over each string plus a constant 26-slot scan.
- **Space:** O(1).

## Elegant Alternative: XOR

Because every original character appears an even number of times across `s + t`
and only the added letter appears an odd number of times, XOR-ing the code points
of all characters of both strings cancels the pairs and leaves the extra letter:

```python
def findTheDifference(s: str, t: str) -> str:
    acc = 0
    for ch in s + t:
        acc ^= ord(ch)
    return chr(acc)
```

Also O(n) time and O(1) space, using no auxiliary array at all. The XOR trick is
the "sum/xor invariant" cousin of the frequency-count idea. A summation variant
(`chr(sum(map(ord, t)) - sum(map(ord, s)))`) works too.

## Key Insights & Edge Cases

- **Empty `s`:** `t` is a single character, which nets to `+1` and is returned
  directly — no special casing needed.
- **Repeated letters** (e.g. `s = "aabb"`, `t = "abbba"`): counting handles
  multiplicity correctly, whereas a naive "which letter is new?" set-difference
  would wrongly report nothing new.
- **Exactly one differing letter is guaranteed** by the constraints, so a single
  positive bucket always exists; the trailing `return ""` is defensive only.
