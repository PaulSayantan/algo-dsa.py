# Solution — Sort the People

## Brute Force

Zip the two arrays into pairs, sort the pairs by height descending, then project out the names:

```python
def sortPeople(self, names, heights):
    return [name for _, name in sorted(zip(heights, names), reverse=True)]
```

- **Time:** `O(n log n)` for the built-in sort.
- **Space:** `O(n)` for the pair list.

This is the idiomatic library approach, but it hides the mechanics. The exercise here is to move the
elements ourselves with Selection Sort so the two parallel arrays stay synchronized.

## Optimal Approach (Selection Sort)

We run Selection Sort on `heights`, but selecting the **maximum** each pass (descending order). The
crucial detail: whenever we swap two heights we perform the **same swap on `names`**, so index `i`
of both arrays always refer to the same person.

```python
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n - 1):
            max_idx = i
            for j in range(i + 1, n):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            if max_idx != i:
                heights[i], heights[max_idx] = heights[max_idx], heights[i]
                names[i], names[max_idx] = names[max_idx], names[i]
        return names
```

### Why it is correct

The Selection Sort invariant guarantees that after pass `i`, positions `0 .. i` hold the `i + 1`
tallest people in descending order. Because we mirror **every** height swap with the matching name
swap, the association between a height and its name is never broken — `names[k]` always describes the
person whose height is `heights[k]`. When the heights end up in descending order, `names` is
therefore in the desired order.

Since all heights are distinct, the strict `>` comparison produces a unique, unambiguous ordering —
there are no ties to worry about.

### Step-by-step on `names=["Mary","John","Emma"]`, `heights=[180,165,170]`

| i | max in suffix | swap indices | heights          | names                      |
|---|---------------|--------------|------------------|----------------------------|
| 0 | `180` @0      | none         | `[180,165,170]`  | `["Mary","John","Emma"]`   |
| 1 | `170` @2      | swap 1,2     | `[180,170,165]`  | `["Mary","Emma","John"]`   |

Result: `["Mary", "Emma", "John"]`.

### Complexity

- **Time:** `O(n²)` — the double loop performs `n(n-1)/2` height comparisons.
- **Space:** `O(1)` extra — everything is swapped in place within the two given arrays.

## Key Insights & Edge Cases

- **Two arrays, one swap decision:** the sort key lives in `heights`, but each swap must touch both
  arrays. Forgetting to swap `names` (or swapping it on a different condition) desynchronizes the
  data — a classic bug when sorting parallel arrays.
- **Descending order:** the only change from the ascending template is `>` instead of `<` (selecting
  the max rather than the min). Everything else is identical.
- **Distinct heights:** the problem promises distinct heights, so there is exactly one valid answer
  and stability is irrelevant here.
- **Single person:** `range(n - 1)` is empty, so `names` is returned unchanged.
- **Duplicate names:** perfectly fine — names are never used as the comparison key, only heights are.
- **Alternative:** rather than swapping two arrays, you can Selection-Sort an index array
  `order = list(range(n))` by `heights[order[j]]` and then map `names` through it; this avoids
  mutating the inputs.
