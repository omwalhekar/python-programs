class node:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def nameFunc(self):
        print("Hello, My name is " + self.name +
              " and my age is " + str(self.age))


t = node('Omkar Walhekar', 20)
t.nameFunc()
del t
t.nameFunc()
