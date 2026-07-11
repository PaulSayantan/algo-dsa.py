# Solution — Product of Array Except Self

## Brute Force

For each index `i`, multiply every other element.

```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= nums[j]
        answer[i] = p
    return answer
```

- **Time:** O(n^2).
- **Space:** O(1) extra.

### Why not just divide?

You could compute the total product once and set `answer[i] = total / nums[i]`, but:
(1) the problem forbids division, and (2) it breaks when any element is `0`. Prefix
and suffix products sidestep both issues.

## Optimal Approach (Prefix Products x Suffix Products)

The product of everything except `nums[i]` factors cleanly into two pieces:

```
answer[i] = (product of nums[0 .. i-1])  *  (product of nums[i+1 .. n-1])
          =         prefix[i]            *          suffix[i]
```

`prefix[i]` is the product of all elements to the **left** of `i`; `suffix[i]` is the
product of all elements to the **right**. Both are cumulative and can be built in one
pass each. Since `max`/product is not needed on the fly — just left and right
products — this is the classic "combine a prefix pass with a suffix pass" pattern.

### Two-array version (clearest)

```python
def productExceptSelf(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    return [prefix[i] * suffix[i] for i in range(n)]
```

### O(1) extra space version (follow-up)

Write the prefix products directly into the output, then multiply by a running
suffix product on a second reverse pass:

```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):                 # answer[i] = product of everything left of i
        answer[i] = answer[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):        # fold in the running product from the right
        answer[i] *= right
        right *= nums[i]
    return answer
```

**Why it is correct.** After the first loop, `answer[i]` holds `prefix[i]` = product
of `nums[0..i-1]` (with `answer[0] = 1`, the empty product). In the second loop,
`right` holds the product of `nums[i+1..n-1]` at the moment we reach `i` (it is
updated *after* multiplying into `answer[i]`). Multiplying gives
`prefix[i] * suffix[i]`, exactly the product of all elements except `nums[i]`.

**Step by step** on `[1, 2, 3, 4]`:

```
prefix pass:  answer = [1, 1, 2, 6]          # 1, 1, 1*2, 1*2*3

suffix pass (right starts at 1):
    i=3: answer[3] = 6*1 = 6;   right = 1*4 = 4
    i=2: answer[2] = 2*4 = 8;   right = 4*3 = 12
    i=1: answer[1] = 1*12 = 12; right = 12*2 = 24
    i=0: answer[0] = 1*24 = 24; right = 24*1 = 24

result = [24, 12, 8, 6]
```

- **Time:** O(n) — two linear passes.
- **Space:** O(1) extra (output array excluded), or O(n) for the two-array version.

## Key Insights & Edge Cases

- **No division needed**, and the approach is robust to zeros. With one zero, only its
  own index gets a nonzero answer; with two or more zeros, every answer is `0` — the
  prefix/suffix products handle this automatically (see Example 2: the single `0`
  makes every `answer[i]` for `i != 2` include a zero factor).
- The empty-product convention (`prefix[0] = 1`, `suffix[n-1] = 1`) is what makes the
  edges correct; `1` is the multiplicative identity, analogous to `0` for prefix sums.
- Update the running `right` product *after* using it, mirroring the "update prefix
  after the check" pattern from Find Pivot Index.
- The problem guarantees every prefix/suffix product fits in 32 bits, so overflow is
  not a concern here (and Python ints are unbounded anyway).
