'''
Base Database class
'''
class Database:
    def __init__(self):
        pass

    def get_data(self):
        pass

    def set_data(self,data):
        pass


'''
An interface between Sql Server and Application
'''
class SqlAdapter(Database):
    def __init__(self):
        super().__init__()

    def get_data(self):
        print("get data from Sql")

    def set_data(self,data):
        print("set data to Sql") 


'''
An interface between Mongo Server and Application
'''
class MongoAdapter(Database):
    def __init__(self):
        super().__init__()

    def get_data(self):
        print("get data from Mongo")

    def set_data(self,data):
        print("set data to Mongo") 



db=SqlAdapter()
dbm=MongoAdapter()