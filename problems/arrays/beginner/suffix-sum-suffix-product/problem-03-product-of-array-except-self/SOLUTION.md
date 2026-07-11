# Solution — Product of Array Except Self

## Brute Force

For each index `i`, multiply together every other element with an inner loop.

```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if j != i:
                prod *= nums[j]
        answer[i] = prod
    return answer
```

- **Time:** O(n^2) — an inner scan per index.
- **Space:** O(1) extra.

### Why not just divide?

The tempting O(n) trick is `total_product / nums[i]`. It is disallowed here, and
for good reason: it breaks when any element is `0` (division by zero, and the
distinction between one zero vs. two zeros needs special handling). The
prefix/suffix product approach sidesteps division entirely.

## Optimal Approach (Prefix Product * Suffix Product)

The product of all elements except `nums[i]` equals

```
(product of everything to the LEFT of i) * (product of everything to the RIGHT of i)
```

The left factor is a **prefix product**; the right factor is a **suffix
product**. Build both and multiply.

A space-optimized version writes prefix products into the answer array during a
left-to-right pass, then multiplies in the suffix products during a
right-to-left pass using a single rolling variable — O(1) extra space beyond the
output.

Reference implementation (O(1) extra space):

```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    # Pass 1 (left -> right): answer[i] = product of nums[0..i-1]
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Pass 2 (right -> left): multiply in product of nums[i+1..n-1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```

**Why it is correct:** After pass 1, `answer[i]` holds the product of all
elements strictly before `i`. In pass 2, `suffix` holds the product of all
elements strictly after `i` at the moment index `i` is processed, so
`answer[i] * suffix` is (left product) * (right product) = product of everything
except `nums[i]`. The identity value `1` seeds both the empty prefix (index 0)
and the empty suffix (index n-1).

**Step by step** for `nums = [1, 2, 3, 4]`:

```
Pass 1 (prefix products written into answer):
  answer = [1, 1, 2, 6]     (prefix goes 1 -> 1 -> 2 -> 6 -> 24)

Pass 2 (multiply by suffix products, right to left):
  i=3: answer[3] *= 1  -> 6*1  = 6 ;  suffix = 4
  i=2: answer[2] *= 4  -> 2*4  = 8 ;  suffix = 12
  i=1: answer[1] *= 12 -> 1*12 = 12;  suffix = 36
  i=0: answer[0] *= 36 -> 1*36 = 24;  suffix = 36

answer = [24, 12, 8, 6]
```

- **Time:** O(n) — two linear passes.
- **Space:** O(1) extra (the output array is not counted). A clearer variant that
  keeps separate `prefix` and `suffix` arrays uses O(n) extra and is equally
  correct.

## Key Insights & Edge Cases

- The core template — "prefix aggregate * suffix aggregate = aggregate of all but
  self" — is exactly the same shape used for sum-based "except self" problems;
  only the operator changes from `*` to `+` and the identity from `1` to `0`.
- **Zeros are handled automatically.** One zero in the array makes every position
  that still includes it a `0`; only the zero's own index keeps a non-zero
  product (product of the rest). Two or more zeros make every answer `0`. The
  prefix/suffix method gets all of this right with no special casing — unlike the
  division approach.
- **Sign** is preserved naturally: multiplying signed prefix and suffix products
  yields the correct sign (e.g. Example 2's `answer[2] = 9`).
- Seed both rolling products with the multiplicative identity `1` so the boundary
  indices (empty prefix at 0, empty suffix at n-1) are correct.
