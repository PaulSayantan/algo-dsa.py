# The Skyline Problem — Solution

## Brute Force

Collect every distinct x-coordinate (all building edges). For each x, scan all
buildings and take the max height of those covering `x`; emit a key point whenever this
max changes from the previous x.

- **Time:** `O(n^2)` — for each of up to `2n` coordinates you scan all `n` buildings.
- **Space:** `O(n)`.

Correct and a good way to *verify* an answer, but quadratic.

## Optimal Approach (Divide and Conquer)

**Idea (mirror merge sort):** the skyline of a set of buildings can be built by
splitting the buildings into two halves, recursively computing each half's skyline, and
then **merging** the two skylines. Merging two contours is analogous to merging two
sorted lists — but instead of picking the smaller element, we advance along both
contours by x and emit the running **max** height.

1. **Divide:** split `buildings` into two halves.
2. **Conquer:** recursively compute the skyline of each half. Base case: a single
   building `[l, r, h]` has skyline `[[l, h], [r, 0]]`.
3. **Combine (merge two skylines):** sweep both skylines left to right with pointers
   `i, j`, maintaining the current height contributed by each side (`h1`, `h2`). At
   each step take the smaller x (or advance both on a tie), update that side's current
   height, and record `[x, max(h1, h2)]` — but only if that max differs from the last
   emitted height (this collapses consecutive equal segments).

```python
def getSkyline(buildings):
    if len(buildings) == 1:
        l, r, h = buildings[0]
        return [[l, h], [r, 0]]
    mid = len(buildings) // 2
    left = getSkyline(buildings[:mid])
    right = getSkyline(buildings[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    h1 = h2 = 0
    result = []

    def push(x, y):
        if not result or result[-1][1] != y:  # dedupe equal-height segments
            result.append([x, y])

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x, h1 = left[i][0], left[i][1]; i += 1
        elif left[i][0] > right[j][0]:
            x, h2 = right[j][0], right[j][1]; j += 1
        else:                                  # same x: advance both
            x, h1, h2 = left[i][0], left[i][1], right[j][1]; i += 1; j += 1
        push(x, max(h1, h2))

    while i < len(left):  push(left[i][0], left[i][1]);  i += 1
    while j < len(right): push(right[j][0], right[j][1]); j += 1
    return result
```

**Why it is correct:** each half's skyline is a correct height-vs-x step function over
its buildings (by induction, base case a single building). The true height at any x is
the max of the two halves' heights there, because the overall skyline is the pointwise
max of the two sub-skylines. The sweep evaluates that pointwise max at every point
where either contour changes — the only places the combined max can change — and the
`push` dedupe guarantees no two consecutive equal-height key points survive.

**Recurrence:** `T(n) = 2T(n/2) + O(n)` — the merge is linear in the total number of
key points, which is `O(n)` → `O(n log n)` by the Master Theorem.

- **Time:** `O(n log n)`.
- **Space:** `O(n)` for the merged contours plus `O(log n)` recursion stack.

## Key Insights & Edge Cases

- **The overall skyline is the pointwise maximum of sub-skylines** — that single fact
  is what licenses the D&C split, exactly as merge sort relies on "merging two sorted
  runs yields a sorted run."
- **Tie on x (`left[i][0] == right[j][0]`)** must advance *both* pointers and update
  *both* heights before taking the max; handling only one side there produces a wrong
  transient height. See example 2 (`[[0,2,3],[2,5,3]]`) where both segments touch at
  x=2 and must merge into one flat run.
- **Collapsing equal heights** is required by the problem ("no consecutive horizontal
  segments of equal height"). The `push` guard handles it uniformly, including inside
  the drain loops where a leftover segment may match the last emitted height.
- **Track `h1`/`h2` as persistent state**: once a side's current height is set it holds
  until that side's next key point — do not reset it to `0` between steps.
- **Alternative:** a sweep-line using a max-heap / multiset of active heights over
  sorted edge events also runs in `O(n log n)`. The Divide and Conquer version is the
  cleaner illustration of the split → recurse → merge structure and needs no heap.
