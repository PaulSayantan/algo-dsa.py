# Solution — Static Range Sum Query

## Brute Force

For each query, loop from `l` to `r` and accumulate.

```python
def query(nums, l, r):
    return sum(nums[l:r+1])
```

- **Time:** O(n) per query, O(q·n) total.
- **Space:** O(1) extra.

Too slow when both `n` and `q` are up to 1e5 (up to 1e10 operations).

## Optimal Approach (Sqrt Tree)

We build a **Sqrt Tree** with `op = +`. Any range `[l, r]` is answered from three
precomputed pieces, so a query costs O(1).

### Structure

Let `n` be the array length. On each *layer* the current segment is split into blocks of
size `b = 2^ceil(log2(len)/2)` (roughly `√len`). For every layer we store:

- `pref[layer][i]` — `op` of everything from the start of `i`'s block up to and including
  `i`.
- `suf[layer][i]` — `op` of everything from `i` to the end of `i`'s block.
- `between[layer][·]` — for whole-block indices `(bl, br)`, the `op` over all elements from
  block `bl` through block `br`. There are `blockCount^2 ≈ len` such entries per segment.

The structure is then applied **recursively** to each block, so that queries lying inside
a single block are also O(1). Recursion depth is `O(log log n)`.

### Query decomposition

For a query `[l, r]` with `l < r` (spanning at least two blocks at the chosen layer):

```
answer = suf[layer][l]                      # from l to the end of its block
if there are whole blocks strictly between:
    answer = op(answer, between[layer][bl..br])
answer = op(answer, pref[layer][r])         # from the start of r's block to r
```

Choosing the layer: the two indices differ first at bit position `msb(l XOR r)`. A
precomputed `on_layer` table maps that bit position to the layer whose block size is large
enough that `l` and `r` fall in *different* blocks but the *same* segment — guaranteeing
the three-piece decomposition applies. If `l == r` return `nums[l]`; if `l + 1 == r`
return `op(nums[l], nums[r])`.

### Why it is correct

Addition is **associative**, so grouping the range as
`(l..blockEnd) · (whole blocks) · (blockStart..r)` yields the same total regardless of how
we parenthesize. Each of the three groups is a value we precomputed exactly. The layer
selection guarantees `l` and `r` sit in distinct blocks of one segment, so the suffix,
between, and prefix pieces are disjoint and cover `[l, r]` exactly.

### Reference implementation (answer key)

```python
class RangeSum:
    def __init__(self, nums):
        self.op = lambda x, y: x + y
        self.v = list(nums)
        self.n = len(self.v)
        self.lg = max(1, (self.n - 1).bit_length())
        self.layers, self.on_layer = [], [0] * (self.lg + 1)
        tlg = self.lg
        while tlg > 1:
            self.on_layer[tlg] = len(self.layers)
            self.layers.append(tlg)
            tlg = (tlg + 1) >> 1
        for i in range(self.lg - 1, -1, -1):
            self.on_layer[i] = max(self.on_layer[i], self.on_layer[i + 1])
        L = len(self.layers)
        self.pref = [[0] * self.n for _ in range(L)]
        self.suf = [[0] * self.n for _ in range(L)]
        self.between = [[0] * (1 << (self.lg + 1)) for _ in range(L)]
        if L:
            self._build(0, 0, self.n)

    def _build(self, layer, lb, rb):
        if layer >= len(self.layers):
            return
        bs = 1 << ((self.layers[layer] + 1) >> 1)
        l = lb
        while l < rb:
            r = min(l + bs, rb)
            self.pref[layer][l] = self.v[l]
            for i in range(l + 1, r):
                self.pref[layer][i] = self.op(self.pref[layer][i - 1], self.v[i])
            self.suf[layer][r - 1] = self.v[r - 1]
            for i in range(r - 2, l - 1, -1):
                self.suf[layer][i] = self.op(self.v[i], self.suf[layer][i + 1])
            self._build(layer + 1, l, r)
            l += bs
        bsl = (self.layers[layer] + 1) >> 1
        bcl = self.layers[layer] >> 1
        bcnt = (rb - lb + (1 << bsl) - 1) >> bsl
        for i in range(bcnt):
            acc = None
            for j in range(i, bcnt):
                add = self.suf[layer][lb + (j << bsl)]
                acc = add if i == j else self.op(acc, add)
                self.between[layer][lb + (i << bcl) + j] = acc

    def query(self, l, r):
        if l == r:
            return self.v[l]
        if l + 1 == r:
            return self.op(self.v[l], self.v[r])
        layer = self.on_layer[(l ^ r).bit_length()]
        bsl = (self.layers[layer] + 1) >> 1
        bcl = self.layers[layer] >> 1
        lb = (l >> self.layers[layer]) << self.layers[layer]
        lblk = ((l - lb) >> bsl) + 1
        rblk = ((r - lb) >> bsl) - 1
        ans = self.suf[layer][l]
        if lblk <= rblk:
            ans = self.op(ans, self.between[layer][lb + (lblk << bcl) + rblk])
        return self.op(ans, self.pref[layer][r])
```

- **Build:** O(n log log n) time, O(n log log n) space.
- **Query:** O(1).

## Key Insights & Edge Cases

- **Single-element / adjacent queries** (`l == r`, `l + 1 == r`) are special-cased because
  the three-piece decomposition needs `l` and `r` in different blocks.
- **`on_layer` via `msb(l XOR r)`** is the trick that makes queries O(1): the highest set
  bit of `l ^ r` tells you the coarsest block size at which `l` and `r` already separate.
- Because addition is invertible, a plain **prefix-sum array** solves this specific problem
  in O(n) build / O(1) query and is simpler. Use it as a **ground-truth oracle** to test
  your Sqrt Tree. The Sqrt Tree earns its keep on the *later* problems where prefix sums
  and sparse tables both fail.
- **Overflow:** in Python, integers are unbounded; in C++/Java use 64-bit for the sums.
