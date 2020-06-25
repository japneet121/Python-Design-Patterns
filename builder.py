'''
A builder design pattern is a type of design pattern in which large complex objects are created without letting 
end user know about the complexity fo teh objects

E.g: In the example below teh document object is made up of text,image, line, table objects but the end used is
 not aware of creation of all these objects separately

'''


class Document:
    
    def __init__(self):
        print("Creating Document object")
        self.text_obj=Text()
        self.img_obj=Image()
        self.line_obj=Line()
        self.table_obj=Table()

class Text:

    def __init__(self):
        print("creating text object")

class Image:

    def __init__(self):
        print("creating image object")

class Line:

    def __init__(self):
        print("creating line object")

class Table:

    def __init__(self):
        print("creating table object")


doc=Document()