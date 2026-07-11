from typing import List, Tuple

Date = Tuple[int, int, int]  # (day, month, year)


def sort_records_by_date(records: List[Date]) -> List[Date]:
    """Sort (day, month, year) records chronologically using multi-key radix sort.

    Sort by year, then month, then day (all ascending) by applying a *stable*
    counting sort one field at a time, starting from the least significant field
    (day) and finishing with the most significant field (year). Equal dates must
    retain their original relative order.

    Args:
        records: List of ``(day, month, year)`` tuples with day in 1..31, month
            in 1..12, and year in 1900..2100. Duplicates are allowed.

    Returns:
        A new list of the same records in chronological order, stable on ties.

    Example:
        >>> sort_records_by_date([(15, 3, 2021), (2, 3, 2021), (15, 1, 2021)])
        [(15, 1, 2021), (2, 3, 2021), (15, 3, 2021)]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(sort_records_by_date([(15, 3, 2021), (2, 3, 2021), (15, 1, 2021)]))
    # Expected: [(15, 1, 2021), (2, 3, 2021), (15, 3, 2021)]
    print(sort_records_by_date([(1, 1, 2020), (31, 12, 2019), (1, 1, 2019)]))
    # Expected: [(1, 1, 2019), (31, 12, 2019), (1, 1, 2020)]
    print(sort_records_by_date([(5, 6, 2000), (5, 6, 2000), (4, 6, 2000)]))
    # Expected: [(4, 6, 2000), (5, 6, 2000), (5, 6, 2000)]
