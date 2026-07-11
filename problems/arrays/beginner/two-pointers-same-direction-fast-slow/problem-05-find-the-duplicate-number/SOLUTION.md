# Find the Duplicate Number — Solution

## Brute Force

Use a hash set: scan the array and return the first value you see twice.

```python
def findDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
```

- **Time:** O(n).
- **Space:** O(n) for the set — violates the constant-space requirement.

(Sorting the array would be O(n log n) time and **modifies** the input, which the
problem also forbids.)

## Optimal Approach (Fast-Slow / Floyd's Cycle Detection)

**Model the array as a linked list of indices.** From index `i`, follow the edge
to `nums[i]`. Because every value lies in `[1, n]`, every edge lands on a valid
index, and starting at index `0` we can walk forever: `i -> nums[i] -> ...`.

Since two different indices share the same value (the duplicate), two edges point
into the same node — so this "functional graph" **must contain a cycle**, and the
node where the cycle begins is exactly the duplicated value. Finding a cycle's
entrance with O(1) space is precisely Floyd's tortoise-and-hare algorithm.

### Phase 1 — find a meeting point inside the cycle

Advance `slow` by one hop and `fast` by two hops until they collide.

```python
slow = fast = nums[0]
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break
```

### Phase 2 — find the cycle entrance (the duplicate)

Reset one pointer to the start. Move both one step at a time; they meet at the
entrance.

```python
slow2 = nums[0]
while slow2 != slow:
    slow2 = nums[slow2]
    slow = nums[slow]
return slow
```

Full solution:

```python
def findDuplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = nums[0]
    while slow2 != slow:
        slow2 = nums[slow2]
        slow = nums[slow]
    return slow
```

### Why it is correct

- **A cycle must exist.** The map `i -> nums[i]` sends `n + 1` index-nodes into
  values within `[1, n]`; index `0` is never a target of the walk once we leave
  it because all values are `>= 1`, so the path from `0` eventually revisits a
  node. The pigeonhole duplicate is what merges two edges into a single cycle
  entry.
- **Phase 1 meets inside the cycle.** With `fast` moving twice as fast, the gap
  shrinks by one each step once both are in the cycle, so they collide.
- **Phase 2 locates the entrance.** Let `mu` be the distance from `nums[0]` to
  the cycle entrance and `lambda` the cycle length. At the meeting point the
  slow pointer has traveled a distance that is a multiple of `lambda` past the
  entrance; walking `mu` more steps from both `nums[0]` and the meeting point
  lands both at the entrance simultaneously. That entrance node's value is the
  repeated number.
- **Constraints satisfied:** only a few integer variables are used (O(1) space)
  and `nums` is only **read**, never written.

### Complexity

- **Time:** O(n) — each phase is linear in the cycle/tail lengths, bounded by
  `n`.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Why start at `nums[0]` (or index `0`).** Index `0` is a safe starting node
  that is guaranteed not to sit *on* the cycle as an entrance target, because no
  value equals `0`; this keeps the tail-then-cycle structure that Floyd needs.
- **Duplicate appearing many times** (`[2, 2, 2, 2, 2]`): still a single cycle
  entrance; the algorithm returns `2`.
- **Do not confuse with cycle *detection* on a normal linked list** — here the
  "next" pointer is `nums[value]`, so the meeting value, not a node object, is
  the answer.
- **Alternative:** binary search on the value range using a count of elements
  `<= mid` is O(n log n) time / O(1) space and also non-destructive, but Floyd's
  is the optimal O(n)-time constant-space solution.
- **Must not sort or use a set** if you want to meet the stated constraints;
  those break either the "don't modify" or "constant space" rule.
