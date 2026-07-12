# Linked-List-Based Stack

A stack can also be built from a singly linked list: push and pop both happen at the **head**, so each is O(1) *worst-case* (no array resizing). This mirrors how recursion frames chain together and is the natural representation when you want guaranteed constant-time operations.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design a Linked-List Stack](problem-01-design-linked-stack/PROBLEM.md) | Linked stack, O(1) head | Easy |
| 2 | [Maximum Nesting Depth of Parentheses](problem-02-max-nesting-depth/PROBLEM.md) | Stack height as depth | Easy |
| 3 | [Valid Parentheses](problem-03-valid-parentheses/PROBLEM.md) | Push openers, pop/match closers | Easy |
| 4 | [Baseball Game](problem-04-baseball-game/PROBLEM.md) | Push/pop/peek the score record | Easy |
| 5 | [Remove All Adjacent Duplicates In String](problem-05-remove-adjacent-duplicates/PROBLEM.md) | Pop on matching top | Easy |
