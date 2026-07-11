# Solution — Daily Temperatures

## Brute Force

For each day `i`, scan forward until you find a day `j > i` with
`temperatures[j] > temperatures[i]`, and record `j - i`.

```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break
    return answer
```

- **Time:** O(n^2) — a decreasing array like `[100, 99, 98, ...]` forces every inner
  scan to run to the end.
- **Space:** O(1) beyond the output.

## Optimal Approach (Amortized Analysis with a Monotonic Stack)

Maintain a **stack of day indices whose warmer day has not yet been found**. The
temperatures at these indices are in **strictly decreasing** order from bottom to top
(a monotonic decreasing stack). Walk left to right; for each new day `i`:

```
for i in range(n):
    while stack is non-empty AND temperatures[i] > temperatures[stack.top()]:
        prev = stack.pop()
        answer[prev] = i - prev        # day i is prev's next warmer day
    stack.push(i)
# any indices still on the stack keep answer 0 (no warmer day exists)
```

Reference implementation:

```python
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack: list[int] = []          # indices, decreasing temperatures
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer
```

### Why it is correct

The stack holds exactly the days still "waiting." Because it stays strictly decreasing,
when a warmer day `i` arrives it resolves a *contiguous run* of the most recent waiting
days that are cooler than `temperatures[i]` — and `i` is genuinely the *first* warmer
day for each of them (they were waiting, and no day between them and `i` was warm enough
to pop them earlier). Days never popped had no warmer future day, so their answer stays 0.

### Why it is O(n) (the amortized argument)

The inner `while` loop can, on a single iteration of the outer loop, pop many indices —
so a naive glance suggests O(n^2). But use the **aggregate method**: **each index is
pushed onto the stack exactly once and popped at most once** over the entire run. The
total number of `while`-loop iterations across *all* `i` is therefore bounded by the
total number of pushes, which is `n`. Outer loop does O(n) pushes; inner loop does O(n)
pops in total ⇒ **O(n) total**, i.e. **O(1) amortized per day**.

- **Time:** O(n) total (O(1) amortized per element).
- **Space:** O(n) for the stack in the worst case (strictly decreasing input).

## Key Insights & Edge Cases

- Store **indices, not temperatures**, so you can compute the distance `i - prev`.
- Use a **strict** comparison (`>`). Equal temperatures do not count as "warmer," so
  equal elements should remain on the stack.
- Elements left on the stack at the end correctly keep answer `0`; initialize the
  output to zeros so no special end-handling is needed.
- Single-element input `[x]` → `[0]`.
- The "each element pushed/popped once" bound is the signature of amortized analysis —
  the same reasoning powers Next-Greater-Element, stock-span, and histogram problems.
