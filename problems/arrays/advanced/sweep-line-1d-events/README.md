# Sweep Line (1D events)

**Sweep line** turns a set of *intervals* on a number line into a stream of
**events** — a `+` when an interval opens and a `-` when it closes — and then
processes those events in sorted order while dragging an imaginary vertical line
(the *frontier*) from left to right. At every event the line crosses, you update
a small piece of running state (an integer counter, a running sum, a heap of
active heights, …). Because the events are sorted once and each is touched once,
the whole family of "interval overlap / union / count-or-sum along a line"
problems collapses into a single `O(n log n)` sort followed by an `O(n)` linear
pass.

The mental model:

```
intervals ──▶ events ──▶ sort by coordinate ──▶ scan left→right, keeping state
[l, r)          (l,+w)                            counter / sum / heap / union
                (r,-w)
```

## When to reach for it

Reach for a 1D sweep line when the input is a **collection of intervals or
ranges on one axis** and the question is about how they **interact along that
axis**:

- **Overlap count** — "maximum number of intervals covering any point"
  (meeting rooms, max concurrent events). Keep a running `+1 / -1` counter and
  track its peak.
- **Union / coverage** — "merge overlapping intervals", "total length covered".
  Open a merged segment when the counter leaves `0`, close it when the counter
  returns to `0`.
- **Weighted sum ≤ x** — "does the load ever exceed capacity?", "value at each
  point is the sum of active weights" (car pooling, describe-the-painting).
  Carry a running **sum** of active weights instead of a count.
- **Frontier extremum** — "outline / skyline", where the answer at a point is
  the **max (or min)** of all active values. Keep a multiset / heap of active
  heights and emit a key point whenever the extremum changes.

Typical signals: input given as `[start, end]` (or `[start, end, weight]`)
pairs; you may read everything before answering (offline); the answer is a
function of *how many* / *how much* / *what extremum* is active at each point.

### Two ordering rules you must get right

Ties at the same coordinate are where sweeps break. Decide, per problem, whether
a closing event or an opening event goes first:

- **Half-open `[l, r)` semantics** (meeting rooms, car pooling): a slot that
  frees at `t` can be reused by something starting at `t`, so process **ends
  before starts** at equal coordinates.
- **Touching should merge** (`[1,4]` and `[4,5]` become `[1,5]` in Merge
  Intervals): process **starts before ends** at equal coordinates so the counter
  never dips to `0` at the shared endpoint.

## Complexity

| Aspect                                | Cost            |
|---------------------------------------|-----------------|
| Building events                       | `O(n)`          |
| Sorting events                        | `O(n log n)`    |
| Linear scan (counter / sum)           | `O(n)`          |
| Scan with a heap/multiset (skyline)   | `O(n log n)`    |
| Extra space (events + state)          | `O(n)`          |

The sort dominates: **`O(n log n)` time, `O(n)` space** for the whole family.
Two special notes: if coordinates are small integers you can replace the sort
with a **difference array** and get `O(range)` time; and when the answer needs
the running extremum (not just a count) you pay an extra `log n` per event for
the heap.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Meeting Rooms II](problem-01-meeting-rooms-ii/PROBLEM.md) | Peak of a `+1/-1` overlap counter | Medium |
| 2 | [Merge Intervals](problem-02-merge-intervals/PROBLEM.md) | Union: emit a segment each time the open-count returns to 0 | Medium |
| 3 | [Car Pooling](problem-03-car-pooling/PROBLEM.md) | Weighted events; running sum must stay ≤ capacity | Medium |
| 4 | [Describe the Painting](problem-04-describe-the-painting/PROBLEM.md) | Weighted sweep that *emits* output segments with per-segment sums | Medium |
| 5 | [The Skyline Problem](problem-05-the-skyline-problem/PROBLEM.md) | Frontier extremum via a max-heap of active heights | Hard |
