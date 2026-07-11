# Solution — Lyndon Factorization of a String

## Brute Force

Repeatedly find the *longest Lyndon prefix* of the remaining suffix and peel it off.
Checking whether a candidate prefix is Lyndon (compare it against all its suffixes)
costs `O(len^2)`, and we may try many prefix lengths.

```python
def is_lyndon(t):
    return all(t < t[k:] for k in range(1, len(t)))

def factor_brute(s):
    res, i = [], 0
    while i < len(s):
        best = i + 1
        for j in range(i + 1, len(s) + 1):
            if is_lyndon(s[i:j]):
                best = j
        res.append(s[i:best]); i = best
    return res
```

- **Time:** `O(n^3)` in the worst case.
- **Space:** `O(n)` for slices.

Correct but far too slow for `n = 10^5`.

## Optimal Approach (Duval's Algorithm)

Duval's algorithm produces the entire factorization in a single left-to-right pass.

### The three pointers

- `i`: start index of the Lyndon word(s) we are currently forming.
- `j`: the "look-ahead" scanner comparing characters.
- `k`: points into the already-matched prefix; `p = j - k` is the current *period*.

Loop invariant while scanning from `i`: the block `s[i..j)` is a (possibly repeated)
prefix of a Lyndon word with period `p = j - k`, and `s[i..k)` equals the corresponding
prefix one period back.

### The scan and emit

```python
def lyndon_factorization(s):
    n = len(s)
    i = 0
    factors = []
    while i < n:
        j = i + 1
        k = i
        # extend the current Lyndon candidate
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i          # strictly larger char: reset, period grows to j - i + 1
            else:
                k += 1         # equal char: continue the period
            j += 1
        # now the Lyndon word has period p = j - k; emit copies of length p
        while i <= k:
            factors.append(s[i:i + (j - k)])
            i += (j - k)
    return factors
```

Three cases inside the inner loop:

1. `s[k] < s[j]` — the candidate is a proper Lyndon word so far; the newest char makes
   the whole span from `i` a fresh Lyndon prefix. Reset `k = i` so the period becomes
   `j - i + 1`.
2. `s[k] == s[j]` — we might be in a *periodic* Lyndon prefix (like `aab aab`); advance
   `k` alongside `j` keeping the period.
3. `s[k] > s[j]` **or** `j == n` — the run ends. The confirmed Lyndon word has period
   `p = j - k`. Emit `s[i:i+p]` repeatedly (there may be several equal copies, e.g. two
   `"an"` in `"banana"`) advancing `i` by `p` until `i > k`. The leftover tail (indices
   `> k`) becomes the next factor's start.

### Why it's correct

The Chen–Fox–Lyndon theorem guarantees a unique non-increasing factorization. Duval's
invariant ensures that whenever the run breaks (`s[k] > s[j]`), the prefix `s[i:i+p]` is
the *longest* Lyndon word that can start at `i` while keeping the factors non-increasing;
peeling exactly that word (and its equal repeats) preserves the invariant for the rest.
Hence the emitted list is exactly the unique factorization.

- **Time:** `O(n)`. Each character is charged a constant amortized amount: `j` only moves
  forward, and the total distance `i` travels is `n`.
- **Space:** `O(1)` beyond the output (only three integer pointers).

## Key Insights & Edge Cases

- **Equal factors are allowed.** `"banana" -> ["b","an","an","a"]` has two equal `"an"`
  factors; the theorem requires *non-increasing*, not strictly decreasing.
- **All-equal string** `"aaa" -> ["a","a","a"]`: the period is 1, so each char is its own
  factor.
- **Already a Lyndon word** (e.g. `"abac"` inside `"abacaba"` — actually the whole
  `"abc"`): a single factor is emitted.
- **Strictly decreasing string** `"cba" -> ["c","b","a"]`: every character is its own
  factor because each is larger than what follows.
- **The last factor is special:** the rightmost Lyndon factor is always the
  lexicographically smallest suffix of `s`. This fact powers the next problems (least
  rotation, min/max suffix). Track the last emitted start index if you only need that.
