# Delete Adjacent Duplicates

A stack collapses adjacent equal (or matching) elements as you scan: before pushing the current element, check the top — if it would form a duplicate pair, pop instead of pushing. The stack ends up holding the reduced sequence, all in O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Remove All Adjacent Duplicates In String](problem-01-remove-all-adjacent-duplicates/PROBLEM.md) | Adjacent-pair collapse | Easy |
| 2 | [Remove All Adjacent Duplicates in String II](problem-02-remove-adjacent-duplicates-ii/PROBLEM.md) | Run-length stack | Medium |
| 3 | [Backspace String Compare](problem-03-backspace-string-compare/PROBLEM.md) | Pop-on-backspace collapse | Easy |
| 4 | [Make The String Great](problem-04-make-the-string-great/PROBLEM.md) | Opposite-case pair collapse | Easy |
| 5 | [Valid Parentheses](problem-05-valid-parentheses/PROBLEM.md) | Matching-pair cancel | Easy |
