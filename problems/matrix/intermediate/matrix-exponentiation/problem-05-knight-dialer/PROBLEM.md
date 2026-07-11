# Knight Dialer

**Difficulty:** Medium

LeetCode 935 "Knight Dialer" (with the standard large-`n` follow-up that forces
Matrix Exponentiation).

## Description

Imagine a phone keypad laid out like this:

```
1 2 3
4 5 6
7 8 9
  0
```

A chess **knight** is placed on the keypad. From a given digit it may jump to any digit
reachable by a knight's move (two squares in one direction and one square perpendicular). The
valid moves are:

```
0 -> 4, 6
1 -> 6, 8
2 -> 7, 9
3 -> 4, 8
4 -> 0, 3, 9
5 -> (none)
6 -> 0, 1, 7
7 -> 2, 6
8 -> 1, 3
9 -> 2, 4
```

Given an integer `n`, count how many distinct phone numbers of length `n` the knight can dial
by starting on any digit and making exactly `n - 1` valid jumps. Return the count **modulo
`10^9 + 7`**.

Because `n` can be enormous (up to `5·10^9` in this variant), an `O(n)` DP is too slow — you
must advance the per-digit counts in `O(log n)` time.

## Constraints

- `1 <= n <= 5·10^9`
- Return the answer modulo `10^9 + 7`.

## Examples

### Example 1

```
Input:  n = 1
Output: 10
Explanation: The knight can start on any single digit 0-9, giving 10 numbers of length 1.
```

### Example 2

```
Input:  n = 2
Output: 20
Explanation: From each starting digit the knight has a fixed set of next digits; summed over
all starts there are 20 valid length-2 numbers (e.g. "04", "06", "16", "18", ...). Note the
knight can never stand on 5 as a non-final digit because 5 has no outgoing moves.
```

### Example 3

```
Input:  n = 3
Output: 46
Explanation: Extending every length-2 number by one more valid jump yields 46 length-3
numbers in total.
```

## Hint

The vector "count of numbers ending on each digit 0-9" transforms by a fixed 10×10 rule per
appended digit. Raise that matrix to the `(n-1)`-th power with **Matrix Exponentiation**.
