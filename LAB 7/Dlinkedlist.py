"""Name: Kanishk Ashra
  Collaborators: University of ALberta"""

class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        

    def add(self, item):
        new_node = DLinkedListNode(item, self.__head, None)
        if self.__head is not None:
            self.__head.setPrevious(new_node)
        else:
            self.__tail = new_node
        self.__head = new_node
        self.__size += 1
        
    def remove(self, item):
        current = self.__head
        while current is not None:
            if current.getData() == item:
                if current.getPrevious() is not None:
                    current.getPrevious().setNext(current.getNext()) # Update the next of the previous node to skip the current node
                else:
                    self.__head = current.getNext()
                if current.getNext() is not None:
                    current.getNext().setPrevious(current.getPrevious())
                else:
                    self.__tail = current.getPrevious()
                self.__size -= 1
                return
            current = current.getNext()
        
    def append(self, item):
        new_node = DLinkedListNode(item, None, self.__tail)
        if self.__tail is not None:
            self.__tail.setNext(new_node)
        else:
            self.__head = new_node
        self.__tail = new_node
        self.__size += 1
        
    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos == self.__size:
            self.append(item)
        elif 0 < pos < self.__size:
            current = self.__head
            for _ in range(pos):
                current = current.getNext()
            new_node = DLinkedListNode(item, current, current.getPrevious())
            current.getPrevious().setNext(new_node)
            current.setPrevious(new_node)
            self.__size += 1
        else:
            raise IndexError("Index out of bounds")
            
    def pop1(self):
        if self.__tail is not None:
            return self.pop(self.__size - 1)
        else:
            raise IndexError("an empty list")
    
    def pop(self, pos=None):
        if pos is None:
            return self.pop1()
        elif pos>=0 and pos < self.__size:
            current = self.__head
            for _ in range(pos):    #loop to find the data at the position pos
                current = current.getNext()
            item = current.getData()
            if current.getPrevious() is not None:
                current.getPrevious().setNext(current.getNext())
            else:
                self.__head = current.getNext()
            if current.getNext() is not None:
                current.getNext().setPrevious(current.getPrevious())
            else:
                self.__tail = current.getPrevious()
            self.__size -= 1
            return item
        else:
            raise IndexError("Index out of bounds")
    
    def searchLarger(self, item):
        current = self.__head
        pos = 0
        while current is not None:
            if current.getData() > item:
                return pos
            current = current.getNext()
            pos += 1
        return -1
    
    def getSize(self):
        return self.__size
    
    def getItem(self, pos):
        if pos >= 0:# traversing the list from starting to end
            if pos < self.__size:
                current = self.__head
                for _ in range(pos):
                    current = current.getNext()
                return current.getData()
            else:
                raise IndexError("Index out of bounds")




def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
    
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   

    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
    print(str(int_list2))

    is_pass = (int_list2.getItem(-2) == 11)
    assert is_pass == True, "fail the test"

    is_pass = (int_list2.getItem(-1) == 12)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list2.getItem(-4) == 5)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()
