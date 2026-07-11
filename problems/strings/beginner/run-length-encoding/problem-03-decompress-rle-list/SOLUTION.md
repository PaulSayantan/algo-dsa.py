# Solution — Decompress Run-Length Encoded List

## Brute Force

Even the "obvious" solution is already optimal here, because the output itself is
the work: you must produce every decompressed element. A less clean version
manually manages two indices and appends one element at a time in a nested loop.
That is fine, just verbose.

- **Time:** `O(total_output_length)` — unavoidable, you emit each element once.
- **Space:** `O(total_output_length)` for the result.

## Optimal Approach (Run-Length Encoding, decode)

The array is already run-length encoded, alternating `freq` then `val`. Decode by
stepping in strides of two.

Step by step:

1. Create an empty result list.
2. For `i` from `0` to `len(nums) - 1` in steps of `2`:
   - `freq = nums[i]`, `val = nums[i + 1]`.
   - Append `freq` copies of `val` (in Python, `[val] * freq`).
3. Return the result.

```python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            out.extend([val] * freq)
        return out
```

A one-liner using a comprehension is equivalent:

```python
return [nums[i + 1] for i in range(0, len(nums), 2) for _ in range(nums[i])]
```

**Why it is correct:** By the problem's definition each pair `(freq, val)`
expands to `freq` copies of `val`, and the pairs are laid out consecutively at
even indices. Iterating with stride 2 visits each pair exactly once in order and
`[val] * freq` produces exactly the required copies, so the concatenation matches
the specification.

- **Time:** `O(n + m)` where `n = len(nums)` and `m` is the output length (sum of
  frequencies).
- **Space:** `O(m)` for the output.

## Key Insights & Edge Cases

- **Order of the pair matters:** frequency is *first*, value is *second*. Swapping
  them is the classic mistake (e.g. `[1, 2]` must give `[2]`, not `[1, 1]`).
- **Stride of 2:** iterate `range(0, len(nums), 2)` so `i` always lands on a
  frequency and `i + 1` on its value; the even-length guarantee means `i + 1` is
  always in range.
- **Frequency is always `>= 1`** per constraints, so every pair contributes at
  least one element — but `[val] * 0` would harmlessly yield `[]` if a zero ever
  appeared.
- **Single pair** (`nums.length == 2`) is the minimum valid input.
- `extend` avoids building and discarding many temporary lists compared to
  repeated `+` concatenation.
