# Solution — Shortest Palindrome

## Reframing the problem

We may only prepend characters. If the longest **prefix** of `s` that is itself
a palindrome has length `L`, then `s = P + T` where `P = s[:L]` is a palindrome
and `T = s[L:]` is the leftover tail. To make the whole thing a palindrome, we
must mirror `T` and place it in front:

```
answer = reverse(T) + P + T = reverse(s[L:]) + s
```

Because `P` is already a palindrome, this is a valid palindrome, and it is the
shortest possible: any shorter answer would require an even longer palindromic
prefix, contradicting the maximality of `L`. So the whole task reduces to
**finding the longest palindromic prefix length `L`**.

## Brute Force

Check each prefix length from longest to shortest and test if that prefix is a
palindrome.

```python
def shortestPalindrome(s):
    n = len(s)
    for L in range(n, 0, -1):
        if s[:L] == s[:L][::-1]:
            return s[L:][::-1] + s
    return s        # empty string
```

- **Time:** `O(n^2)` — `O(n)` candidate lengths, each palindrome check `O(n)`.
  Too slow for `n` up to `5 * 10^4`.
- **Space:** `O(n)` for the reversed slices.

## Optimal Approach — KMP on a combined string

Build the string

```
combined = s + '#' + reverse(s)
```

and compute its LPS array. The **last value** `lps[-1]` is the length of the
longest prefix of `combined` (which is a prefix of `s`) that is also a suffix of
`combined` (which is a suffix of `reverse(s)`, i.e. a prefix of `s` read
backward). A prefix of `s` that equals the reverse of that same prefix is
exactly a **palindromic prefix**. So `L = lps[-1]` is the longest palindromic
prefix length.

```python
def build_lps(p):
    m = len(p)
    lps = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and p[i] != p[k]:
            k = lps[k - 1]
        if p[i] == p[k]:
            k += 1
        lps[i] = k
    return lps

def shortestPalindrome(s):
    if not s:
        return ""
    combined = s + '#' + s[::-1]
    lps = build_lps(combined)
    L = lps[-1]                    # longest palindromic prefix length
    return s[L:][::-1] + s
```

### Why the `#` separator is essential

Without the separator, the LPS overlap could run past the midpoint and match
characters of `s` against characters of `reverse(s)` across the join, producing a
"border" longer than `len(s)` and a wrong `L`. Inserting a sentinel character
that appears in **neither half** (here `#`) caps every matched border at
`len(s)`, so `lps[-1]` is guaranteed to be a real prefix of `s`.

### Trace `s = "aacecaaa"`

`combined = "aacecaaa#aaacecaa"`. Building the LPS gives `lps[-1] = 7`, so
`L = 7`, the palindromic prefix is `"aacecaa"`, tail `T = "a"`, and the answer is
`reverse("a") + "aacecaaa" = "a" + "aacecaaa" = "aaacecaaa"`. Correct.

For `s = "abcd"`: `combined = "abcd#dcba"`, `lps[-1] = 1`, `L = 1`, tail `"bcd"`,
answer `"dcb" + "abcd" = "dcbabcd"`. Correct.

### Complexity

Let `n = len(s)`. The combined string has length `2n + 1`.

- **Time:** **O(n)** to build the LPS over the combined string.
- **Space:** **O(n)** for the combined string and its LPS array.

## Key Insights & Edge Cases

- **Empty input** → return `""` (no characters, already a palindrome).
- **Already a palindrome** (`s = "aba"`) → `L = n`, tail is empty, answer is `s`
  unchanged.
- **No shared characters at the front** (`s = "abcd"`) → `L = 1` (single first
  char is always a length-1 palindrome), so almost all of `s` is mirrored.
- **The separator must be outside the alphabet.** If the problem allowed the
  sentinel character to appear in `s`, pick one guaranteed absent (or use a
  non-string sentinel). For lowercase-only input, `#` is safe.
- **Prepend, not append.** The mirrored tail goes in *front*; appending would
  solve a different problem.
