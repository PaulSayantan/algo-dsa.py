# Tower of Hanoi — Solution

## Brute Force

There is no meaningful "brute force" that beats the recursive structure: any legal
solution must make at least `2^n - 1` moves, and the recursive strategy achieves
exactly that. A non-recursive attempt would try to enumerate or search sequences of
moves for a valid ordering — an exponential search space with no benefit. One could
also solve it **iteratively** (there is a known parity-based loop that moves the
smallest disk every other turn), but that iterative rule is far less intuitive than the
recursion and is really just the recursion's move-order unrolled.

- **Search-based brute force:** effectively exponential and pointless here.
- The recursive decomposition below *is* the optimal algorithm.

## Optimal Approach (Recursion)

To move `n` disks from `source` to `target` with `auxiliary` as the spare peg, the
largest disk (disk `n`, on the bottom) can only move once everything above it is out of
the way. That gives a clean three-step plan:

1. **Move the top `n - 1` disks** from `source` to `auxiliary` (using `target` as the
   temporary spare). This is the same problem, one disk smaller.
2. **Move disk `n`** — the single largest disk — directly from `source` to `target`.
3. **Move the `n - 1` disks** from `auxiliary` to `target` (using `source` as the
   temporary spare). Again the same problem, one disk smaller.

```python
class Solution:
    def towerOfHanoi(self, n, source="A", auxiliary="B", target="C"):
        moves = []

        def rec(k, src, aux, tgt):
            if k == 0:                    # base case: no disks to move
                return
            rec(k - 1, src, tgt, aux)      # step 1: top k-1 to the spare
            moves.append((src, tgt))       # step 2: move the largest disk
            rec(k - 1, aux, src, tgt)      # step 3: k-1 from spare to target

        rec(n, source, auxiliary, target)
        return moves
```

**Why it is correct:** By induction on `k`.

- *Base case:* `k == 0` requires no moves — correct.
- *Inductive step:* assume `rec(k-1, ...)` correctly and legally moves any `k - 1`
  disks between two pegs using the third as spare. Then step 1 legally relocates the
  top `k - 1` disks onto `aux` (they never touch disk `k`, which is larger than all of
  them, so no rule is violated). With `src` now holding only disk `k`, step 2 moves it
  onto an empty-or-larger-topped `tgt` — legal because disk `k` is the largest. Step 3
  legally stacks the `k - 1` disks back on top of disk `k`. The result is all `k` disks
  on `tgt`. Each recursive call reduces `k` by one, guaranteeing termination.

**Move count:** `T(n) = 2·T(n-1) + 1`, with `T(0) = 0`. Solving: `T(n) = 2^n - 1`.

**Step by step for `n = 2` (`source=A, aux=B, target=C`):**

1. `rec(2, A, B, C)` → first `rec(1, A, C, B)`: moves the small disk `A -> B`.
2. Record disk 2: `A -> C`.
3. `rec(1, B, A, C)`: moves the small disk `B -> C`.

Result: `[('A','B'), ('A','C'), ('B','C')]` — 3 = `2^2 - 1` moves. ✓

- **Time:** `O(2^n)` — there are `2^n - 1` moves, and the work is proportional to the
  number of moves produced.
- **Space:** `O(n)` recursion-stack depth (plus `O(2^n)` to store the move list itself,
  if you return all moves).

## Key Insights & Edge Cases

- **The peg roles rotate on each call.** The trickiest part is passing the pegs in the
  right order: in step 1 the *target* becomes the spare (`rec(k-1, src, tgt, aux)`), and
  in step 3 the *source* becomes the spare (`rec(k-1, aux, src, tgt)`). Getting these
  swaps right is the whole problem.
- **Base case `k == 0`** (rather than `k == 1`) keeps the recursion uniform — every
  disk is moved by exactly one `moves.append`, and there is no special-casing of a
  single disk.
- **Exponential is unavoidable:** the output itself has `2^n - 1` moves, so no algorithm
  can be faster than `O(2^n)`. This is *not* the overlapping-subproblems kind of
  exponential (memoization would not help) — the work is inherent in the answer's size.
- **Stack depth is only `O(n)`,** even though the running time is `O(2^n)`: the tree of
  calls is broad, not deep. For `n <= 20` (up to ~1,048,575 moves) this is fine.
- The two-branch recurrence `T(n) = 2T(n-1) + 1` is a canonical example of **branching
  recursion** and contrasts sharply with linear recursion (`T(n) = T(n-1) + O(1)`) —
  the extra branch is what turns linear time into exponential time.
