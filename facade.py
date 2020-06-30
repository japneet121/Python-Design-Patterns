'''
Facade pattern helps in hiding the complexity of creating multiple objects from user and encapsulating many objects under one object.
This helps in providing unified interface for end user
'''

class OkButton:
    
    def __init__(self):
        pass
    
    def click(self):
        print("ok clicked")

class CancelButton:

    def __init__(self):
        pass
    
    def click(self):
        print("cancel clicked")

class SaveButton:
    def __init__(self):
        pass

    def click(self):
        print("save clicked")


'''
Page class encapsulates the behaviour of all the three buttons and the end user only needs to manage one object
'''
class Page:

    def __init__(self):
        self.ok=OkButton()
        self.save=SaveButton()
        self.cancel=CancelButton()

    def press_ok(self):
        self.ok.click()
    
    def press_save(self):
        self.save.click()

    def press_cancel(self):
        self.cancel.click()



p=Page()
p.press_cancel()
p.press_ok()
p.press_save()