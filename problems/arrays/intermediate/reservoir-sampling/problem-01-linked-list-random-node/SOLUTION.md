# Solution — Linked List Random Node

## Brute Force

Walk the list once to count the nodes (`n`), then draw a random index `r` in
`[0, n-1]` and walk again to return the value at index `r`. Or copy every value into an
array in the constructor and index into it.

```python
class Solution:
    def __init__(self, head):
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self):
        return random.choice(self.vals)
```

- **Time:** `O(n)` to build the array in the constructor; `O(1)` per `getRandom`.
- **Space:** `O(n)` — the whole list is buffered.

This is perfectly fine when the list fits in memory and you know its length, but it
fails the follow-up: it needs `O(n)` space and effectively requires knowing/counting
the length.

## Optimal Approach (Reservoir Sampling, k = 1)

Keep a single candidate. Traverse the list, and at the **i-th** node (1-indexed) replace
the candidate with the current node's value with probability `1/i`. Return the surviving
candidate. No length count, no buffering.

### Why it is correct

Node `j` ends up as the answer iff it is picked at step `j` **and** survives every later
replacement:

```
P(node j returned)
  = (1/j)  ·  P(not replaced at j+1) · ... · P(not replaced at n)
  = (1/j)  ·  (1 - 1/(j+1)) · (1 - 1/(j+2)) · ... · (1 - 1/n)
  = (1/j)  ·  (j/(j+1)) · ((j+1)/(j+2)) · ... · ((n-1)/n)
  = (1/j)  ·  (j/n)                       # telescoping
  = 1/n
```

Every node gets probability `1/n`, so the sample is uniform — independent of `n`.

### Step-by-step

1. Start at `head` with `result = head.val` and counter `i = 1`.
2. Move to the next node, increment `i`.
3. Draw `random.randint(1, i)`; if it equals `1` (probability `1/i`), set
   `result = node.val`.
4. Repeat until the list ends; return `result`.

### Reference implementation

```python
import random
from typing import Optional


class Solution:
    def __init__(self, head: Optional[ListNode]) -> None:
        self.head = head            # O(1) space, no counting

    def getRandom(self) -> int:
        result = self.head.val
        node = self.head.next
        i = 2                       # head was position 1
        while node:
            if random.randint(1, i) == 1:   # replace with prob 1/i
                result = node.val
            node = node.next
            i += 1
        return result
```

- **Time:** `O(n)` per `getRandom` call (one traversal).
- **Space:** `O(1)` — only the head reference and a couple of scalars.

## Key Insights & Edge Cases

- **The 1/i replacement is the whole trick.** Using a fixed probability (e.g. always
  `1/2`) is *not* uniform — later nodes would be over- or under-represented.
- **Single node:** at `i = 1` the candidate is set once and never challenged, so a
  one-node list always returns that node (probability `1`).
- **`randint(1, i) == 1` vs `randint(0, i-1) == 0`** — both give probability exactly
  `1/i`; just be consistent and avoid off-by-one on the range.
- **Trade-off:** this makes each `getRandom` `O(n)` time but `O(1)` space. If you had
  many queries and abundant memory, precomputing the array (`O(n)` space, `O(1)` query)
  is faster per call. Reservoir sampling wins precisely when space or unknown length is
  the constraint.
- **Seeding:** for reproducible tests, seed the RNG; correctness of the distribution does
  not depend on the seed.
