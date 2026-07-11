from typing import List


def transpose_sparse(
    num_rows: int, num_cols: int, triplets: List[List[int]]
) -> List[List[int]]:
    """Transpose a sparse matrix given in triplet (row, col, value) form.

    Each input triplet [r, c, v] represents a non-zero entry. The transpose
    turns it into [c, r, v]. The result must be returned in row-major order:
    ascending by row, then ascending by column within a row.

    Args:
        num_rows: Number of rows in the original matrix (>= 1).
        num_cols: Number of columns in the original matrix (>= 1).
        triplets: Non-zero entries as [row, col, value], given in row-major
            order with distinct coordinates and non-zero values.

    Returns:
        The transposed matrix's non-zero entries as [row, col, value] lists,
        sorted in row-major order. The transposed matrix has shape
        num_cols x num_rows.

    Example:
        >>> transpose_sparse(2, 2, [[0, 1, 7], [1, 0, 9]])
        [[0, 1, 9], [1, 0, 7]]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(transpose_sparse(3, 4, [[0, 2, 5], [1, 0, 3], [2, 1, 2], [2, 3, 1]]))
    # Expected: [[0, 1, 3], [1, 2, 2], [2, 0, 5], [3, 2, 1]]

    print(transpose_sparse(2, 2, [[0, 1, 7], [1, 0, 9]]))
    # Expected: [[0, 1, 9], [1, 0, 7]]

    print(transpose_sparse(3, 3, []))
    # Expected: []
