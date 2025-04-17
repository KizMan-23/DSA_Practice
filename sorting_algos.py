#selection sort
#Insertion sort
#bubble sort
#quick sort
#merge sort
#shell sort


class QuickSort:   #log0(n log n)
    def __init__(self, arr: list):
        self.arr = arr

    def partition(self, low: int, high: int) -> int:
        pivot = self.arr[high]
        i = low - 1 

        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                # swap 
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        # swap pivot 
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def quick_sort(self, low: int = 0, high: int = None):
        if high is None:
            high = len(self.arr) - 1

        # base case
        if low < high:
            p = self.partition(low, high)
            # recursive sort
            self.quick_sort(low, p - 1)
            self.quick_sort(p + 1, high)

    def sorted(self) -> list:
        # proper sorting
        self.quick_sort()
        return self.arr


array: list  = [7, 12, 14, 13, 6, 8, 2, 9, 11, 10]
sort_list = QuickSort(array).sorted()
# print(f"Quick Sort algo {sort_list}")


def MergeSort(arr: list) -> int:    #log0(n log n)
    len_arr = len(arr)
    l_arr = []
    r_arr = []

    if len_arr <= 1:  #base case
        return
    else:
        middle = len_arr // 2 #flat division
        l_arr = [None]* middle  #left array
        r_arr = [None] * (len_arr - middle)  #right array
 
        i = 0  #index for the left array
        j = 0  #index for the right array
        
        while i < len_arr:
            if i < middle:
                l_arr[i] = arr[i]
                i += 1
            else:
                r_arr[j] = arr[i]
                i += 1
                j += 1

    MergeSort(l_arr)
    MergeSort(r_arr)
    Merge(l_arr, r_arr, arr)


def Merge(left_array: list, right_array: list, array: list):
    array_size = len(array)
    left_size = len(left_array)
    right_size = len(right_array)
    i, l, r = 0, 0, 0  #indices

    while l < left_size and r < right_size:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i += 1
            l += 1
        else:
            array[i] = right_array[r]
            r += 1
            i += 1
    
    while l < left_size:
        array[i] = left_array[l]
        i += 1
        l += 1

    while r < right_size:
        array[i] = right_array[r]
        r += 1
        i += 1

    for a in range(array_size):  #this prints each sorted subarray
        val = array[a]
        print(val, end=" - > ")
    print(".")

# MergeSort(array)


def SelectionSort(arr:list):  #Log0(n^2)
    array_size = len(arr)
   
    for a in range(array_size):
        min_index = Min_Value(arr, a, len(arr))
        #swap
        arr[a], arr[min_index] = arr[min_index], arr[a]
    
    return arr  

def Min_Value(arr, start: int, end:int) -> int:
    i = start
        
    for b in range(start + 1, end):
        if arr[i] > arr[b]:
            i = b

    return i     

array: list  = [7, 12, 14, 13, 6, 8, 2, 9, 11, 10]

# print(array) 

# print(SelectionSort(array))


def BubbleSort(arr:list):  #log0(n^2)

    for a in range(len(arr) - 1): 
        for b in range(len(arr) - a - 1):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1] = arr[b + 1], arr[b]
    
    return arr 

# bub_sort = BubbleSort(array)
# print(bub_sort)


def InterpolationProbe(arr:list, value:int):  #Log0(log(log n))
    #Improvement of Binary Search
    #Most Effective for Semi-Uniformly distributed array
    low = 0
    high = len(arr) - 1
    while value >= arr[low] and value <= arr[high] and low <= high:
        probe: int = low + (high - low) * (value - arr[low] ) // (arr[high] - arr[low])

        print(f"Probe: {probe}")
        if arr[probe] == value:
            return probe
        elif arr[probe] < value:
            low = probe + 1
        else:
            high = probe - 1
    
    return -1

def InterpolationSearch(arr:list, value: int):
    index = InterpolationProbe(arr, value)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element Not Found")

# interpolation_list = [2,3,4,6,7,8,10]

# InterpolationSearch(interpolation_list, 7)

# interpol_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# InterpolationSearch(interpol_list, 128)


def BinarySearch(arr:list, value:int):
    low = 0
    high = len(arr) - 1     

    while low <= high:
        middle = low + (high - low) // 2 
        mid_ind = arr[middle]
        print(f"Middle: {middle}")

        if value < mid_ind:
            high = middle - 1
        elif value > mid_ind:
            low = middle + 1
        else:
            return middle
    return -1

bin_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

print(BinarySearch(bin_list, 32))
