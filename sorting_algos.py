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
        self.size = len(arr)
        self.pvt = arr[self.size - 1]
        self.pnt_i = -1
        self.pnt_j = 0 
     
    def arrange(self):
        for _ in range((self.size - 1)):
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
        self.arr[self.pnt_i] = self.arr[self.pnt_j]
        self.arr[self.pnt_j] = temp
        
        return self.arr

    def __getindex__(self, value):
        for a in range(self.size):
           while self.arr:
               if value ==  self.arr[a]:
                   index = a
        
        return index

    def partition(self):   # np.partition()
        pvt_index = self.__getindex__(self.pvt)
        part_a = self.arr[:pvt_index - 1]
        part_b = self.arr[pvt_index + 1: ]
        
        return part_a, part_b
    
    def final_sort(self):

        final_list = []
        for parts in self.partition():
            final_list.append(self.arrange(parts), self.pvt)

        ano_list = []
        while self.arr:
            first = self.arrange(self.arr)
            
            for part in self.partition(first):
                ano_list.append(part, self.pvt)

        return final_list, ano_list


   

arry: list  = [7, 12, 14, 13, 6, 8, 2, 9, 11, 10]

sorter = Quick_Sort(arry)
sort_list = sorter.final_sort()
print(f"Quick Sort algo {sort_list}")
