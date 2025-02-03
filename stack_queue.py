class Node:
    def __init__(self, data):
        self.data = data
        


class CustomStack():
    def __init__(self, size):
        self.data = [None] * size
        self.size = 0
        self.ptr = -1
    # ptr = -1

    def len(self):
        return self.size
    
    def IsEmpty(self):
        if self.ptr == -1:
            return True
        else:
            return False
        
    def IsFull(self):
        if self.ptr == self.len():
            return True
        else:
            return False

    def doublesize(self):
        if self.IsFull():
            self.size = self.len() * 2
        return self.size
    
    def __getitem__(self, index):
        if index < 0 or index > self.ptr:
            raise IndexError("Index Out of range.")
        else:
            return self.data[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.ptr:
            raise IndexError("Index out of range.")
        else:
            self.data[index] = value

    def pop(self):
        if self.IsEmpty():
            print("Can't Pop from an Empty Stack")
            return
        else:
            item = self.data.pop(self.ptr) # value = self.__getitem__(self.ptr)
            self.ptr -= 1                  #self.__setitem__(self.ptr, None)    
            #del item
            self.size -= 1
        return item
    
    def push(self, value):
        if self.IsFull():
            print("Stack is Full")
        else:
            new_node = Node(value)  #self.__setitem__(self.ptr, value)
            self.ptr += 1
            self.data[self.ptr] = new_node.data

            self.size +=1 

    def peek(self):
        if self.IsEmpty():
            print("Cant Peek on Empty Stack")
        else:
            item = self.__getitem__(self.ptr)
        return item 
    
    def __str__(self):
        for i in range(self.ptr + 1):
            print(f"{self.data} - > ")
        print("END")

    

cst = CustomStack(size = 5)

cst.push(10)
cst.push(20)
cst.push(30)
cst.push(40)
cst.push(50)

print(f"stack has the initial size of {cst.size}")

print(f"first pop from the top {cst.pop()}")
print(f"second pop from the top {cst.pop()}")
print(f"Third pop from the top {cst.pop()}")
print(f"Look at the peak from the Top {cst.peek()}")
print(f"Forth pop from the top {cst.pop()}")
print(f"Fifth pop from the top {cst.pop()}")
print(f"Sixth pop from the top {cst.pop()}")

print(f"Final size of the stack is {cst.size}")
        
    
        
