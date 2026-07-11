# RLE Iterator

**Difficulty:** Medium

Source: LeetCode 900 — "RLE Iterator"

## Description

We can use **Run-Length Encoding** to describe an integer sequence: the encoding
is a flat array `encoding` where, for each `i`, the pair
`(encoding[2*i], encoding[2*i + 1])` means "the value `encoding[2*i + 1]` is
repeated `encoding[2*i]` times." For example `[3, 8, 0, 9, 2, 5]` encodes the
sequence `[8, 8, 8, 5, 5]` (three `8`s, zero `9`s, two `5`s).

Design an iterator `RLEIterator` that walks this run-length encoded sequence
**without ever expanding it fully**:

- `RLEIterator(encoding)` initializes the iterator with the encoding array.
- `next(n)` exhausts the next `n` elements of the sequence and returns the value
  of the last element exhausted. If there are fewer than `n` elements remaining,
  it exhausts all of them and returns `-1`.

Successive calls to `next` continue from where the previous call left off.

## Constraints

- `2 <= encoding.length <= 1000`
- `encoding.length` is **even**.
- `0 <= encoding[i] <= 10^9`
- `1 <= n <= 10^9`
- At most `1000` calls will be made to `next`.

## Examples

### Example 1
```
Input:
  ["RLEIterator", "next", "next", "next", "next"]
  [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
Output:
  [null, 8, 8, 5, -1]
Explanation:
  RLEIterator([3,8,0,9,2,5]) decodes the sequence [8,8,8,5,5].
  next(2): exhaust [8,8]; last exhausted is 8. Remaining: [8,5,5]. -> 8
  next(1): exhaust [8];   last exhausted is 8. Remaining: [5,5].   -> 8
  next(1): exhaust [5];   last exhausted is 5. Remaining: [5].     -> 5
  next(2): only 1 element (5) remains; exhaust it, still short. -> -1
```

### Example 2
```
Input:
  ["RLEIterator", "next", "next", "next"]
  [[[1000000000, 7]], [500000000], [400000000], [200000000]]
Output:
  [null, 7, 7, -1]
Explanation:
  The sequence is 1,000,000,000 copies of 7.
  next(500000000): exhaust 500,000,000 of them; last exhausted is 7.
                   Remaining: 500,000,000 copies of 7. -> 7
  next(400000000): exhaust 400,000,000 more; last exhausted is 7.
                   Remaining: 100,000,000 copies of 7. -> 7
  next(200000000): only 100,000,000 remain, which is < 200,000,000, so exhaust
                   all remaining and return -1 (the sequence is now empty). -> -1
```

## Hint

Keep the sequence in **Run-Length Encoding** form and never materialize it.
Track a pointer into the encoding and how much of the current run is already
consumed; `next(n)` subtracts `n` from run counts, skipping exhausted runs, so
each call is `O(number of runs consumed)` rather than `O(n)`.

## Note on the reference solution

The provided reference implementation *mutates* the counts stored in the
`encoding` array to track consumption (a common accepted approach). If you prefer
not to mutate the input, keep a separate "amount consumed in the current run"
counter instead.
