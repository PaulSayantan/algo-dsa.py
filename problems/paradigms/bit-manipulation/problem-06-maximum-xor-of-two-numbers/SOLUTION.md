# Maximum XOR of Two Numbers — Solution

## Brute Force

Try every pair and track the maximum XOR.

```python
def findMaximumXOR(self, nums):
    best = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            best = max(best, nums[i] ^ nums[j])
    return best
```

- **Time:** O(n^2) — too slow for n up to 2 * 10^5.
- **Space:** O(1).

## Optimal Approach (Bit Manipulation)

Numbers fit in about **L = 31** bits (since `nums[i] < 2^31`). We build the answer
**greedily from the most significant bit to the least**. At each step we optimistically
assume the next answer bit can be `1` and test whether some pair of numbers can actually
realize that prefix.

### Prefix / hash-set method

Key XOR identity: `a ^ b = c` **iff** `a ^ c = b`.

For the current `bit`, form `candidate = answer | (1 << bit)` (the best prefix if this
bit can be 1). Take the set of high-bit **prefixes** `p = num >> bit` for all numbers.
The candidate is achievable iff there exist two prefixes `p1, p2` with `p1 ^ p2 ==
candidate`. By the identity, that means for some prefix `p` in the set, `candidate ^ p`
is also in the set. If so, keep the bit; otherwise leave it 0 and move on.

```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer = 0
        L = max(nums).bit_length()          # highest meaningful bit
        for bit in range(L - 1, -1, -1):
            answer <<= 1
            candidate = answer | 1          # try to make this bit a 1
            prefixes = {num >> bit for num in nums}
            found = any((candidate ^ p) in prefixes for p in prefixes)
            if found:
                answer = candidate
            # else answer already shifted with trailing 0
        return answer
```

- **Time:** O(L * n) = O(31 n) = O(n) — for each of ~31 bits we build a set and scan it.
- **Space:** O(n) for the prefix set.

### Binary-trie method (equivalent, classic)

Insert each number's bits (MSB first) into a binary trie. Then for each number, walk the
trie greedily choosing the **opposite** bit at every level to maximize XOR; track the
best value. Also O(L * n) time and O(L * n) space. The prefix/hash method above is
simpler to code and has the same asymptotics.

### Step-by-step on `[3, 10, 5, 25, 2, 8]`

Binary (5-bit): 3=`00011`, 10=`01010`, 5=`00101`, 25=`11001`, 2=`00010`, 8=`01000`.
The answer is `5 ^ 25 = 00101 ^ 11001 = 11100 = 28`.

Greedy from the top bit:

| bit | candidate prefix (binary) | realizable? | answer so far |
|---|---|---|---|
| 4 | `1` | yes (25 has it, 0 has it) | `1` |
| 3 | `11` | yes (25`11`, 5`00` -> `11`) | `11` |
| 2 | `111` | yes (25`110`, 5`001` -> `111`) | `111` |
| 1 | `1110` | yes (25`1100`, 5`0010` -> `1110`) | `1110` |
| 0 | `11100` | yes (25`11001`, 5`00101` -> `11100`) | `11100` |

Final `11100` = **28**.

## Key Insights & Edge Cases

- **Greedy is safe:** a higher bit outweighs all lower bits combined, so securing a `1`
  at the most significant achievable position can never be worse than leaving it `0`.
- **XOR identity powers the test:** checking `candidate ^ p in prefixes` turns "does some
  pair produce this prefix?" into O(1) set lookups.
- **Single element** (`[0]` or `[7]`): no distinct pair sets a high bit; the greedy loop
  finds nothing realizable and returns 0 (`x ^ x = 0`).
- **Determining L:** using `max(nums).bit_length()` avoids wasting iterations on leading
  zero bits; a fixed `L = 31` (or 32) also works.
- **Duplicates:** harmless — identical numbers XOR to 0 and never beat a genuine pair.
- **All zeros:** answer is 0, handled naturally.
