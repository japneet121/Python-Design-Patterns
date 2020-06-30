'''
Composite pattern is a type of structural design pattern in which a class composes of group of objects of it's own types.
For example:
An employee class has the objects of it own type to store manager and subordinates details
'''


class Employee:
    def __init__(self,name,dept,manager=None):
        self.name=name
        self.dept=dept
        self.manager=manager
        self.subordinates=[]

    def add_subordinate(self,sub):
        self.subordinates.append(sub)

    def get_subordinates(self):
        return self.subordinates


e1=Employee("Vivek","Eng")
e2=Employee("Japneet","Eng",e1)
e3=Employee("Japneet","Eng",e1)

e2.add_subordinate(e1)
e2.add_subordinate(e3)

for e in e2.get_subordinates():
    print(e.name)