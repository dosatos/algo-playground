def _to_bitmask_array(number: int, length: int = 8):
    stringified_subset = _to_subset_as_str(number, length)
    return [
        int(i)
        for i in list(stringified_subset)
    ]


def _to_subset_as_str(number: int, length: int = 8):
    return bin(number)[2:].zfill(length)


def _remove_bit(subset: int, position: int) -> int:
    return int(bin(subset ^ 1 << position), 2)


def _add_bit(subset: int, position: int) -> int:
    return int(bin(subset ^ 1 << position), 2)


def main():
    number = 12
    print(_to_bitmask_array(number))
    removed = _remove_bit(number, 2)
    removed = _remove_bit(removed, 3)
    print(removed)
    print(_to_bitmask_array(removed))

    print(_to_bitmask_array(_add_bit(removed, 3)))


if __name__ == '__main__':
    main()
