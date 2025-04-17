def GenerateBBSTArray(a):
    a.sort()
    if not a:
        return None

    result = []
    queue = []
    queue.append((0, len(a) - 1))

    while queue:
        left, right = queue.pop(0)
        if left > right:
            continue

        mid = (left + right) // 2
        result.append(a[mid])

        queue.append((left, mid-1))
        queue.append((mid + 1, right))

    return result







