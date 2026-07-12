# Jump Hash Bucket Distribution

**Difficulty:** Medium

**Source:** Classic — jump consistent hashing (distribution)

## Description

Using jump consistent hashing, map several keys into a fixed number of buckets and report each key's bucket. Implement `jumpConsistentHash(key, num_buckets)` (as above) and `buckets(keys, num_buckets)` returning the list of buckets, one per key in order. The result is deterministic and each entry lies in `[0, num_buckets)`.

## Hint

Just apply jumpConsistentHash to every key and collect the results in order.
