# Linear Search

**Difficulty:** Easy

**Source:** Classic (GeeksforGeeks "Linear Search"; CLRS §2.1)

## Description

You are given an array of integers `nums` and an integer `target`. Return the
**index** of the first occurrence of `target` in `nums`. If `target` does not appear
in the array, return `-1`.

The array is **not** sorted, so you cannot assume any ordering of the values. Indices
are 0-based (the first element is at index 0).

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Examples

### Example 1

```
Input:  nums = [10, 50, 30, 70, 80, 20, 90, 40], target = 30
Output: 2
```

**Explanation:** Walking left to right, `nums[0]=10`, `nums[1]=50`, `nums[2]=30`
matches the target, so we return index 2.

### Example 2

```
Input:  nums = [5, 1, 4], target = 9
Output: -1
```

**Explanation:** We compare 5, then 1, then 4. None equals 9 and there are no more
elements, so the target is absent and we return -1.

### Example 3

```
Input:  nums = [7], target = 7
Output: 0
```

**Explanation:** The single element matches immediately at index 0.

## Hint

Use **Linear Search**: scan the array from index 0 onward and return the position of
the first element that equals the target.
