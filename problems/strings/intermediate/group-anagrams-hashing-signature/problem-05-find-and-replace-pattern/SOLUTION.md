# Find and Replace Pattern — Solution

## Brute Force

For each word, try to build the letter mapping `pattern -> word` on the fly while
also tracking the reverse mapping to enforce the bijection. Reject the word the
moment a conflict appears.

```python
def matches(word, pattern):
    forward, backward = {}, {}
    for pc, wc in zip(pattern, word):
        if forward.setdefault(pc, wc) != wc:
            return False
        if backward.setdefault(wc, pc) != pc:
            return False
    return True

def findAndReplacePattern(words, pattern):
    return [w for w in words if matches(w, pattern)]
```

This is actually already `O(n * k)` and correct — the "brute force" label here
just means we re-derive a mapping per word instead of precomputing a single
canonical key. It needs *two* dictionaries because a one-directional map would
wrongly accept `"ccc"` for pattern `"aba"` (both `a` and `b` mapping to `c`).

- **Time:** `O(n * k)` where `n = len(words)`, `k = len(pattern)`.
- **Space:** `O(k)` per word for the two maps (`O(A)` alphabet-bounded).

## Optimal Approach (Hashing Signature)

Give every string a canonical **isomorphism signature** so that two strings are
bijection-equivalent **iff** their signatures are equal. The cleanest signature
is **first-occurrence normalization**: relabel each character by the order in
which it first appears.

```
"abb" -> a is new -> 0, b is new -> 1, b seen -> 1   => (0, 1, 1)
"mee" -> m -> 0,     e -> 1,           e -> 1         => (0, 1, 1)   match
"ccc" -> c -> 0,     c -> 0,           c -> 0         => (0, 0, 0)   no match
```

Why it is correct: a bijective relabeling of letters preserves the *pattern of
repetition* — which positions are equal to which — and nothing else. Two strings
are related by a bijection exactly when they share the same repetition pattern.
First-occurrence normalization outputs precisely that repetition pattern: the
`i`-th entry says "this position holds the same letter as the first position
whose normalized id equals this value." Equal signatures therefore imply a valid
bijection in both directions, and unequal signatures rule one out.

Compute the pattern's signature once, then keep the words whose signature equals
it.

Step by step:

1. Write a helper `normalize(word)` that walks the word, assigns each new
   character the next unused integer id, and emits the tuple of ids.
2. `target = normalize(pattern)`.
3. Return `[w for w in words if normalize(w) == target]`.

```python
from typing import List, Tuple

def normalize(word: str) -> Tuple[int, ...]:
    mapping = {}
    out = []
    for ch in word:
        if ch not in mapping:
            mapping[ch] = len(mapping)   # next unused id
        out.append(mapping[ch])
    return tuple(out)

def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    target = normalize(pattern)
    return [w for w in words if normalize(w) == target]
```

- **Time:** `O(n * k)` — normalize each of `n` words in `O(k)`.
- **Space:** `O(k)` for a signature (plus `O(n * k)` if you materialize all of
  them; the generator/comparison approach keeps it to `O(k)` at a time).

## Key Insights & Edge Cases

- **Bijection needs both directions** — the naive one-map approach fails on
  `"ccc"` vs `"aba"`. First-occurrence normalization sidesteps this because a
  single canonical form captures the two-way constraint automatically:
  `"aba" -> (0,1,0)` can never equal `"ccc" -> (0,0,0)`.
- **Equal lengths are guaranteed** by the constraints, but the signature encodes
  length anyway (its tuple length equals the word length), so it is robust even
  if lengths differed.
- **Single-character words** normalize to `(0)` and match a single-character
  pattern — see Example 2.
- **Alternative signature** — you could also key on the tuple of first-occurrence
  *positions* or use the two-dictionary check inline; first-occurrence integer
  ids are the most compact hashable form.
- Same family as Group Shifted Strings (Problem 4): both reduce a string to a
  relabeling/shift-invariant normal form and then compare or bucket.
