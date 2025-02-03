class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(f"Node(data = self.data)")

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = new_node
            while current.next:
                current = current.next
            current.next = new_node

    def insert_data(self, data, position):
        new_node = Node(data)
        #inserting at the head
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 2):
                if current is None:
                    print("Invalid Position")
                    return
                current = current.next
            new_node.next = current.next
            current.next  = new_node
        return  #insert at the tail


    def delete_node(self, position):
        if not self.head:
            print("List in Empty")
            return
        if position == 1:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 2):
                if current.next is None:
                    print("Ivalid Position")
                    return
                current = current.next
            if current.next is None:
                print("Invalid Position")
                return
            current.next = current.next.next

    def __display__(self):
        current = self.head

        while current:
            print(str(current), end=" - > ")
            current = current.next
        return print("END")
    

#try out the add function
def create_linked_list():
    n = int(input("Enter the number of nodes: "))
    linkedlist = LinkedList()

    for _ in range(n):
        n_data = input("Enter the data for the node: ")
        linkedlist.add(n_data)

    return linkedlist.__display__() 


class CustomLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        if self.size is None:
            print("Linked List is Empty")
    
    def __getitem__(self, index):
        #retrieving at index[i]
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        #traverse the linked list
        for _ in range(index - 1):
            current = current.next
        return current #error
    
    def __setitem__(self, index, value):
        #assign value at obj[index] = value

        if index < 0  or index >= self.size:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current = value
               

    def __delitem__(self, index):
        # Delete item at obj[index]
        if index < 0 or index > self.size:
            raise IndexError("Index Out of range.")
        
        if index == self.size: 
            #Try this at the last index
            try:
                current = self.head
                for _ in range(index - 1):
                    current =  current.next
                del current
            except:
                raise Exception("Couldn't delete at the last Index")
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 2):
                #two indexes before the supposed index
                current = current.next
            if current.next is None:
                raise IndexError("Next Index is None.")
            current.next = current.next.next
        self.size -= 1
    
    def _dellast():
        #delete at the last index
        pass
    
    def __contains__(self, value):
        #Define behavoir for 'in' keyword
        current = self.head
        while current:
            if current == value:
                return True
            current = current.next
        return False
    
    def __append__(self, value):
        #add a new node at the last.. 
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def __indexadd__(self, value, index):
        #add at an index
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        
        if index == self.size:
            current = current[index]
            current.next = new_node
        else:
            current = self.head
            for _ in range(index - 2):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def __str__(self):
        #User-Friendly string representation
        values = []
        current = self.head
        while current:
            values.append(str(current))
            current = current.next
        return " - > ".join(values)




# ll = create_linked_list()
# print(ll)

cll = CustomLinkedList()
cll.__append__(10)
cll.__append__(20)
cll.__append__(30)
cll.__append__(40)
cll.__append__(50)


cl.add