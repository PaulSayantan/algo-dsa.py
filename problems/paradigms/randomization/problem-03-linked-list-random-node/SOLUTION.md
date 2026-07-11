# Linked List Random Node — Solution

## Brute Force

Walk the list once in the constructor and copy every value into an array `vals`. Then
`getRandom` returns `vals[random.randint(0, len(vals) - 1)]`.

- Constructor: **O(n)** time and **O(n)** extra space to store the copy.
- `getRandom`: **O(1)** time, and clearly uniform since every index is equally likely.

This is correct and fast per query, but it uses O(n) extra memory and requires knowing (by
traversal) the full list up front — which the follow-up explicitly rules out for a huge list
of unknown length.

## Optimal Approach (Randomization: reservoir sampling, k = 1)

Reservoir sampling selects a uniform sample of fixed size from a stream of unknown length in
a single pass using O(1) space (for one sample). With reservoir size 1:

Traverse the list. Keep a single running `result`. At the i-th node (using a 1-based
counter `i`), replace `result` with the current node's value with probability `1/i`:

```python
def getRandom(self):
    result = None
    i = 1
    node = self.head
    while node:
        # Replace with probability 1/i. random.random() < 1/i  <=>  randint(1, i) == 1
        if random.randint(1, i) == 1:
            result = node.val
        node = node.next
        i += 1
    return result
```

Store only `self.head` in the constructor — no array, no length.

### Why every node has probability 1/n

Consider node `k` (1-indexed), and a list of total length `n`. Node `k` becomes the answer
iff it is *selected* when we reach it and then *never overwritten* afterward:

- It is selected at step `k` with probability `1/k`.
- At each later step `j` (for `j = k+1, ..., n`) it survives if that step does **not** pick
  the new node, i.e. with probability `1 - 1/j = (j-1)/j`.

Multiplying:

```
P(node k wins) = (1/k) * (k/(k+1)) * ((k+1)/(k+2)) * ... * ((n-1)/n)
              = 1/k * [k/(k+1) * (k+1)/(k+2) * ... * (n-1)/n]
```

The bracketed product telescopes to `k/n`, giving `(1/k) * (k/n) = 1/n`. This holds for
every `k` from 1 to `n`, so the selection is exactly uniform — and the proof never needed to
know `n` in advance.

### Complexity

- Constructor: **O(1)** time and space (just store the head).
- `getRandom`: **O(n)** time (one traversal), **O(1)** extra space.
- Trade-off vs. brute force: reservoir sampling makes each query O(n) but uses no extra
  memory and needs no known length — ideal for a very large / streaming list. If the list is
  static and queried many times, the O(n)-space array with O(1) queries is faster per call.

## Key Insights & Edge Cases

- **1-based counter is critical.** The i-th node must be kept with probability exactly `1/i`.
  Off-by-one here (e.g., using a 0-based `i` and `1/(i+1)` vs `1/i`) is the classic bug — the
  first node would get the wrong probability.
- **Always accept the first node.** At `i = 1`, `1/1 = 1`, so the first node initializes the
  reservoir with certainty; the `result is None` case is handled automatically.
- **Single node:** the loop runs once, keeps it with probability `1/1 = 1`, returns it every
  time — correct.
- **Independence across calls:** each `getRandom` runs its own fresh traversal with new coin
  flips, so successive results are independent.
- **Generalization:** for a reservoir of size `k > 1`, fill the reservoir with the first `k`
  items, then for the i-th item (`i > k`) keep it with probability `k/i`, replacing a
  uniformly random one of the `k` slots. The `k = 1` case above is the special instance.
