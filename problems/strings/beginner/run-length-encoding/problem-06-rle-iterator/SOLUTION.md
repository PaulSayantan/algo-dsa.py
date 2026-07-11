# Solution — RLE Iterator

## Brute Force

Decode the whole encoding into an explicit list, keep a cursor, and for `next(n)`
move the cursor forward by `n`.

- **Fatal flaw:** counts can be up to `10^9` (and `next(n)` can request up to
  `10^9`), so the decoded sequence may have on the order of `10^9`–`10^12`
  elements. Materializing it blows the time and memory budget.
- **Time:** `O(total_sequence_length)` to build. **Space:** `O(total_sequence_length)`.

This is exactly the situation where you must operate *on the RLE form directly*.

## Optimal Approach (walk the Run-Length Encoding in place)

Keep a pointer `i` into `encoding` that points at the count of the current run,
and never expand the sequence. On each `next(n)`, peel elements off runs.

State:

- `encoding`: the array (we track consumption by decrementing counts here).
- `i`: index of the current run's count (`encoding[i]` = remaining count in the
  run, `encoding[i + 1]` = its value). Starts at `0`, advances by `2` per
  exhausted run.

`next(n)`:

1. While `n > 0` and `i < len(encoding)`:
   - If `encoding[i] >= n`: this run covers the request. Subtract:
     `encoding[i] -= n`, set `n = 0`, and return `encoding[i + 1]` (the value of
     the last exhausted element).
   - Else: the whole run is consumed. `n -= encoding[i]`, then advance
     `i += 2` to the next run.
2. If we exit the loop with `n > 0`, the sequence ran out — return `-1`.

```python
class RLEIterator:
    def __init__(self, encoding: List[int]) -> None:
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.encoding):
            if self.encoding[self.i] >= n:
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]
            # consume the entire remaining run and move on
            n -= self.encoding[self.i]
            self.i += 2
        return -1
```

(If mutating the input is undesirable, keep a separate `consumed` counter for the
current run and compare `encoding[i] - consumed` instead of decrementing
`encoding[i]`.)

**Why it is correct:** The pointer `i` always sits on the first run that still has
unexhausted elements. When `encoding[i] >= n`, the `n`-th element lies inside the
current run, so its value is `encoding[i + 1]`; decrementing the stored count
records that those `n` elements are gone. When `encoding[i] < n`, that run cannot
satisfy the request, so we consume all of it (`n -= encoding[i]`) and move to the
next run. If we run past the end while `n` is still positive, there were fewer
than the requested elements left, so `-1` is the specified answer. Consumed runs
are skipped permanently because `i` only ever increases, giving correct
continuation across calls.

- **Time:** each `next` is `O(1 + number of runs fully consumed by this call)`.
  A run is fully consumed at most once across the whole lifetime, so the total
  work over all calls is `O(len(encoding) + number_of_calls)`. Amortized, each
  call is very cheap — never proportional to `n`.
- **Space:** `O(1)` extra (we reuse the given array plus one index).

## Key Insights & Edge Cases

- **Never expand the sequence** — the entire point is that `n` and the run counts
  can be up to `10^9`. Peel from runs arithmetically.
- **Zero-length runs** (e.g. `[..., 0, 9, ...]` meaning "zero 9s") are handled for
  free: `encoding[i] = 0 < n`, so we skip them via `i += 2` without emitting the
  value. This is why value `9` never appears in the worked example.
- **Exact boundary** (`encoding[i] == n`) correctly leaves a count of `0` at
  `encoding[i]`; the next call sees `0 < n'` and advances past it.
- **Running out:** once exhausted, every subsequent `next` returns `-1` because
  `i` has walked off the end.
- **Return value semantics:** `next(n)` returns the *value of the last exhausted
  element*, not how many were consumed. When it returns `-1`, all remaining
  elements are still consumed (the iterator is left empty).
- **Large counts** need no special handling since Python integers are arbitrary
  precision; in fixed-width languages, use 64-bit counters.
