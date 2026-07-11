# Solution — Shifting Letters

## Brute Force

Follow the problem literally: for each index `i` from `0` to `n-1`, walk positions
`0..i` and advance each of those letters by `shifts[i]` (mod 26). This applies each
shift to its whole prefix.

```python
def shiftingLetters(s, shifts):
    arr = [ord(c) - ord('a') for c in s]
    n = len(s)
    for i in range(n):
        for j in range(i + 1):
            arr[j] = (arr[j] + shifts[i]) % 26
    return "".join(chr(x + ord('a')) for x in arr)
```

- **Time:** O(n^2) — the nested prefix updates. With `n` up to 10^5 this is ~10^10
  operations and will time out.
- **Space:** O(n) for the working array.

The wasteful part is re-touching early positions once per later shift. Each
position `j` really only needs the *total* it will receive, which is a suffix sum.

## Optimal Approach (Case Conversion & ASCII Arithmetic)

Observe that position `j` is affected by `shifts[i]` for every `i >= j` (since each
such shift covers the prefix `0..i`). So the total shift for position `j` is the
suffix sum `shifts[j] + shifts[j+1] + ... + shifts[n-1]`.

Compute these suffix sums in one right-to-left pass, keeping a running accumulator,
and rotate each letter as you go. To rotate a lowercase letter by `total`:

1. `idx = ord(c) - ord('a')` maps it to 0..25.
2. `idx = (idx + total) % 26` advances it, wrapping around the 26-letter alphabet.
3. `chr(idx + ord('a'))` maps the 0..25 result back to a lowercase character.

```python
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        result = []
        for c, sh in zip(reversed(s), reversed(shifts)):
            total = (total + sh) % 26          # keep suffix sum small
            idx = (ord(c) - ord('a') + total) % 26
            result.append(chr(idx + ord('a')))
        return "".join(reversed(result))
```

### Step-by-step for `s = "abc"`, `shifts = [3, 5, 9]`

Process right to left:

1. `'c'`, `sh=9`: `total = 9`; `idx = (2 + 9) % 26 = 11` -> `'l'`.
2. `'b'`, `sh=5`: `total = 14`; `idx = (1 + 14) % 26 = 15` -> `'p'`.
3. `'a'`, `sh=3`: `total = 17`; `idx = (0 + 17) % 26 = 17` -> `'r'`.

Collected `['l', 'p', 'r']`, reversed -> `"rpl"`.

**Why it is correct:** by definition shift `i` advances all of `s[0..i]`, so summing
the contributions to a fixed position `j` counts every `shifts[i]` with `i >= j` —
exactly the suffix sum. Building it right-to-left lets the accumulator carry that
suffix sum in O(1) per step. Taking `% 26` on both the accumulator and the final
index keeps the arithmetic bounded and reflects the alphabet's 26-letter wrap-around
(`'z' -> 'a'`). The `ord`/`chr` conversions are the ASCII-arithmetic bridge between
letters and their 0..25 indices.

- **Time:** O(n) — a single pass.
- **Space:** O(n) for the output list (O(1) auxiliary beyond it).

## Key Insights & Edge Cases

- The core reframe is "prefix shifts applied at each index" == "suffix sum of
  shifts per position." Recognizing this collapses O(n^2) into O(n).
- Reduce the running total mod 26 each step. `shifts[i]` can be up to 10^9 and
  there are up to 10^5 of them, so an un-reduced sum reaches ~10^14; keeping it
  mod 26 avoids large-number cost (and overflow in fixed-width languages).
- A shift that is a multiple of 26 is a no-op: `(25 + 52) % 26 = 25`, so `'z'`
  stays `'z'` (Example 3).
- Wrap-around is handled entirely by `% 26`; there is no need to special-case
  letters near `'z'`.
- Every character is guaranteed lowercase, so `ord(c) - ord('a')` always lands in
  0..25 — no case handling needed.
