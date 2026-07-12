# Valid Parentheses

**Difficulty:** Easy

**Source:** LeetCode 20 — Valid Parentheses

## Description

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine whether the input string is **valid**. A string is valid when every open bracket is closed by the same type of bracket and brackets are closed in the correct order (each closing bracket matches the most recently opened, still-open bracket).

Constraints: `1 <= len(s) <= 10^4`; `s` consists only of the six bracket characters.

## Examples

### Example 1

```
Input:  s = "()[]{}"
Output: True
```

**Explanation:** Each closing bracket matches the bracket on top of the stack, and the stack ends empty.

### Example 2

```
Input:  s = "(]"
Output: False
```

**Explanation:** `']'` does not match the top-of-stack `'('`.

## Hint

Push each opening bracket onto a linked-list stack; on a closing bracket, pop the head and check it is the matching opener. Valid iff the stack is empty at the end.
