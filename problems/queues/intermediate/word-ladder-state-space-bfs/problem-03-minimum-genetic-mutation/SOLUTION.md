# Minimum Genetic Mutation — Solution

## Optimal Approach

This is Word Ladder with a 4-letter alphabet (`ACGT`) and a fixed length of 8. Each
gene is a state; its neighbors flip one position to a different base, and only genes
present in `bank` are legal to step onto. BFS from `startGene` and return the level
at which `endGene` is dequeued. If `endGene` is not in the bank there is no valid
path, so a short-circuit is optional but the BFS handles it naturally.

### Reference implementation

```python
class Solution:
    def minMutation(self, startGene, endGene, bank):
        bankset = set(bank)
        if endGene not in bankset:
            return -1
        q = deque([(startGene, 0)])
        seen = {startGene}
        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                for ch in "ACGT":
                    nxt = gene[:i] + ch + gene[i + 1:]
                    if nxt in bankset and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
        return -1
```
