# Holes — Ball Jumping with Power Updates — Solution

## Brute Force

Store `powers`. `set_power` overwrites a cell in `O(1)`. `throw(start)`
simulates the ball one jump at a time:

```python
def throw(self, start):
    pos, jumps, last = start, 0, start
    while pos < self.n:
        last = pos
        pos += self.powers[pos]
        jumps += 1
    return [last, jumps]
```

When many powers equal `1`, a single throw makes `O(n)` jumps, so `q` throws
cost `O(q * n) = 10^{10}` in the worst case — too slow. The waste is re-walking
the same short hops over and over.

## Optimal Approach (Square Root Decomposition on the Jump Graph)

The jumps form a forest: hole `i` points to `i + powers[i]` (or off the row).
Answering a throw is walking this chain. Sqrt decomposition lets us **compress**
each block of the chain into a single hop.

Split holes into blocks of size `b ≈ sqrt(n)`; hole `i` is in block `i // b`.
For **every** hole `i` precompute three values that describe what happens once
the ball enters `i` and follows jumps *only until it leaves i's block*:

- `jumps[i]` — number of jumps to leave the block (or the row) starting at `i`.
- `exit_hole[i]` — the hole the ball lands on right after leaving the block
  (this may be `>= n`, meaning it left the row entirely).
- `last_in_block[i]` — the last hole *inside this block* the ball occupies
  before leaving.

**Computing a block (right to left).** Let `be = min((k + 1) * b, n)` be the
block's exclusive end. Process indices from `be - 1` down to `k * b`:

```python
def _rebuild_block(self, k):
    b, n = self.b, self.n
    start = k * b
    be = min(start + b, n)
    for i in range(be - 1, start - 1, -1):
        j = i + self.powers[i]
        if j >= be:                        # one jump leaves the block (or row)
            self.jumps[i] = 1
            self.exit_hole[i] = j
            self.last_in_block[i] = i
        else:                              # stays in block -> reuse j's answers
            self.jumps[i] = self.jumps[j] + 1
            self.exit_hole[i] = self.exit_hole[j]
            self.last_in_block[i] = self.last_in_block[j]
```

Because `j > i` and `j < be`, the values for `j` are already computed when we
reach `i` — that is why we sweep **right to left**. Building all blocks once is
`O(n)`.

**set_power(index, val)** — only the block containing `index` can change (jumps
never point left, and no hole outside the block relies on `index`'s stored
values). Overwrite the power and rebuild that one block:

```python
def set_power(self, index, val):
    self.powers[index] = val
    self._rebuild_block(index // self.b)
```

That is `O(b) = O(sqrt(n))`.

**throw(start)** — hop **block by block** using the compressed edges:

```python
def throw(self, start):
    pos, total, last = start, 0, start
    while pos < self.n:
        last = self.last_in_block[pos]
        total += self.jumps[pos]
        pos = self.exit_hole[pos]
    return [last, total]
```

Each iteration advances `pos` into a strictly later block (or off the row), so
the loop runs at most `n / b + 1 ≈ sqrt(n)` times.

**Why it is correct.** For a fixed configuration, the exact jump chain from any
hole is deterministic. The block precomputation encodes precisely the segment of
that chain that stays within one block: `jumps[i]` counts those jumps,
`last_in_block[i]` is the final hole reached before crossing the block boundary,
and `exit_hole[i]` is where the chain continues. Concatenating these per-block
summaries reproduces the full chain: the total jump count is the sum of the
per-block jump counts, and the last occupied hole is `last_in_block` of the
final block entered (the block from which the ball leaves the row). Since
`set_power` rebuilds the affected block, all stored summaries stay consistent
with `powers`.

**Complexity.** `throw` is `O(sqrt(n))` (block-to-block hops); `set_power` is
`O(sqrt(n))` (rebuild one block); build is `O(n)`. Total for `q` operations:
`O(n + q * sqrt(n))`. Space is `O(n)` for the three auxiliary arrays.

## Key Insights & Edge Cases

- **Right-to-left rebuild is essential.** A hole depends only on holes to its
  right within the block, so processing in decreasing index order lets each
  entry reuse an already-finished neighbor in `O(1)`.
- **`exit_hole` can exceed `n - 1`.** That sentinel value ( `>= n` ) is exactly
  what stops the `throw` loop, signalling the ball left the row; no special flag
  is needed.
- **Locality of updates.** Because jumps always move forward and each stored
  answer is computed only from same-block holes, a power change never affects
  another block — this is what keeps `set_power` at `O(sqrt(n))`.
- **Last block is variable length** (`min((k+1)*b, n)`); using `be` as the
  exclusive end handles the ragged final block.
- **`last` initialization:** seeding `last = start` is harmless since any
  `start < n` immediately overwrites it on the first loop iteration; a throw
  with `start >= n` is out of the constraints.
- This "pointer-jumping / block-jump" pattern is a hallmark hard application of
  sqrt decomposition: it compresses a linked-list walk rather than aggregating
  values, showing the technique reaches well beyond simple range sums.
