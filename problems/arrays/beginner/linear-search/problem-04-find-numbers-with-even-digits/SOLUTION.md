# Solution — Find Numbers with Even Number of Digits

## Brute Force

The "brute force" and the optimal are the same shape here — you must inspect every
number. The only real choice is *how* you count a number's digits. A straightforward
way is to convert to a string and take its length; a more arithmetic way divides by 10
repeatedly. Both are constant work per element for the given constraints
(`nums[i] <= 10^5`, at most 6 digits).

- **Time:** O(n · d) where d ≤ 6 is the max digit count → effectively O(n).
- **Space:** O(1).

## Optimal Approach (Linear Search)

Do a single linear pass over the array. For each number, determine its digit count and
increment the answer if that count is even.

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            digits = len(str(x))          # or: count digits by dividing by 10
            if digits % 2 == 0:
                count += 1
        return count
```

Arithmetic digit-count without string conversion:

```python
def num_digits(x: int) -> int:
    d = 0
    while x > 0:
        x //= 10
        d += 1
    return d
```

**Why it is correct:** Each element is independently tested against the "even number of
digits" predicate, and the counter accumulates exactly the elements that satisfy it.
After the full scan the counter equals the number of qualifying elements.

**Step by step** on `[12, 345, 2, 6, 7896]`:

- 12 → 2 digits, even → count = 1
- 345 → 3 digits, odd → count = 1
- 2 → 1 digit, odd → count = 1
- 6 → 1 digit, odd → count = 1
- 7896 → 4 digits, even → count = 2

Final answer: **2**.

- **Time:** O(n) (each digit-count is O(d), d ≤ 6, a small constant).
- **Space:** O(1).

## Key Insights & Edge Cases

- This is linear search generalized: instead of matching a fixed target you test a
  **predicate** ("digit count is even") on each element.
- **Digit counting:** `len(str(x))` is simplest; the arithmetic version avoids string
  allocation and is preferred if micro-optimizing. Given the constraint `nums[i] >= 1`,
  you never have to worry about 0 (which would need a special case since `str(0)` has
  length 1 but the arithmetic loop would return 0).
- A slick trick: since `nums[i] <= 10^5`, an even-digit number is one in the ranges
  `[10,99]`, `[1000,9999]`, or exactly `100000`. Explicit counting is clearer, though.
