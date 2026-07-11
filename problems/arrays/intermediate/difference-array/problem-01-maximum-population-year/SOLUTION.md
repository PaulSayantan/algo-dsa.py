# Solution — Maximum Population Year

## Brute Force

For every person, increment a counter for **each** year they are alive, then
scan the counters for the earliest maximum.

```python
def maximumPopulation(logs):
    count = {}                      # year -> population
    for birth, death in logs:
        for year in range(birth, death):   # note: death is exclusive
            count[year] = count.get(year, 0) + 1
    best_year, best_pop = 10**9, -1
    for year in sorted(count):
        if count[year] > best_pop:
            best_pop, best_year = count[year], year
    return best_year
```

- **Time:** `O(n * Y)` where `n` is the number of people and `Y` is the span of
  years a person can live (up to ~100 here). With wider year ranges this becomes
  a real bottleneck.
- **Space:** `O(Y)`.

## Optimal Approach (Difference Array)

The years form a fixed, small universe: `[1950, 2050]`. Build a difference array
over that universe. A person alive during `[birth, death)` contributes exactly a
range increment of `+1` over years `birth .. death - 1`. With a difference array
that is two O(1) writes:

```
diff[birth] += 1        # population rises when they are born
diff[death] -= 1         # population drops the year they die (death excluded)
```

Because `death` is the first year the person is **not** counted, subtracting at
`death` (not `death - 1`) is exactly correct — the increment covers
`birth .. death - 1`.

After recording every person, take a running prefix sum across years in
ascending order. The prefix sum at year `x` equals the number of people whose
range covers `x`, i.e. the live population. Track the running maximum and, since
we scan years in increasing order, the first year that hits a new maximum is the
earliest — exactly what we return.

```python
def maximumPopulation(logs):
    OFFSET = 1950
    diff = [0] * (2051 - OFFSET + 1)   # index 0..101 covers years 1950..2051
    for birth, death in logs:
        diff[birth - OFFSET] += 1
        diff[death - OFFSET] -= 1
    best_year, best_pop, running = OFFSET, 0, 0
    for i in range(len(diff)):
        running += diff[i]
        if running > best_pop:
            best_pop = running
            best_year = i + OFFSET
    return best_year
```

- **Time:** `O(n + Y)` — O(n) to record deltas, O(Y) to sweep.
- **Space:** `O(Y)` for the difference array.

**Why it is correct:** the difference array turns each "alive interval" into a
constant-time +1/-1 pair, and the prefix sum inverts the difference operation to
recover the true population per year. Scanning left to right guarantees the
*earliest* peak year wins ties.

## Key Insights & Edge Cases

- **Death year is exclusive.** The clean `+1 at birth`, `-1 at death` mapping
  works precisely *because* the person is not counted in the death year. If the
  problem counted the death year, you would instead do `-1 at death + 1`.
- **Fixed universe = no coordinate compression needed.** Years are bounded to
  `[1950, 2050]`, so a plain array indexed by `year - 1950` suffices. If the
  range were huge or unbounded, you would coordinate-compress the event points
  first (sort birth/death events) — the same +1/-1 idea, sweep-line style.
- **Off-by-one on array size.** Size the difference array so that writing
  `diff[death - OFFSET]` never goes out of bounds when `death == 2050`. Allocate
  one extra slot.
- **Earliest tie-break** falls out for free from scanning years in increasing
  order and using strict `>` when updating the best population.
