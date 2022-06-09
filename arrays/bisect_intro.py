import bisect


def main():
    x = [1, 2, 3, 5, 7, 10, 100]
    print(x)
    print(bisect.insort_left(x, 11))
    print(x)
    print(bisect.insort_right(x, 7))
    print(x)


if __name__ == '__main__':
    main()
