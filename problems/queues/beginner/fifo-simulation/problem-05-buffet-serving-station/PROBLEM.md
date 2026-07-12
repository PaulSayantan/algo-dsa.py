# Buffet Serving Station

**Difficulty:** Easy

**Source:** Classic — serve-or-rotate FIFO simulation

## Description

Guests line up at a buffet station that has a limited number of `servings` in total. `hunger[i]` is how many portions guest `i` still wants, with `hunger[0]` at the front of the line. The server repeatedly hands the front guest **one** portion (using up one serving); that guest then goes to the **back** of the line if they still want more, otherwise they leave satisfied. Serving stops the moment the shared `servings` run out.

Return the number of guests who are still in line (not fully satisfied) when the servings run out. If everyone is satisfied before the food runs out, return `0`.

## Examples

### Example 1

```
Input:  hunger = [1, 2, 1], servings = 3
Output: 1
```

**Explanation:** Guest 0 takes 1 and leaves (2 left), guest 1 takes 1 and rejoins wanting 1 more (1 left), guest 2 takes 1 and leaves (0 left). The food is gone but guest 1 still wants a portion, so 1 guest is unsatisfied.

### Example 2

```
Input:  hunger = [2, 3, 2], servings = 4
Output: 2
```

**Explanation:** After 4 portions are handed out the servings are exhausted while two guests are still waiting in line.

## Hint

`deque` of remaining portions per guest; each step popleft, spend one serving, and re-enqueue `count - 1` if it is still positive. Stop when `servings` hits 0 and return the queue length.
