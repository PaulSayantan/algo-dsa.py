# Digit-Square Sequence Length

**Difficulty:** Medium

**Source:** Classic — sum-of-squared-digits cycle

## Description

Starting from `start`, repeatedly replace the current value by the sum of the squares of its digits. Return how many distinct values appear before the sequence first repeats a value (the count includes the start and every value up to but not including the repeat).

## Hint

Add each value to a set; stop when a value would repeat; return the set size.
