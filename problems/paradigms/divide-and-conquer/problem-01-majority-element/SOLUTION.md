# Majority Element — Solution

## Brute Force

For each element, scan the whole array and count how many times it appears; return the
first element whose count exceeds `⌊n/2⌋`.

- **Time:** `O(n^2)` — a count scan per candidate.
- **Space:** `O(1)`.

A hash map of counts improves this to `O(n)` time / `O(n)` space, and Boyer–Moore
voting achieves `O(n)` time / `O(1)` space. But the instructive approach here is
Divide and Conquer.

## Optimal Approach (Divide and Conquer)

**Key claim:** If an element is the majority of the range `[lo, hi]`, then it must be
the majority of the left half `[lo, mid]` **or** the right half `[mid+1, hi]` (or
both). Proof by contradiction: if a value `x` were a majority of the whole range but
of *neither* half, it would appear at most `⌊len_left/2⌋ + ⌊len_right/2⌋ ≤ ⌊len/2⌋`
times — not a strict majority. So the whole-range majority is always inherited from a
half.

**Algorithm:**

1. **Divide:** split `[lo, hi]` at `mid`.
2. **Conquer:** recursively find the majority candidate of each half. Base case: a
   single element is the majority of its length-1 range.
3. **Combine:** if the two half-candidates agree, that value is the answer for the
   range. Otherwise count each candidate's occurrences within `[lo, hi]` and return
   whichever appears more.

```python
def majorityElement(nums):
    def rec(lo, hi):
        if lo == hi:                 # base case: single element
            return nums[lo]
        mid = (lo + hi) // 2
        left = rec(lo, mid)
        right = rec(mid + 1, hi)
        if left == right:
            return left
        # combine: count each candidate over [lo, hi]
        lc = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        rc = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
        return left if lc > rc else right

    return rec(0, len(nums) - 1)
```

**Recurrence:** `T(n) = 2T(n/2) + O(n)` (the two counts in combine are linear) →
`O(n log n)` by the Master Theorem.

- **Time:** `O(n log n)`.
- **Space:** `O(log n)` recursion stack.

## Key Insights & Edge Cases

- **The load-bearing lemma** is that a global majority is inherited by at least one
  half. Without it there would be no reason the recursion could find the answer.
- **Combine is where the work is:** dividing is free; the linear count that decides
  between two candidates is what gives the `O(n)` term in the recurrence.
- **Single element / all identical:** the base case handles length 1, and when both
  halves return the same value we skip the count entirely.
- **Ties in the count cannot mislead:** because a true majority exists, one candidate
  will strictly out-count the other over the full array at the top level.
- Divide and Conquer here is *not* optimal (Boyer–Moore is `O(n)`/`O(1)`), but it is a
  perfect first illustration of the split → recurse → combine shape.
