# Sum of Subarray Minimums — Solution

## Brute Force

Enumerate every subarray `(i, j)` and track its running minimum, adding each minimum to the
total.

- Number of subarrays: `O(n^2)`; maintaining the min as `j` grows is `O(1)` per step.
- **Time:** `O(n^2)`.
- **Space:** `O(1)` beyond the input.

With `n` up to `3 * 10^4`, `O(n^2)` (~9 * 10^8) is borderline-to-too-slow and wasteful.

## Optimal Approach (Monotonic Stack / Queue)

**Contribution counting.** Rather than summing over subarrays, sum over *elements*: each
`arr[i]` contributes `arr[i]` once for every subarray in which it is the minimum. If we know
how many such subarrays exist, we can add the contribution in one shot.

For index `i`, let:

- `left[i]` = number of consecutive elements ending at `i` (including `i`) that are all
  **strictly greater** than `arr[i]` on the left — i.e. distance to the **previous strictly
  smaller** element.
- `right[i]` = number of consecutive elements starting at `i` (including `i`) that are all
  **greater than or equal to** `arr[i]` on the right — i.e. distance to the **next smaller**
  element.

Then `arr[i]` is the minimum of exactly `left[i] * right[i]` subarrays (choose any start in
the left span and any end in the right span). Total answer:

```
sum over i of  arr[i] * left[i] * right[i]   (mod 1e9+7)
```

### Handling duplicates (the asymmetric tie-break)

To avoid double-counting subarrays whose minimum is achieved by more than one equal element,
use a **strict** comparison on one side and a **non-strict** comparison on the other. Here we
break ties to the left: previous element must be **strictly smaller** to stop the left span,
while the next span extends over elements **greater or equal**. This assigns each subarray's
minimum to a unique index (the leftmost occurrence of the minimum value).

Both `left` and `right` are computed with a **monotonic (increasing) stack**.

### Reference implementation

```python
def sumSubarrayMins(self, arr):
    MOD = 10**9 + 7
    n = len(arr)
    prev_smaller = [-1] * n          # index of previous strictly smaller element
    next_smaller = [n] * n           # index of next smaller-or-equal element

    stack = []                       # increasing stack of indices
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:   # strict: pop >  arr[i]
            next_smaller[stack.pop()] = i
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)

    total = 0
    for i in range(n):
        left = i - prev_smaller[i]
        right = next_smaller[i] - i
        total = (total + arr[i] * left * right) % MOD
    return total
```

Here the single left-to-right pass fills `prev_smaller[i]` (top of stack when `i` is pushed)
and, via the pop step, `next_smaller[j]` for each popped `j`. The strict `>` pop combined
with the "top of stack" read gives the strict-left / non-strict-right tie-break.

### Complexity

- **Time:** `O(n)`. Every index is pushed and popped at most once.
- **Space:** `O(n)` for the stack and the boundary arrays.

## Key Insights & Edge Cases

- **Count contributions, not subarrays:** the `left * right` product is the number of
  subarrays whose minimum is `arr[i]`.
- **Break ties on exactly one side:** using `>` on the pop (strict) plus reading the surviving
  stack top (non-strict left boundary) prevents equal minimums from being counted twice. If
  you used `>=` on both sides you would over- or under-count.
- **Take the modulo as you go:** products of `arr[i]` (up to 3*10^4) with spans (up to
  3*10^4 each) can reach ~2.7*10^13, which fits in Python ints, but the running total can
  overflow fixed-width integers in other languages — reduce mod `1e9+7` each step.
- **Boundaries:** `prev_smaller = -1` and `next_smaller = n` correctly represent "no smaller
  element on that side," making the span reach the array edge.
- **All-equal array** (e.g. `[2,2,2]`): the asymmetric comparison still assigns each subarray
  to a unique minimizing index, so the count is exact.
