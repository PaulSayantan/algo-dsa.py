# Reverse String — Solution

## Brute Force

Build the answer in a fresh array by copying characters from back to front,
then copy it back over `s`:

```python
reversed_chars = s[::-1]     # or a manual back-to-front loop
for i in range(len(s)):
    s[i] = reversed_chars[i]
```

- **Time:** `O(n)` — one pass to build, one pass to copy back.
- **Space:** `O(n)` — the temporary reversed array violates the `O(1)`
  memory requirement.

This is correct but wastes memory. The whole point of the problem is to avoid
that extra buffer.

## Optimal Approach (Reverse Words / String)

Use the **two-pointer in-place reversal** primitive. Put `left` at index `0`
and `right` at index `n - 1`. Repeatedly swap `s[left]` with `s[right]`, then
move `left` forward and `right` backward. Stop once the pointers cross.

```python
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

**Why it is correct.** Each iteration places the character that belongs at the
final position `right` into `right` and vice versa. After swapping, the two
outermost unfixed characters are correct, so we shrink the window by one on each
side. The invariant "everything outside `[left, right]` is already in its final
reversed position" holds after every step. When `left >= right` every position
has been fixed (the exact middle element of an odd-length array never needs to
move).

**Step-by-step on `["h","e","l","l","o"]`:**

| left | right | array after swap |
|------|-------|------------------|
| 0 | 4 | `["o","e","l","l","h"]` |
| 1 | 3 | `["o","l","l","e","h"]` |
| 2 | 2 | loop stops (`left == right`) |

Result: `["o","l","l","e","h"]`.

- **Time:** `O(n)` — each character is touched once.
- **Space:** `O(1)` — only two index variables.

## Key Insights & Edge Cases

- **Loop condition is `left < right`, not `left <= right`.** With `<=`, an
  odd-length array would swap the middle element with itself (harmless but
  wasteful), and worse, an off-by-one can re-swap already-fixed pairs.
- **Length 1:** the loop body never runs; the single character is already
  reversed. Correct by construction.
- **Even vs odd length:** even length pairs up every element; odd length leaves
  the exact middle element untouched. Both are handled by `left < right`.
- **In place matters:** Python's `s[::-1]` is elegant but allocates a new list,
  so it does not satisfy the `O(1)` space constraint even though it produces the
  right values. The tuple-swap idiom `s[l], s[r] = s[r], s[l]` mutates in place.
- This two-pointer swap is the atomic building block reused by every other
  problem in this folder.
