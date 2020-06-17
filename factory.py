# A factory pattern is a creational design pattern which helps outside world to create objects without even knowing about 
# how the actual objects are getting created, hence maintaining the abstraction about object creation


'''
    Factory class which helps in creation different types of documents
'''
class DocumentFactory:
    def __init__(self):
        pass

    def write(self,text):
        pass

    @classmethod
    def get_document(self,type):
        if type=="pdf" or type=="PDF":
            return Pdf()

        elif type=="word" or type=="Word":
            return Word()
        
        elif type=="Img" or type=="img":
            return Img()



'''
    Individual implementation of different documents 
'''

class Pdf:
    def __init__(self):
        print("Created a PDF document")    


class Img:
    def __init__(self):
        print("Created a Img document")    


class Word:
    def __init__(self):
        print("Created a Word document")    



#Factory in play
DocumentFactory.get_document("Img")
DocumentFactory.get_document("PDF")
DocumentFactory.get_document("Word")
print(globals())