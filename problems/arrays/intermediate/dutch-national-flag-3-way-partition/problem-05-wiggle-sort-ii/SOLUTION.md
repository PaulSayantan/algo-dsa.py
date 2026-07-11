# Wiggle Sort II — Solution

## Brute Force

**Sort, then interleave the two halves.** Sort ascending, split into a smaller half and a
larger half, then fill the **even** indices from the smaller half and the **odd** indices
from the larger half. Crucially, fill each half from its **largest element downward** so
that copies of the median are pushed as far apart as possible.

```python
def wiggleSort(nums):
    arr = sorted(nums)
    n = len(nums)
    # smaller half -> even positions, larger half -> odd positions, both reversed
    mid = (n + 1) // 2
    small = arr[:mid][::-1]   # descending
    large = arr[mid:][::-1]   # descending
    nums[0::2] = small
    nums[1::2] = large
```

- **Time:** O(n log n) for the sort.
- **Space:** O(n) for the auxiliary sorted copy.

This is correct and the easiest to reason about. The reason for reversing each half is subtle
but essential: if you filled the halves in ascending order, duplicate medians could end up
adjacent (e.g. the largest of the small half touching the smallest of the large half). By
placing the largest of the small half at index 0 and the largest of the large half at index
1, equal medians are separated by roughly `n/2` positions — the maximum possible.

## Optimal Approach — Median via Quickselect + Dutch National Flag on Virtual Indices

To reach expected **O(n)** time (and O(1) extra space beyond the array), combine two ideas:

1. **Quickselect** to find the median value in expected O(n) (itself best done with a 3-way
   partition — see the Kth-Largest problem).
2. A **Dutch National Flag 3-way partition** around the median, but performed over a
   **virtual index mapping** that writes directly into the interleaved wiggle positions, so
   no second array is needed.

### The index-mapping trick

Define a bijection on `0..n-1` that lists the odd slots first (`1, 3, 5, ...`) and then the
even slots (`0, 2, 4, ...`):

```
A(i) = (1 + 2*i) mod (n | 1)
```

where `n | 1` is `n` rounded up to the next odd number. Walking `i = 0, 1, 2, ...` through
`A(i)` visits `1, 3, 5, ..., 0, 2, 4, ...`. If we now run DNF over this mapping and place
**larger-than-median** values at the front (the odd slots) and **smaller-than-median** values
at the back (the even slots), the wiggle property falls out automatically.

```python
def wiggleSort(nums):
    n = len(nums)
    median = quickselect_median(nums)     # expected O(n), 3-way quickselect

    def A(i):
        return (1 + 2 * i) % (n | 1)

    lt, i, gt = 0, 0, n - 1               # Dutch National Flag pointers
    while i <= gt:
        if nums[A(i)] > median:
            nums[A(lt)], nums[A(i)] = nums[A(i)], nums[A(lt)]
            lt += 1
            i += 1
        elif nums[A(i)] < median:
            nums[A(i)], nums[A(gt)] = nums[A(gt)], nums[A(i)]
            gt -= 1
        else:                              # nums[A(i)] == median
            i += 1
```

Here the "colors" are: **greater than median** (goes to the low/odd end), **equal to median**
(stays in the middle), **less than median** (goes to the high/even end). It is the classic
DNF loop with the comparison direction flipped, applied through `A(i)`.

### Why it is correct

The wiggle constraint `nums[even] < nums[odd]` needs the larger half on odd indices and the
smaller half on even indices, with the medians straddling the boundary and separated as much
as possible. The mapping `A` lays the odd indices out first and even indices last as one
linear sequence; DNF partitions that sequence into `> median | == median | < median`. Because
the medians (equal block) sit in the middle of the *virtual* order, they are spread across the
junction between odd and even real positions and never become adjacent — this is exactly what
makes the **strict** inequalities hold, which is the whole difficulty of Wiggle Sort II versus
Wiggle Sort I. The problem guarantees a valid answer exists, which is equivalent to "no value
appears more than ceil(n/2) times", the precondition under which this separation succeeds.

### Worked example on `nums = [1, 3, 2, 2, 3, 1]`

`n = 6`, median (lower median, index 2 of sorted `[1,1,2,2,3,3]`) `= 2`. Running the virtual
DNF places the two `3`s into the odd slots, the two `1`s into the even slots, and the two
median `2`s at opposite ends. One resulting arrangement is `[2, 3, 1, 3, 1, 2]`, which checks
out: `2 < 3 > 1 < 3 > 1 < 2`.

- **Time:** O(n) expected (quickselect) + O(n) (single DNF pass) = **O(n)** expected.
- **Space:** **O(1)** extra — the partition writes back into `nums` through the mapping.

## Key Insights & Edge Cases

- **Strict vs. non-strict:** Wiggle Sort II demands `<`/`>` (no equal neighbors). Placing the
  median copies as far apart as possible — via reversed halves in the simple version, or the
  `A(i)` mapping in the optimal version — is what prevents equal adjacency.
- **`n | 1` rounds up to odd** so that the virtual index cycle length is coprime-friendly and
  `A` is a bijection for both even and odd `n`. Using plain `n` breaks the mapping when `n` is
  even.
- **Which median?** Use the lower median at sorted index `(n-1)//2`. Combined with "larger
  half to odd slots," this correctly handles both even and odd lengths.
- If a value's frequency exceeds `ceil(n/2)` no valid wiggle exists; the problem guarantees
  this does not happen, so you need not detect it, but it explains why the median-separation
  argument is tight.
- Single element and two-element inputs are handled with no special casing.
- The results are **not unique** — the PROBLEM examples show one valid answer each; your
  output may differ while still satisfying every `<`/`>` relation.
- If O(1) space is not required, the sort-and-interleave version is far easier to get right in
  an interview; reach for the quickselect + virtual-index DNF only when O(n)/O(1) is demanded.
