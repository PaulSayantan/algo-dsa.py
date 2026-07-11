# Insertion Sort List

**Difficulty:** Medium

*Source: LeetCode 147 (Insertion Sort List).*

## Description

Given the `head` of a singly linked list, sort the list using **insertion sort** and return
the sorted list's head.

The classic insertion sort algorithm works as follows:

1. Insertion sort iterates, consuming one input element each repetition and growing a sorted
   output list.
2. At each iteration, it removes one element from the input data, finds the location it
   belongs within the sorted list, and inserts it there.
3. It repeats until no input elements remain.

You should perform the insertion on the list nodes themselves (rewiring `next` pointers), not
by copying values into an array and sorting that. A **dummy head** node makes it easy to
insert before the current first element.

## Constraints

- The number of nodes in the list is in the range `[1, 5000]`.
- `-5000 <= Node.val <= 5000`

## Examples

**Example 1**

```
Input:  head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]
```
Explanation: Take nodes one at a time into a growing sorted list: `[4]` → `[2,4]` →
`[1,2,4]` → `[1,2,3,4]`.

**Example 2**

```
Input:  head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]
```
Explanation: `-1` starts the sorted list; `5` appends; `3` inserts before `5`; `4` inserts
between `3` and `5`; `0` inserts between `-1` and `3`.

**Example 3**

```
Input:  head = [1]
Output: [1]
```
Explanation: A single node is already sorted, so it is returned unchanged.

## Hint

Use **Insertion Sort** adapted for a linked list: keep a separate sorted list behind a dummy
head. For each node in the input, scan the sorted list from the dummy to find the first node
whose next value is greater than the current value, then splice the current node in there.
