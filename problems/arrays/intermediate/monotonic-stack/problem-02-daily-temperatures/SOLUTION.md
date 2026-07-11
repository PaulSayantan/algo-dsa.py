# Daily Temperatures — Solution

## Brute Force

For each day `i`, scan forward until you find a strictly warmer day.

```python
def brute(temps):
    n = len(temps)
    ans = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temps[j] > temps[i]:
                ans[i] = j - i
                break
    return ans
```

- **Time:** `O(n^2)` worst case (e.g. a strictly decreasing array).
- **Space:** `O(1)` beyond the output.

## Optimal Approach (Monotonic Stack)

This is the canonical **"next greater element, but report the distance"** problem.

Keep a stack of **indices** whose temperatures are **decreasing** from bottom to
top. Iterate `i` from left to right:

- While the stack is non-empty and `temps[i] > temps[stack[-1]]`, the current day
  `i` is the first warmer day for the day on top. Pop that index `j` and set
  `answer[j] = i - j`.
- Push `i`.

Indices left on the stack at the end never found a warmer day, so their answer
stays `0`.

```python
def optimal(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # indices, temperatures decreasing bottom -> top
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
```

### Why it is correct

An index sits on the stack only while it is still waiting for a warmer day. The
stack stays decreasing, so when a warmer temperature `t` arrives it resolves a
contiguous run of colder days from the top down — and `i` is genuinely the
*nearest* warmer day for each, because any nearer warmer day would have popped
them earlier. Storing indices lets us report the gap `i - j` directly.

### Step-by-step on `[73, 74, 75, 71, 69, 72, 76, 73]`

| i | t  | stack (idx) before | pops -> answer set        | stack after |
|---|----|--------------------|---------------------------|-------------|
| 0 | 73 | []                 | —                         | [0]         |
| 1 | 74 | [0]                | ans[0]=1-0=1              | [1]         |
| 2 | 75 | [1]                | ans[1]=2-1=1              | [2]         |
| 3 | 71 | [2]                | —                         | [2,3]       |
| 4 | 69 | [2,3]              | —                         | [2,3,4]     |
| 5 | 72 | [2,3,4]            | ans[4]=1, ans[3]=2       | [2,5]       |
| 6 | 76 | [2,5]              | ans[5]=1, ans[2]=4       | [6]         |
| 7 | 73 | [6]                | —                         | [6,7]       |

Leftover indices `6, 7` keep `answer = 0`. Result: `[1, 1, 4, 2, 1, 1, 0, 0]`.

- **Time:** `O(n)` — each index is pushed once and popped at most once.
- **Space:** `O(n)` for the stack (worst case a strictly decreasing input).

## Key Insights & Edge Cases

- Use **strict** comparison (`<` when popping) because equal temperatures are not
  "warmer" — see Example 3 where two equal `60`s and two equal `90`s behave as
  the strict rule requires.
- Store indices, not temperatures, so you can compute the day gap `i - j`.
- A strictly non-increasing array yields all zeros.
- Single element returns `[0]`.
- An alternative `O(n)` right-to-left DP exists that jumps using previously
  computed answers, but the stack version is the cleaner mental model.
