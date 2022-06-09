from heapq import heapify, heappop, heappush


def merge_sorted_arrays(arrays):
    pq = [(arr[0], i, 0) for i, arr in enumerate(arrays)]
    heapify(pq)

    res = []
    while pq:
        # i - index to the array
        # j - is a pointer to a latest appended item from an array -> to control no going beyond the array
        num, i, j = heappop(pq)
        res.append(num)
        if j + 1 < len(arrays[i]):
            heappush(pq, (arrays[i][j + 1], i, j + 1))
    return res


def main():
    arrays = [[2, 6, 12],
              [1, 9],
              [23, 34, 90, 2000]]
    print(merge_sorted_arrays(arrays))


if __name__ == '__main__':
    main()
