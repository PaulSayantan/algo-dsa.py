# Minimum Number of Steps to Make Two Strings Anagram — Solution

## Brute Force

Try to think of it as an alignment/matching problem: pair up characters of `t` with
characters of `s` and count mismatches. Naively you might sort both strings and, for
each position, count where they differ — but that over-counts, because a replacement
in `t` can create *any* letter, so what matters is the multiset difference, not
positional differences. A truly naive approach (search over which positions to change)
is exponential and unnecessary.

- **Time:** exponential if you literally search over subsets of positions.
- **Space:** varies.

We can do far better by reasoning about frequencies directly.

## Optimal Approach (Anagram Check — sort or count)

`t` is an anagram of `s` exactly when their character-frequency tables are identical.
Since `s` and `t` have equal length, the total surplus of characters in `t` equals the
total deficit. Every replacement removes one surplus character and adds one deficient
character, fixing exactly one unit of imbalance. Therefore:

> **Answer = number of character occurrences that `s` has but `t` lacks**
> = `sum over each letter c of max(count_s[c] - count_t[c], 0)`.

Equivalently, it is half the total absolute difference of the two frequency tables (the
surplus side equals the deficit side).

Algorithm:

1. Count characters in `s` -> `count_s`.
2. For each character in `t`, decrement its entry in `count_s` (reuse the same table).
   After this, positive leftover values are letters `s` still needs that `t` did not
   provide.
3. Sum the positive leftovers. That sum is the answer.

```python
def minSteps(self, s: str, t: str) -> int:
    count = Counter(s)
    for c in t:
        count[c] -= 1                     # t "supplies" this character
    return sum(v for v in count.values() if v > 0)  # letters s still needs
```

An equally valid formulation with two counters:

```python
def minSteps(self, s: str, t: str) -> int:
    cs, ct = Counter(s), Counter(t)
    return sum((cs - ct).values())        # Counter subtraction keeps only positive parts
```

**Why it is correct:** Let `deficit = sum(max(count_s[c] - count_t[c], 0))` and
`surplus = sum(max(count_t[c] - count_s[c], 0))`. Because `|s| == |t|`, we have
`deficit == surplus`. Each replacement in `t` deletes one surplus letter and writes one
deficient letter, reducing both by one, so `deficit` replacements are necessary (you
must supply every missing occurrence) and sufficient (each surplus slot can be
retargeted to a needed letter). Hence the minimum is `deficit`.

- **Time:** `O(n)` — two linear scans plus a constant-size (26-entry) summation.
- **Space:** `O(1)` for the fixed lowercase alphabet (`O(k)` in general).

## Key Insights & Edge Cases

- **Only the deficit side matters.** Summing `max(count_s[c] - count_t[c], 0)` already
  gives the answer; don't add the surplus side too or you'll double-count.
- **Equal length is essential.** It guarantees surplus == deficit so a single count of
  missing characters is exact. (If lengths could differ, you'd also need insertions/
  deletions.)
- **Already an anagram** -> every difference is `<= 0`, sum of positives is `0`
  (Example 3).
- **Symmetry:** `minSteps(s, t) == minSteps(t, s)` because surplus and deficit swap but
  are equal in magnitude.
- Using `Counter` subtraction (`cs - ct`) is a neat one-liner: Python's `Counter`
  subtraction drops zero and negative counts, leaving exactly the deficit.
