# Solution — Count Distinct Bracelets

## Brute Force

For each string, build the full set of "equivalent" strings — all rotations of `s` and
all rotations of `reverse(s)` — and merge strings that share any member.

```python
def count_brute(words):
    def equiv_set(s):
        rots = {s[i:] + s[:i] for i in range(len(s))}
        r = s[::-1]
        rots |= {r[i:] + r[:i] for i in range(len(r))}
        return rots
    reps = []
    for w in words:
        es = equiv_set(w)
        if not any(rep in es for rep in reps):
            reps.append(w)
    return len(reps)
```

- Building the equivalence set of one length-`L` word is `O(L^2)`, and comparing against
  all representatives is worse.
- **Time:** `O(N * L^2)` or more. **Space:** `O(L)` per equivalence set.

Infeasible when total length nears `10^6`.

## Optimal Approach — Booth's Canonicalization Under Rotation + Reflection

A bracelet is an equivalence class under the **dihedral** group action (rotations
combined with one reflection). We build a canonical name that is invariant under both:

```
canonical(s) = min( smallest_rotation(s), smallest_rotation(reverse(s)) )
```

- `smallest_rotation(s)` is invariant under rotation (it collapses all rotations of `s`
  to one string) — that handles the rotational symmetry.
- Taking the smaller of that and `smallest_rotation(reverse(s))` additionally makes the
  name invariant under reflection: reversing `s` and then applying the same two-way min
  yields the identical value, because the two arguments simply swap.

Then count distinct canonical strings.

```python
def least_rotation(s: str) -> int:
    n = len(s)
    ss = s + s
    f = [-1] * len(ss)
    k = 0
    for j in range(1, len(ss)):
        sj = ss[j]
        i = f[j - k - 1]
        while i != -1 and sj != ss[k + i + 1]:
            if sj < ss[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != ss[k + i + 1]:
            if sj < ss[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k % n


def smallest_rotation(s: str) -> str:
    if not s:
        return s
    k = least_rotation(s)
    return s[k:] + s[:k]


def canonical_bracelet(s: str) -> str:
    a = smallest_rotation(s)
    b = smallest_rotation(s[::-1])
    return a if a <= b else b


def count_distinct_bracelets(words):
    return len({canonical_bracelet(w) for w in words})
```

### Why it is correct

- **Rotational invariance:** `smallest_rotation` maps every rotation of a string to the
  same value (its minimum rotation), so the rotation orbit collapses to one name.
- **Reflection invariance:** for any `s`, let `A = smallest_rotation(s)` and
  `B = smallest_rotation(reverse(s))`. For the reversed string `reverse(s)`, the two
  quantities are `smallest_rotation(reverse(s)) = B` and
  `smallest_rotation(reverse(reverse(s))) = smallest_rotation(s) = A`. So the pair
  `{A, B}` is identical for `s` and `reverse(s)`, and `min(A, B)` agrees. Rotations of
  `s` or of `reverse(s)` also don't change `A` or `B`. Hence every member of a bracelet
  gets the same canonical name.
- **Distinct lengths** cannot collide since reversal and rotation preserve length.
- Therefore counting distinct canonical names counts distinct bracelets.

- **Time:** `O(total length)` — two Booth's runs and a reversal per word, all linear;
  hashing the canonical strings is linear in total length.
- **Space:** `O(total length)`.

## Key Insights & Edge Cases

- **Necklace vs bracelet:** a necklace uses rotation only (`canonical = smallest_rotation`);
  a bracelet adds the reflection via the extra `min` with the reversed string. Example 1
  gives 3 necklaces but 2 bracelets — the reflection is exactly what merges `"abcd"` and
  `"dcba"`.
- **Palindromes** (`"xyyx"`, `"aba"`): the string equals its reverse, so both arguments to
  `min` are equal; canonicalization still works, and palindromic strings simply pair with
  themselves under reflection.
- **`<=` vs `<` in the final min:** either is fine since when `a == b` the value is the
  same string; pick one consistently.
- **Careful with reversal cost:** `s[::-1]` is `O(L)`; doing it once per word keeps the
  total linear.
- **Generalization:** this "canonical form under a symmetry group" pattern extends to any
  dihedral-symmetry counting (rotationally + reflectively symmetric tilings, cyclic
  sequence deduplication that must treat a strand and its reverse as equal, etc.).
