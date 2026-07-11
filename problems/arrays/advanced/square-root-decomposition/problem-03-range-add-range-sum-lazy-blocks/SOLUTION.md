# Range Add & Range Sum (Lazy Blocks) — Solution

## Brute Force

Store the array. `range_add(left, right, delta)` loops over every index in the
range adding `delta` (`O(n)`); `range_sum(left, right)` loops adding values
(`O(n)`).

```python
def range_add(self, left, right, delta):
    for i in range(left, right + 1):
        self.nums[i] += delta
def range_sum(self, left, right):
    return sum(self.nums[left:right + 1])
```

With `10^5` operations of size up to `10^5`, this is `O(q * n) = 10^{10}` in the
worst case — too slow. The key waste is `range_add` touching every element even
when it spans many whole blocks that could be updated in bulk.

## Optimal Approach (Square Root Decomposition + Lazy Add)

Divide the array into blocks of size `b ≈ sqrt(n)` (element `i` in block
`i // b`). Keep two auxiliary arrays over blocks:

- `block_sum[k]` — sum of the **explicitly stored** element values in block `k`.
- `block_add[k]` — a **pending (lazy) add** applied conceptually to *every*
  element of block `k` but not yet pushed into `nums`.

The true value of element `i` is always `nums[i] + block_add[i // b]`, and the
true sum of block `k` is `block_sum[k] + block_add[k] * (size of block k)`.

**range_add(left, right, delta)** — same three-part split as a query:

1. **Partial left block:** add `delta` directly to each in-range element and to
   that block's `block_sum`.
2. **Whole interior blocks:** just do `block_add[k] += delta`. This records the
   update for the entire block in `O(1)` — the lazy trick.
3. **Partial right block:** update element-by-element like the left.

```python
def range_add(self, left, right, delta):
    b = self.b
    lb, rb = left // b, right // b
    if lb == rb:
        for i in range(left, right + 1):
            self.nums[i] += delta
            self.block_sum[lb] += delta
        return
    for i in range(left, (lb + 1) * b):     # partial left block
        self.nums[i] += delta
        self.block_sum[lb] += delta
    for k in range(lb + 1, rb):             # whole interior blocks (lazy)
        self.block_add[k] += delta
    for i in range(rb * b, right + 1):      # partial right block
        self.nums[i] += delta
        self.block_sum[rb] += delta
```

**range_sum(left, right)** — mirror the split, adding the lazy contribution:

1. **Partial left block:** for each in-range element `i`, add
   `nums[i] + block_add[lb]`.
2. **Whole interior blocks:** add
   `block_sum[k] + block_add[k] * (block length)`.
3. **Partial right block:** like the left.

```python
def range_sum(self, left, right):
    b = self.b
    lb, rb = left // b, right // b
    total = 0
    if lb == rb:
        for i in range(left, right + 1):
            total += self.nums[i] + self.block_add[lb]
        return total
    for i in range(left, (lb + 1) * b):     # partial left block
        total += self.nums[i] + self.block_add[lb]
    for k in range(lb + 1, rb):             # whole interior blocks
        length = min((k + 1) * b, self.n) - k * b
        total += self.block_sum[k] + self.block_add[k] * length
    for i in range(rb * b, right + 1):      # partial right block
        total += self.nums[i] + self.block_add[rb]
    return total
```

**Why it is correct.** The invariant "true value of `i` =
`nums[i] + block_add[i // b]`" holds after every operation:

- Whole-block adds bump only `block_add[k]`, preserving the invariant for those
  blocks without touching individual elements.
- Partial-block adds bump the actual `nums[i]` (and `block_sum`), so those
  elements' true values are correct with their block's existing lazy tag.

`range_sum` reconstructs each element's true value by adding back its block's
lazy tag, and for whole blocks it multiplies the tag by the block length —
exactly the sum of the pending adds over that block. Every index is counted
once (partial loops for boundary blocks, block totals for interior blocks).

**Complexity.** Both operations touch `< b` elements per boundary plus
`< n / b` whole blocks. With `b ≈ sqrt(n)` that is `O(sqrt(n))` per operation.
Overall `O(n + q * sqrt(n))` time, `O(n)` space.

## Key Insights & Edge Cases

- **Lazy tags are the whole point.** Recording a whole-block add in `O(1)` is
  what makes `range_add` sublinear; without it you would touch every element.
- **Block length varies for the last block.** Use
  `min((k + 1) * b, n) - k * b` rather than assuming every block has size `b`.
- **Two consistent views.** Element loops read `nums[i] + block_add[k]`; block
  loops read `block_sum[k] + block_add[k] * length`. Mixing these up (e.g.
  forgetting the lazy tag in the element loop) is the classic bug.
- **Single-block ranges** (`lb == rb`) are special-cased so boundaries are not
  processed twice.
- **Alternative: push-down.** You could instead "flush" a block's lazy tag into
  its elements before a partial touch; the version above avoids that by always
  reading the tag on the fly, which is simpler.
- A segment tree with lazy propagation solves this in `O(log n)` per op; sqrt
  decomposition is a lighter-weight structure with the same big-picture idea.
