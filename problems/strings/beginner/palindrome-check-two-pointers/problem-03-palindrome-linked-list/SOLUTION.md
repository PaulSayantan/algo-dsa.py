# Solution — Palindrome Linked List

## Brute Force

Copy every value into a Python list, then apply the standard two-pointer
palindrome check (or compare with the reversed list).

```python
def isPalindrome(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    left, right = 0, len(vals) - 1
    while left < right:
        if vals[left] != vals[right]:
            return False
        left += 1
        right -= 1
    return True
```

- **Time:** O(n) — one pass to copy, one pass to compare.
- **Space:** O(n) — the auxiliary array holds every value.

This is the simplest correct answer and is often good enough, but it fails
the O(1)-space follow-up.

## Optimal Approach (Two Pointers, O(1) Space)

A singly linked list has no backward links, so we cannot start a pointer at
the tail directly. The trick is to physically reverse the second half so both
halves can be traversed forward, then compare them like the two ends of an
array meeting in the middle.

```python
def isPalindrome(head):
    if head is None or head.next is None:
        return True

    # 1. Find the middle with slow/fast pointers.
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # `slow` is at the end of the first half.

    # 2. Reverse the second half (nodes after `slow`).
    prev, cur = None, slow.next
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    # `prev` is the head of the reversed second half.

    # 3. Compare first half (from head) with reversed second half.
    left, right = head, prev
    result = True
    while right:                     # second half is never longer
        if left.val != right.val:
            result = False
            break
        left = left.next
        right = right.next

    return result
```

### Why it is correct

- **Slow/fast** advances `fast` twice as quickly as `slow`, so when `fast`
  reaches the end, `slow` sits at the middle. Using the `fast.next and
  fast.next.next` condition leaves the middle node in the first half for odd
  lengths, so the reversed second half is never longer than the first half.
- **Reversing** the second half turns the list into two forward-traversable
  runs whose k-th elements, compared in lockstep, are exactly the pairs an
  array palindrome check would compare from the two ends.
- If every compared pair is equal until the (shorter) reversed half is
  exhausted, the list is a palindrome. A middle node in an odd-length list is
  the axis of symmetry and needs no partner, which is why we stop when
  `right` becomes `None`.

### Step-by-step on `1 -> 2 -> 2 -> 1`

1. Slow/fast stop with `slow` at the first `2` (end of first half).
2. Reverse `2 -> 1` into `1 -> 2`; `prev` -> `1`.
3. Compare head `1`==`1`, then `2`==`2`; `right` runs out -> `True`.

- **Time:** O(n) — finding the middle, reversing, and comparing are each
  linear.
- **Space:** O(1) — only a handful of pointers; the reversal is in place.

## Key Insights & Edge Cases

- **Empty or single node:** return `True` immediately; a 0- or 1-element
  sequence is a palindrome.
- **Even vs odd length:** the `fast.next and fast.next.next` loop condition
  handles both; for odd lengths the extra middle node stays in the first half
  and is harmlessly ignored during comparison.
- **Restore the list (optional):** the in-place reversal mutates the input.
  In production code you may want to reverse the second half again afterward
  to leave the list untouched.
- **Compare `.val`, not the nodes:** the palindrome property is about values,
  not object identity.
