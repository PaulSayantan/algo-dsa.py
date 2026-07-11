# Solution — Implement Queue using Stacks

## Brute Force

Keep a single stack `s` that always stores the elements in **queue order** (front on
top). `push` is the hard part: to insert a new element at the *bottom* you must pop
everything off into a temporary stack, push the new element, then push everything
back.

- `push(x)`: O(n) — move all n elements out and back.
- `pop` / `peek`: O(1) — front is on top.

This works but every push is O(n), so a sequence of n pushes costs O(n^2). It also
does not exploit the amortized insight at all.

## Optimal Approach (Amortized Analysis)

Use **two stacks**:

- `in_stack` — new elements are pushed here. Its top is the *most recently* enqueued
  element (the back of the queue).
- `out_stack` — when we need the front, we pour `in_stack` into `out_stack`. Reversing
  the order means the top of `out_stack` is the *oldest* element (the front).

### Operations

```
push(x):
    in_stack.push(x)              # O(1)

_transfer():                      # only when out_stack is empty
    while in_stack not empty:
        out_stack.push(in_stack.pop())

peek():
    if out_stack empty: _transfer()
    return out_stack.top()

pop():
    if out_stack empty: _transfer()
    return out_stack.pop()

empty():
    return in_stack empty AND out_stack empty
```

Reference implementation:

```python
class MyQueue:
    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
```

### Why it is correct

`out_stack` is a reversed copy of the order elements entered `in_stack`, so its top is
always the earliest-inserted element still in the queue — exactly FIFO order. We only
refill `out_stack` when it is empty, so we never interleave a stale order with fresh
elements: all currently-in-`out_stack` elements were pushed before any currently-in-
`in_stack` element.

### Why it is O(1) amortized (the whole point)

A single `pop`/`peek` that triggers a transfer costs O(k) where k is the size of
`in_stack`. That looks like O(n) worst case. But use the **accounting method**: charge
each element **3 credits** when it is pushed — 1 for the `in_stack.push`, 1 saved to
pay for its future move onto `out_stack`, and 1 saved to pay for its future
`out_stack.pop`. Every element is moved from `in_stack` to `out_stack` **at most once**
and popped from `out_stack` **at most once** in its lifetime. So across any sequence of
n operations the total transfer work is bounded by the number of pushes ≤ n. Total work
O(n) ⇒ **O(1) amortized** per operation.

Equivalently, the **potential method**: let Φ = number of elements currently in
`in_stack`. A `push` raises Φ by 1 (amortized cost 2). A `pop` that transfers k elements
has actual cost ~k but drops Φ by k (ΔΦ = −k), so amortized cost is O(1).

- **Time:** O(1) amortized per operation; O(n) total for n operations. Worst-case
  single operation O(n).
- **Space:** O(n) across the two stacks.

## Key Insights & Edge Cases

- **Lazy transfer is essential.** Transferring on *every* pop (or eagerly rebalancing)
  breaks the amortized bound because an element could be moved back and forth
  repeatedly. Transfer only when `out_stack` is empty.
- **Do not transfer if `out_stack` is non-empty** — doing so would put newer elements
  on top of older ones and violate FIFO.
- `empty()` must check **both** stacks; the front can live in either one.
- Because constraints guarantee `pop`/`peek` are only called on a non-empty queue, no
  explicit underflow handling is required, but a robust implementation could raise on
  an empty queue.
- The two-stack trick generalizes to the classic "queue from stacks" and even to a
  persistent/functional queue (front list + reversed back list).
