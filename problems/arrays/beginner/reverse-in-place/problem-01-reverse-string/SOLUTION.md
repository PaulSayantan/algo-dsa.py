# Reverse String — Solution

## Brute Force

Allocate a new array, copy characters from the end of `s` to the front of the new
array, then copy the new array back into `s`.

```python
reversed_chars = []
for i in range(len(s) - 1, -1, -1):
    reversed_chars.append(s[i])
for i in range(len(s)):
    s[i] = reversed_chars[i]
```

- **Time:** O(n) — two linear passes.
- **Space:** O(n) — the temporary array violates the O(1) requirement.

You could also call `s.reverse()` or `s[:] = s[::-1]`, but the point of the exercise is
to understand the underlying in-place swap.

## Optimal Approach (Reverse In-Place)

Use two pointers, `left` starting at index `0` and `right` at index `n - 1`. Swap
`s[left]` and `s[right]`, then move `left` forward and `right` backward. Stop when
`left >= right`.

```python
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

**Why it is correct:** Each iteration places the element at `left` into its mirror
position `right` and vice-versa. After the `i`-th swap, positions `i` and `n-1-i` hold
their final reversed values. Once the pointers meet, every position in the first half
has been swapped with its mirror in the second half, so the whole array is reversed.
For odd length the single middle element already sits in its correct spot.

- **Time:** O(n) — the loop runs n/2 times, each doing constant work.
- **Space:** O(1) — only two index variables (Python's tuple swap uses no extra array).

## Key Insights & Edge Cases

- **Loop bound `left < right`** guarantees we never double-swap; using `<=` would
  swap the middle element with itself (harmless) but is unnecessary.
- **Length 1:** the loop body never executes; the single character is already reversed.
- **Even vs. odd length:** even length swaps every element; odd length leaves the exact
  middle untouched. Both are handled by the same condition.
- **In-place requirement:** the tuple assignment `s[left], s[right] = s[right], s[left]`
  swaps without an auxiliary list, satisfying O(1) extra space.
