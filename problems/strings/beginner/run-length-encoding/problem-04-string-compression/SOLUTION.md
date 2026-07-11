# Solution — String Compression

## Brute Force

Build the compressed string in a *separate* buffer (list), then copy it back into
`chars`:

1. Scan runs, appending `char` and, when the run length `> 1`, the digit
   characters of the count, into a new list `tmp`.
2. Copy `tmp` back over `chars[0:len(tmp)]`.
3. Return `len(tmp)`.

This is correct and `O(n)` time, but it uses `O(n)` extra space, violating the
`O(1)` auxiliary-space requirement of the problem.

- **Time:** `O(n)`.
- **Space:** `O(n)` extra — **does not meet the constraint.**

## Optimal Approach (in-place Run-Length Encoding, two pointers)

Because the compressed form is never longer than the input (a run of length `k`
occupies at most `1 + len(str(k))` cells, and `1 + len(str(k)) <= k` for all
`k >= 1`), we can safely overwrite from the front while reading ahead. Use two
indices:

- `read` — scans the input to find each run.
- `write` — the next position to place output.

Step by step:

1. Set `read = 0`, `write = 0`, `n = len(chars)`.
2. While `read < n`:
   - Let `ch = chars[read]`. Advance a `run_end` pointer while
     `chars[run_end] == ch`; the run length is `count = run_end - read`.
   - Write the character: `chars[write] = ch`; `write += 1`.
   - If `count > 1`, write each digit of `count` in order: convert `count` to its
     decimal string and place each digit character, incrementing `write` for each.
   - Set `read = run_end` to jump to the next run.
3. Return `write`.

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read = 0
        write = 0
        while read < n:
            ch = chars[read]
            run_end = read
            while run_end < n and chars[run_end] == ch:
                run_end += 1
            count = run_end - read

            chars[write] = ch
            write += 1
            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1
            read = run_end
        return write
```

**Why it is correct / why `write` never overtakes `read`:** When we finish a run
we have consumed `count` input cells and written at most `1 + len(str(count))`
cells. Since `1 + len(str(count)) <= count` for every `count >= 1` (equality only
at `count == 1`), the cumulative `write` position is always `<= read`. So the
cells we still need to read are never clobbered before we read them. Each run is
processed once and produces exactly the specified output (char, plus digits only
when `count > 1`), so the front of `chars` holds the correct compressed array and
`write` is its length.

- **Time:** `O(n)` — every character is read once by the inner scan and written at
  most once.
- **Space:** `O(1)` auxiliary (the `str(count)` is at most 4 characters for
  `n <= 2000`, i.e. constant).

## Key Insights & Edge Cases

- **Write digits individually.** The count `12` must become two array entries
  `'1', '2'`, not a single `'12'` element. Iterating over `str(count)` does this
  cleanly.
- **Length-1 runs omit the count.** Guard the digit-writing with `if count > 1`.
  This is what distinguishes LeetCode 443 from the "always emit count" RLE of
  Problem 1.
- **In-place safety** relies on the length inequality above; it is the crux of the
  problem and the reason a two-pointer overwrite is valid.
- **Single element** `['a']` -> return `1`, no digits written.
- **All identical**, e.g. 2000 `'a'`s -> `['a','2','0','0','0']`, return `5`.
- **Multi-digit counts across the boundary of 9/10/100** are handled uniformly by
  `str(count)`; no special casing of digit boundaries is needed.
- Do **not** early-return based on `len(chars)`; even a single group must still
  write its character.
