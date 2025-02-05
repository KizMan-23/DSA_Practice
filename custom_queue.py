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
        if self.lpt == self.rpt:
            return True
        else:
            return False
        
    def IsFull(self):
        if self.rpt == self.lpt - 1 or self.rpt == self.size - 1:
            return True  #create a circular queue loop
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
            # return self.data  #might clear this line
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.IsFull():
            self.rpt = self.size % (self.rpt + 1) #rpt == mod of size and rpt
            self.__setitem__(self.rpt, new_node.data)
            self.rpt += 1
            self.size += 1
        else:
            self.__setitem__(self.rpt, new_node.data)
            self.rpt += 1
            self.size +=  1

    def dequeu(self):
        if self.__IsEmpty__():
            print("Cant dequeue an empty Queue")
        else:
            item = self.__getitem__(self.lpt)
            self.lpt += 1
            self. size -= 1

            return item

    def __str__(self):
        result = []
        for i in range(self.lpt + 1):
            current = self.__getitem__(self.lpt)
            result.append(f"{str(current)} - > ")
        result.append("END")
        return " ".join(result)


cq = CustomQueue(size = 5)

cq.enqueue(3)
print(cq)



class DeQueue():
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def enqueue(self, data):
        pass

    def dequeue(self, index):
        pass

    def pop_first(self, index):
        pass
    def pop_last(self, index):
        pass
    def push_first(self, data):
        pass
    def push_last(self, data):
        pass
    