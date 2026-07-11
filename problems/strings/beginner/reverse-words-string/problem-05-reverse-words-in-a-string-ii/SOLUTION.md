# Reverse Words in a String II — Solution

## Brute Force

Join the array into a string, split into words, reverse the token list, join
with single spaces, and copy the characters back:

```python
def reverseWords(self, s: List[str]) -> None:
    words = "".join(s).split(" ")
    rebuilt = " ".join(reversed(words))
    for i, ch in enumerate(rebuilt):
        s[i] = ch
```

- **Time:** `O(n)`.
- **Space:** `O(n)` — the joined string, the token list, and the rebuilt string
  all scale with the input, violating the `O(1)` extra-space requirement.

It produces the right answer but defeats the purpose of the "in place" version.

## Optimal Approach (Reverse Words / String)

The canonical **reverse-whole-then-per-word** algorithm. It needs only the
two-pointer `reverse(arr, lo, hi)` helper and a couple of index variables.

```python
def reverse(arr, lo, hi):
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1

def reverseWords(self, s: List[str]) -> None:
    n = len(s)
    # Step 1: reverse the whole array.
    reverse(s, 0, n - 1)
    # Step 2: reverse each word back to fix its letters.
    start = 0
    for i in range(n + 1):
        if i == n or s[i] == " ":
            reverse(s, start, i - 1)
            start = i + 1
```

**Why it is correct.** Let the original words be `w1 w2 ... wk`. Reversing the
whole array reverses both the sequence of words and the letters inside each one,
yielding `reverse(wk) ... reverse(w2) reverse(w1)`. The words are now in the
target order, but each is spelled backwards. Step 2 walks the array, and at each
space (or the virtual end at index `n`) reverses the segment that makes up the
current word, undoing the letter flip. The result is `wk ... w2 w1` — the words
reversed, each spelled correctly. Since the spaces occupy the same slots before
and after step 1 (a single space maps to a single space), the layout stays
valid and no extra array is needed.

**Step-by-step on `"the sky is blue"`:**

1. Reverse whole: `"eulb si yks eht"`.
2. Reverse each word segment back:
   - `[0,3]` `"eulb"` → `"blue"` ⇒ `"blue si yks eht"`
   - `[5,6]` `"si"` → `"is"` ⇒ `"blue is yks eht"`
   - `[8,10]` `"yks"` → `"sky"` ⇒ `"blue is sky eht"`
   - `[12,14]` `"eht"` → `"the"` ⇒ `"blue is sky the"`
3. Result: `"blue is sky the"`.

- **Time:** `O(n)` — step 1 is one pass; step 2 reverses disjoint segments whose
  lengths sum to `n`. Total work is linear.
- **Space:** `O(1)` — only index variables; all swaps happen in the given array.

## Key Insights & Edge Cases

- **Order of the two reversals is interchangeable in principle** (you could
  reverse each word first, then the whole array), but reverse-whole-first is the
  standard framing and pairs naturally with the boundary-scan in step 2.
- **The virtual boundary `i == n`** flushes the final word, which has no trailing
  space — the same fix needed in Problem 2.
- **Single word / single character:** `["a"]` → reverse whole is a no-op, then
  the one segment reverses to itself. Output unchanged, as required.
- **This is the in-place sibling of Problem 4.** Problem 4 allows extra space and
  must also normalize irregular spacing; here the input is already clean and the
  challenge is strictly the `O(1)`-space reordering.
- The very same triple/double reversal identity powers array rotation
  (Problem 6): rotating by `k` is "reverse whole, reverse first `k`, reverse the
  rest," which is two words treated as blocks.
