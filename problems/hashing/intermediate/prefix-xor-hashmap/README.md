# Prefix XOR + Hash Map

The XOR analogue of prefix sums. Define `prefix[i]` as the XOR of the first `i` elements; then the XOR of any subarray `(j, i]` equals `prefix[i] ^ prefix[j]`, because XOR is its own inverse. To count or measure subarrays with a target XOR `k`, note the subarray XOR equals `k` iff `prefix[j] == prefix[i] ^ k`, so a hash map over prefix values turns an O(n^2) scan into O(n). Use a **frequency** map when counting subarrays and an **earliest-index** map when maximising length. The same idea extends to per-character parity bitmasks (treat the 10-bit mask as an integer key).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Count Triplets That Can Form Two Arrays of Equal XOR](problem-01-count-equal-xor-triplets/PROBLEM.md) | Prefix XOR equality -> zero-XOR spans | Medium |
| 2 | [Count Subarrays With XOR Equal to K](problem-02-count-subarrays-xor-k/PROBLEM.md) | Prefix XOR + frequency map | Medium |
| 3 | [Number of Wonderful Substrings](problem-03-number-of-wonderful-substrings/PROBLEM.md) | Parity bitmask prefix + count array | Medium |
| 4 | [Longest Subarray With XOR Equal to K](problem-04-longest-subarray-xor-k/PROBLEM.md) | Prefix XOR + earliest-index map | Medium |
| 5 | [Count Subarrays With XOR Equal to Zero](problem-05-count-subarrays-xor-zero/PROBLEM.md) | Equal-prefix-XOR pairs | Medium |
