def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
def merge_sort(array):
    _sort(array, [0] * len(array), 0, len(array) - 1)


def _sort(array, aux, low, high):
    print(low, high, high <= low)
    if high <= low:
        return
    mid = (low + (high - low)) // 2
    print(low, mid, high)
    _sort(array, aux, low, mid)
    _sort(array, aux, mid + 1, high)
    # _merge(array, aux, low, mid, high)


def _merge(arr, aux, low, mid, high):
    print("Sorting for", arr, aux, low, mid, high)
    for i in range(low, high + 1):
        aux[i] = arr[i]
    left, right = low, mid + 1
    for i in range(low, high + 1):
        # print(">> Comparing", left, right, " as ", aux[left], aux[right])
        if left > mid:
            print("if left > mid:")
            arr[i] = aux[right]
            right += 1
        elif right > high:
            print("elif right > high:")
            arr[i] = aux[left]
            left += 1
        elif aux[right] < aux[left]:
            print("elif array[right] < array[left]:")
            arr[i] = aux[right]
            right += 1
        else:
            print("elif array[left] <= array[right]:")
            arr[i] = aux[left]
            left += 1
        print(arr)
        print(aux)


def main():
    array = [1, 4, 6, 8, 3, 5, 7]
    mergeSort(array)
    # _merge(array, [0] * len(array), 0, (len(array)) // 2, len(array) - 1)
    print("Finished", array)
    
    


if __name__ == "__main__":
    main()
