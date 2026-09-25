def merge_sort(items, key=lambda x: x, reverse=False):
    if len(items) <= 1:
        return items.copy()

    mid = len(items) // 2
    left = merge_sort(items[:mid], key, reverse)
    right = merge_sort(items[mid:], key, reverse)

    return _merge(left, right, key, reverse)

def _merge(left, right, key, reverse):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if reverse:
            take_left = key(left[i]) >= key(right[j])
        else:
            take_left = key(left[i]) <= key(right[j])

        if take_left:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Sort attractions by ticket price using Merge Sort.
def merge_sort_by_price(attractions, ascending=True):
    return merge_sort(attractions, key=lambda a: a.ticket_price, reverse=not ascending)