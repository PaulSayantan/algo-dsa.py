# Letter Combinations of a Phone Number — Solution

## Brute Force

Each digit independently contributes one letter. The set of all combinations is
the Cartesian product of the per-digit letter strings. Complete search builds
this product by starting from a single empty partial string and, for each digit
in order, replacing the running list with every extension by that digit's
letters.

```python
class Solution:
    def letter_combinations(self, digits):
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        combos = [""]
        for d in digits:
            combos = [prefix + ch for prefix in combos for ch in phone[d]]
        return combos
```

- **Time:** `O(4^n · n)` where `n = len(digits)` — up to `4^n` combinations
  (digits 7 and 9 have 4 letters), each of length `n` to build. With `n <= 4`
  that is at most `4^4 = 256` combinations.
- **Space:** `O(4^n · n)` for the output; `O(1)` extra beyond it (aside from the
  intermediate `combos` list, which is bounded by the output size).

## Optimal Approach

The number of results can be as large as `4^n`, so producing all of them is at
best `O(4^n · n)` — the iterative Cartesian product above already meets this
bound and is the idiomatic complete-search solution. A recursive backtracking
variant is equivalent:

```python
class Solution:
    def letter_combinations(self, digits):
        if not digits:
            return []
        phone = {"2":"abc","3":"def","4":"ghi","5":"jkl",
                 "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        def dfs(i, path):
            if i == len(digits):
                result.append("".join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return result
```

**Why it is correct.** A valid combination is exactly one choice of letter for
each digit position, independently. The iterative build maintains the invariant
"`combos` holds every possible prefix using the digits processed so far." Each
iteration extends every prefix by every letter of the next digit — precisely the
definition of the Cartesian product — so after the last digit `combos` holds
every full combination, with none missing and none duplicated (distinct
letter-choice tuples give distinct strings).

**Step by step** for `digits = "23"`:

1. Start: `combos = [""]`.
2. Digit `'2'` → letters `"abc"`: `combos = ["a", "b", "c"]`.
3. Digit `'3'` → letters `"def"`: extend each of `a, b, c` by `d, e, f`:
   `["ad","ae","af", "bd","be","bf", "cd","ce","cf"]` — 9 strings.

- **Time:** `O(4^n · n)`.
- **Space:** `O(4^n · n)` output.

## Key Insights & Edge Cases

- **Empty input must return `[]`, not `[""]`.** Guard `if not digits: return []`
  first. Without the guard, starting from `[""]` would leave `[""]` — a wrong
  answer of one empty string.
- **Digits `7` and `9` map to four letters** (`pqrs`, `wxyz`); the others map to
  three. That is why the bound is `4^n`, not `3^n`.
- **`1` and `0` never appear** per the constraints, so the map needs only keys
  `2`-`9`.
- **The iterative approach is often cleaner** than recursion here because there
  is no early pruning — every path reaches full length — so a plain product loop
  suffices.
