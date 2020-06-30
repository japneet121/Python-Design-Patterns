'''
Flyweight is a design pattern which is used to reduce the memory footprint of the objected created of  a class.
As per this design pattern, a class mentains a copy of all the created objects and before creating a new object class checks if the similar object 
exists in the list, if the object is there it returns the same object else creates a new objects and also adds it to the list
'''

class Shape:

    def __init__(self,type):
        self.type=type

    def show_type(self):
        print(self.type)

class ShapeFactory:
    
    def __init__(self):
        self.shapes=[]

    def get_object(self,type):
        for shape in self.shapes:
            if type == shape.type:
                return shape
        print("creating new object")
        sh= Shape(type)
        self.shapes.append(sh)
        return sh


sf=ShapeFactory()

sf.get_object("circle")
sf.get_object("circle")
sf.get_object("square")
