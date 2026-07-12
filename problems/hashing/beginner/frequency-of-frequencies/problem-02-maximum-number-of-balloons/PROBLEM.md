# Maximum Number of Balloons

**Difficulty:** Easy

**Source:** LeetCode 1189 — Maximum Number of Balloons

## Description

Given a string `text`, return the maximum number of times the word `"balloon"` can be formed using its characters. Each character in `text` may be used in at most one `"balloon"`.

## Examples

### Example 1

```
Input:  text = "nlaebolko"
Output: 1
```

### Example 2

```
Input:  text = "loonbalxballpoon"
Output: 2
```

## Hint

Count text's letters; for each letter of 'balloon' compute supply//demand and take the minimum (l and o are needed twice).
