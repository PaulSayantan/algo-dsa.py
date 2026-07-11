# Solution — Sample K Items From a Stream

## Brute Force

Materialize the whole stream into a list, then use a standard sampler
(`random.sample`, or a partial Fisher–Yates shuffle) to pick `k` items.

```python
def reservoir_sample(stream, k):
    items = list(stream)                 # buffers everything
    if len(items) <= k:
        return items
    return random.sample(items, k)
```

- **Time:** `O(n)`.
- **Space:** `O(n)` — the entire stream is held in memory.

Correct and simple, but it violates the core constraints: it needs to know/hold all `n`
items and cannot handle an unbounded stream or a single-pass iterator that you cannot
rewind.

## Optimal Approach (Reservoir Sampling — Algorithm R)

Maintain a `reservoir` of size `k`. Seed it with the first `k` items. For each subsequent
item at 1-indexed position `i > k`, draw `j = random.randint(0, i-1)`; if `j < k`,
replace `reservoir[j]` with the new item, otherwise skip it. When the stream ends, the
reservoir is a uniform sample.

### Why it is correct

**Claim:** after processing `i` items, every one of them is in the reservoir with
probability `k/i`. Proof by induction on `i`.

- **Base case** `i = k`: the first `k` items are all in the reservoir, each with
  probability `k/k = 1`. ✔
- **Inductive step:** assume the claim for `i-1`. When item `i` arrives:
  - It is **added** with probability `k/i` (because `j < k` happens with probability
    `k/i`), matching the target.
  - Consider an older item that was in the reservoir (probability `k/(i-1)` by the
    hypothesis). It **stays** unless item `i` is added *and* happens to evict its slot.
    Item `i` evicts a specific slot with probability `(k/i)·(1/k) = 1/i`, so the item
    survives with probability `1 - 1/i = (i-1)/i`. Its new probability is
    `k/(i-1) · (i-1)/i = k/i`. ✔

By induction, after all `n` items each is present with probability `k/n`, and since every
subset is reached by symmetric choices, all `C(n, k)` subsets are equally likely.

### Step-by-step

1. Pull the first `k` items into `reservoir` (indices `0..k-1`). If the stream ends early,
   return what you have.
2. Keep a running position counter `i` (starts at `k`, 1-indexed just past the seed).
3. For each further item: `i += 1`; draw `j = randint(0, i-1)`; if `j < k`, set
   `reservoir[j] = item`.
4. Return `reservoir`.

### Reference implementation

```python
import random
from typing import Iterable, List, TypeVar

T = TypeVar("T")


def reservoir_sample(stream: Iterable[T], k: int) -> List[T]:
    it = iter(stream)
    reservoir: List[T] = []

    # Phase 1: fill the reservoir with the first k items.
    for item in it:
        reservoir.append(item)
        if len(reservoir) == k:
            break
    else:
        return reservoir            # stream had < k items -> return all

    # Phase 2: replace with decreasing probability.
    i = k                           # number of items seen so far
    for item in it:
        i += 1
        j = random.randint(0, i - 1)   # uniform in [0, i-1]
        if j < k:
            reservoir[j] = item
    return reservoir
```

- **Time:** `O(n)` — constant work per streamed item.
- **Space:** `O(k)` — only the reservoir; independent of `n`.

## Key Insights & Edge Cases

- **The probability schedule matters.** Item `i` enters with probability `k/i`, which
  decreases as the stream grows; this exactly balances the growing number of survivors so
  every item ends at `k/n`.
- **`randint(0, i-1)` covers `[0, i-1]` inclusive** — `i` total slots. Getting this range
  wrong (e.g. `randint(0, i)`) breaks uniformity.
- **Short stream (`n <= k`):** return everything; there is no sampling to do. The `for...
  else` handles this cleanly.
- **Without replacement:** each reservoir slot holds a distinct stream position, so the
  result has no repeated positions (values may repeat if the stream itself had duplicates).
- **Single pass / unknown n:** the algorithm never rewinds and never needs `n`, which is
  what makes it suitable for logs, network feeds, and database cursors.
- **Weighted variants:** if items carry weights and you want probability proportional to
  weight, plain Algorithm R is *not* correct — use A-Res / Efraimidis–Spirakis (see the
  weighted problem in this folder).
