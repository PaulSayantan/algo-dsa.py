# Students Unable to Eat Lunch — Solution

## Optimal Approach

Model the line as a FIFO `deque` and the sandwiches as a pointer into the stack. Serve the front student when their preference matches the top sandwich; otherwise send them to the back. Track how many students in a row have been rotated without a take — once that count reaches the current line length, a full lap has passed with no possible taker, so everyone remaining is stuck.

### Reference implementation

```python
class Solution:
    def countStudents(self, students, sandwiches):
        q = deque(students)
        top = 0  # index of the sandwich on top of the stack
        stuck = 0  # students rotated in a row without a take
        while q and stuck < len(q):
            if q[0] == sandwiches[top]:
                q.popleft()
                top += 1
                stuck = 0
            else:
                q.append(q.popleft())
                stuck += 1
        return len(q)
```
