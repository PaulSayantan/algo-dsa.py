# Solution — Online Stock Span

## Brute Force

Store every price in a list. On each `next(price)`, walk backward from the current day
counting consecutive prices ≤ `price` until you hit a larger one.

```python
class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1
        return span
```

- **Time:** O(n) per call, O(n^2) for n calls — a non-decreasing stream like
  `[1, 2, 3, ...]` makes every call scan all the way back.
- **Space:** O(n) to store the prices.

## Optimal Approach (Amortized Analysis with a Monotonic Stack)

Keep a **stack of `(price, span)` pairs** in strictly decreasing order of price from
bottom to top. Each pair summarizes a block of already-processed days: `span` is how
many consecutive days that block covers. When a new price arrives, repeatedly pop every
block whose price is `<= price`, **absorbing its span into the running total**, then push
the new merged block.

```
next(price):
    span = 1
    while stack not empty AND stack.top().price <= price:
        span += stack.pop().span      # absorb the whole block at once
    stack.push((price, span))
    return span
```

Reference implementation:

```python
class StockSpanner:
    def __init__(self) -> None:
        self.stack: list[tuple[int, int]] = []   # (price, span), decreasing prices

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
```

### Why it is correct

Every popped block has price ≤ today's price, so all of its days extend today's
backward run — and because the stack is decreasing, those blocks are exactly the
contiguous most-recent days that qualify. The first block we *cannot* pop has price
> today's, which correctly terminates the run. Merging the popped spans into one pushed
block `(price, span)` preserves the invariant and lets a future day absorb this whole
run in a single pop instead of re-walking its members.

### Why it is O(1) amortized (the amortized argument)

A single `next` may pop many blocks — worst case O(n). But use the **accounting
method**: charge each `next` call **2 credits** — 1 to push its own block, 1 saved to
pay for the *future* pop of that block. **Every block is pushed exactly once and popped
at most once** over the spanner's entire lifetime. So across n calls the total number of
pops is ≤ n, and total work is O(n) ⇒ **O(1) amortized per `next`**.

Equivalently with the **potential method**: let Φ = current stack size. A call that pops
k blocks and pushes 1 has actual cost ~k+1 and ΔΦ = 1 − k, so amortized cost
= (k+1) + (1−k) = 2 = O(1).

- **Time:** O(1) amortized per `next`; O(n) total. Worst-case single call O(n).
- **Space:** O(n) for the stack.

## Key Insights & Edge Cases

- **Absorb spans, do not re-scan.** Storing `span` in each block is what turns repeated
  scans into single pops — this is the trick that makes the amortization work.
- The comparison is `<=` (prices equal to today still extend the run), matching the
  problem's "less than or equal to."
- The **first** day always returns 1 (empty stack, nothing to pop).
- A strictly non-decreasing stream is the worst case for a single call (it pops the
  entire stack) yet is still O(1) amortized because it can only happen after those
  blocks were cheaply pushed.
- Same monotonic-stack skeleton as Daily Temperatures and Next Greater Element — only
  the accumulated payload (`span`) differs.
