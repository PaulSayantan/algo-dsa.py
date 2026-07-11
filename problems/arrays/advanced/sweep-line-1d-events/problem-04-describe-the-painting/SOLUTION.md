# Describe the Painting — Solution

## Brute Force

Paint every unit cell and then group equal-value runs.

- Allocate a `color[x]` array over the coordinate range. For each segment
  `[s, e, c]`, add `c` to `color[x]` for every `x` in `[s, e)`. Then walk the
  array left to right, grouping maximal runs of equal, nonzero value into output
  segments.
- Time: `O(n * L + L)` where `L` is the coordinate range (up to `10^5`). With
  `n = 2*10^4` this is `~2*10^9` in the worst case — too slow — and it fails
  entirely if coordinates are large or non-integer. Space: `O(L)`.

The painting only changes at segment endpoints, so touching every unit cell is
wasteful. Sweep the endpoints instead.

## Optimal Approach — Sweep Line (1D events)

Treat each `[s, e, c]` as a weighted difference on a map keyed by coordinate:

- add `+c` at coordinate `s`,
- add `-c` at coordinate `e`.

Accumulate these into `delta[x]` (summing deltas that land on the same
coordinate). Now sort the distinct coordinates. Sweep them left to right holding
`cur`, the running sum of active colors:

- Between the previous coordinate `prev` and the current coordinate `x`, the
  active color set is fixed, so the mixed color over `[prev, x)` is exactly the
  current `cur`. If `cur > 0`, emit `[prev, x, cur]`.
- Then apply this coordinate's delta: `cur += delta[x]`, and set `prev = x`.

Because a boundary is created at **every** endpoint coordinate, two neighboring
emitted pieces can carry the same numeric sum but remain separate (their
underlying color sets differ) — which is exactly what the problem wants
(Example 3).

### Why it is correct

`cur` just before crossing coordinate `x` equals `Σ c` over all segments with
`s <= prev` and `e > prev`, i.e. the additive mixed color everywhere on
`[prev, x)`. Since colors can only start or stop at endpoint coordinates, the
mixed color is constant on each `[prev, x)` gap, so emitting one piece per
positive gap reconstructs the painting exactly. Ignoring gaps where `cur == 0`
drops the unpainted regions, as required.

### Step-by-step (Example 2: `[[1,7,9],[6,8,15],[8,10,7]]`)

Accumulated deltas by coordinate:

```
1: +9      6: +15     7: -9     8: -15 +7 = -8    10: -7
```

Sweep the sorted coordinates `[1, 6, 7, 8, 10]`:

```
prev=None cur=0
x=1:  gap none;            cur += 9  -> 9    prev=1
x=6:  [1,6) cur=9  -> emit [1,6,9];  cur += 15 -> 24   prev=6
x=7:  [6,7) cur=24 -> emit [6,7,24]; cur += -9 -> 15   prev=7
x=8:  [7,8) cur=15 -> emit [7,8,15]; cur += -8 -> 7    prev=8
x=10: [8,10) cur=7 -> emit [8,10,7]; cur += -7 -> 0    prev=10
```

Output = `[[1,6,9], [6,7,24], [7,8,15], [8,10,7]]`.

### Reference implementation

```python
from collections import defaultdict
from typing import List

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        delta = defaultdict(int)
        for s, e, c in segments:
            delta[s] += c
            delta[e] -= c

        result = []
        prev = None
        cur = 0
        for x in sorted(delta):
            if prev is not None and cur > 0:
                result.append([prev, x, cur])
            cur += delta[x]
            prev = x
        return result
```

- **Time:** `O(n log n)` — sorting the distinct coordinates dominates.
- **Space:** `O(n)` — the delta map and output.

## Key Insights & Edge Cases

- **Emit segments, not a scalar.** The novelty versus problems 1–3 is that the
  sweep produces *output intervals*: one piece per positive gap between adjacent
  event coordinates.
- **Boundaries at every endpoint.** Because a coordinate is created at each
  start/end, adjacent pieces are split whenever the active color *set* changes,
  even if the numeric sum is identical (Example 3: two `12`s stay separate).
  This is why we do **not** merge by equal sum in the core sweep.
- **Combine deltas at the same coordinate** (Example 3, coordinate `4` has both
  `-5-7` from the ending pair and `+1+11` from the starting pair). Using a map
  keyed by coordinate handles this automatically; a plain event list must sum
  ties.
- **Big values:** `color_i` up to `10^9` with up to `2*10^4` overlaps means sums
  can reach `~2*10^13` — use 64-bit integers (Python ints are unbounded, so no
  overflow there, but note it for typed languages).
- **Unpainted gaps** (where `cur` drops to `0` between segments, e.g. Example 2
  has none but a disjoint input would) are simply skipped because we only emit
  when `cur > 0`.
- A cosmetic post-pass may merge neighbors with equal sum *and* no gap between
  them if a problem variant asks for it; the base LeetCode version does not,
  because every retained boundary reflects a real change in the color set.
