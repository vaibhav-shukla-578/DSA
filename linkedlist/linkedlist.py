class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self,value):
        new_node = Node(value)
        if self.length == 0: #can also do if self.head is None
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    
    def pop(self):
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
        return temp
    
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                    temp = temp.next
            return temp.value
        
    def set(self, index, value):
        if index < 0 and index > self.length :
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
        if self.length == 0:
            self.tail = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.head
            for _ in range (index -1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            
        self.length += 1
        return True
    

def remove(self, index):
    if index < 0 or index >= self.length:  # fix bounds
        return None
    
    if index == 0:  # remove head
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:  # list became empty
            self.tail = None
        return temp.value
    
    elif index == self.length - 1:  # remove tail
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        temp = prev.next
        prev.next = None
        self.tail = prev
        self.length -= 1
        return temp.value
    
    else:  # remove from middle
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value
    

def reverse(self):
    if self.length == 0:
        return None
    if self.length == 1:
        return self.head
    
    prev = None
    current = self.head
    self.tail = self.head
    while current:
        after = current.next
        current.next = prev
        prev = current
        current = after
    self.head = prev
    return True


my_linked_list = LinkedList(7)
my_linked_list.append(9)
my_linked_list.print_list()