# Random Flip Matrix

**Difficulty:** Hard

**Source:** LeetCode 519 — Random Flip Matrix

## Description

There is an `m x n` binary grid `matrix` where **all** cells are initially `0`. Design
an algorithm to randomly pick an index `(i, j)` where `matrix[i][j] == 0` and flip it
to `1`. All the cells that are currently `0` should be **equally likely** to be
returned.

Optimize your algorithm to minimize the number of calls to the built-in random
function and to use as **little extra space** as possible.

Implement the `Solution` class:

- `Solution(m, n)` initializes the object with the size of the grid `m x n`.
- `int[] flip()` returns a random index `[i, j]` of a cell currently equal to `0`, and
  flips it to `1`.
- `void reset()` resets all values of the grid back to `0`.

Flatten the grid into a virtual array of `total = m * n` cell ids `0 .. total-1`, where
id `id` maps to `(id // n, id % n)`. Each `flip()` should behave like drawing the next
element of a Fisher–Yates shuffle over that virtual array: pick a uniformly random id
from the shrinking pool of not-yet-flipped ids, and "swap" it out of the pool. Because
`total` can be up to `10^9`, you cannot materialize the array — record only the swaps
in a **hash map**.

## Constraints

- `1 <= m, n <= 10^4`
- There will be at least one free cell for each call to `flip`.
- At most `1000` calls will be made to `flip` and `reset`.

## Examples

### Example 1

```
Input:
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]

Output:
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

Explanation:
Solution solution = new Solution(3, 1);  // a 3x1 grid, ids 0->[0,0], 1->[1,0], 2->[2,0]
solution.flip();  // returns e.g. [1, 0] — one of the 3 zero cells, each prob 1/3
solution.flip();  // returns e.g. [2, 0] — one of the 2 remaining zeros, each prob 1/2
solution.flip();  // returns [0, 0] — the last remaining zero (forced)
solution.reset(); // all cells back to 0
solution.flip();  // returns e.g. [2, 0] — again any of the 3 cells, each prob 1/3
```

### Example 2

```
Input:
["Solution", "flip", "flip", "reset", "flip"]
[[2, 3], [], [], [], []]

Output:
[null, [1, 2], [0, 0], null, [1, 1]]

Explanation:
A 2x3 grid has 6 cells (ids 0..5), id -> (id // 3, id % 3).
flip() returns each of the 6 zero cells with probability 1/6; here it returns
id 5 -> [1, 2]. The next flip() draws from the 5 remaining ids, returning id 0 -> [0, 0]
with probability 1/5. reset() restores all 6 cells to 0, and the following flip() again
picks uniformly from all 6.
```

## Hint

Treat the grid as a flat virtual array of `m * n` cell ids and run a lazy, map-backed
**Fisher–Yates Shuffle**: keep a `remaining` count, draw a random id in `[0, remaining)`,
translate it through a hash map that remembers prior swaps, then map the last live id
into that slot and shrink `remaining`. `reset()` just clears the map and restores the
count.
