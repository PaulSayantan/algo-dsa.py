# Brute Force / Complete Search

**Enumerate every candidate solution, test each one, and keep the ones that work.**

Brute force (also called *complete search* or *exhaustive search*) is the most
direct problem-solving paradigm: rather than being clever, you systematically
generate the *entire* space of possible answers and check each candidate against
the problem's conditions. It is almost never the fastest approach, but it is
almost always the easiest to reason about and get correct.

## When to reach for it

- **As a baseline first.** Before optimizing, write the obvious exhaustive
  solution. It gives you a *correct* reference you can test faster algorithms
  against (e.g., with randomized stress testing).
- **When the input is small.** If `n <= 20` for subset enumeration
  (`2^n` states), or `n <= 10` for permutations (`n!` states), or the total
  candidate space fits comfortably in the time limit, exhaustive search is often
  the *intended* solution — not just a fallback.
- **When correctness matters more than speed.** One-off scripts, contest
  problems with tiny constraints, or verifying a hypothesis.
- **When no better structure is obvious.** Some problems genuinely have no known
  polynomial algorithm; complete search (with pruning) is the honest answer.

## The core recipe

1. **Identify the candidate space** — subsets (`2^n`), permutations (`n!`),
   pairs/triples (`n^2`, `n^3`), grid cells, digit strings, etc.
2. **Enumerate it systematically** — nested loops, bitmask iteration
   (`for mask in range(1<<n)`), `itertools.permutations`/`combinations`, or
   recursion.
3. **Test each candidate** against the problem's constraints / objective.
4. **Track the best / collect all valid** candidates as you go.

## Typical complexity

| Candidate space         | Count      | Feasible up to (rough) |
|-------------------------|------------|------------------------|
| All pairs               | `O(n^2)`   | `n` ~ 10^4             |
| All triples             | `O(n^3)`   | `n` ~ a few hundred    |
| All subsets (bitmask)   | `O(2^n·n)` | `n` ~ 20               |
| All permutations        | `O(n!·n)`  | `n` ~ 10-11            |

Space is usually `O(n)` for the current candidate (plus output size if you must
return every valid candidate). The defining trait of brute force is that runtime
scales with the size of the *search space*, not with clever reuse of subresults.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Two Sum](problem-01-two-sum/PROBLEM.md) | Try every pair of indices to hit a target sum | Easy |
| 2 | [Subsets](problem-02-subsets/PROBLEM.md) | Enumerate all `2^n` subsets via bitmasking | Medium |
| 3 | [Permutations](problem-03-permutations/PROBLEM.md) | Generate all `n!` orderings of distinct numbers | Medium |
| 4 | [Letter Combinations of a Phone Number](problem-04-letter-combinations-phone-number/PROBLEM.md) | Cartesian product over per-digit letter sets | Medium |
| 5 | [Maximum Score Words Formed by Letters](problem-05-maximum-score-words/PROBLEM.md) | Try every subset of words under a letter budget | Hard |
