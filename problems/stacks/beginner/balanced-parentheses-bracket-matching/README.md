# Balanced Parentheses / Bracket Matching

The canonical stack application: scan left to right, **push** each opening bracket, and on a closing bracket check that the top of the stack is its matching opener (and pop it). The string is balanced iff every closer matches and the stack is empty at the end. Runs in O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Valid Parentheses](problem-01-valid-parentheses/PROBLEM.md) | Bracket matching | Easy |
| 2 | [Minimum Add to Make Parentheses Valid](problem-02-min-add-to-make-valid/PROBLEM.md) | Balance counting | Medium |
| 3 | [Remove Outermost Parentheses](problem-03-remove-outermost-parentheses/PROBLEM.md) | Depth tracking | Easy |
| 4 | [Maximum Nesting Depth of the Parentheses](problem-04-maximum-nesting-depth-of-parentheses/PROBLEM.md) | Stack height | Easy |
| 5 | [Matching Bracket Indices](problem-05-matching-bracket-indices/PROBLEM.md) | Index pairing | Easy |
