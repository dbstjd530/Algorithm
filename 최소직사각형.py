def solution(sizes):
    newSize = []
    for size in sizes:
        first = size[0]
        second = size[1]

        if second > first:
            newSize.append([second, first])
        else:
            newSize.append(size)

    maxWidth = max(list(zip(*newSize))[0])
    maxLength = max(list(zip(*newSize))[1])

    answer = maxWidth * maxLength
    return answer