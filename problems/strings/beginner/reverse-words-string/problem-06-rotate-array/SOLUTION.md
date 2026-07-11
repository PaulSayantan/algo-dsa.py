# Rotate Array — Solution

## Brute Force

Rotate one step at a time, `k` times. Each step pops the last element and
inserts it at the front:

```python
def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    for _ in range(k % n):
        last = nums.pop()          # O(1)
        nums.insert(0, last)       # O(n) shift
```

- **Time:** `O(n * k)` — up to `k` rotations, each doing an `O(n)` shift. With
  `k` up to `10^5` and `n` up to `10^5` this is far too slow.
- **Space:** `O(1)`.

An alternative brute force copies into a new array `result[(i + k) % n] = nums[i]`
then writes back: that is `O(n)` time but `O(n)` extra space.

## Optimal Approach (Reverse Words / String)

The **reversal identity** — the same double/triple reversal used to reorder
words, applied to two blocks. Rotating right by `k` means the last `k` elements
move to the front and the first `n - k` move to the back. You can achieve that
with three in-place reversals:

```python
def reverse(nums, lo, hi):
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1

def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n                     # rotations beyond n wrap around
    reverse(nums, 0, n - 1)    # reverse the whole array
    reverse(nums, 0, k - 1)    # reverse the first k
    reverse(nums, k, n - 1)    # reverse the remaining n - k
```

**Why it is correct.** Write the array as two blocks `A` (first `n - k`) and
`B` (last `k`), so `nums = A B`. The goal is `B A`. Reversing the whole array
gives `reverse(B) reverse(A)`. Reversing the first `k` elements restores `B`
(they occupy the first `k` slots now), and reversing the remaining `n - k`
elements restores `A`. The net result is `B A`, exactly the right rotation.

**Step-by-step on `nums = [1,2,3,4,5,6,7]`, `k = 3`:**

1. `k %= 7` → `k = 3`.
2. Reverse whole `[0,6]`: `[7,6,5,4,3,2,1]`.
3. Reverse first `k=3`, i.e. `[0,2]`: `[5,6,7,4,3,2,1]`.
4. Reverse the rest `[3,6]`: `[5,6,7,1,2,3,4]`.

Result: `[5,6,7,1,2,3,4]`.

- **Time:** `O(n)` — three reversals touching each element a constant number of
  times.
- **Space:** `O(1)` — in-place swaps only.

## Key Insights & Edge Cases

- **Always take `k %= n` first.** If `k >= n`, rotating by `k` equals rotating by
  `k mod n`. Skipping this makes the sub-reversals go out of bounds or do
  redundant work. With `k = 0` (after mod) all three reversals cancel out and the
  array is unchanged — correct.
- **Right vs left rotation.** This recipe rotates *right*. To rotate *left* by
  `k`, either use `reverse(0, k-1); reverse(k, n-1); reverse(0, n-1)`, or rotate
  right by `n - k`.
- **`n = 1`:** `k %= 1` is `0`, so nothing happens; a single element is invariant
  under rotation.
- **Connection to the technique.** Reordering the words of a sentence and
  rotating an array are the *same* operation viewed differently: both split the
  buffer into blocks and swap the blocks' order via reversals, achieving `O(1)`
  extra space. Recognizing this identity is the payoff of mastering
  reverse-whole-then-per-part.
