# Round-Robin Load Balancer — Solution

## Optimal Approach

Store the servers in a list and a cursor index `idx`. `next()` returns
`servers[idx]` and advances `idx = (idx + 1) % len`. The subtle part is
`removeServer`: after popping the server at position `pos`, if `pos < idx` the
cursor must shift left by one so it still points at the same upcoming server;
then re-mod `idx` against the new length so the cycle wraps correctly (and reset
to 0 when the list becomes empty).

### Reference implementation

```python
class RoundRobinBalancer:
    def __init__(self):
        self.servers = []
        self.idx = 0

    def addServer(self, server_id):
        self.servers.append(server_id)

    def removeServer(self, server_id):
        if server_id not in self.servers:
            return
        pos = self.servers.index(server_id)
        self.servers.pop(pos)
        if not self.servers:
            self.idx = 0
            return
        if pos < self.idx:
            self.idx -= 1
        self.idx %= len(self.servers)

    def next(self):
        if not self.servers:
            return -1
        sid = self.servers[self.idx]
        self.idx = (self.idx + 1) % len(self.servers)
        return sid
```
