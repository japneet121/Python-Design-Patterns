class DocumentFactory:
    def __init__(self):
        pass
    @classmethod
    def get_document(self,type):
        if type=="image" or type=="Image":
            return ImageFactory()

        elif type=="Text" or type=="text":
            return TextFactory()


class TextFactory:
    def __init__(self):
        pass
    
    @classmethod
    def get_document(self,type):
        if type=="pdf" or type=="PDF":
            return Pdf()

        elif type=="word" or type=="Word":
            return Word()
        

class ImageFactory:
    def __init__(self):
        pass

    @classmethod
    def get_document(self,type):
        if type=="Img" or type=="img":
            return Img()

        elif type=="Gif" or type=="gif":
            return Gif()


class Pdf:
    def __init__(self):
        print("Created a PDF document")    


class Word:
    def __init__(self):
        print("Created a Word document")    


class Img:
    def __init__(self):
        print("Created a Img document")    


class Gif:
    def __init__(self):
        print("Created a Img document")    





doc=DocumentFactory.get_document("Text")
doc.get_document("Word")