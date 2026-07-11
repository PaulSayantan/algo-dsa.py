# Solution — Happy Number

## Brute Force

Iterate the digit-square-sum process and store every number you have seen in a
hash set. If you reach `1`, return `True`; if you reach a number already in the
set, you have found a cycle that never hit `1`, so return `False`.

```python
def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
```

- **Time:** O(k) where k is the number of steps before reaching 1 or repeating.
  It is bounded because values quickly fall below ~243 (the max square-sum of
  any 3-digit number) and then live in a small finite range.
- **Space:** O(k) for the set.

## Optimal Approach — Floyd's Cycle Detection (Tortoise & Hare)

The function `next(x) = sum of squares of digits of x` is deterministic: every
number has exactly one successor. So the sequence `n, next(n), next(next(n)),
...` is an implicit linked list, and "is n happy?" is exactly "does this list
reach the value 1, or does it contain a cycle?".

Run two pointers over the sequence:

- `slow = next(slow)` — one hop per step.
- `fast = next(next(fast))` — two hops per step.

Because the sequence is finite-valued, `fast` and `slow` **must** eventually
meet. When they do, check the value: if it is `1`, the number is happy;
otherwise they met inside a non-`1` cycle.

```python
def isHappy(n):
    def sq_sum(x):
        total = 0
        while x:
            x, d = divmod(x, 10)
            total += d * d
        return total

    slow = n
    fast = sq_sum(n)
    while fast != 1 and slow != fast:
        slow = sq_sum(slow)
        fast = sq_sum(sq_sum(fast))
    return fast == 1
```

### Why it is correct

Every trajectory of this process is eventually periodic (there are finitely
many reachable values, and each value has a unique successor). The number `1`
is a fixed point (`1 -> 1`), i.e. a self-loop of length 1. So there are only two
possible outcomes: the sequence enters the `1` self-loop, or it enters some
other cycle. Floyd guarantees the two pointers collide; the collision value is
`1` iff the sequence reached the happy fixed point.

### Step-by-step on `n = 19`

Sequence: `19 -> 82 -> 68 -> 100 -> 1 -> 1 -> ...`

| Step | slow | fast |
|------|------|------|
| start| 19   | 82   |
| 1    | 82   | 100  |
| 2    | 68   | 1    |

`fast == 1`, loop ends, return `True`.

- **Time:** O(log n) to process the digits of the starting number, then O(1)
  amortized per step within the bounded region; overall bounded by a small
  constant number of steps. Effectively O(log n).
- **Space:** O(1) — no hash set, just two integer "pointers".

## Key Insights & Edge Cases

- **`n = 1`** is happy by definition; with `fast = sq_sum(1) = 1` the loop body
  never runs and we return `True`.
- **The sequence is guaranteed to terminate or cycle** because square-sums of
  numbers rapidly shrink into the range `[1, 243]`; there is no unbounded
  growth to worry about, so both pointers stay well-defined.
- **Compare values, not references** here — the "nodes" are plain integers.
- **Careful with the initial offset:** start `slow` at `n` and `fast` at
  `sq_sum(n)` (one step ahead) so the `while slow != fast` condition does not
  trivially trigger on the first iteration.
