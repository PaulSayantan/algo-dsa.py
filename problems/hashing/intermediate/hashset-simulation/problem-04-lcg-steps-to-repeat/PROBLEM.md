# Steps Until a Sequence Repeats

**Difficulty:** Medium

**Source:** Classic — linear-congruential loop detection

## Description

A pseudo-random sequence starts at `start` and advances by `x -> (a*x + c) mod m`. Return the number of steps taken until the sequence first revisits a value it has already produced (i.e. the index at which the first repeat occurs).

## Hint

Store seen states; count steps; stop when the next value is already in the set.
