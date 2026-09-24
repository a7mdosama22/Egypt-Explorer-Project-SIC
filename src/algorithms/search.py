"""
Search algorithms.
Owner: Member 2

Requirement: search by name must be O(log n) -> Binary Search.
Binary Search needs the list SORTED BY NAME first — sort before searching.
Do NOT use Python's built-in search shortcuts (e.g. `in`, list.index()).
"""


def binary_search_by_name(attractions_sorted_by_name, target_name):
    """
    attractions_sorted_by_name: list[Attraction], already sorted by .name (A-Z)
    target_name: str to search for (case-insensitive, exact match)

    Returns the matching Attraction, or None if not found.
    Time complexity: O(log n)
    """
    target = target_name.strip().lower()
    low, high = 0, len(attractions_sorted_by_name) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = attractions_sorted_by_name[mid].name.strip().lower()

        if mid_name == target:
            return attractions_sorted_by_name[mid]
        elif mid_name < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# TODO (Bonus): partial/substring search, or search by governorate
