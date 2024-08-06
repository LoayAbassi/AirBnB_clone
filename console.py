#!/usr/bin/python3

import cmd
import sys


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    
if __name__=="__main__":
    if len(sys.argv) > 1:
        command = ' '.join(sys.argv[1:])
        HBNBCommand().onecmd(command)
    else:
        HBNBCommand().cmdloop()
