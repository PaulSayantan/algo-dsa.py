# Boats to Save People — Solution

## Brute Force

Model it as a matching problem: try every way to pair people into boats (each boat holds
1 or 2 people with total weight `<= limit`) and take the arrangement using the fewest
boats.

- Enumerating pairings is exponential; even a smarter maximum-matching formulation is
  overkill here.
- **Time:** exponential in the naive form. **Space:** `O(n)`.

The difficulty is deciding *who pairs with whom* without a principled order.

## Optimal Approach (Sorting as Preprocessing)

**Idea:** Sort the weights ascending. Use two pointers, `lo` at the lightest remaining
person and `hi` at the heaviest remaining person. Each boat must carry the current
heaviest person `people[hi]` (someone has to). Greedily check whether the **lightest**
remaining person can ride along: if `people[lo] + people[hi] <= limit`, seat both;
otherwise the heaviest goes alone. Either way `hi` moves inward.

**Why it is correct (exchange argument):** The heaviest remaining person must occupy some
boat. The best possible companion for them is the *lightest* remaining person, because
that maximizes the chance the pair fits and never "wastes" pairing capacity. If even the
lightest person doesn't fit with the heaviest, no one does, so the heaviest rides alone.
If the lightest *does* fit with the heaviest, pairing them is at least as good as any
other pairing: giving the lightest person to a lighter partner instead could only leave
the heaviest to occupy a boat alone anyway. Sorting is what makes "lightest" and
"heaviest" O(1) to access at every step.

**Step by step:**

1. Sort `people` ascending.
2. Set `lo = 0`, `hi = n-1`, `boats = 0`.
3. While `lo <= hi`:
   - If `people[lo] + people[hi] <= limit`, the lightest rides with the heaviest:
     `lo += 1`.
   - In all cases the heaviest is now seated: `hi -= 1` and `boats += 1`.
4. Return `boats`.

```python
def numRescueBoats(self, people: List[int], limit: int) -> int:
    people.sort()
    lo, hi = 0, len(people) - 1
    boats = 0
    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1          # lightest person shares the boat
        hi -= 1              # heaviest person is always seated this boat
        boats += 1
    return boats
```

- **Time:** `O(n log n)` for the sort, then `O(n)` for the two-pointer sweep.
- **Space:** `O(1)` beyond the in-place sort.

## Key Insights & Edge Cases

- **Pair the extremes.** Sorting turns a fuzzy pairing problem into a crisp
  lightest-with-heaviest greedy that provably minimizes boats.
- **The heaviest is always seated each iteration** (`hi -= 1` unconditionally). The only
  question is whether the lightest gets to tag along (`lo += 1`).
- **`lo <= hi` (not `<`):** when one person is left, `lo == hi` and the condition
  `people[lo] + people[hi] <= limit` (i.e. `2*w <= limit`) is fine — the single person is
  counted once because after `lo += 1` and `hi -= 1` the loop ends. If they don't "pair
  with themselves," they still get exactly one boat via the `hi -= 1` / `boats += 1`.
- **At most two per boat** is baked in: each iteration seats one or two people and burns
  exactly one boat.
- **Everyone fits alone** by the guarantee `people[i] <= limit`, so the loop always
  terminates with a valid answer.
- **All too heavy to pair** (e.g. `[3,5,3,4]`, `limit=5`): the `if` never fires, so every
  person consumes their own boat — answer equals `n`.
