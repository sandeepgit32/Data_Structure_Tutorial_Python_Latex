class Heap:
    def __init__(self, MAX_SIZE):
        self.heapList = []
        self.currentSize = 0
        self.MAX_SIZE = MAX_SIZE


    def insert(self, item):
        self.heapList.append(item)
        self.currentSize += 1
        self.bubbleUp(self.currentSize - 1)


    def bubbleUp(self, index):
        parentIdx = abs(index - 1) // 2
        while (index > 0) and (self.heapList[index] > self.heapList[parentIdx]):
            # Swap the child and parent nodes
            self.heapList[index], self.heapList[parentIdx] = self.heapList[parentIdx], \
                                self.heapList[index]
            index = parentIdx
            parentIdx = (index - 1) // 2


    def remove(self):
        lastItem = self.heapList[self.currentSize - 1]
        self.heapList[0] = lastItem
        self.currentSize -= 1
        self.heapList.pop() # Remove the last element in the list
        self.sinkDown(0)


    def sinkDown(self, index):
        itemAtIndex = self.heapList[index] # Saving the item at index
        largerIdx = self.getLargerChildIdx(index)
        
        while (largerIdx != -1) and (itemAtIndex < self.heapList[largerIdx]):
            self.heapList[index], self.heapList[largerIdx] = self.heapList[largerIdx], \
                                        self.heapList[index]
            index = largerIdx
            largerIdx = self.getLargerChildIdx(index)


    def getLargerChildIdx(self, index):
        leftChildIdx = 2*index + 1
        rightChildIdx = 2*index + 2
        if leftChildIdx >= self.currentSize:
            # No child exist
            return -1
        elif rightChildIdx >= self.currentSize:
            # Left child exist but not the right child
            return leftChildIdx
        else:
            # Both children exist
            if self.heapList[leftChildIdx] > self.heapList[rightChildIdx]:
                # Left child value is greater than the right child value
                return leftChildIdx
            else:
                return rightChildIdx


if __name__ == '__main__':
    heap = Heap(10)
    for item in [82, 70, 53, 63, 27, 43, 37, 10, 51]:
        heap.insert(item)
    print(heap.heapList)
    heap.remove()
    print(heap.heapList)