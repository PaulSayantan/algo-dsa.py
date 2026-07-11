# Number of Operations to Make GCD Array Uniform (Cyclic GCD Windows)

**Difficulty:** Hard

**Source:** Codeforces 1547F ("Array Stabilization (GCD version)")

## Description

You are given a cyclic array `a` of `n` positive integers (index `n` wraps to index
`0`). In one **operation**, you simultaneously replace every element with the gcd of
itself and its clockwise neighbor:

```
new a[i] = gcd(a[i], a[(i + 1) mod n])   for all i, done simultaneously
```

Repeat the operation until **all elements are equal**. Return the **minimum number of
operations** needed. (It is a known fact that the array always stabilizes, and the
final common value is `G = gcd(a[0], a[1], ..., a[n-1])`.)

### Reformulation (the key to solving it efficiently)

After `k` operations, `a[i]` equals the gcd of the **cyclic window of length `k + 1`**
starting at `i`:

```
a_after_k[i] = gcd( a[i], a[i+1], ..., a[i+k] )   (indices mod n)
```

All elements become equal (to `G`) exactly when **every** length-`(k+1)` cyclic window
has gcd `G`. So the answer is the smallest `k` such that all `n` cyclic windows of
length `k + 1` have gcd `G` — equivalently `(maxWindowLen - 1)`, where `maxWindowLen`
is, over all start positions, the shortest window length whose gcd equals `G`.

You must compute this efficiently for `n` up to `2 * 10^5`.

## Constraints

- `1 <= n <= 2 * 10^5`
- `1 <= a[i] <= 10^6`
- The array is cyclic: window indices are taken modulo `n`.

## Examples

### Example 1

```
Input:  a = [16, 24, 10, 5]
Output: 3
```

Explanation: `G = gcd(16, 24, 10, 5) = 1`. Simulating the operation:
- start:  `[16, 24, 10, 5]`
- after 1: `[gcd(16,24), gcd(24,10), gcd(10,5), gcd(5,16)] = [8, 2, 5, 1]`
- after 2: `[2, 1, 1, 1]`
- after 3: `[1, 1, 1, 1]` → all equal. Answer **3**.

### Example 2

```
Input:  a = [42, 42, 42, 42]
Output: 0
```

Explanation: Already all equal, so `0` operations are needed. (Every length-1 window
already has gcd `42 = G`.)

### Example 3

```
Input:  a = [4, 6, 4]
Output: 2
```

Explanation: `G = gcd(4, 6, 4) = 2`. Length-2 cyclic windows have gcds
`gcd(4,6)=2, gcd(6,4)=2, gcd(4,4)=4`; the window starting at index 2 is still `4 != 2`,
so 1 operation is not enough. Length-3 windows all equal `G = 2`, so the answer is
`3 - 1 = 2`.

## Hint

The gcd of an arbitrary cyclic window is an **idempotent** range query. Duplicate the
array (`a + a`) so cyclic windows become ordinary subarrays, build a **Sparse Table**
over gcd, then for each start binary-search (or use the sparse structure) the shortest
window whose gcd reaches `G`. The answer is `(max over starts of that length) - 1`.
