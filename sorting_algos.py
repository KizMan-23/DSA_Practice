import numpy as np
import random

#selection sort
#Insertion sort
#bubble sort
#quick sort
#merge sort
#shell sort

class Quick_Sort():
    def __init__(self, arr: list):
        self.arr = arr
        self.start = 0
        self.size = len(arr)
        self.end = self.size - 1
        self.pvt = arr[self.size - 1]
        self.pnt_i = -1
        self.pnt_j = 0 
     
    def partition(self):
        for _ in range(self.size - 1):
            if self.arr[self.pnt_j] >= self.pvt:
                self.pnt_j += 1
            else:
                self.pnt_i += 1

                temp = self.arr[self.pnt_i]
                self.arr[self.pnt_i] = self.arr[self.pnt_j]
                self.arr[self.pnt_j] = temp

                self.pnt_j += 1

        self.pnt_i += 1

        temp = self.arr[self.pnt_i]
        self.arr[self.pnt_i] = self.arr[self.size - 1]   #index at the end
        self.arr[self.size - 1] = temp
        
        return self.pnt_i

    def quick_sort(self, ar, s, e):   # np.partition()
            ar = self.arr
            s = self.start
            e = self.end
            if ar[e] <= s:
                pvt_index = self.partition()
                self.quick_sort(self.arr, s, pvt_index -1)
                self.quick_sort(self.arr, pvt_index + 1, e)
            else:
                return


#NEW QUICK_SORT
class QuickSort:
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


arry: list  = [7, 12, 14, 13, 6, 8, 2, 9, 11, 10]
sort_list = QuickSort(arry).sorted()
# print(f"Quick Sort algo {sort_list}")


def MergeSort(arr: list) -> int:
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

MergeSort(arry)

