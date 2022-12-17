from pymongo import MongoClient
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username="aacuser", password="Mangopwd123"):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:50565' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:50565')
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary 
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("data parameter is empty")


    # Create method to implement the R in CRUD.
    def read(self,criteria=None):

        # criteria is not None then this find will return all rows which matches the criteria
        if criteria:
         # {'_id':False} just omits the unique ID of each row        
            
            data = self.database.animals.find(criteria,{"_id":False})
        else:
        #if there is no search criteria then all the rows will be return  
            data = self.database.animals.find( {} , {"_id":False})

        return data