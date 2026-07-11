# Sort Colors — Solution

## Brute Force

Call a general-purpose comparison sort on the array.

```python
def sortColors(nums):
    nums.sort()   # disallowed by the problem, and O(n log n)
```

- **Time:** `O(n log n)`.
- **Space:** `O(1)` extra (for an in-place sort).

The problem explicitly forbids the library sort, and it wastes the fact that there are only
three keys.

## Optimal Approach (Counting Sort, k = 3)

With only three possible values this is the textbook counting-sort scenario. Do two passes:

1. **Count pass:** tally the number of `0`s, `1`s, and `2`s into `count[0..2]`.
2. **Overwrite pass:** write `count[0]` zeros, then `count[1]` ones, then `count[2]` twos back
   into `nums`, using a single running write index.

```python
def sortColors(nums):
    count = [0, 0, 0]
    for x in nums:
        count[x] += 1

    i = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[i] = color
            i += 1
```

**Why it is correct:** After the count pass, `count[c]` is exactly how many cells must hold
color `c`. Writing colors in increasing order (`0`, then `1`, then `2`) fills the array with
the correct multiplicities in the required red-white-blue order, and the running index `i`
covers every position exactly once.

- **Time:** `O(n + k)` with `k = 3`, i.e. `O(n)`.
- **Space:** `O(k) = O(1)` — a fixed three-slot count array.

### Alternative: one-pass Dutch National Flag

You can also solve it in a single pass with three pointers (`low`, `mid`, `high`) that
partition the array into `<1`, `==1`, and `>1` regions, swapping as `mid` advances. This is
`O(n)` time and truly one pass. It is a partition scheme rather than a pure counting sort, but
it is the canonical "follow-up" answer, so it is worth knowing:

```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

## Key Insights & Edge Cases

- **Tiny fixed `k`** makes counting sort trivially optimal here; the count array never grows
  with `n`.
- **In-place overwrite** is valid because counting sort with a fixed key set does not need the
  original values once they are counted — we regenerate them from the tallies.
- **Single-element or already-sorted arrays** work with no special casing.
- **All-same-color arrays** (e.g. all `2`s) are handled: two of the three inner loops simply
  run zero times.
- Counting-sort overwrite is **not stable**, but stability is meaningless here since equal
  keys are indistinguishable.
