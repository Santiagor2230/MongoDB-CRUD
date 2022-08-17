from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

class AnimalShelter(object):
    
    def __init__(self,user,password):
        #intilializing the monogClient
        self.client = MongoClient('mongodb://%s:%s@localhost:36449/AAC' % (user, password))
        self.database = self.client['AAC']
        
        #Creates a new instance inside the database
    def create(self,data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        
        else:
            return False
            
        #Allows to read data from the database AAC.animals
    def read(self,find_data):
        if find_data is not None:
             return self.database.animals.find(find_data)
        
        else:
            raise Exception("There is no such data")
        
    def update(self, query, new_data):
        if new_data is not None:
            if new_data:
                self.database.animals.update_many(query, new_data)
                return "Succesfully updated:"," ", new_data
        
        else:
            raise Exception("There is no way to update")
            
    def delete(self,data):
        if data is not None:
            if data:
                result = self.database.animals.delete_many(data)
                return "Succesfully deleted", result.deleted_count
        
        else:
            raise Exception("There is no such data to delete")