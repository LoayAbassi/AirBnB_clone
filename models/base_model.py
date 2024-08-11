#!/usr/bin/python3
"""
this the basemodule class location where every other calass 
will inherit from 
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """attributes and methods are below"""

    def __init__(self,*args,**kwargs):
        """this is the constructor method."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """this is the string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the updated_at attribute to the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        dict_rep = self.__dict__.copy() # just avoiding problems 
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
    


