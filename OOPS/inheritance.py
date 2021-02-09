class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname + " " + self.lname)


class Student(Person):  # this is inheriting Person class to Student class
    pass


me = Student('Omkar', 'Walhekar')
print(me.fname)
