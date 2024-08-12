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
        key = f"{obj.__class__.__name__}.{obj['id']}"
        self.__objects[key] = obj

    def save(self):
        """Save/serialize obj dictionaries to json file"""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)



    def reload(self):
        """deserializes the json file to __objects"""
        try:
            with open(self.__file_path,"r") as f:
                data = json.load(f)
                for key,value in data.items():
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

