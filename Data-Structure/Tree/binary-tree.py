import queue


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if(self.data):
            if data < self.data:
                if(self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if(self.right is None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def printInorder(self):
        if(self.left):
            self.left.printInorder()
        print(self.data, end=' ')
        if(self.right):
            self.right.printInorder()

    def printPreorder(self):
        print(self.data, end=' ')
        if(self.left):
            self.left.printPreorder()
        if(self.right):
            self.right.printPreorder()

    def printPostorder(self):
        if(self.left):
            self.left.printPostorder()
        if(self.right):
            self.right.printPostorder()
        print(self.data, end=' ')


def maxDepth(root):
    if(not root):
        return 0
    else:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1


def sumOfTree(root):
    if(root == None):
        return 0
    return root.data + sumOfTree(root.left) + sumOfTree(root.right)


def breadthFirst(root):
    q = queue.Queue()
    q.enqueue(root)
    while(not q.isEmpty()):
        if(root.left):
            q.enqueue(root.left)
        if(root.right):
            q.enqueue(root.right)
        temp = q.dequeue()
        if(not q.isEmpty()):
            root = q.peek()
        print(temp.data, end=" ")


if __name__ == "__main__":
    root = Node()
    B = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]
    for i in B:
        root.insert(i)

    breadthFirst(root)
