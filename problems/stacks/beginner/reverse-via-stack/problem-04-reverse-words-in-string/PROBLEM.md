# Reverse the Order of Words in a String

**Difficulty:** Easy

**Source:** Classic — word-level LIFO (LeetCode 151 simplified)

## Description

Given a string `s` containing words separated by single spaces (no leading or
trailing spaces), return a string with the words in reverse order, again joined
by single spaces. Solve it with a stack: split into words, push each word, then
pop them all to assemble the reversed sentence.

Constraints: `s` has at least one word; words contain no spaces.

## Examples

### Example 1

```
Input:  s = "the sky is blue"
Output: "blue is sky the"
```

**Explanation:** Push `the, sky, is, blue`; popping gives `blue, is, sky, the`.

### Example 2

```
Input:  s = "hello world"
Output: "world hello"
```

**Explanation:** The two words swap places.

## Hint

Push each word onto a stack, then pop until empty — the pops come out as the reversed word order.
