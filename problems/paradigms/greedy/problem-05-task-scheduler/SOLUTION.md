# Task Scheduler — Solution

## Brute Force

Simulate time tick by tick, at each step choosing among the tasks currently off
cooldown. Trying every choice (which runnable task to pick, or whether to idle) and
searching for the shortest schedule is a combinatorial search.

- **Time:** exponential in the number of tasks in the naive branching search.
- **Space:** `O(tasks)` for the recursion / schedule state.

Even a "reasonable" simulation that always runs *a* task tends to `O(total_time)` and
needs a good tie-break to be correct — which motivates the greedy insight below.

## Optimal Approach (Greedy)

**Idea:** The task with the highest frequency `maxCount` is the bottleneck. Lay its
copies out first, each separated by exactly `n` cooldown slots. This creates
`maxCount - 1` full "frames" of length `n + 1`, followed by one final copy:

```
[ A _ _ ] [ A _ _ ] ... [ A ]      <- (maxCount - 1) frames of size (n+1), then last A
```

Every other task is dropped into the `_` gaps. As long as there is room, no idle time
is wasted. The only time we must idle is when the gaps aren't fully filled — which
happens exactly when the most frequent task is scarce relative to the cooldown.

This yields the closed form:

```python
from collections import Counter

def leastInterval(tasks, n):
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for c in counts.values() if c == max_count)
    # frame skeleton (may be smaller than len(tasks) when there are many task types)
    frame = (max_count - 1) * (n + 1) + num_max
    return max(len(tasks), frame)
```

- `(max_count - 1) * (n + 1)` — the `maxCount - 1` frames, each of width `n + 1`.
- `+ num_max` — the final block: every task tied for the max contributes one trailing run.
- `max(len(tasks), frame)` — if there are enough *distinct* tasks to fill all the gaps,
  no idling is needed and the answer is simply `len(tasks)`; otherwise idle slots push
  it up to the frame size.

**Why it is correct:** The most frequent task cannot be scheduled in fewer than
`(max_count - 1) * (n + 1) + 1` units — each of its runs forces `n` intervening units.
Tasks tied at `max_count` extend the tail by `num_max`. Filling gaps with other tasks
never *lengthens* this skeleton (they occupy slots that would otherwise idle), and if
they overflow the gaps the total is just the raw count `len(tasks)`. So the true
minimum is the larger of the two. This is a greedy argument: always place the scarcest
resource (the busiest task) first, and everything else fits around it.

- **Time:** `O(N)` where `N = len(tasks)` — one pass to count (the alphabet is fixed at 26).
- **Space:** `O(1)` — at most 26 counts.

## Key Insights & Edge Cases

- **The bottleneck is the max-frequency task**, not the total. That single observation
  turns simulation into arithmetic.
- **`n = 0`:** frame = `(max_count - 1) * 1 + num_max`, which never exceeds `len(tasks)`,
  so the answer is `len(tasks)` — the CPU never idles. (Example 3 → 6.)
- **Many distinct tasks:** when there are more task types than `n`, the gaps fill up and
  the answer is exactly `len(tasks)` (Example 2 → 6). The `max(len(tasks), ...)` term
  captures this.
- **Ties at the top:** multiple tasks sharing `max_count` add to the final block via
  `num_max`; forgetting this undercounts the tail.
- If you prefer, a **max-heap + cooldown queue** simulation (run the currently most
  frequent available task each tick) is an equivalent greedy that also produces an
  actual schedule, at `O(N log 26)` time.
