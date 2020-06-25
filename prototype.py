'''
Prototype pattern is required when we want to clone an object
'''

import copy

class Document:
    def __init__(self):
        pass
    
    #create a copy of existing object
    def clone(self):
        return copy.copy(self)


doc=Document()
new_doc=doc.clone()

#this will print different id's
print(id(doc))
print(id(new_doc))