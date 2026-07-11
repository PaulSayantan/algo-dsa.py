# Solution — Maximum XOR of Two Numbers in an Array

## Brute Force

Try every pair and track the maximum XOR:

```python
best = 0
for i in range(n):
    for j in range(i + 1, n):
        best = max(best, nums[i] ^ nums[j])
```

- Time: **O(n²)**.
- Space: O(1).

With `n` up to 2·10^5 this is ~4·10^10 operations — far too slow. We need to exploit the bit
structure, which is exactly what a binary Trie does.

## Optimal Approach (Binary Trie, greedy bit-by-bit)

Treat each number as a fixed-width string of bits (say 32 or "highest bit in the data" wide),
**most-significant bit first**. Store these bit-strings in a Trie whose nodes have two children,
`0` and `1`.

To maximize `x XOR y`, process bits from the top. At each bit position, XOR contributes to the
result iff the two bits differ. Greedy rule: for the current number's bit `b`, if the child for
the **opposite** bit `1 - b` exists, take it (that bit of the XOR becomes 1); otherwise follow
`b` (that bit becomes 0). Because higher bits dominate the value, locking in a 1 as high as
possible is always optimal.

Two common structures:

1. **Insert all, then query all** — build the full Trie, then for each number greedily descend
   to find its best partner.
2. **Insert-then-query online** — insert each number and immediately query, which still finds
   every pair because XOR is symmetric.

### Reference implementation

```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if not nums:
            return 0
        HIGH = max(nums).bit_length() - 1      # index of the top meaningful bit
        if HIGH < 0:                           # all zeros
            return 0

        root: dict = {}
        # insert every number's bits, most-significant first
        for num in nums:
            node = root
            for i in range(HIGH, -1, -1):
                bit = (num >> i) & 1
                node = node.setdefault(bit, {})

        best = 0
        for num in nums:
            node, cur = root, 0
            for i in range(HIGH, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit                 # prefer the opposite bit
                if want in node:
                    cur |= (1 << i)            # this XOR bit is 1
                    node = node[want]
                else:
                    node = node[bit]           # forced to the same bit -> XOR bit 0
            best = max(best, cur)
        return best
```

**Why greedy is optimal.** The value of a binary number is dominated by its most significant
bit. If we can make the top XOR bit a 1 (by finding some stored number whose top bit differs),
any such choice beats every number that has a 0 there, regardless of lower bits. Applying this
argument recursively down the levels yields the maximum. The Trie guarantees that whenever the
opposite-bit child exists, at least one stored number actually realizes that prefix, so the
greedy choice is always achievable.

**Complexity.**
- Build: O(n · B) where `B` is the bit width (≤ 31).
- Query all: O(n · B).
- Overall **O(n · B)** time and **O(n · B)** space — effectively linear in the input.

## Key Insights & Edge Cases

- **Bits, most-significant first.** Descending from the high bit is what lets the greedy
  "take the opposite bit" rule maximize the result.
- **Prefer the opposite bit** at each node; only fall back to the same bit when the opposite
  child is absent.
- **Fixed width matters.** Pad every number to the same number of bits (use the max value's
  bit length, or a constant like 31) so equal-length bit-strings align by significance.
- **`i == j` is allowed** by the statement but `x XOR x = 0` never improves the maximum, so
  querying each number against the whole set (including itself) is safe.
- **All equal / single element:** the maximum XOR is 0; handle the all-zero case so
  `bit_length()` does not underflow.
- A `dict`-of-`dict` Trie is concise; a two-slot array (`[None, None]`) per node is faster and
  is the usual choice in performance-critical settings.
