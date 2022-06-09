class Insert:
    def sort(self, array):
        for i in range(len(array)):
            self._sort_left_to(i, array)
    
    def _sort_left_to(self, i, array):
        while i > 0 and array[i] < array[i-1]:
            self._swap(array, i-1, i)
            i -= 1

    def _swap(self, array, left, right):
        array[left], array[right] = array[right],array[left]
  
  
def main():
    array = [1, 6, 7, 3, 1]
    Insert().sort(array)
    print(array)


if __name__ == "__main__":
    main()
