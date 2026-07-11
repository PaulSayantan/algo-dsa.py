# Student Attendance Record II

**Difficulty:** Hard

LeetCode 552 "Student Attendance Record II".

## Description

A student's attendance record is a string of length `n` where each character is one of:

- `'A'` — Absent
- `'L'` — Late
- `'P'` — Present

A record is considered **rewardable** if it satisfies **both** conditions:

- It contains **strictly fewer than 2** occurrences of `'A'` (at most one absence total).
- It does **not** contain **3 or more consecutive** `'L'` characters (no run of `L` of length 3+).

Given an integer `n`, return the number of distinct rewardable attendance records of length
`n`, **modulo `10^9 + 7`**.

The follow-up variant here allows very large `n` (up to `10^18`), so the standard `O(n)` DP is
too slow and you must count in `O(log n)` time.

## Constraints

- `1 <= n <= 10^18`
- Return the answer modulo `10^9 + 7`.

## Examples

### Example 1

```
Input:  n = 2
Output: 8
Explanation: There are 3^2 = 9 total strings over {A,L,P}. Only "AA" is not rewardable
(two absences), so 9 - 1 = 8 records are rewardable.
```

### Example 2

```
Input:  n = 1
Output: 3
Explanation: "A", "L", and "P" are all rewardable, so the answer is 3.
```

### Example 3

```
Input:  n = 3
Output: 19
Explanation: Of the 3^3 = 27 length-3 strings, 8 are rejected: "LLL" (three consecutive L),
and the 7 strings containing two or more 'A' characters ("AAA","AAL","AAP","ALA","APA","LAA",
"PAA"). That leaves 27 - 8 = 19 rewardable records.
```

## Hint

Track the state `(number of A's so far in {0,1}, length of the current trailing run of L in
{0,1,2})` — six states. Each appended character is a fixed linear transition, so raise the
6×6 transition matrix to the `n`-th power with **Matrix Exponentiation**.
