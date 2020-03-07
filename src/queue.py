class Queue:
    
    # Constructor
    def __init__(self):
        self.items = []
        
    # Check whether the queue is empty or not
    def is_empty(self):
        return self.items == []
    
    # Insert new item to the rear of the queue
    def enqueue(self, item):
        self.items.insert(0, item)
        
    # Removes the front item from the queue and returns it
    def dequeue(self):
        return self.items.pop()
    
    # Returns the number of items in the queue
    def size(self):
        return len(self.items)
    
    # Display the queue
    def display(self):
        for i in self.items:
            print('| {} '.format(i), end='')
        print('|')
        
q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.display()

print('Removed item =', q.dequeue())
q.display()

q.enqueue(61)
q.display()
print('Queue size =', q.size())