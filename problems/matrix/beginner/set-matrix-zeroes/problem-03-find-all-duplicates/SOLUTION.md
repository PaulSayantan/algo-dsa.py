# Solution — Find All Duplicates in an Array

## Brute Force

Count occurrences with a hash map (or `collections.Counter`) and return the keys
with count 2.

```python
from collections import Counter

def findDuplicates(nums):
    return [v for v, c in Counter(nums).items() if c == 2]
```

- **Time:** `O(n)`.
- **Space:** `O(n)` for the counter.

Correct, but violates the constant-space requirement. The in-place version
below spends `O(1)` extra space.

## Optimal Approach (In-Place Sign Marking)

**Key observation:** the values are exactly `1..n`, so `v - 1` is always a valid
index. We use the sign at `nums[v-1]` as a one-bit "have I seen `v` before?"
flag.

### Step by step

1. Iterate over the array. For each position, read the *magnitude*
   `v = abs(nums[i])` and compute `idx = v - 1`.
2. Inspect `nums[idx]`:
   - If `nums[idx]` is **negative**, we have already visited `idx` for this
     value, so `v` occurs a second time — append `v` to the answer.
   - Otherwise negate it: `nums[idx] = -nums[idx]` to record the first visit.
3. Return the collected duplicates.

```python
def findDuplicates(nums):
    result = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            result.append(idx + 1)
        else:
            nums[idx] = -nums[idx]
    return result
```

### Why it is correct

- Each value appears once or twice. The first occurrence flips its target slot
  negative; the second occurrence sees the negative slot and reports the value.
  A value appearing only once never triggers a report.
- Reading `abs(nums[i])` before computing the index means an already-negated
  slot never yields a bogus (negative) index, so the `value -> index` mapping
  stays intact across the whole scan.
- We report `idx + 1` (equivalently `abs(nums[i])`), which is the original value
  — never the mangled stored value.

### Complexity

- **Time:** `O(n)` — a single pass.
- **Space:** `O(1)` extra — the result list is required output.

## Key Insights & Edge Cases

- **This is the mirror image of LeetCode 448 (Problem 1).** There, slots that
  stay *positive* reveal *missing* values. Here, slots that are *already
  negative* when revisited reveal *duplicate* values. Same marking mechanism,
  opposite question.
- **Always `abs()` on read.** Forgetting it is the #1 bug: after a few
  negations, `nums[i]` may be negative and `nums[i] - 1` becomes an invalid or
  wrong index.
- **Single element / all unique:** `[1]` and `[1,2,3]` produce `[]` — no slot is
  ever revisited.
- **Output order:** duplicates are reported in the order their second occurrence
  is encountered; the problem does not require sorted output.
- **Restoring the array:** if needed, a final pass of `nums[i] = abs(nums[i])`
  undoes all the sign flips.
