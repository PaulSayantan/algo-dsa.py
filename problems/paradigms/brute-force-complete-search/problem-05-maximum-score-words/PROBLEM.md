# Maximum Score Words Formed by Letters

**Difficulty:** Hard

**Source:** LeetCode 1255 (Maximum Score Words Formed by Letters)

## Description

Given a list of `words`, a list of single-character available `letters`, and a
`score` array where `score[i]` is the point value of the `i`-th letter of the
alphabet (`score[0]` for `'a'`, `score[1]` for `'b'`, ..., `score[25]` for
`'z'`), return the **maximum score** of any valid set of words you can form.

Rules:

- You may use each letter in `letters` **at most once** across all chosen words.
- Each **word** must be used **at most once** — you either take the whole word or
  leave it; you cannot split a word or use only part of it.
- You do **not** have to use all available letters, and you do **not** have to
  form every word.
- The score of a chosen set of words is the sum of the scores of every letter in
  every chosen word.

Because there are at most 14 words, there are at most `2^14 = 16384` subsets of
words to consider. Brute force / complete search examines every subset, checks
whether its letter demand fits within the available supply, and keeps the
highest-scoring feasible subset.

## Constraints

- `1 <= words.length <= 14`
- `1 <= words[i].length <= 15`
- `1 <= letters.length <= 100`
- `letters[i]`, `words[i][j]` are lowercase English letters.
- `score.length == 26`
- `0 <= score[i] <= 10`

## Examples

### Example 1

```
Input:  words   = ["dog", "cat", "dad", "good"]
        letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
        score   = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                   (a=1, c=9, d=5, g=3; every other letter scores 0)
Output: 19
Explanation: Available letters are {a:2, c:1, d:3, g:1, o:2}.
  - "cat" needs a 't', which we do not have -> can never be chosen.
  - "dad" costs d,a,d and scores 5+1+5 = 11.
  - "good" costs g,o,o,d and scores 3+0+0+5 = 8.
  Choosing {"dad", "good"} needs a:1, d:3, g:1, o:2 -- all within budget -- for
  a total of 11 + 8 = 19. We cannot also add "dog" (that would need d:4, but only
  3 d's exist). No subset beats 19, so the answer is 19.
```

### Example 2

```
Input:  words   = ["xxxz", "ax", "bx", "cx"]
        letters = ["z", "a", "b", "c", "x", "x", "y", "y"]
        score   = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
                   (a=4, b=4, c=4, x=5, z=10; every other letter scores 0)
Output: 18
Explanation: Available letters are {a:1, b:1, c:1, x:2, y:2, z:1}.
  - "xxxz" needs three x's, but only two are available -> can never be chosen.
  - "ax", "bx", "cx" each score 4+5 = 9 and each consumes one 'x'.
  With only two x's, we can pick at most two of these three words. Any two give
  9 + 9 = 18, which is the maximum.
```

## Hint

Use **Brute Force / Complete Search**: enumerate all `2^n` subsets of `words`;
for each, tally the required letters, keep it only if the tally never exceeds the
available letters, and track the maximum total score.
