class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("Head")
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def peek(self):
        if(self.isEmpty()):
            raise Exception("Stack is empty")
        return self.head.next.data

    def pop(self):
        if(self.isEmpty()):
            raise Exception("Stack is empty")

        nxt = self.head.next.next
        val = self.head.next.data
        del self.head.next
        self.head.next = nxt
        self.size -= 1
        return val

    def __str__(self):
        cur = ''
        temp = self.head.next
        while(temp):
            cur += str(temp.data) + '->'
            temp = temp.next
        return cur[:-2]


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
