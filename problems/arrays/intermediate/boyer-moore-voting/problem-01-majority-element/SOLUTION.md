# Majority Element — Solution

## Brute Force

**Hash-map counting.** Count every value's frequency, then return the one whose count
exceeds `n // 2`.

```python
from collections import Counter

def majorityElement(nums):
    counts = Counter(nums)
    return max(counts, key=counts.get)
```

- **Time:** O(n) — one pass to count, one pass over distinct keys.
- **Space:** O(n) — the map may hold up to n distinct keys.

An alternative brute force is sorting and returning `nums[n // 2]` (the middle element must
be the majority once sorted): O(n log n) time, O(1)–O(n) space depending on the sort. Both
work, but neither achieves the O(1)-space linear-time target.

## Optimal Approach — Boyer–Moore Voting

Maintain a single `candidate` and an integer `count`:

- When `count == 0`, adopt the current element as the new `candidate`.
- If the current element equals `candidate`, increment `count`; otherwise decrement it.

```python
def majorityElement(nums):
    candidate = None
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate
```

### Why it is correct

Model each element as a **vote**. A vote for the current candidate is `+1`; any other value
is `-1` and cancels one candidate vote. Group the elements into pairs of "candidate vs.
non-candidate"; each pair cancels out. Because the true majority element `m` occurs more than
`n/2` times, it has *strictly more* votes than every other value **combined**, so the total
sum of votes for `m` versus everything-else is positive. No matter how cancellations
interleave, `m` cannot be reduced to zero-and-replaced across the whole array: whenever the
count resets to `0`, the elements seen so far split into equal +/- contributions, so the
suffix that remains *still* contains `m` as a majority. Hence the final surviving candidate
is `m`.

Since the problem **guarantees** a majority exists, the verification pass can be skipped. (If
it were not guaranteed, you would count the candidate's real occurrences in a second pass and
confirm they exceed `n // 2`.)

### Worked trace on `[2,2,1,1,1,2,2]`

| x | count before | action | candidate | count after |
|---|---------------|--------|-----------|-------------|
| 2 | 0 | count==0 → adopt 2, then +1 | 2 | 1 |
| 2 | 1 | equals candidate → +1 | 2 | 2 |
| 1 | 2 | differs → −1 | 2 | 1 |
| 1 | 1 | differs → −1 | 2 | 0 |
| 1 | 0 | count==0 → adopt 1, then +1 | 1 | 1 |
| 2 | 1 | differs → −1 | 1 | 0 |
| 2 | 0 | count==0 → adopt 2, then +1 | 2 | 1 |

Final candidate: `2`, which is the majority. ✓

- **Time:** O(n) — a single pass.
- **Space:** O(1) — two scalar variables.

## Key Insights & Edge Cases

- **The candidate is only meaningful if a majority truly exists.** For `[1, 2, 3]` voting
  returns `3` (the last element), which is *not* a majority — that is why verification matters
  when the guarantee is absent. Here the problem promises one, so it is safe.
- **Adopt-then-vote order:** when `count == 0` you set the candidate to `x` and then the same
  element contributes `+1`. Writing it as "set candidate, then `count += 1 if x == candidate`"
  handles this cleanly since `x == candidate` is now true.
- Single-element arrays and arrays that are entirely one value both work with no special case.
- Overflow is a non-issue in Python, but note that `count` never exceeds `n`.
