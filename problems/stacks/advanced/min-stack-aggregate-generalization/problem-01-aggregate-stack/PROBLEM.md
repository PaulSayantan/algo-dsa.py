# Stack with O(1) Min, Max, and GCD

**Difficulty:** Medium

**Source:** Classic — associative-aggregate stack

## Description

Design a stack of positive integers that supports `push`, `pop`, and O(1) queries `getMin`, `getMax`, and `getGcd` (gcd of all current elements). Each frame stores the aggregate of everything at or below it, so popping restores the previous aggregates instantly.

## Hint

Store (value, min, max, gcd) per frame folding the new value with the previous top's aggregates.
