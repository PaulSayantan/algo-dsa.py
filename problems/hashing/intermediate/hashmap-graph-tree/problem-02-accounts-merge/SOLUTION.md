# Accounts Merge — Solution

## Optimal Approach

Union emails within each account; sorted output makes it canonical.

### Reference implementation

```python
class Solution:
    def accountsMerge(self, accounts):
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        owner = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                owner[email] = name
                union(acc[1], email)
        groups = defaultdict(list)
        for email in owner:
            groups[find(email)].append(email)
        result = []
        for root, emails in groups.items():
            result.append([owner[root]] + sorted(emails))
        return sorted(result)
```

### Complexity

Near-linear in total emails.

## Key Insights & Edge Cases

The two John accounts merge via b@x.com; Mary stays separate.
