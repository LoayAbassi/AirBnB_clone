# python
import unittest
self.assertIsInstance(obj, cls)
// used within unit testing for auto error report

"BaseModel" is a base class in frameworks like Pydantic or ORMs that provides common functionality and attributes for other models to inherit.
class for all other classes to inhirit from 

# __init__.py
instead of importing each file of a dir alone like bleow : 
    from dir.f1 import obj 
    from dir.f2 import obj 

we can use the init file that takes care of everything for us 
import dir // once u import a dir it runs the __init__ automatically 

__init__.py will contain all the from dir.fn import obj
then when we type import dir in any module it will be easier to use them
in multiple files 

NB : JSON files for data storage

# args vs kwargs

function(A,B,C)

A: 1st positional argument example 5
B: (args)rest of normal arguments example(4,8,9,19)
C: (kwargs) after args tuple format , example (a=5,8=7,x=9)

