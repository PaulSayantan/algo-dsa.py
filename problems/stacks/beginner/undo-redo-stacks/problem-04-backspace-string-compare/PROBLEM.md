# Backspace String Compare

**Difficulty:** Easy

**Source:** LeetCode 844 — Backspace String Compare

## Description

Given two strings `s` and `t`, return `True` if they are equal when both are typed
into empty text editors. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue to be empty.

Constraints:

- `1 <= s.length, t.length <= 200`
- `s` and `t` only contain lowercase letters and `'#'` characters.

## Examples

### Example 1

```
Input:  s = "ab#c", t = "ad#c"
Output: True
```

**Explanation:** Both `s` and `t` become `"ac"`. Typing `a`, `b`, backspace, `c`
leaves `"ac"`; typing `a`, `d`, backspace, `c` also leaves `"ac"`.

### Example 2

```
Input:  s = "a##c", t = "#a#c"
Output: True
```

**Explanation:** Both `s` and `t` become `"c"`.

## Hint

Build each final string on a stack: a letter is a push, and `'#'` is an undo —
pop the last typed character (if any). Compare the two resulting stacks.
