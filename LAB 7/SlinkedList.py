"""Name: Kanishk Ashra
   Written by: Kanishk Ashra and University of Alberta
"""
class SLinkedListNode:
    # an instance of this class is a node in a Single Linked List
    # a node has a reference to data and reference to next
    def __init__(self,initData,initNext):
        self.data = initData
        self.next = initNext
        
    def getNext(self):
        return self.next
    
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def setNext(self,newNext):
        self.next = newNext


class SLinkedList:
    # an instance of this class is a Singly-Linked List object
    # it has reference to the first node in the list
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add(self,item):
        # adds an item at the start of the list
        new_node = SLinkedListNode(item,None)
        new_node.setNext(self.head)
        self.head = new_node
        self.size = self.size + 1
        
    def append(self,item):
        # adds an item at the end of the list
        new_node = SLinkedListNode(item,None)
        current = self.head # Start the traversal
        if self.size == 0: # check if list is empty
            self.add(item)
        else:
            while (current.getNext()!=None):
                current= current.getNext() # traversing the list
            current.setNext(new_node)
            self.size = self.size +1


    def insert(self,pos,item):
        # inserts the item at pos
        # pos should be a positive number (or zero) of type int
        # TO DO: write assert statement that tests if pos is int
        # TO DO: write assert statement that tests that pos is not negative
        try:
            newNode=SLinkedListNode(item,pos)
            if pos == 0:  # this takes account of the case when the element is supposed to inserted at the starting
                newNode.next = self.head
                self.head = newNode
            else:
                current = self.head     
                prev = None
                index = 0
                # Traversing the list to find the position to insert
                while current is not None and index < pos: # checks if the position to be inserted is not in the start
                    prev = current
                    current = current.next
                    index += 1
                # Case 2: Inserting at the end or in the middle of the list
                newNode.next = current    
                prev.next = newNode    #changing the pointers after inserting the element 
        except ValueError:
            print("Position should be positive and it should be an integer!")

    def remove(self,item):
        # remove the node containing the item from the list
        if self.size == 0:
            raise Exception('List is Empty')
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            raise Exception('Item not in list')
        else:
            if previous == None: # the item is in the first node of the list
                self.head = current.getNext()
            else: # item is not in the first node
                previous.setNext(current.getNext())
            self.size = self.size -1
            
    def index(self,item):
        # finds the location of the item in the list
        if self.size == 0:
            raise Exception('List is empty')
        position = 0
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                position = position + 1
        if found:
            return position
        else:
            return 'Item not found'
        
    def pop(self):
        # removes the node from the end of the list and returns the item 
        if self.size == 0:
            raise Exception('List is empty')
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size = self.size -1
        return current.getData()
    
    def __str__(self):
        # returns a string representation of the list
        current = self.head
        string = ''
        while current != None:
            string = string + str(current.getData())+'->'
            current = current.getNext()
        return string
    
    def getSize(self):
        return self.size

    
def main():
    # Testing Singly-Linked List
    slist = SLinkedList()
    slist.add(89)
    slist.add(96)
    slist.add('Kanishk')
    slist.append(77)
    slist.append(669)
    slist.append('nesfjnrdgj')
    print('Original List:', slist.getSize(), 'elements')
    print(slist)
    print()
    slist.insert(0,'start')
    print('After inserting the word start at position 0:', slist.getSize(), 'elements')
    print(slist)
    print()
    slist.insert(7,'end')
    print('After inserting the word end at position 7:', slist.getSize(), 'elements')
    print(slist)
    print()
    slist.insert(4,'middle')
    print('After inserting middle at position 4:', slist.getSize(), 'elements')
    print(slist)
    
if __name__=="__main__":
    main()