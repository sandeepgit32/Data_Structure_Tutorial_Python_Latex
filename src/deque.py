class Deque:
    
    # Constructor
    def __init__(self):
        self.items = []
    
    # Check whether the deque is empty or not
    def is_empty(self):
        return self.items == []
    
    # Insert new item at the front of the deque
    def add_front(self, item):
        self.items.append(item)
    
    # Insert new item to the rear of the deque
    def add_rear(self, item):
        self.items.insert(0,item)
    
    # Removes the front item from the deque and returns it
    def remove_front(self):
        return self.items.pop()
    
    # Removes the rear item from the deque and returns it
    def remove_rear(self):
        return self.items.pop(0)
    
    # Returns the number of items in the deque
    def size(self):
        return len(self.items)
    
    # Display the deque
    def display(self):
        for i in self.items:
            print('| {} '.format(i), end='')
        print('|')
                                
def main():
    
    # Main function is used so as not to run this part
    # when imported from outside
    d = Deque()       
    d.add_rear(4)
    d.display()
    d.add_rear('dog') 
    d.display()
    d.add_front('cat') 
    d.display()
    d.add_front(45)
    d.display()
    print('Deque size =', d.size())
    
    d.display()
    print('Removed item from rear =', d.remove_rear())
    d.display()
    print('Removed item from front =', d.remove_front())
    d.display()
    
if __name__ == '__main__':
    main()