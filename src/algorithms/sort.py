"""
Sorting algorithms.
Owner: Member 2

Requirement: sort by Ticket Price (ascending/descending), implemented
manually. Do NOT use Python's built-in sorted() / list.sort().
"""


def merge_sort_by_price(attractions, ascending=True):
    """
    attractions: list[Attraction]
    Returns a NEW sorted list (does not mutate the input).
    """
    if len(attractions) <= 1:
        return attractions[:]

    mid = len(attractions) // 2
    left = merge_sort_by_price(attractions[:mid], ascending)
    right = merge_sort_by_price(attractions[mid:], ascending)

    return _merge(left, right, ascending)


def _merge(left, right, ascending):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        take_left = (
            left[i].ticket_price <= right[j].ticket_price
            if ascending
            else left[i].ticket_price >= right[j].ticket_price
        )
        if take_left:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_by_name(attractions):
    """
    Helper needed before binary_search_by_name() can run.
    Simple manual sort by name (reuses the same merge pattern).
    """
    if len(attractions) <= 1:
        return attractions[:]

    mid = len(attractions) // 2
    left = sort_by_name(attractions[:mid])
    right = sort_by_name(attractions[mid:])

    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i].name.lower() <= right[j].name.lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# TODO (Bonus): sort by rating, governorate, or estimated_visit_time
