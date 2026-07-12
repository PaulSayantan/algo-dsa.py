# Linear Counting: Empty Buckets

**Difficulty:** Medium

**Source:** Classic — linear counting cardinality estimator

## Description

Linear counting hashes each item into one of `m` buckets and sets that bucket's bit. The distinct-count estimate is a function of how many buckets remain empty. Implement `add(x)` with `h(x) = (x * 2654435761 + 40503) mod m`, and return the EXACT deterministic intermediate quantities: `filled_buckets()` (bits set) and `empty_buckets()` (`m` minus that). Adding a colliding item does not change either count.

## Examples

### Example 1

```
Input:  add 1,2,3,8 (m=10)
Output: filled=4, empty=6
```

**Explanation:** Four distinct buckets set.

### Example 2

```
Input:  then add 11
Output: filled=4, empty=6
```

**Explanation:** 11 collides with 1's bucket, so no change.

## Hint

Set one bit per add; filled = sum of bits; empty = m - filled. Collisions don't add new bits.
