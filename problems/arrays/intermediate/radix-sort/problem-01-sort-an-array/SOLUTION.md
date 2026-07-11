# Solution — Sort an Array

## Brute Force

The naive baseline is any `O(n^2)` comparison sort (selection/insertion sort):
repeatedly find the minimum of the unsorted region and place it. Simple, but far
too slow for `n = 5 * 10^4`.

- **Time:** `O(n^2)`
- **Space:** `O(1)`

A standard improvement is a comparison sort like merge/heap/quick sort at
`O(n log n)`. That is acceptable here, but the value range is small and bounded,
so we can do better with a non-comparison approach.

## Optimal Approach (Radix Sort)

The keys are bounded integers, so we can sort in (effectively) linear time with
**LSD radix sort** built on a **stable counting sort**.

### Handling negatives

Radix sort operates on non-negative digit sequences. The cleanest trick is to
**offset** every value by the minimum:

1. Let `mn = min(nums)`.
2. Replace each value `x` with `x - mn`, making all values `>= 0`.
3. Radix sort the shifted, non-negative values.
4. Add `mn` back to each element.

Offsetting preserves relative order, so the sorted shifted array maps directly
back to the sorted original.

### LSD radix sort with base `B`

Process digits from least significant to most significant. Each pass is a stable
counting sort keyed on the current digit `(x // exp) % B`:

```python
def sortArray(self, nums):
    if len(nums) <= 1:
        return nums
    mn = min(nums)
    shifted = [x - mn for x in nums]          # make everything >= 0
    mx = max(shifted)

    BASE = 256                                # radix; a power of two is fast
    exp = 1
    while mx // exp > 0:                       # one pass per digit of mx
        count = [0] * BASE
        for x in shifted:
            count[(x // exp) % BASE] += 1
        for i in range(1, BASE):               # prefix sums -> end positions
            count[i] += count[i - 1]
        output = [0] * len(shifted)
        for x in reversed(shifted):            # reverse pass keeps it stable
            d = (x // exp) % BASE
            count[d] -= 1
            output[count[d]] = x
        shifted = output
        exp *= BASE

    return [x + mn for x in shifted]
```

### Why it is correct

- **Counting sort is stable:** iterating the input in reverse while filling from
  the end of each digit-bucket preserves the input order among equal digits.
- **Stability across passes:** when we sort on a more significant digit, ties on
  that digit retain the order produced by the previous (less significant) pass.
  By induction, after the final pass the array is fully sorted by the complete
  key.
- **Offset trick** guarantees all digits are non-negative and keeps the ordering
  identical to the original signed ordering.

### Complexity

Let `n` be the number of elements, `k = BASE` the radix, and `d` the number of
digits needed for the largest shifted value (`d = ceil(log_B(range))`).

- **Time:** `O(d · (n + k))`. With a fixed range and `BASE = 256`, `d` is a
  small constant, so this is `O(n)`.
- **Space:** `O(n + k)` for the output buffer and the count array.

## Key Insights & Edge Cases

- **Negatives:** the offset-by-min trick is the least error-prone way to support
  them. Alternatively, sort by magnitude, then split into negatives/positives,
  reverse the negatives, and concatenate.
- **All equal / single element:** the `while mx // exp > 0` loop runs zero times
  when `mx == 0` (e.g. every value equals `mn`), returning the array unchanged.
- **Choice of base:** a larger base means fewer passes but a bigger count array.
  Powers of two (256) let you replace division/modulo with shifts and masks.
- **Duplicates:** handled automatically — counting sort places equal keys
  contiguously and stably.
- **Stability direction:** filling `output` while scanning the input in reverse
  is what makes each pass stable; scanning forward would break the invariant.
