# Sort List

**Difficulty:** Medium

**Source:** LeetCode 148 — Sort List

## Description

Given the `head` of a singly linked list, return the list after sorting it in
**ascending order**.

**Follow-up:** Can you sort the linked list in `O(n log n)` time and `O(1)`
memory (i.e. constant space, not counting recursion)?

A linked list has no random access, so array-oriented sorts are awkward. Merge
sort, by contrast, only ever walks the list sequentially and splices nodes —
which makes it the textbook choice for sorting linked lists.

## Constraints

- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Examples

### Example 1

```
Input:  head = [4,2,1,3]
Output: [1,2,3,4]
```

**Explanation:** The nodes with values `4,2,1,3` are relinked so that traversing
from the new head visits `1 -> 2 -> 3 -> 4`.

### Example 2

```
Input:  head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Explanation:** The list is reordered into ascending order, including the
negative value `-1` at the front.

### Example 3

```
Input:  head = []
Output: []
```

**Explanation:** An empty list is already sorted; return it unchanged.

## Hint

Use **Merge Sort**. Split the list into two halves with the slow/fast pointer
technique, recursively sort each half, then merge two sorted lists by splicing
nodes. No auxiliary array is needed.
