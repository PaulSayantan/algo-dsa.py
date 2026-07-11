# Solution — Repeated DNA Sequences

## Brute Force

Enumerate every 10-letter substring and count occurrences with a hash map keyed
by the *actual string*.

```python
def findRepeatedDnaSequences(s: str) -> List[str]:
    seen, repeated = set(), set()
    for i in range(len(s) - 9):
        sub = s[i:i + 10]          # slicing a fixed 10-char string
        if sub in seen:
            repeated.add(sub)
        else:
            seen.add(sub)
    return list(repeated)
```

- **Time:** `O(n · L)` where `L = 10`. Building each substring key and hashing
  it costs `O(L)`. Because `L` is a fixed constant here (10), this is
  effectively `O(n)` in practice — but the constant factor from re-reading 10
  characters per window is exactly what a rolling hash removes.
- **Space:** `O(n · L)` in the worst case for storing all the substring keys.

## Optimal Approach (Rabin–Karp)

Map each nucleotide to a small integer (`A→0, C→1, G→2, T→3`) and treat each
length-10 window as a base-4 (or larger base, modulo a large prime) number.
Maintain the window value with a rolling update so each shift is `O(1)`.

### Why it is correct

Two windows with different content produce the same *integer* only on a hash
collision. Two strategies keep the answer exact:

1. **Exact fingerprint (recommended for this problem).** With a 4-symbol
   alphabet and length 10, a window is fully described by
   `10 · 2 = 20` bits, so it fits in a single machine integer with **no modulus
   and no collisions at all**. The rolling value *is* a perfect, lossless
   identifier of the substring. This makes the "hash" approach exact by
   construction.
2. **Polynomial hash modulo a prime.** If you use a large prime modulus, keep a
   map from hash to the actual substring so hash matches can be verified,
   avoiding false positives.

### Step by step (exact 20-bit fingerprint)

1. If `len(s) < 10`, return `[]`.
2. Encode letters: `code = {'A':0,'C':1,'G':2,'T':3}`.
3. Build the fingerprint of the first window as a base-4 integer using 2 bits
   per letter. Keep a mask `(1 << 20) - 1` to retain only the low 20 bits.
4. Slide: `value = ((value << 2) | code[s[i+9]]) & mask`. The `& mask` drops the
   oldest letter automatically — that is the rolling step.
5. Track hashes in `seen`; when a hash reappears, add the *substring* (or its
   window) to `repeated`. Return the collected substrings.

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        code = {"A": 0, "C": 1, "G": 2, "T": 3}
        mask = (1 << 20) - 1        # keep only 20 low bits == 10 letters
        value = 0
        seen, repeated = set(), set()

        for i in range(n):
            value = ((value << 2) | code[s[i]]) & mask
            if i >= 9:              # a full 10-letter window ends here
                if value in seen:
                    repeated.add(s[i - 9:i + 1])
                else:
                    seen.add(value)
        return list(repeated)
```

- **Time:** `O(n)` — one `O(1)` rolling update per character. The `s[i-9:i+1]`
  slice only runs on a repeat, and even then is a constant 10 characters.
- **Space:** `O(n)` for the sets of fingerprints/results.

## Key Insights & Edge Cases

- **Fixed window length is the key enabler.** Because every candidate is exactly
  10 characters, a single rolling value compares them all.
- **`n < 10` → `[]`.** No window exists.
- **Return each repeat once.** Use a *set* for the results so a sequence
  occurring three or more times is reported a single time (Example 2).
- **Bit-packing gives an exact hash.** With a 4-letter alphabet, 2 bits/letter
  and a 20-bit mask means zero collisions — no separate verification needed.
- **Overlapping repeats count.** In `"AAAAAAAAAAAAA"` the windows overlap; they
  are still separate occurrences of the same sequence, so it is repeated.
