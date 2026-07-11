# Solution — Sort the People

## Brute Force

Zip the two arrays into pairs, sort with the language built-in using a key, then project the
names:

```python
order = sorted(zip(heights, names), key=lambda p: -p[0])
return [name for _, name in order]
```

- Time: `O(n log n)` (built-in sort)
- Space: `O(n)` for the paired list.

This is what you would ship in production. But the exercise is to reorder the pairs yourself
with bubble sort, so that you see how a **key** and **satellite data** (the name) travel
together during swaps.

## Optimal Approach (Bubble Sort on paired keys)

Keep `names` and `heights` aligned. On each pass, compare adjacent heights; when the front
person is *shorter* than the person behind them, swap **both** the heights and the names so the
pairing is preserved. Because we want **descending** order, the "out of order" test is
`heights[j] < heights[j+1]`.

```python
def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    n = len(heights)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if heights[j] < heights[j + 1]:          # shorter in front -> swap
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
                names[j], names[j + 1] = names[j + 1], names[j]
                swapped = True
        if not swapped:
            break
    return names
```

**Why it is correct.** This is ordinary bubble sort keyed on `heights`, just with the
comparison reversed to produce descending order. The invariant becomes: *after pass `i`, the
last `i` slots hold the `i` smallest heights (in place), and everything to their left is
larger.* Because every swap moves the name in lockstep with its height, the `(height, name)`
association is never broken, so the returned `names` correspond to the sorted heights.

- Time: `O(n^2)` worst/average, `O(n)` best (already tallest-first) with the early-exit flag.
- Space: `O(1)` — sorts the two arrays in place; the returned list is `names` itself.

## Key Insights & Edge Cases

- **Move satellite data with the key.** The single most common bug is swapping `heights` but
  forgetting to swap the matching `names` (or vice versa). Always swap both together.
- **Descending order** just flips the comparison to `<`. Everything else is identical to the
  ascending template.
- **Distinct heights** mean there are no ties to break, so stability is irrelevant here; if
  heights could tie, bubble sort's stability would keep equal-height people in input order.
- **Single element / empty** input returns immediately (outer loop body does not run).
- If you must not mutate the inputs, first copy: `heights = list(heights)` and
  `names = list(names)`.
