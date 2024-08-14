#!/usr/bin/python3
"""console file"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = "(hbnb)"
    def do_quit(self,arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True
    
    def emptyline(self):
        """does nothing when uuser puts empty line"""
        pass
    
    def do_create(self,arg):
        """create a new instance of a class and save it to file"""
        if not arg:
            print("** class name missing **")
        else:
            cls = globals().get(arg)
            if not cls:
                print("** class doesn't exist **")
                return
            
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self,arg):
        """prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            cls = globals().get(args[0])
            if not cls:
                print("** class doesn't exist **")
                return
            try:
                """here goes the code after id is found"""
                objects = storage.all()
                form = f"{args[0]}.{args[1]}"

                if form in objects:
                    print(objects[form])
                else:
                    print("** no instance found **")
            except:
                print("** instance id missing **")

    def do_destroy(self,arg):
        """deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            cls = globals().get(args[0])
            if not cls:
                print("** class doesn't exist **")
                return
            try:
                """here goes the code after id is found"""
                objects = storage.all()
                print("read file")
                form = f"{args[0]}.{args[1]}"

                if form in objects:
                    del objects[form]
                    storage.save()
                else:
                    print("** no instance found **")
            except:
                print("** instance id missing **")

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()