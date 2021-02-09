class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.last = self.front
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def enqueue(self, data):
        if(self.front == None):
            self.front = Node(data)
            self.last = self.front
        else:
            newNode = Node(data)
            self.last.next = newNode
            self.last = newNode

        self.size += 1

    def dequeue(self):
        size = self.getSize()
        val = self.front.data
        nxt = self.front.next
        del self.front
        self.front = nxt
        if(size == 1):
            self.front = self.last = nxt
            self.size -= 1
            return val
        elif(size == 0):
            raise Exception("Queue is Empty")
        else:
            self.size -= 1
            return val

    def peek(self):
        return self.front.data

    def __str__(self):
        cur = ''
        temp = self.front
        while(temp):
            cur += str(temp.data) + '->'
            temp = temp.next
        return cur[:-2]


if(__name__ == '__main__'):
    print("This is from queue file")
