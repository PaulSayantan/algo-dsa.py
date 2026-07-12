# Maximum Nesting Depth of Parentheses

**Difficulty:** Easy

**Source:** LeetCode 1614 — Maximum Nesting Depth of the Parentheses

## Description

Given a **valid parentheses string** `s` (digits and `+-*/` may also appear), return the maximum nesting depth of the parentheses. The depth is the number of unmatched `(` at the deepest point — exactly the maximum stack height if you push on `(` and pop on `)`.

## Examples

### Example 1

```
Input:  s = "(1+(2*3)+((8)/4))+1"
Output: 3
```

**Explanation:** The deepest nesting is 3.

## Hint

Track a running counter (a stack of height only): +1 on '(', -1 on ')', record the max.
