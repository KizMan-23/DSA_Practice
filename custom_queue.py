class Node:
    def __init__(self, data):
        self.data = data


class CustomQueue():
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.count = 0
        self.lpt = 0   #remove an item and ++
        self.rpt = 0   # add an item and ++
    
    def IsEmpty(self):
        return self.count == 0


    def IsFull(self):
        return (self.rpt + 1) % self.size == self.lpt  #the rpt pointer wraps around
    
    def __getitem__(self, index):
        #return index at assignment
        if index < 0 or index >= self.rpt:
            raise IndexError("Index Out of range.")
        else:
            return self.data[index]
        
    def __setitem__(self, index, value):
        if index < 0 or index > self.rpt:
            raise IndexError("Index out of range.")
        else:
            self.data[index] = value
    
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.IsFull():
            print("Queue is Full")
            return
        
        self.__setitem__(self.rpt, new_node.data)
        self.rpt = (self.rpt + 1) % self.size      #increament the pointer
        self.count += 1

    def dequeu(self):
        if self.IsEmpty():
            print("Cant dequeue an empty Queue")
            return None
        
        item = self.__getitem__(self.lpt)
        self.__setitem__(self.lpt, None)
        self.lpt = (self.lpt + 1) % self.size

        self.count -= 1
        return item

    def __str__(self):
        result = []
        for i in range(self.rpt):
            current = self.__getitem__(i)
            result.append(f"{str(current)} - > ")
        result.append("END")
        return " ".join(result)



class DeQue():
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.data = [None] * size
        self.rpt = 0
        self.lpt = 0

    def IsEmpty(self):
        return self.count == 0

    def IsFull(self):
        return self.count == self.size     #creates a circular movement

    def enqueue(self, data):
        new_node = Node(data)
        if self.IsFull():
            print("DQueue is Full...")
            return
        
        # self.__setitem__(self.rpt, new_node.data)
        self.data[self.rpt] = new_node.data
        self.rpt = (self.rpt + 1) % self.size

        self.count += 1
        

    def dequeue(self):
        if self.IsEmpty():
            print("Cant dequeue an empty Queue")
            return None
        
        # item = self.__getitem__(self.lpt)
        item = self.data[self.lpt]
        self.data[self.lpt] = None
        self.lpt  = (self.lpt + 1) % self.size
        self.count -= 1
        
        return item

    def pop_first(self):
        # item = self.__getitem__(self.lpt)
        item = self.data[self.lpt]
        self.data[self.lpt] = None
        self.lpt = (self.lpt + 1) % self.size
        
        self.count -= 1

        return item

    def pop_last(self):
        self.rpt = (self.rpt - 1) % self.size
        item = self.data[self.rpt]
        self.data[self.rpt]  = None

        self.count -= 1
        return item
    
    def push_first(self, data):
        #switch the front pionter back
        new_node = Node(data)
        index = (self.lpt - 1) % self.size
        self.data[index] = None
        self.data[index] = new_node.data

        self.lpt = (self.lpt - 1) % self.size
        
        self.count += 1      
        
        return f"{new_node.data} added"
        
    def push_last(self, data):
        #switch the rear pointer forward
        new_node = Node(data)
        index = (self.rpt) % self.size
        self.data[index]  = None
        self.data[index] = new_node.data

        self.rpt = (self.rpt + 1) % self.size

        self.count += 1
        
        return f"{new_node.data} added"
    
    def __str__(self):
        result = []
        index = self.lpt
        for i in range(self.size): #active nodes are only self.rpt - 1
            result.append(str(self.data[i]))
            index = (self.lpt + 1) % self.size
        result.append("END")
        return " - > ".join(result)
    


cq = CustomQueue(size = 6)
deque = DeQue(size = 6)

cq.enqueue(2)
cq.enqueue(4)
cq.enqueue(6)
cq.enqueue(8)
cq.enqueue(10)    #Test for circular queue
# cq.enqueue(12)   
# cq.enqueue(14)

deque.enqueue(2)
deque.enqueue(4)
deque.enqueue(6)
deque.enqueue(8)
deque.enqueue(10)
deque.enqueue(12)
deque.enqueue(14)              #DQueue is Full...


print(deque)       # 2 - > 4 - > 6 - > 8 - > 10 - > 12 - > END
print(f"Pop from the left {deque.dequeue()}")   #Pop from the left 2
print(deque)                                    #None - > 4 - > 6 - > 8 - > 10 - > 12 - > END
print(deque.push_first(30))
print(deque)                                    #30 - > 4 - > 6 - > 8 - > 10 - > 12 - > END
print(deque.push_last(40))
print(deque)                                    #40 - > 4 - > 6 - > 8 - > 10 - > 12 - > END
print(deque.pop_first())                        #40
print(deque.pop_last())                         # None
print(deque)                                    #None - > 4 - > 6 - > 8 - > 10 - > 12 - > END
print(deque.pop_first())                        # 4
print(deque.pop_last())                         # 12
print(deque)                                    #None - > None - > 6 - > 8 - > 10 - > None - > END
deque.enqueue(45)
deque.enqueue(55)
print(deque)                                    #55 - > None - > 6 - > 8 - > 10 - > 45 - > END
print(deque.count)                              #5


# print(cq)
# print(cq.size)
# print(cq.IsFull())
# print(cq.IsEmpty())
# print(f"Pop from the left {cq.dequeu()}")
# print(cq)
# cq.enqueue(14)
# print(cq)