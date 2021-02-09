class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        if(not temp):
            print("List is empty")
            return
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    def getListLength(self):
        temp = self.head
        cnt = 0
        while(temp):
            cnt += 1
            temp = temp.next
        return cnt

    def getNode(self, key=-1):
        temp = self.head
        if(key == -1):
            while(temp.next):
                temp = temp.next
            return temp
        elif(key < self.getListLength()):
            cnt = 0
            while(key != cnt):
                temp = temp.next
                cnt += 1
            return temp

        return None

    def insertNode(self, data, key=-1):
        temp = node(data)
        if((key == -1 or key == 0) and self.getListLength() == 0):
            self.head = temp
        elif(key == -1):
            self.getNode(key).next = temp
        elif(key == 0):
            temp.next = self.head
            self.head = temp
        elif(self.getNode(key)):
            currentNode = self.getNode(key)
            prevNode = self.getNode(key-1)
            temp.next = currentNode
            prevNode.next = temp
        else:
            print("Node Doesn't Exist")

    def deleteNode(self, key=-1):
        currentNode = self.getNode(key)
        if(currentNode):
            temp = self.head
            if(key == 0 or self.getListLength() == 1):
                temp = self.head.next
                del self.head
                self.head = temp
            elif(key == -1):
                key = self.getListLength()-1
                prevNode = self.getNode(key-1)
                prevNode.next = None
            else:
                prevNode = self.getNode(key-1)
                prevNode.next = currentNode.next

            del currentNode

        else:
            print("Node Doesn't Exist")

    def deleteList(self):
        temp = self.head
        while(temp):
            self.deleteNode()
            temp = self.head

    def reverseList(self):
        temp = linkedlist()
        l = self.getListLength()-1
        for i in range(l, -1, -1):
            temp.insertNode(self.getNode(i).data)
        return temp


if(__name__ == "__main__"):
    llist = linkedlist()
    llist2 = linkedlist()

    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third

    llist2 = llist.reverseList()
    llist2.printList()
