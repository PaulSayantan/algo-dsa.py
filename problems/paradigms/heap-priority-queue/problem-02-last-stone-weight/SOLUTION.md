# Last Stone Weight — Solution

## Brute Force

Simulate directly on a list. Each turn, sort the list (or scan it twice) to find the two
largest weights, remove them, and if their difference is non-zero append it back. Repeat
until 0 or 1 stones remain.

- **Time:** `O(n^2 log n)` if you re-sort every turn (up to `n` turns × `O(n log n)`
  sort), or `O(n^2)` with a two-pass max scan per turn.
- **Space:** `O(n)` (or `O(1)` extra beyond the list).

Correct, but each turn we pay linear (or worse) work just to find the two maxima, even
though only two elements changed.

## Optimal Approach (Heap / Priority Queue)

**Idea:** Every turn we need the *two heaviest* stones. That is exactly the "repeatedly
extract the max" pattern, so use a **max-heap**. Python's `heapq` is a min-heap, so store
**negated weights** and negate back when reading.

Procedure:

1. Build a max-heap of all stone weights: `heap = [-w for w in stones]`, then
   `heapify`.
2. While at least 2 stones remain, pop the two largest `y` and `x` (as negatives,
   `-heappop` gives the real values with `y >= x`). If `y != x`, push `-(y - x)` back.
3. Return `-heap[0]` if a stone remains, else `0`.

```python
import heapq

def lastStoneWeight(stones):
    heap = [-w for w in stones]
    heapq.heapify(heap)                 # O(n)
    while len(heap) > 1:
        y = -heapq.heappop(heap)        # largest
        x = -heapq.heappop(heap)        # second largest, x <= y
        if y != x:
            heapq.heappush(heap, -(y - x))
        # if y == x, both destroyed: push nothing
    return -heap[0] if heap else 0
```

**Why it is correct:** The game's rule is defined purely in terms of the two current
maxima, and a max-heap always exposes them at the root in `O(log n)` per extraction.
Pushing the residual `y - x` re-inserts the smashed stone's remaining mass while keeping
the heap invariant, so the next turn again sees the true two heaviest. Each turn removes
at least one stone, so the loop terminates after at most `n - 1` turns with 0 or 1 stone
left.

- **Time:** `O(n log n)` — up to `n - 1` turns, each doing a constant number of
  `O(log n)` heap operations; the initial `heapify` is `O(n)`.
- **Space:** `O(n)` for the heap.

## Key Insights & Edge Cases

- **Negate for a max-heap:** `heapq` only gives a min-heap, so store `-weight`. Forgetting
  to negate on the way out is the classic bug here.
- **Equal top two** (`y == x`): both stones vanish and nothing is pushed back — this is
  how the count can drop by two in one turn.
- **Single stone** (`[1]`): the loop never runs, return that stone's weight.
- **Everything cancels** (`[3, 3]`): heap empties, return `0`.
- Constraints are tiny (`n <= 30`), so even the brute force passes — but the heap is the
  clean, idiomatic answer and generalizes to large inputs.
