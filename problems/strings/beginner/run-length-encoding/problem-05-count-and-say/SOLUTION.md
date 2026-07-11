# Solution — Count and Say

## Brute Force

There is no shortcut around building the sequence: term `n` is defined only in
terms of term `n - 1`, so you must generate terms `1, 2, ..., n` one after
another. The "brute" concern is *how* you build each term. Constructing each new
term with repeated string concatenation (`result += ...`) inside the run loop
creates a fresh string every append, pushing a single term's construction toward
`O(L^2)` in its length `L`.

- **Time:** up to `O(n * L_max^2)` with naive concatenation.
- **Space:** `O(L_max)`.

## Optimal Approach (iterated Run-Length Encoding)

Start with the base term `"1"` and apply the RLE "say" step `n - 1` times. The
say step is Run-Length Encoding emitted as `count` then `digit` for each run.

Step by step:

1. Set `term = "1"`.
2. Repeat `n - 1` times:
   - Build the next term by scanning `term`'s runs: for each maximal run of an
     identical digit `d` of length `count`, append `str(count) + d`.
   - Use a list of chunks and `"".join(...)` so each term is built in linear time.
   - Replace `term` with the newly built string.
3. Return `term`.

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"
        for _ in range(n - 1):
            chunks = []
            i = 0
            L = len(term)
            while i < L:
                d = term[i]
                count = 0
                while i < L and term[i] == d:
                    count += 1
                    i += 1
                chunks.append(str(count))
                chunks.append(d)
            term = "".join(chunks)
        return term
```

**Why it is correct:** The definition *is* "read the previous term as runs and
write count+digit." The inner two-pointer scan groups each maximal run exactly
once and emits `count` then the digit, which is precisely the specified
transformation. Iterating it `n - 1` times starting from `countAndSay(1) = "1"`
yields `countAndSay(n)` by induction on the recurrence.

- **Time:** `O(n * L)` where `L` is the length of the longest term reached. Terms
  grow at roughly the Conway constant (~1.303) per step, so for `n <= 30` this is
  a few thousand characters — trivially fast.
- **Space:** `O(L)` to hold a term and its successor.

## Key Insights & Edge Cases

- **Order is count-then-digit** (`"21"` = two 1s), the opposite of Problem 1's
  digit-count order. Mixing them up is the classic bug.
- **Base case** `n == 1` returns `"1"` with zero iterations of the loop
  (`range(0)` is empty).
- **Only digits appear** in every term (counts of small runs stay single-digit in
  practice for this sequence, but writing `str(count)` handles any width safely).
- **A run never mixes digits**, so grouping strictly by equality is correct; you
  never need to look beyond adjacency.
- **Build with `join`, not `+=`**, to keep each term's construction linear.
- The recurrence is strictly sequential — you cannot compute `countAndSay(n)`
  without first computing all earlier terms.
