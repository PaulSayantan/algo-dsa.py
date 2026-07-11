# Solution — Accounts Merge

## Brute Force

Build a graph where every email is a node, and add an edge between the first email of an account
and each of its other emails (so all emails in one account are connected). Then run BFS/DFS from
each unvisited email to collect a full connected component, sort it, and prepend the name.

```python
def accountsMerge(accounts):
    graph = defaultdict(set)
    email_to_name = {}
    for name, *emails in accounts:
        for e in emails:
            email_to_name[e] = name
            graph[emails[0]].add(e)
            graph[e].add(emails[0])
    seen, out = set(), []
    for start in graph:
        if start in seen:
            continue
        stack, comp = [start], []
        seen.add(start)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        out.append([email_to_name[start]] + sorted(comp))
    return out
```

- **Time:** `O(N · K · log(N · K))` dominated by the sorting, where `N` is the number of accounts
  and `K` the max emails per account; graph traversal itself is `O(N · K)`.
- **Space:** `O(N · K)` for the adjacency structure.

This works and is a common accepted answer. The DSU version below replaces the explicit graph +
traversal with two hash maps and is the idiomatic "grouping" solution.

## Optimal Approach (Union-Find / Disjoint Set Union)

Every distinct email is an element. Within a single account, union its first email with each of
the others — this transitively connects all emails in that account. Because accounts that share
an email will share a DSU root, the final connected components are exactly the people.

**Steps:**

1. Assign each distinct email an integer id (or use the email string as the key). Record
   `email -> owner name` while scanning (all emails in an account map to that account's name).
2. For each account, `union(first_email, other_email)` for every other email.
3. Bucket every email under `find(email)`. Each bucket is one person.
4. For each bucket, sort the emails and prepend the owner's name.

```python
class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU()
        email_to_name = {}
        for name, *emails in accounts:
            for e in emails:
                dsu.add(e)
                email_to_name[e] = name
                dsu.union(emails[0], e)

        groups = {}
        for e in email_to_name:
            root = dsu.find(e)
            groups.setdefault(root, []).append(e)

        return [[email_to_name[root]] + sorted(mails)
                for root, mails in groups.items()]
```

**Why it is correct.** Union is transitive: if account A and account B both contain email `x`,
then A's emails are all unioned with `x` and B's emails are all unioned with `x`, so every email
across A and B shares the root of `x`. Two accounts with no common email never get connected, so
they remain distinct components. Names are consistent because all accounts sharing emails have
the same person's name (guaranteed by the problem).

- **Time:** `O(N · K · α + total_emails · log(max_group))` — near-linear unions plus the final
  per-group sort. `N` accounts, `K` emails each.
- **Space:** `O(N · K)` for the DSU maps and buckets.

## Key Insights & Edge Cases

- **Union emails, not account indices.** Emails are the shared identity; a person may be spread
  across several account rows. Keying the DSU on the email string (or a mapped id) is what makes
  the merge work.
- Use `email_to_name` keyed on the email; any email in a group yields the correct name, so
  reading `email_to_name[root]` is sufficient.
- Sort each merged email list to satisfy the output format; the outer account order is free.
- An account can contain duplicate emails or a single email — `add` + self-consistent `union`
  handle both without special cases.
- Iterating `email_to_name` (distinct emails) rather than re-iterating accounts avoids adding the
  same email to a group twice.
