# Daily Temperatures — Solution

## Brute Force

For each day `i`, scan forward `j = i+1, i+2, ...` until `temperatures[j] > temperatures[i]`,
then record `j - i`. If none found, record `0`.

- **Time:** `O(n^2)` in the worst case (e.g. a strictly decreasing array where every scan
  reaches the end).
- **Space:** `O(1)` beyond the output.

With `n` up to `10^5`, `O(n^2)` (~10^10 operations) is too slow.

## Optimal Approach (Monotonic Stack / Queue)

This is the classic "next greater element, but return the distance" problem. Maintain a
**monotonic stack of indices** whose temperatures are **non-increasing** from bottom to top.

Scan `i` from left to right:

1. While the stack is non-empty **and** `temperatures[i] > temperatures[stack[-1]]`, the
   current day is the first warmer day for the day on top. Pop that index `j` and set
   `answer[j] = i - j`.
2. Push `i`.

Indices left on the stack at the end never saw a warmer day; their answers stay `0`
(the default the output array is initialized to).

### Why it is correct

The stack always contains days that are still waiting for a warmer day, ordered so that
their temperatures decrease from bottom to top. When day `i` is warmer than the top, `i` is
necessarily the *closest* warmer day for that popped index, because we process days in order
and any earlier warmer day would have already popped it. Storing indices (not values) lets
us compute the exact distance `i - j`.

### Reference implementation

```python
def dailyTemperatures(self, temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []                       # indices, non-increasing temperatures
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
```

### Complexity

- **Time:** `O(n)`. Each index is pushed once and popped at most once.
- **Space:** `O(n)` for the stack (worst case: a strictly decreasing array).

## Key Insights & Edge Cases

- **Store indices, not temperatures:** the answer is a *distance*, so you need positions.
- **Strictly warmer:** use `>`. With `>=` you would (incorrectly) treat equal temperatures
  as "warmer" and pop them too early.
- **Default 0:** initializing the answer array to `0` handles all days with no warmer future
  automatically — no special post-processing needed.
- **Monotone decreasing input:** worst case for the stack size but still `O(n)` total work.
- **Single day:** stack push once, nothing pops, answer stays `[0]`.
