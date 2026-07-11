# Compute the Burrows–Wheeler Transform

**Difficulty:** Easy

**Source:** Rosalind "Construct the Burrows-Wheeler Transform of a String" (BA9I); classic bioinformatics / stringology exercise.

## Description

You are given a string `text` that ends with a unique sentinel character `$`. The
sentinel is assumed to be lexicographically **smaller** than every other character in
the string (this makes the transform well-defined and reversible).

The **Burrows–Wheeler Transform** of `text` is produced as follows:

1. Form all `n` cyclic rotations of `text` (where `n = len(text)`). The `i`-th rotation
   is `text[i:] + text[:i]`.
2. Sort these `n` rotations lexicographically. Arranged as rows, they form the
   **Burrows–Wheeler Matrix**.
3. The BWT is the **last column** of this matrix — i.e. the concatenation of the final
   character of every sorted rotation, read top to bottom.

Return this last column as a string of length `n`.

Because `$` is unique and smallest, the sorted rotations are in one-to-one
correspondence with the sorted suffixes of `text`, so the BWT is also `text[SA[i]-1]`
for each entry of the suffix array `SA` (with index `-1` wrapping to the sentinel).

## Constraints

- `1 <= len(text) <= 10^5`
- `text` consists of uppercase/lowercase letters and exactly one `$` character, which
  appears at the **end** of `text` and is the lexicographically smallest character.
- The output has exactly `len(text)` characters.

## Examples

### Example 1

```
Input:  text = "banana$"
Output: "annb$aa"
```

Explanation: The 7 cyclic rotations sorted lexicographically are

```
$banana   -> a
a$banan   -> n
ana$ban   -> n
anana$b   -> b
banana$   -> $
na$bana   -> a
nana$ba   -> a
```

Reading the last character of each sorted row top-to-bottom gives `a n n b $ a a` = `"annb$aa"`.

### Example 2

```
Input:  text = "abracadabra$"
Output: "ard$rcaaaabb"
```

Explanation: Sorting all 12 rotations and taking the final character of each row
yields `"ard$rcaaaabb"`. Notice how the equal `a`s and `b`s get clustered toward the
end — this clustering is exactly what downstream compressors exploit.

### Example 3

```
Input:  text = "AA$"
Output: "AA$"
```

Explanation: The sorted rotations are `$AA`, `A$A`, `AA$`; their last characters are
`A`, `A`, `$`, giving `"AA$"`.

## Hint

Use the **Burrows–Wheeler Transform (BWT)**: sorting the cyclic rotations is equivalent
to sorting the suffixes, so you can build the answer either by sorting rotations
directly or, more efficiently, from a suffix array where `L[i] = text[SA[i] - 1]`.
