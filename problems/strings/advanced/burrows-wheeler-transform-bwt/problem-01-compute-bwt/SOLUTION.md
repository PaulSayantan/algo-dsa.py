# Solution — Compute the BWT

## Brute Force

Directly follow the definition:

1. Generate all `n` cyclic rotations. Rotation `i` is `text[i:] + text[:i]`.
2. Sort the list of rotations lexicographically.
3. Concatenate the last character of each sorted rotation.

```python
def bwt(text: str) -> str:
    n = len(text)
    rotations = sorted(text[i:] + text[:i] for i in range(n))
    return "".join(rot[-1] for rot in rotations)
```

- **Time:** `O(n^2 log n)`. There are `n` rotations, each of length `n`; sorting does
  `O(n log n)` comparisons and each comparison can touch up to `O(n)` characters.
- **Space:** `O(n^2)` because every rotation is materialized in full.

This is fine for small inputs and is the clearest way to *understand* the transform,
but it blows up for large `n`.

## Optimal Approach (BWT via suffix array)

The key observation that makes BWT efficient and connects it to the rest of stringology:

> Because the sentinel `$` is **unique** and **smallest**, sorting the cyclic rotations
> produces exactly the same order as sorting the **suffixes** of `text`. A rotation
> starting at index `i` and the suffix starting at index `i` agree on every character
> up to and including the `$`, and no comparison ever needs to look past `$`.

So if `SA` is the suffix array (indices of suffixes in sorted order), the `i`-th sorted
rotation begins at `SA[i]`, and the **last** character of that rotation is the character
*just before* position `SA[i]` in the cyclic string:

```
L[i] = text[(SA[i] - 1) mod n]
```

When `SA[i] == 0` the rotation is the full string `text` itself, whose last character is
the sentinel `$`; `(0 - 1) mod n = n - 1` correctly indexes that `$`.

```python
def suffix_array(text: str):
    # O(n log^2 n) with prefix-doubling; O(n) with DC3/SA-IS in libraries.
    return sorted(range(len(text)), key=lambda i: text[i:])

def bwt(text: str) -> str:
    sa = suffix_array(text)
    return "".join(text[i - 1] for i in sa)   # i - 1 == -1 -> last char == '$'
```

- **Time:** dominated by suffix-array construction — `O(n log n)` with prefix doubling,
  or `O(n)` with SA-IS / DC3. The final pass is `O(n)`.
- **Space:** `O(n)` for the suffix array and output, versus `O(n^2)` for the naive
  version.

**Why it is correct:** the map `i -> SA[i]` enumerates rotations in sorted order (by the
suffix-vs-rotation equivalence above), and `text[SA[i]-1]` is by definition the last
column of the BWM for that row.

## Key Insights & Edge Cases

- **Sentinel is mandatory.** Without a unique smallest `$`, two rotations could be equal
  (e.g. `"abab"`) and the transform would not be uniquely invertible. Every problem in
  this set assumes the `$` terminator.
- **The last column groups similar characters.** Characters preceding similar contexts
  end up adjacent, giving long runs — the property `bzip2` compresses.
- **`L[i] = text[SA[i]-1]`** is the single most useful identity; it links BWT, suffix
  arrays, and the FM-index.
- **Edge case — all identical letters** like `"AA$"`: the transform is well-defined and
  the roundtrip still works because `$` breaks ties.
- **Edge case — length 1** (just `"$"`): the BWT is `"$"`.
- Prefer the suffix-array route for `n` beyond a few thousand; the naive rotation sort
  is quadratic in memory and will not scale.
