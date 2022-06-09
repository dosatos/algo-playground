class Select:
    def sort(self, array):
        for start in range(len(array)):
            arg_min = self._get_arg_min(start, array)
            if arg_min != start:
                self._swap(array, arg_min, start)
    
    def _get_arg_min(self, start, array):
        min_so_far = (start, array[start])
        for idx in range(start + 1, len(array)):
            value = array[idx]
            if value < min_so_far[1]:
                min_so_far = (idx, value)
        return min_so_far[0]
                

    def _swap(self, array, left, right):
        array[left], array[right] = array[right],array[left]


def main():
    array = [1, 6, 7, 3, 1]
    Insert().sort(array)
    print(array)


if __name__ == "__main__":
    main()
