#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
print()
print()
print()
print()

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "abassi"
my_model.my_number = 555
print(my_model)
print()
print()
print()
print()
my_model.save()
print(my_model)
