from algorithms.sort import merge_sort

# Sort attractions alphabetically by name.
def sort_by_name(attractions):
    return merge_sort(attractions, key=lambda a: a.name.lower())


# Binary Search for an attraction by name.
def binary_search(attractions, target):
    attractions = sort_by_name(attractions)

    left = 0
    right = len(attractions) - 1
    target = target.strip().lower()

    while left <= right:
        mid = (left + right) // 2
        current_name = attractions[mid].name.lower()

        if current_name == target:
            return attractions[mid]

        if current_name < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

#search by additional attributes (Governorate, Rating).
def _binary_search_range(sorted_items, target, key):
    left, right = 0, len(sorted_items) - 1
    pivot = -1

    while left <= right:
        mid = (left + right) // 2
        value = key(sorted_items[mid])

        if value == target:
            pivot = mid
            break
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    if pivot == -1:
        return []

    start = end = pivot
    while start > 0 and key(sorted_items[start - 1]) == target:
        start -= 1
    while end < len(sorted_items) - 1 and key(sorted_items[end + 1]) == target:
        end += 1

    return sorted_items[start:end + 1]


def _binary_search_lower_bound(sorted_items, min_value, key):
    left, right = 0, len(sorted_items)

    while left < right:
        mid = (left + right) // 2
        if key(sorted_items[mid]) < min_value:
            left = mid + 1
        else:
            right = mid

    return sorted_items[left:]

# Return every attraction located in the given governorate
def search_by_governorate(attractions, governorate):
    sorted_attractions = merge_sort(attractions, key=lambda a: a.governorate.lower())
    target = governorate.strip().lower()
    return _binary_search_range(sorted_attractions, target, key=lambda a: a.governorate.lower())

# Return every attraction with rating >= min_rating
def search_by_min_rating(attractions, min_rating):
    sorted_attractions = merge_sort(attractions, key=lambda a: a.rating)
    return _binary_search_lower_bound(sorted_attractions, min_rating, key=lambda a: a.rating)