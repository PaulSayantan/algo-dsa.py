# Solution — Compare Version Numbers

## Brute Force

Use two pointers that walk both strings simultaneously. At each step, manually
read the characters up to the next `'.'`, build the integer revision digit by
digit, compare, and advance both pointers past the dot. This avoids allocating
lists but requires careful index management and a hand-rolled string-to-int
conversion.

```python
def compareVersion(version1: str, version2: str) -> int:
    i = j = 0
    n, m = len(version1), len(version2)
    while i < n or j < m:
        r1 = 0
        while i < n and version1[i] != ".":
            r1 = r1 * 10 + int(version1[i]); i += 1
        r2 = 0
        while j < m and version2[j] != ".":
            r2 = r2 * 10 + int(version2[j]); j += 1
        if r1 != r2:
            return -1 if r1 < r2 else 1
        i += 1; j += 1   # skip the dot
    return 0
```

- **Time:** `O(n + m)`.
- **Space:** `O(1)`.

Correct and space-optimal, but verbose. Splitting expresses the same logic far
more directly.

## Optimal Approach (String Tokenization / Split)

Split each version on `'.'`, map the tokens to integers, then compare index by
index, treating out-of-range revisions as 0:

```python
def compareVersion(version1: str, version2: str) -> int:
    r1 = [int(x) for x in version1.split(".")]
    r2 = [int(x) for x in version2.split(".")]
    for i in range(max(len(r1), len(r2))):
        a = r1[i] if i < len(r1) else 0
        b = r2[i] if i < len(r2) else 0
        if a != b:
            return -1 if a < b else 1
    return 0
```

**Why it is correct.** Splitting on `"."` yields the list of revision tokens in
order. Converting each with `int(...)` **discards leading zeros automatically**
(`int("001") == 1`), which is exactly the "compare by integer value" rule. By
iterating up to the longer length and substituting `0` for missing indices, we
honor the "missing trailing revision counts as 0" rule. The first differing
revision decides the result; if none differ, the versions are equal.

**Step by step** for `version1 = "1.0"`, `version2 = "1.0.0.0"`:

1. `r1 = [1, 0]`, `r2 = [1, 0, 0, 0]`.
2. `i=0`: `1 == 1`. `i=1`: `0 == 0`.
3. `i=2`: `r1` has no index 2, so `a = 0`; `b = 0`. Equal. `i=3`: same, `0 == 0`.
4. Loop ends with no difference → return `0`. Done.

For `version1 = "1.2"`, `version2 = "1.10"`: `[1,2]` vs `[1,10]`; at `i=1`,
`2 < 10` → return `-1`.

- **Time:** `O(n + m)` — split, int conversion, and the comparison scan are all
  linear in the input sizes.
- **Space:** `O(n + m)` for the two revision lists.

## Key Insights & Edge Cases

- **`int()` handles leading zeros**, so `"1.01"` vs `"1.001"` → `[1,1]` vs
  `[1,1]` → equal. Never compare revisions as raw strings (`"2" > "10"`
  lexicographically, which is wrong).
- **Different lengths** are the classic trap. Iterate to `max(len)` and pad the
  shorter side with `0`, rather than stopping at the shorter length.
- **Trailing-zero revisions** (`"1.0.0.0"`) compare equal to a shorter version,
  which the zero-padding handles naturally.
- A neat alternative uses `itertools.zip_longest(r1, r2, fillvalue=0)` to iterate
  padded pairs without manual index bounds.
- Return values must be exactly `-1`, `0`, or `1` — do not return the raw
  difference `a - b`.
