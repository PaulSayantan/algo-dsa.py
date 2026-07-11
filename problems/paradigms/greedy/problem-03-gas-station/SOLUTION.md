# Gas Station — Solution

## Brute Force

Try every station as a starting point. From each candidate `start`, simulate driving
the full circle, tracking the tank; if it never goes negative, return `start`.

- **Time:** `O(n^2)` — `n` candidate starts, each simulated over up to `n` stations.
- **Space:** `O(1)`.

Correct but quadratic; the wasted work is re-simulating stretches we've already
proven unusable.

## Optimal Approach (Greedy)

**Two facts drive the greedy solution:**

1. **Feasibility check.** If `sum(gas) < sum(cost)`, the loop is impossible from any
   start — return `-1`. If `sum(gas) >= sum(cost)`, a valid start is *guaranteed* to
   exist (and is unique per the problem).

2. **Locating the start.** Sweep once, keeping a running `tank` from the current
   candidate start. The moment `tank` drops below zero at station `i`, *no* station in
   `[start, i]` can be a valid start: each such station only ever contributes an even
   smaller running balance at `i`. So skip the entire stretch and set the next
   candidate start to `i + 1`, resetting `tank` to 0.

```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    total = 0        # running tank from the current candidate start
    start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start = i + 1   # every station in [start, i] fails; jump past
            total = 0
    return start
```

**Why it is correct:** Let `diff[i] = gas[i] - cost[i]`. Suppose the run from `start`
first goes negative at `i`. For any `j` in `(start, i]`, the partial sum from `start`
to `j-1` was non-negative (that's why we hadn't reset yet), so starting at `j` instead
gives a running sum from `j` to `i` that is *even more negative* — `j` cannot survive
to `i` either. Hence the earliest possible valid start is `i + 1`. Because a valid
start is guaranteed to exist when the totals allow it, whatever `start` survives to the
end of the sweep is that unique answer.

- **Time:** `O(n)` — one pass for the totals check, one pass to find the start (or a
  single combined pass).
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **The global sum is the gatekeeper:** it alone decides feasibility. The greedy scan
  then only *locates* the start; it does not need to re-verify the wrap-around.
- **Reset, don't restart:** the trick is that a failed prefix can be discarded wholesale
  rather than re-simulated — this is what turns `O(n^2)` into `O(n)`.
- **All zeros / equal gas and cost** (`gas == cost`): every `diff` is 0, `tank` never
  goes negative, so `start` stays 0 (a valid answer).
- **Single station** (`n = 1`): valid iff `gas[0] >= cost[0]`, handled by the sum check.
- Watch the ordering: do the total-sum feasibility check, otherwise the returned
  `start` could be an index that can't actually complete the loop.
