class Node:
    
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    # Constructor
    def __init__(self):
        self.head = None

    # Display the linked list
    def display(self):
        cur_node = self.head
        while cur_node:
            print('['+str(cur_node.data)+'] ---> ', end='')
            cur_node = cur_node.next
        print('None')

    # Returns the length of the linked list
    def length(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
        
    # Insert item at the end of linked list
    def insertLast(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return None

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Insert item at the beginning of linked list
    def insertFirst(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Insert item at a specific position of linked list
    def insert_at_pos(self, pos, data):

        if pos < 0 or pos > self.length():
            print('No node exists at this position')
            return None
        
        new_node = Node(data)
        cur_node = self.head
        if pos == 0:
            self.insertFirst(data)
        else:
            for i in range(pos-1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node

    # Delete item by value (key)
    def delete_by_key(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return None

        prev_node = None 
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return None

        prev_node.next = cur_node.next
        cur_node = None

    # Delete item by position(index)
    def delete_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return None

        prev_node = None
        count = 1
        while cur_node and count != pos:
            prev_node = cur_node 
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return 

        prev_node.next = cur_node.next
        cur_node = None

    # Reversing the linked list
    def reverse(self):
        cur_node = self.head
        prev_node = None
        
        while cur_node:
            next_node = cur_node.next
            # next_node for saving cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node
        
    # Search the element in a linked list using key
    def searchkey(self, key):
        cur_node = self.head
        pos = 0
        
        if self.head == None:
            print('No such value found in the Linked List')
        else:
            while cur_node:
                if cur_node.data == key:
                    print("Search value index = "+str(pos))
                    return None
                cur_node = cur_node.next
                pos += 1
            if cur_node == None:
                print('No such value found in the Linked List')

llist = LinkedList()
llist.insertLast("A")
llist.insertLast("B")
llist.insertLast("C")
llist.display()

llist.insert_at_pos(2, 'D')
llist.insert_at_pos(1, 5)
llist.display()

llist.delete_by_key("B")
llist.display()

llist.reverse()
llist.display()

llist.searchkey('A')
llist.display()

