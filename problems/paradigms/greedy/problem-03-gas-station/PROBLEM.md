# Gas Station

**Difficulty:** Medium

**Source:** LeetCode 134 (Gas Station)

## Description

There are `n` gas stations arranged in a **circle**. At station `i` you can acquire
`gas[i]` units of fuel. It costs `cost[i]` units of fuel to travel from station `i`
to the next station `i + 1` (and from station `n - 1` back to station `0`).

You begin the journey with an **empty tank** at one of the gas stations. Your car has
an unlimited tank capacity.

Return the starting station's index if you can travel around the circuit **once in
the clockwise direction**, otherwise return `-1`. If a solution exists, it is
**guaranteed to be unique**.

## Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

## Examples

### Example 1

```
Input:  gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
Output: 3
```

Explanation: Start at station 3 (gas = 4). Tank = 4 - 1 = 3 → station 4.
Tank = 3 + 5 - 2 = 6 → station 0. Tank = 6 + 1 - 3 = 4 → station 1.
Tank = 4 + 2 - 4 = 2 → station 2. Tank = 2 + 3 - 5 = 0 → back to station 3.
The circuit completes, so the answer is **3**.

### Example 2

```
Input:  gas = [2, 3, 4], cost = [3, 4, 3]
Output: -1
```

Explanation: Total gas = 9, total cost = 10. Since total cost exceeds total gas, no
starting point can complete the loop, so return **-1**.

### Example 3

```
Input:  gas = [5, 1, 2, 3, 4], cost = [4, 4, 1, 5, 1]
Output: 4
```

Explanation: Total gas (15) equals total cost (15), so a solution exists. Starting at
station 4 (gas = 4): tank = 4 - 1 = 3 → 0; 3 + 5 - 4 = 4 → 1; 4 + 1 - 4 = 1 → 2;
1 + 2 - 1 = 2 → 3; 2 + 3 - 5 = 0 → back to 4. Circuit completes, so the answer is **4**.

## Hint

Use a **Greedy** scan. First, a solution exists only if total gas ≥ total cost. Then
track a running tank as you sweep; whenever it dips below zero, no station in the
stretch you just covered can be the start, so reset the candidate start to the next
station.
