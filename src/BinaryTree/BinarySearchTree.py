# Binary Search Tree
class Node():
    # Constructor
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree():
    # Constructor
    def __init__(self, data):
        self.root = Node(data)
        
        
    # Find a Node in a BST 
    def findNode(self, data):
        if self.root.data == data:
            return self.root
        else:
            currentNode = self.root
            while data != currentNode.data:
                if data < currentNode.data:
                    currentNode = currentNode.leftChild
                else:
                    currentNode = currentNode.rightChild
                if currentNode == None: # If no child
                    return None 
            return currentNode


    # Insert a New Node in a Binary Search Tree 
    def insert(self, data):
        currentNode = self.root
        while True:
            if data < currentNode.data:
                if not currentNode.leftChild:
                    currentNode.leftChild = Node(data)
                    return None
                currentNode = currentNode.leftChild
            else:
                if not currentNode.rightChild:
                    currentNode.rightChild = Node(data)
                    return None
                currentNode = currentNode.rightChild


    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
    
    
    # Delete node from Binart Search Tree
    # To-Implement
    # def deleteNode(self, data):
    #     currentNode = self.root
    #     isLeftChild = True
    #     # 'isLeftChild' is used to check whether the current
    #     # is whether the left or right child of parents
    #     while data != currentNode:
    #         parentNode = currentNode
    #         if data < currentNode.data:
    #             isLeftChild = True
    #             currentNode = currentNode.leftChild
    #         else:
    #             isLeftChild = False
    #             currentNode = currentNode.rightChild
    #         if currentNode == None:
    #             return False # No no found

    
    # Remove Node from Binary Search Tree 
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:                                    # If node is Empty i.e None, return the node
            return node

        # If data < root, traverse through the left child till we get the "data" node
        # Look for node we want to get rid of
        if data < node.data:                            # If the node data to be deleted is less than root, go to left
            node.leftChild = self.removeNode(data, node.leftChild) # Tell parent node that its left child is None
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        # Else we are standing at that node which we want to delete.
        # It may be a node with children (1 or 2) or a leaf node
        else:
            # If the current node is a leaf node i.e no left and right child
            if not node.leftChild and not node.rightChild:
                print('Removing leaf node...')
                del node
                return None                             # Returning None tells its parent Node that its left or right child has been deleted
            # If the node to be deleted is a parent and has only one child (on right)
            # Node -> Right Child
            if not node.leftChild:
                print('Removing Node with single right child...')
                tempNode = node.rightChild              # Put the right child value in a temporary variable
                del node                                # Delete the parent node
                return tempNode                         # Return the temp node. Parent of deleted node --> Temp node

            # If the node to be deleted is a parent and has only one child (on Left)
            # Node -> Left Child
            elif not node.rightChild:
                print('Removing Node with single left child...')
                tempNode = node.leftChild
                del node
                return tempNode

            # If node to be deleted is a parent node with two children
            print('Removing node with two children...')
            # Fetch the largest node in left subtree to root in temp Node.
            tempNode = self.getPredecessor(node.leftChild)
            # Replace the node to be deleted data with the largest node value data
            node.data = tempNode.data
            # Remove the node with largest value in the left subtree to root/node to be deleted.
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        return node


    # Find the parent node
    def findParentNode(self, data):
        if data == self.root.data:
            return None # Data found at root node, no parent
        currentNode = self.root
        while  data != currentNode.data:
            if data < currentNode.data:
                parentNode = currentNode # Saving the parent node
                currentNode = currentNode.leftChild
            else:
                parentNode = currentNode
                currentNode = currentNode.rightChild
            if currentNode == None: # data is not found
                return None
        return parentNode


    # Get the Minimum Value in a BST 
    # The left most value is the Smallest Value
    def getMinValue(self):
        currentNode = self.root
        while True:
            if not currentNode.leftChild:
                return currentNode.data
            currentNode = currentNode.leftChild


    # Get the Maximum Value in a BST 
    # The right most value is the Maximum Value
    def getMaxValue(self):
        currentNode = self.root
        while True:
            if not currentNode.rightChild:
                return currentNode.data
            currentNode = currentNode.rightChild


    # Traversing BST In-Order: Left --> Root --> Right
    def traverseInOrder(self, rootNode):
        currentNode = rootNode
        if currentNode.leftChild:
            self.traverseInOrder(currentNode.leftChild)
        print(currentNode.data, end=" ")
        if currentNode.rightChild:
            self.traverseInOrder(currentNode.rightChild)


    # Traversing BST Pre-Order: Root --> Left --> Right
    def traversePreOrder(self, rootNode):
        currentNode = rootNode
        print(currentNode.data, end=" ")
        if currentNode.leftChild:
            self.traversePreOrder(currentNode.leftChild)
        if currentNode.rightChild:
            self.traversePreOrder(currentNode.rightChild)


    # Traversing BST Pre Order: Left --> Right --> Root
    def traversePostOrder(self, rootNode):
        currentNode = rootNode
        if currentNode.leftChild:
            self.traversePostOrder(currentNode.leftChild)
        if currentNode.rightChild:
            self.traversePostOrder(currentNode.rightChild)
        print(currentNode.data, end=" ")


if __name__ == '__main__':
    bst = BinarySearchTree(10)
    bst.insert(13)
    bst.insert(14)
    bst.insert(5)
    bst.insert(1)
    
    foundNode = bst.findNode(75)
    if foundNode == None:
        print("Could not find the node with data = 75")
    else:
        print("Found the node with data = 75")
        
    foundNode = bst.findParentNode(1)
    if foundNode == None:
        print("Could not find the parent node with data = 1")
    else:
        print(f"The data in the parent node is {foundNode.data}")

    print("Inorder traversing --> ")
    bst.traverseInOrder(bst.root)
    print()
    print("Preorder traversing --> ")
    bst.traversePreOrder(bst.root)
    print()
    print("Preorder traversing --> ")
    bst.traversePostOrder(bst.root)
    print()
    
    bst.remove(10)