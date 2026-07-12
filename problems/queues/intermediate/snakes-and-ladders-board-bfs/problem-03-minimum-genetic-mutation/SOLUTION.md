# Minimum Genetic Mutation — Solution

## Optimal Approach

The gene strings form a graph: two genes are adjacent when they differ in exactly
one position AND both are legal (in the bank). BFS from `startGene` finds the
minimum number of mutations to reach `endGene`. If `endGene` is not even in the
bank, no path exists. At each position try substituting each of the other three
bases and enqueue any resulting gene that is in the bank and unseen.

### Reference implementation

```python
class Solution:
    def minMutation(self, startGene, endGene, bank):
        bankset = set(bank)
        if endGene not in bankset:
            return -1
        if startGene == endGene:
            return 0
        genes = "ACGT"
        seen = {startGene}
        q = deque([(startGene, 0)])
        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                for ch in genes:
                    if ch == gene[i]:
                        continue
                    nxt = gene[:i] + ch + gene[i + 1:]
                    if nxt in bankset and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
        return -1
```
