# Solution — Find the Duplicate Number

## Brute Force

Use a hash set: scan the array and return the first value already seen.

```python
def findDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
```

- **Time:** O(n).
- **Space:** O(n) for the set.

A sorting variant is O(n log n) time / O(1) extra space but modifies (or copies)
the array. Both violate at least one of the problem's constraints (no
modification **and** O(1) space).

## Optimal Approach — Floyd's Cycle Detection (Tortoise & Hare)

### Model the array as a linked list

Interpret each index `i` as a node whose single outgoing edge points to index
`nums[i]`. Since every value lies in `[1, n]`, no edge points to index `0`, so
index `0` is a pure starting node that nothing points back to. Because there are
`n + 1` indices but values only range over `[1, n]`, by the pigeonhole
principle two indices share the same value — meaning two edges point into the
same node — which forces a **cycle**, and the node where the cycle begins is the
duplicated value.

### Phase 1 — find a meeting point inside the cycle

```python
slow = nums[0]
fast = nums[nums[0]]
while slow != fast:
    slow = nums[slow]
    fast = nums[nums[fast]]
```

### Phase 2 — find the cycle entrance (the duplicate)

Reset one pointer to the start index `0`. Advance both one step at a time; they
meet exactly at the cycle's entry node.

```python
slow = 0
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
return slow  # == the duplicated value
```

### Why phase 2 lands on the entrance

Let the distance from the start to the cycle entrance be `x`, the distance from
the entrance to the first meeting point be `y`, and the cycle length be `C`.
When slow and fast meet in phase 1, slow has traveled `x + y` and fast has
traveled `2(x + y)`; since fast is exactly some whole number of loops ahead,
`2(x + y) - (x + y) = x + y` is a multiple of `C`. Hence `x + y = kC`, so
`x = kC - y`. Now place one pointer at the start and leave the other at the
meeting point. After `x` steps, the start pointer reaches the entrance, while
the other advances `x = kC - y` steps from the meeting point — which is `y`
before the entrance plus `k` full loops — landing it exactly on the entrance
too. They coincide at the entry node.

### Step-by-step on `nums = [1, 3, 4, 2, 2]`

Edges (index `i` -> `nums[i]`): `0->1, 1->3, 2->4, 3->2, 4->2`. Following from
index 0: `0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> ...`, so the cycle is `2 -> 4 -> 2`
and its **entrance is value `2`** (the duplicate).

Phase 1 — start `slow = nums[0] = 1`, `fast = nums[nums[0]] = 3`, then step:

| Step | slow            | fast                         |
|------|-----------------|------------------------------|
| init | 1               | 3                            |
| 1    | nums[1]=3       | nums[nums[3]]=nums[2]=4       |
| 2    | nums[3]=2       | nums[nums[4]]=nums[2]=4       |
| 3    | nums[2]=4       | nums[nums[4]]=nums[2]=4       |

`slow == fast == 4`: they meet at value `4`.

Phase 2 — reset `slow = 0`, keep `fast = 4`, advance both one step:

| Step | slow      | fast      |
|------|-----------|-----------|
| init | 0         | 4         |
| 1    | nums[0]=1 | nums[4]=2 |
| 2    | nums[1]=3 | nums[2]=4 |
| 3    | nums[3]=2 | nums[4]=2 |

`slow == fast == 2`: the cycle entrance is `2`, so the duplicated number is
**2**, matching the expected output.

- **Time:** O(n) — each phase is a linear number of pointer hops.
- **Space:** O(1) — only integer pointers; the array is never modified.

## Key Insights & Edge Cases

- **Index 0 is never a cycle node**, because values are in `[1, n]` and thus no
  edge targets index 0. Starting the tortoise/hare from index 0 guarantees the
  cycle lies "downstream," which is what makes phase 2's entrance-finding valid.
- **Duplicates ≥ 2 occurrences:** the algorithm works whether the repeated value
  appears exactly twice or many times (e.g. `[2,2,2,2,2]`), because at least two
  edges into the same node is all that is needed to create the cycle.
- **Do not use `nums[nums[0]]` semantics loosely.** Initialize `slow = nums[0]`
  and `fast = nums[nums[0]]` (or start both at index 0 and take one/two steps
  before the first comparison) so the `while slow != fast` loop does not exit
  before it begins.
- **Read-only friendly:** unlike the "negate visited indices" trick, this never
  writes to `nums`, satisfying the immutability constraint.
