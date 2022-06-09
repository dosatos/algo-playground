from typing import List

# row - vendor, column - cost
# how to allocate to get the least cost
matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4],
]


def _get_least_(job_index: int, vendor_availability: int) -> int:
    pass


def _get_lowest_combination(matrix: List[List[int]]) -> List[int]:
    pass
    # 0, 1 -> 1 00, 01
    # 2, 3 -> 2, 10, 11
    # 4, 5 -> 3, 100, 101
    # 6, 7 -> 3, 110, 111


def _bitmask(number: int) -> str:
    return bin(number)[2:].zfill(number.bit_length())


def _bitmask_array(number: int) -> List[int]:
    return [int(i) for i in bin(number)[2:].zfill(number.bit_length())]


def main():
    number = 0
    # To check if j-th bit is set, we use 1 << k - 1
    print(_bitmask_array(number))
    print(_bitmask_array(1 << 2))
    print(_bitmask_array(number & 1 << 2))

    if bin(1 << 2) == bin(number & 1 << 2):
        print(f"If bit is set number: {number} has bit at index: {2}")

    print(1 << 2)  # '100' == 4

    print(bin(1 << 3))


if __name__ == '__main__':
    main()
