def GenerateBBSTArray(a):
    a.sort()
    if not a:
        return []

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


a = [1, 2, 3, 4, 5, 6, 7, 8]
resulting = GenerateBBSTArray(a)
print(resulting)





