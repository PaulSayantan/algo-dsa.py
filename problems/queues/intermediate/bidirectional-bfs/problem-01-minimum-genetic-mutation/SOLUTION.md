# Minimum Genetic Mutation — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        if startGene == endGene:
            return 0
        front, back = {startGene}, {endGene}
        steps = 0
        chars = 'ACGT'
        while front and back:
            if len(front) > len(back):
                front, back = back, front
            steps += 1
            nxt = set()
            for gene in front:
                for i in range(len(gene)):
                    for ch in chars:
                        cand = gene[:i] + ch + gene[i + 1:]
                        if cand in back:
                            return steps
                        if cand in bank_set:
                            nxt.add(cand)
                            bank_set.discard(cand)
            front = nxt
        return -1
```
