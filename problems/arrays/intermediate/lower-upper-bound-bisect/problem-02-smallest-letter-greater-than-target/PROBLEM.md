# Find Smallest Letter Greater Than Target

**Difficulty:** Easy

**Source:** LeetCode 744 — Find Smallest Letter Greater Than Target

## Description

You are given an array of characters `letters` that is sorted in **non-decreasing** order, and a
character `target`. There are **at least two different** characters in `letters`.

Return the **smallest character** in `letters` that is **strictly greater than** `target`.

If such a character does not exist (i.e. `target` is greater than or equal to every letter),
the search **wraps around**: return `letters[0]`.

## Constraints

- `2 <= letters.length <= 10^4`
- `letters[i]` is a lowercase English letter.
- `letters` is sorted in non-decreasing order.
- `letters` contains at least two different characters.
- `target` is a lowercase English letter.

## Examples

### Example 1
```
Input:  letters = ['c', 'f', 'j'], target = 'a'
Output: 'c'
Explanation: The smallest letter strictly greater than 'a' is 'c'.
```

### Example 2
```
Input:  letters = ['c', 'f', 'j'], target = 'c'
Output: 'f'
Explanation: We need something STRICTLY greater than 'c'. The letter 'c' itself
             does not count, so the answer is 'f'.
```

### Example 3
```
Input:  letters = ['x', 'x', 'y', 'y'], target = 'z'
Output: 'x'
Explanation: No letter is greater than 'z', so the search wraps around and
             returns the first letter, 'x'.
```

## Hint

You want the first letter **strictly greater** than `target` — that is the **upper bound**. Use a
**Lower/Upper Bound (bisect)** search, then take the result modulo the array length to handle the
wraparound.
