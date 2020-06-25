'''
    A singleton pattern is a mainly used with data adapters where we only need a single instance of the class
'''

class DbAdapter:
    
    __obj=None

    def __init__(self):
        if DbAdapter.__obj==None:
            DbAdapter.__obj=self
            print("Created a new instance")
        
    @staticmethod
    def return_instance():
        if DbAdapter.__obj==None:
            DbAdapter()
            return DbAdapter.__obj
        else:
            return DbAdapter.__obj
    

DbAdapter.return_instance()
DbAdapter.return_instance()