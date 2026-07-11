# Solution — Range Minimum Query

## Brute Force

Scan `l..r` for each query.

```python
def query(nums, l, r):
    return min(nums[l:r+1])
```

- **Time:** O(n) per query, O(q·n) total.
- **Space:** O(1) extra.

## Optimal Approach (Sqrt Tree)

Identical machinery to Problem 1, but with `op = min`. The Sqrt Tree stores, per layer:

- `pref[layer][i]` — minimum from the start of `i`'s block through `i`.
- `suf[layer][i]` — minimum from `i` through the end of `i`'s block.
- `between[layer][(bl, br)]` — minimum over whole blocks `bl..br`.

A query `[l, r]` is `min(suf[l], between[inner blocks], pref[r])`. Special cases: `l == r`
returns `nums[l]`; `l + 1 == r` returns `min(nums[l], nums[r])`. Layer chosen from
`msb(l XOR r)`.

### Why it is correct

`min` is associative, so partitioning `[l, r]` into the suffix of `l`'s block, the whole
blocks in between, and the prefix of `r`'s block and taking the `min` of the three partial
minima reproduces the min of the whole range. Crucially, the three pieces are **disjoint**
and their union is exactly `[l, r]`. Sqrt Tree never queries overlapping subranges, so —
unlike a sparse table — it does **not** depend on idempotence (`min(x, x) = x`); that is why
the identical code base carries over to product-mod and function composition.

### Reference implementation (answer key)

Reuse the class from Problem 1 verbatim and set `self.op = lambda x, y: min(x, y)` in the
constructor. Nothing else changes. (See `../problem-01-static-range-sum/SOLUTION.md` for the
full generic Sqrt Tree; only the `op` differs.)

```python
class RangeMin(SqrtTree):     # SqrtTree = the generic class from problem 1
    def __init__(self, nums):
        super().__init__(nums, op=lambda x, y: min(x, y))
```

- **Build:** O(n log log n) time & space.
- **Query:** O(1).

## Key Insights & Edge Cases

- **Sparse Table is the textbook answer** for RMQ (O(n log n) build, O(1) query) precisely
  because `min` is idempotent so overlapping the two covering ranges is harmless. Sqrt Tree
  matches the O(1) query with a slightly different build cost (O(n log log n)) and — the key
  teaching point — **without** needing idempotence.
- **Negative numbers and duplicates** need no special handling; `min` treats them normally.
- **Single-element query** must be handled before the XOR-based layer lookup (which assumes
  `l != r`).
- Use a sentinel of `+inf` only if you build via an identity element; the prefix/suffix
  formulation used here seeds each block with `nums[l]` / `nums[r-1]` directly and needs no
  sentinel.
