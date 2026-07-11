# Best Fuzzy Match (Minimum Edits)

**Difficulty:** Hard

**Source:** Classic "how close is the best approximate occurrence?" problem — the scoring core behind fuzzy
finders, "did you mean …?" spell suggestions, and `agrep -B` (best-match mode).

## Description

Given a `text` and a `pattern`, return the **minimum number of edits** (insertions, deletions, substitutions —
Levenshtein distance) needed to make `pattern` equal to **some** substring of `text`. Equivalently: over all
substrings `s` of `text`, return `min(editDistance(pattern, s))`. The empty substring is allowed, so the answer
never exceeds `len(pattern)` (you can always delete the whole pattern).

Rather than solve a fresh edit-distance DP, use Bitap as an **oracle**: for a fixed budget `k`, the Wu–Manber
Bitap can answer "does the pattern occur within `k` edits *anywhere* in the text?" in `O(n · k)` time. Run that
test for `k = 0, 1, 2, …` and return the first `k` that succeeds. Because the search is monotone (if it matches
within `k` edits it also matches within `k+1`), the first success is the true minimum.

## Constraints

- `1 <= text.length <= 10^5`
- `1 <= pattern.length <= 64` (the pattern fits in a single 64-bit machine word).
- `text` and `pattern` consist of lowercase English letters.
- The answer is an integer in the range `[0, len(pattern)]`.
- Return `0` iff `pattern` occurs exactly as a substring of `text`.

## Examples

### Example 1
```
Input:  text = "the quikc brown", pattern = "quick"
Output: 1
```
Explanation: The substring `"quik"` of the text is one insertion away from `"quick"` (insert the missing `c`), so
the minimum over all substrings is `1`. Bitap reports "no match" for `k = 0` and "match" for `k = 1`, so the
answer is `1`.

### Example 2
```
Input:  text = "recieve", pattern = "receive"
Output: 2
```
Explanation: The common `ie`/`ei` misspelling: turning the substring `"recieve"` into `"receive"` needs two
substitutions (swap the `i` and `e`), and no substring does better. Bitap fails for `k = 0, 1` and succeeds at
`k = 2`.

### Example 3
```
Input:  text = "aabbcc", pattern = "xyz"
Output: 3
```
Explanation: No character of `"xyz"` appears in the text, so the best you can do is match `"xyz"` against the
**empty** substring by deleting all three characters — distance `3 = len(pattern)`. Bitap fails for `k = 0, 1, 2`
and succeeds at `k = 3`.

## Hint

Wrap the **Bitap / Fuzzy Matching** Wu–Manber "occurs within `k` edits?" test in a loop over `k = 0, 1, 2, …` and
return the first `k` that reports a hit. Remember to check the *initial* register state (which represents matching
against the empty substring via deletions) so large-`k` / short-text cases are handled.

## Follow-up

Once you can compute the minimum, extend your routine to also return the **end position** of a best match, and
think about how binary search over `k` (instead of linear scan) changes the complexity and whether it is
actually worth it here.
