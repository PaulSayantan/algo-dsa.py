# Majority Element II — Solution

## Brute Force

**Hash-map counting.** Tally frequencies, then collect every key whose count exceeds
`n // 3`.

```python
from collections import Counter

def majorityElement(nums):
    n = len(nums)
    counts = Counter(nums)
    return [v for v, c in counts.items() if c > n // 3]
```

- **Time:** O(n).
- **Space:** O(n) — up to n distinct keys in the map.

Correct and linear, but it violates the O(1)-space follow-up.

## Optimal Approach — Two-Candidate Boyer–Moore

**Key fact:** at most two values can each appear more than `n/3` times, because three such
values would sum to more than `n`. So we track **two** candidates, each with its own count.

For each element `x`, resolve the cases **in this exact priority order**:

1. If `x == candidate1`, increment `count1`.
2. Else if `x == candidate2`, increment `count2`.
3. Else if `count1 == 0`, set `candidate1 = x`, `count1 = 1`.
4. Else if `count2 == 0`, set `candidate2 = x`, `count2 = 1`.
5. Else decrement **both** `count1` and `count2` (a vote against both candidates).

The equality checks must come before the zero-count checks; otherwise a value equal to an
existing candidate could be mistakenly installed into the other slot.

Then **verify**: a majority is not guaranteed, so re-count both candidates over the array and
keep only those exceeding `n // 3`.

```python
def majorityElement(nums):
    cand1, cand2 = None, object()   # cand2 sentinel distinct from any int
    cnt1 = cnt2 = 0

    for x in nums:
        if x == cand1:
            cnt1 += 1
        elif x == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cand1, cnt1 = x, 1
        elif cnt2 == 0:
            cand2, cnt2 = x, 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    n = len(nums)
    res = []
    for c in (cand1, cand2):
        if nums.count(c) > n // 3:
            res.append(c)
    return res
```

### Why it is correct

Same cancellation argument, now with a "team" of two candidates. Each non-candidate element
decrements *both* counts — i.e., it takes one vote from each of the two teams simultaneously.
A value `v` with more than `n/3` occurrences cannot be fully cancelled: doing so would require
more than `n/3` "opposing" elements *per candidate slot* that `v` competes in, and there
aren't enough non-`v` elements to exhaust a >n/3 value against both. So any true >n/3 value
ends the voting phase holding one of the two candidate slots. The verification pass filters
out slots that are not actually frequent (voting can leave junk candidates when fewer than two
qualifying values exist).

### Worked trace on `[1, 2, 2, 3, 2, 1, 1]` (n = 7, threshold = 2)

| x | rule | cand1/cnt1 | cand2/cnt2 |
|---|------|-----------|-----------|
| 1 | cnt1==0 → install | 1 / 1 | – / 0 |
| 2 | cnt2==0 → install | 1 / 1 | 2 / 1 |
| 2 | == cand2 → +1 | 1 / 1 | 2 / 2 |
| 3 | neither, both >0 → −1,−1 | 1 / 0 | 2 / 1 |
| 2 | == cand2 → +1 | 1 / 0 | 2 / 2 |
| 1 | cnt1==0 → install | 1 / 1 | 2 / 2 |
| 1 | == cand1 → +1 | 1 / 2 | 2 / 2 |

Candidates: `1` and `2`. Verify: `count(1) = 3 > 2`, `count(2) = 3 > 2`. Result `[1, 2]`. ✓

- **Time:** O(n) — one voting pass plus a constant number of O(n) verification counts.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Verification is mandatory here.** Voting always yields two candidates even when zero or
  one value actually qualifies (e.g. `[1, 2, 3]` leaves candidates but none exceed n/3).
- **Case ordering matters:** check both equality cases before both zero-count cases. Swapping
  the order can duplicate a candidate into both slots.
- **Both counts decrement together** on a non-matching element — a common mistake is
  decrementing only one.
- **Distinct candidate initialization:** initialize the two candidate variables so they are
  not accidentally equal to each other or to a real input value (a sentinel object, or
  guarding with the zero-count checks handles this).
- Edge cases: single element, all-identical arrays (returns that one value), and arrays with
  no qualifying element (returns `[]`) all work.
