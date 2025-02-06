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
        return (self.rpt + 1) % self.size == self.lpt     #creates a circular movement
        
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
            print("DQueue is Full...")
            return
        
        self.__setitem__(self.rpt, new_node.data)
        self.rpt = (self.rpt + 1) % self.size

        self.count += 1
        
        return f"{new_node.data} added"

    def dequeue(self):
        if self.IsEmpty():
            print("Cant dequeue an empty Queue")
            return None
        
        item = self.__getitem__(self.lpt)
        self.__setitem__(self.lpt, self.enqueue(None))
        self.lpt  = (self.lpt + 1) % self.size
        self.count -= 1
        
        return item

    def pop_first(self):
        item = self.__getitem__(self.lpt)
        # self.__setitem__(self.lpt, self.enqueue(None))
        self.lpt = (self.lpt + 1) % self.size
        
        self.count -= 1

        return item

    def pop_last(self):
        index = (self.rpt - 1) % self.size
        item = self.__getitem__(index)

        # self.__setitem__(self.rpt, self.enqueue(None))

        self.count -= 1

        return item
    
    def push_first(self, data):
        #substitutes at the first position
        new_node = Node(data)
        self.__setitem__(self.lpt, new_node.data)
        
        return f"{new_node.data} added"
        

    def push_last(self, data):
        #subsitute at the last position
        new_node = Node(data)
        index = (self.rpt - 1) % self.size
        self.__setitem__(index, new_node.data)

        self.count += 1
        
        return f"{new_node.data} added"
    
    def __str__(self):
        result = []
        for i in range(self.rpt):
            current = self.__getitem__(i)
            result.append(f"{str(current)} - > ")
        result.append("END")
        return " ".join(result)
    


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
# deque.enqueue(12)


print(deque)
print(f"Pop from the left {deque.dequeue()}")
print(deque.data)
print(deque.push_first(30))
print(deque.data)
print(deque.push_last(40))
print(deque.data)
print(deque.pop_first())
print(deque.pop_last())
deque.enqueue(45)
print(deque)


# print(cq)
# print(cq.size)
# print(cq.IsFull())
# print(cq.IsEmpty())
# print(f"Pop from the left {cq.dequeu()}")
# print(cq)
# cq.enqueue(14)
# print(cq)