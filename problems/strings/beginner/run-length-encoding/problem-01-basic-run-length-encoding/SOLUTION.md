# Solution — Basic Run-Length Encoding

## Brute Force

There is no meaningfully "brute" version of this problem — it is inherently a
single scan. A slightly naive framing is: for each index, look backward/forward
to find how many identical characters surround it, then decide what to print.
Doing that per index without remembering where the current run started leads to
repeated re-scanning of the same run and `O(n^2)` behavior in the worst case
(one giant run of the same character).

- **Time:** `O(n^2)` if you re-count the run at every index.
- **Space:** `O(n)` for the output.

## Optimal Approach (Run-Length Encoding)

Make a single left-to-right pass, tracking the character that starts the current
run and how many times it has repeated so far.

Step by step:

1. If `s` is empty, return `""`.
2. Initialize `prev = s[0]` and `count = 1`.
3. For each character `c` in `s[1:]`:
   - If `c == prev`, increment `count` (the run continues).
   - Otherwise the run ended: append `prev + str(count)` to the output, then
     reset `prev = c` and `count = 1`.
4. After the loop, one run is still "open" — append `prev + str(count)`.
5. Join the pieces into the result string.

```python
def run_length_encode(s: str) -> str:
    if not s:
        return ""
    out = []
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            out.append(prev + str(count))
            prev = c
            count = 1
    out.append(prev + str(count))   # flush the final run
    return "".join(out)
```

**Why it is correct:** Every character belongs to exactly one maximal run. The
loop extends the current run while characters match and *flushes* it exactly once
when the character changes; the post-loop flush handles the last run. Thus each
run is emitted once and only once, in order, so concatenating the pieces
reproduces the original grouping.

- **Time:** `O(n)` — each character is examined once.
- **Space:** `O(n)` for the output list (up to about `2n` characters, since a run
  of length 1 costs 2 output characters). `O(1)` auxiliary state beyond that.

## Key Insights & Edge Cases

- **Always flush the last run.** The most common bug is forgetting the append
  after the loop, which drops the final run.
- **Empty string** must return `""` — guard before indexing `s[0]`.
- **Single character** `"a"` -> `"a1"`.
- **All identical** `"aaaa"` -> `"a4"`; **all distinct** `"abcd"` -> `"a1b1c1d1"`,
  which is *longer* than the input. RLE only compresses when runs are long; this
  format never shrinks all-distinct input.
- **Multi-digit counts** must be written in full decimal (`"w12"`, not `"w1w2"`),
  which is why the constraint forbids digits in the input — otherwise `"w12"`
  would be ambiguous.
- Using a list and `"".join(...)` avoids `O(n^2)` string concatenation in Python.
