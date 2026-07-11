# Solution — Car Pooling

## Brute Force

For every trip, add its passengers to every kilometer it occupies, then check the
max. Occupancy at kilometer `k` counts trips with `from <= k < to`.

```python
def carPooling(trips, capacity):
    road = [0] * 1001                      # locations 0..1000
    for num, start, end in trips:
        for k in range(start, end):        # end is exclusive: they get off at `end`
            road[k] += num
            if road[k] > capacity:
                return False
    return True
```

- **Time:** `O(T * L)` where `T = len(trips)` and `L` is the road length (up to
  1000). Fine for the given limits, but wasteful and it blows up if the location
  range is large.
- **Space:** `O(L)`.

## Optimal Approach (Difference Array)

Each trip contributes a range increment of `+num` over kilometers `[from, to)`.
Because riders get off *at* `to`, they occupy `from .. to - 1`, so the clean
difference-array boundaries are:

```
diff[from] += num       # riders board at `from`
diff[to]   -= num       # riders leave exactly at `to` (to is excluded)
```

Prefix-summing `diff` gives the occupancy at each kilometer. If that running
occupancy ever exceeds `capacity`, the answer is `false`; otherwise `true`. You
never need to store the full occupancy array — just track the running sum.

```python
def carPooling(trips, capacity):
    diff = [0] * 1002                      # locations 0..1000, +1 sentinel
    for num, start, end in trips:
        diff[start] += num
        diff[end]   -= num
    running = 0
    for delta in diff:
        running += delta
        if running > capacity:
            return False
    return True
```

- **Time:** `O(T + L)`.
- **Space:** `O(L)` — bounded because locations are capped at 1000. (For an
  unbounded coordinate range, sort the board/leave events and sweep instead —
  same +/- idea, `O(T log T)`.)

**Why it is correct:** the running prefix sum at kilometer `k` equals the number
of passengers currently aboard, since it accumulates every `+num` from a trip
that has boarded (`from <= k`) and subtracts every trip that has already
finished (`to <= k`). Checking this running value against `capacity` at every
kilometer verifies the constraint everywhere it matters — occupancy only changes
at event points, and boundaries are captured exactly.

## Key Insights & Edge Cases

- **`to` is exclusive.** Subtracting at `diff[to]` (not `diff[to] - 1`) models
  passengers leaving *before* the car occupies kilometer `to`. This is what makes
  Example 1 peak at km 3–5 rather than through km 7. Getting this boundary wrong
  is the classic bug.
- **Check while sweeping.** You can bail out the instant the running sum exceeds
  capacity; no need to finish building the array.
- **Bounded coordinates.** The problem caps locations at 1000, so a fixed-size
  array is simplest. Larger/sparse coordinates call for coordinate compression or
  an event-sorting sweep line.
- **Simultaneous board and alight.** If one trip's `to` equals another's `from`
  at the same kilometer, the exclusive `to` correctly frees the seat before the
  new passengers count, because the `-` and `+` land on the same index and net
  out during the prefix sum.
