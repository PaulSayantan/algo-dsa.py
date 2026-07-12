# Build a Queue by Middle Insertion

**Difficulty:** Easy

**Source:** Classic — repeated pushMiddle final order

## Description

Start with an empty front-middle-back queue and insert the values of `nums` one at a time using `pushMiddle`. Each `pushMiddle(v)` inserts `v` at index `len // 2` of the *current* contents (the front-middle slot). Return the final contents of the queue as a list, front first.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 4, 5]
Output: [2, 4, 5, 3, 1]
```

**Explanation:** Insert `1` -> `[1]`; `2` at idx `0` -> `[2,1]`; `3` at idx `1` -> `[2,3,1]`; `4` at idx `1` -> `[2,4,3,1]`; `5` at idx `2` -> `[2,4,5,3,1]`.

## Hint

pushMiddle drops each new value at index `len // 2` of the current queue — apply it in sequence.
