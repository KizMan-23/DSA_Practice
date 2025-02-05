class Node:
    def __init__(self, data):
        self.data = data


class CustomQueue():
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.lpt = 0   #remove an item and ++
        self.rpt = 0   # add an item and ++
    
    def IsEmpty(self):
        return self.rpt == self.lpt


    def IsFull(self):
        if self.rpt == self.lpt - 1:               #creates a circular movement
            return True
        else:
            return False
        
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
            self.rpt = self.size % (self.rpt + 1) #rpt == mod of size and rpt
            self.__setitem__(self.rpt, new_node.data)
            self.rpt += 1
            # self.size += 1  # The array will be continously increased.
        
        self.__setitem__(self.rpt, new_node.data)
        self.rpt += 1
        # self.size +=  1

    def dequeu(self):
        if self.IsEmpty():
            print("Cant dequeue an empty Queue")
        
        item = self.__getitem__(self.lpt)
        self.lpt += 1
        self. size -= 1
        
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
        self.data = [None] * size
        self.rpt = 0
        self.lpt = 0

    def IsEmpty(self):
        return self.rpt == self.lpt

    def IsFull(self):
        return self.rpt == self.lpt - 1 #creates a circular movement
        
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
        if self.isFull():
            self.rpt = self.size % (self.rpt + 1)
            self.data[self.rpt] = new_node.data
            self.rpt += 1
        
        self.__setitem__(self.rpt, new_node.data)
        self.rpt += 1

    def dequeue(self, index):
        if self.IsEmpty():
            print("Cant dequeue an empty Queue")
        
        item = self.__getitem__(self.lpt)
        self.lpt += 1
        # self. size -= 1
        return item

    def pop_first(self):
        item = self.__getitem__(self.lpt)
        self.lpt += 1
        
        return item

    def pop_last(self):
        item = self.__getitem__(self.rpt - 1)
        self.rpt -= 1

        return item
    
    def push_first(self, data):
        new_node = Node(data)
        self.__setitem__(self.lpt, new_node.data)
        self.lpt += 1

    def push_last(self, data):
        new_node = Node(data)
        self.__setitem__(self.rpt - 1, new_node.data)
        self.rpt -= 1
    
    def __str__(self):
        result = []
        for i in range(self.rpt):
            current = self.__getitem__(i)
            result.append(f"{str(current)} - > ")
        result.append("END")
        return " ".join(result)
    


cq = CustomQueue(size = 5)
deque = DeQue(size = 6)

cq.enqueue(2)
cq.enqueue(4)
cq.enqueue(6)
cq.enqueue(8)
cq.enqueue(10)  
# cq.enqueue(12)   #Test for circular queue
# cq.enqueue(14)

print(cq)
print(cq.size)
print(cq.IsFull())
print(cq.IsEmpty())
print(f"Pop from the left {cq.dequeu()}")
print(cq)