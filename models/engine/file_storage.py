#!/usr/bin/python3

"""filestorage class location"""
import json
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return self.__objects

    def new(self,obj):
        """adds new objects to dict of objs"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes the __objects to json file"""
        with open(self.__file_path,"w") as f:
            json.dump(self.__objects,f)

    def reload(self):
        """deserializes the json file to __objects"""
        try:
            with open(self.__file_path,"r") as f:
                data = json.load(f)
                for key,value in data.items():
                    
                    
                

        except FileNotFoundError:
            pass
