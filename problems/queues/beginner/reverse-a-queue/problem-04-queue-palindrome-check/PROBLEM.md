# Palindrome Check on a Queue

**Difficulty:** Easy

**Source:** Classic — palindrome check via queue reversal

## Description

Given a queue as a list (front = index 0), return `True` if the sequence reads the same front-to-back as back-to-front, and `False` otherwise. Reverse the queue with a stack and compare the reversed order against the original element by element. An empty queue is a palindrome.

## Examples

### Example 1

```
Input:  q = [1, 2, 3, 2, 1]
Output: True
```

**Explanation:** Reversing gives `[1, 2, 3, 2, 1]`, identical to the original, so it is a palindrome.

## Hint

Push every element onto a stack; popping yields the reversed queue — compare it position-by-position with the original.
