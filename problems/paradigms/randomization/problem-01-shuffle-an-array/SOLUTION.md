# Shuffle an Array — Solution

## Brute Force

A natural but flawed first idea is to repeatedly pick a random element from the remaining
pool and append it to an output list:

- Keep a list of "unused" elements.
- Repeatedly pick a random index into the unused list, append that element to the answer,
  and remove it from the unused list.

If you remove from the unused list with `list.pop(i)`, each removal shifts elements and
costs O(n), so the whole shuffle is **O(n^2)** time, **O(n)** extra space. It *is* uniform,
but it is quadratic.

An even more naive approach — assign each element a random key and sort by key — is
**O(n log n)** and only uniform if all keys are distinct (ties break in a biased way). It is
also more machinery than necessary.

> Common WRONG shuffle: for each `i`, swap `nums[i]` with `nums[random(0, n-1)]` (a random
> index over the *entire* array). This produces `n^n` equally likely swap-sequences, but
> there are only `n!` permutations and `n^n` is not divisible by `n!` for `n > 2`, so some
> permutations become more likely than others. It is subtly biased — avoid it.

## Optimal Approach (Randomization: Fisher-Yates / Knuth shuffle)

Keep the original array for `reset()`, and shuffle a copy in place.

The Fisher-Yates shuffle walks from the last index down to the first (or first up to last).
At step `i` it swaps element `i` with a uniformly random element chosen from indices
`0..i` (the not-yet-fixed prefix), then treats position `i` as fixed:

```python
def shuffle(self):
    a = self.arr[:]              # work on a copy so reset() still has the original
    for i in range(len(a) - 1, 0, -1):
        j = random.randint(0, i)  # inclusive; j may equal i (element can stay put)
        a[i], a[j] = a[j], a[i]
    self.arr = a
    return a

def reset(self):
    self.arr = self.original[:]  # restore a fresh copy of the original order
    return self.arr
```

`__init__` stores `self.original = nums[:]` and `self.arr = nums[:]`.

### Why it produces a uniform permutation

Think of building the permutation from the back. On the first iteration (`i = n-1`) we
choose which of the `n` elements lands in the last slot; each is chosen with probability
`1/n`. On the next iteration (`i = n-2`) we choose the second-to-last slot from the
remaining `n-1` elements, each with probability `1/(n-1)`, and so on. The probability of
producing any *specific* permutation is therefore

```
1/n * 1/(n-1) * ... * 1/2 * 1/1 = 1/n!
```

Since every permutation has probability exactly `1/n!` and there are `n!` of them, the
distribution is uniform. The key subtlety is that `j` is drawn from `0..i` **inclusive**
(the shrinking unfixed region), not from the full range `0..n-1`.

### Complexity

- **`shuffle()`:** O(n) time (single pass, one swap per position), O(n) space for the copy.
- **`reset()`:** O(n) time to copy back, O(n) space.
- Using an in-place copy per shuffle keeps successive shuffles independent and lets `reset`
  always recover the original.

## Key Insights & Edge Cases

- **Inclusive random index is essential.** Drawing `j` from `0..i` (allowing `j == i`, i.e.
  an element staying in place) is what makes the count come out to exactly `n!`. Drawing
  from `0..n-1` every time is the classic biased bug.
- **Keep the pristine original.** `reset()` must return the construction-time order even
  after many shuffles, so store an untouched copy and never mutate it.
- **Copy on shuffle.** Shuffle a *copy* (or re-copy from the original) so that the ability to
  reset is preserved and repeated shuffles are independent.
- **n = 1:** the loop body never runs; `shuffle()` and `reset()` both return the single-element
  array, which is correct (`1! = 1`).
- **Direction is flexible.** Iterating front-to-back (swap `i` with a random `j` in `i..n-1`)
  is equally valid and equally uniform; just keep the random range over the *unfixed* region.
- **Reproducibility/testing.** Seeding the RNG makes runs deterministic; to empirically check
  uniformity, tally the frequency of each permutation over many trials — they should be
  roughly equal (about `trials / n!` each).
