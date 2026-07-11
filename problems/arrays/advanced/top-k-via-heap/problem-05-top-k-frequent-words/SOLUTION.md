# Solution — Top K Frequent Words

## Brute Force

Count the words, then sort every unique word by the composite key "frequency descending,
then word ascending," and take the first `k`.

```python
from collections import Counter

def topKFrequent(words, k):
    counts = Counter(words)
    # sort by (-count, word): count high-to-low, word alphabetically for ties
    ordered = sorted(counts, key=lambda w: (-counts[w], w))
    return ordered[:k]
```

- **Time:** `O(n + u log u)` where `u` is the number of unique words (`O(n log n)` worst
  case). String comparisons cost up to `O(L)` for word length `L`, but `L <= 10` here.
- **Space:** `O(u)`.

Clean and often the pragmatic choice, but it sorts all `u` unique words when only the top
`k` are needed.

## Optimal Approach (Top-K via Heap)

The subtlety is the **mixed ordering**: higher frequency is better, but on a frequency tie
the *alphabetically smaller* word is better. A size-`k` heap must evict the current *worst*
element, so its comparison must define "worst" as: **lower count**, or **equal count with a
lexicographically larger word**.

Wrap each entry in a small class with a custom `__lt__` so the heap's root is always the
worst survivor:

```python
import heapq
from collections import Counter

class Word:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count   # fewer occurrences => "smaller"/worse
        return self.word > other.word         # later alphabetically => "smaller"/worse

def topKFrequent(words, k):
    counts = Counter(words)
    heap = []
    for word, count in counts.items():
        heapq.heappush(heap, Word(count, word))
        if len(heap) > k:
            heapq.heappop(heap)               # remove the current worst
    # Heap pops worst-first; reverse to get best-first output order.
    result = [heapq.heappop(heap).word for _ in range(len(heap))]
    result.reverse()
    return result
```

**Why it is correct:** the custom `__lt__` makes the min-heap treat the least desirable
entry (lowest count, or same count but later alphabetically) as the minimum, so it sits at
the root and is the first evicted when the heap exceeds `k`. After processing all unique
words, the heap holds exactly the top `k`. Popping yields them worst-to-best, so reversing
produces the required best-to-worst output order.

- **Time:** `O(n + u log k)` — counting is `O(n)`; each of `u` unique words costs `O(log k)`
  in the heap. Emitting the answer is `O(k log k)`.
- **Space:** `O(u)` counter plus `O(k)` heap.

### Simpler alternative: heapify all, pop k

Because Python tuples compare lexicographically, `(-count, word)` already encodes the exact
desired order (highest count first; alphabetical on ties). Heapify all entries and pop `k`:

```python
import heapq
from collections import Counter

def topKFrequent(words, k):
    counts = Counter(words)
    heap = [(-count, word) for word, count in counts.items()]
    heapq.heapify(heap)                       # O(u)
    return [heapq.heappop(heap)[1] for _ in range(k)]
```

- **Time:** `O(u + k log u)` — heapify `O(u)`, then `k` pops at `O(log u)` each.
- **Space:** `O(u)`.

This is `O(u + k log u)` versus the size-`k` heap's `O(u log k)`. When `k` is small relative
to `u`, the size-`k` heap uses less memory (`O(k)` vs `O(u)`); when `k` approaches `u`, the
heapify-all method is simpler and its total work is comparable.

## Key Insights & Edge Cases

- **The tie-break inverts inside a size-k min-heap.** In the final answer, ties go to the
  *smaller* word; but the heap must evict the *worst*, so within the heap the *larger* word
  must compare as "smaller." Getting this backwards is the classic bug on this problem.
- **Remember to reverse.** A size-`k` heap pops worst-first, so the raw pop order is the
  reverse of the required output.
- **Tuple trick avoids a custom class.** `(-count, word)` leverages Python's built-in tuple
  ordering when you heapify everything, sidestepping `__lt__` entirely — but it does not
  compose with the "negate for a max-heap" trick if you also cap at size `k`, which is why
  the size-`k` version needs the explicit comparator.
- **k up to number of unique words.** When `k` equals the unique count, all words are
  returned in the correct order — no special case.
- **Stable, deterministic output.** The ordering is total (frequency then spelling), so the
  answer is unique regardless of input order.
