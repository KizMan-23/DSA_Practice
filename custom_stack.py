class Node:
    def __init__(self, data):
        self.data = data
        

class CustomStack():
    def __init__(self, size):
        self.data = [None] * size
        self.size = size #for static-sized stack, size starts at zero
        self.ptr = -1
    

    def len(self):
        return self.size
    
    def IsEmpty(self):
        return self.ptr == -1 
      
        
    def IsFull(self):
        return self.ptr == self.len() - 1
    

    def doublesize(self):
        if self.IsFull():
            temp = [None] * (self.size * 2)

            for i in range(self.size):
                temp[i] = self.data[i]
            
            self.data = temp
            self.size *= 2
        
    
    def __getitem__(self, index):
        if index < 0 or index > self.ptr:
            raise IndexError("Index Out of range.")
        else:
            return self.data[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index > self.ptr:
            raise IndexError("Index out of range.")
        else:
            self.data[index] = value

    def pop(self):
        if self.IsEmpty():
            print("Can't Pop from an Empty Stack")
            return None
        else:
            item = self.data[self.ptr]     # value = self.__getitem__(self.ptr)
            self.ptr -= 1                  #self.__setitem__(self.ptr, None)

            self.size -= 1     #In dynamic stacks, after doubling the size of an empty is the size of the doubled stack
                               #By reducing the size here, the final size of any empty is the original empty spaces in the stack.
                               # This can help in managing memory. 
            return item
    
    def push(self, value):
        if self.IsFull():
            print("Stack is Full. Doubling Stack......")
            self.doublesize()
        
        new_node = Node(value)
        self.ptr += 1
        self.data[self.ptr] = new_node.data
        # self.__setitem__(self.ptr, new_node.data)

        # self.size +=1 -- In dynamic stacks, size does not ++ or -- with new items

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
print(f"Stack size before doubling of the size {cst.size}")

cst.push(60) #custom dynamic stack
cst.push(66)

print(f"stack size of {cst.size} after doubling in size")

print(f"first pop from the top {cst.pop()}")
print(f"second pop from the top {cst.pop()}")
print(f"Third pop from the top {cst.pop()}")
print(f"Look at the peak from the Top {cst.peek()}")
print(f"Forth pop from the top {cst.pop()}")
print(f"Fifth pop from the top {cst.pop()}")
print(f"Sixth pop from the top {cst.pop()}")
print(f"7th pop from the top {cst.pop()}")  #test for double stack - dynamic stack
print(f"8th pop from the top {cst.pop()}")
print(f"Final size of the stack is {cst.size}")