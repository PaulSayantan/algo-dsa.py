# Solution — Weighted Reservoir Sampling

## Brute Force

Buffer the whole stream, then draw `k` items one at a time using cumulative weights:
compute the total weight, pick a uniform value in `[0, total)`, binary-search the prefix
sums to find the chosen item, remove it, and repeat `k` times.

```python
def weighted_reservoir_sample(stream, k):
    items = list(stream)                 # buffers everything
    chosen = []
    for _ in range(min(k, len(items))):
        total = sum(w for _, w in items)
        r = random.uniform(0, total)
        acc = 0.0
        for idx, (it, w) in enumerate(items):
            acc += w
            if acc >= r:
                chosen.append(it)
                items.pop(idx)
                break
    return chosen
```

- **Time:** `O(n·k)` (re-scanning to renormalize after each removal).
- **Space:** `O(n)` — the entire stream is held in memory.

This is a correct definition of weighted sampling without replacement, but it needs the
full stream and multiple passes, so it fails the streaming / `O(k)`-memory requirement.

## Optimal Approach (A-Res: Efraimidis–Spirakis)

Assign each item a random **key**

```
key_i = u_i ** (1 / weight_i),   with u_i ~ Uniform(0, 1)
```

and keep the `k` items with the **largest** keys. Maintain those with a size-`k`
**min-heap** ordered by key: the heap root is the smallest surviving key, so a new item is
kept only if its key exceeds the root.

### Why it is correct

For a single item, `key = u^(1/w)`. Its CDF is
`P(key <= x) = P(u <= x^w) = x^w` for `x in (0,1)`, so it has density `w·x^(w-1)`.

The probability that item `i` has the **maximum** key among all items equals

```
P(key_i = max_j key_j) = weight_i / (sum_j weight_j)
```

(this is the classical Efraimidis–Spirakis result — integrate item `i`'s density against
the probability that all others fall below `x`). Hence for `k = 1` the survivor is chosen
with probability proportional to its weight. Extending the argument to the top-`k` keys
yields exactly the "draw one at a time proportional to remaining weight, without
replacement" distribution described in the problem.

Crucially, keys are assigned independently per item as it streams by, so the algorithm is
**single-pass** and never needs `n`.

### Step-by-step

1. Keep a min-heap `heap` of `(key, tiebreak, item)` triples, capacity `k`.
2. For each `(item, weight)` in the stream, compute `key = random() ** (1/weight)`.
3. If `len(heap) < k`, push the triple.
4. Else if `key > heap[0][0]` (bigger than the smallest kept key), pop the root and push
   the new triple.
5. After the stream ends, return the items remaining in the heap.

### Reference implementation

```python
import heapq
import itertools
import random
from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def weighted_reservoir_sample(stream: Iterable[Tuple[T, float]], k: int) -> List[T]:
    heap: List[Tuple[float, int, T]] = []      # min-heap by key
    counter = itertools.count()                # unique tiebreaker; avoids comparing items

    for item, weight in stream:
        key = random.random() ** (1.0 / weight)   # u ** (1/w)
        if len(heap) < k:
            heapq.heappush(heap, (key, next(counter), item))
        elif key > heap[0][0]:
            heapq.heapreplace(heap, (key, next(counter), item))

    return [item for _key, _c, item in heap]
```

- **Time:** `O(n log k)` — one `O(log k)` heap operation per item.
- **Space:** `O(k)` — only the heap, independent of `n`.

## Key Insights & Edge Cases

- **The magic key is `u^(1/w)`.** Larger weight pushes the key closer to 1, so heavy items
  are more likely to hold a top-`k` key. Do **not** confuse this with unweighted
  Algorithm R, which would ignore the weights.
- **Min-heap keeps the top k.** The root is the weakest survivor; comparing a newcomer's
  key against the root is the whole admission test.
- **Add a tiebreaker.** Push `(key, unique_counter, item)` so Python never has to compare
  two `item` objects when keys tie — otherwise unorderable items (e.g. dicts) crash.
- **Numerical care with tiny weights.** For very large weight ratios, `random()**(1/w)`
  can underflow toward 0 or lose precision. A common fix is to compare in log space using
  keys `ln(u)/w` (equivalently `key' = -ln(u)/w`, keep the **smallest**), which is more
  stable.
- **`n <= k`:** every item is pushed and none is ever evicted, so the whole stream is
  returned — matching the required behavior.
- **Positive weights only.** A zero weight would make `1/w` undefined; a negative weight
  is meaningless here. Selection is proportional, so relative (unnormalized) weights are
  fine — they need not sum to 1.
