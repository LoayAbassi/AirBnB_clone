#!/usr/bin/python3
import cmd
import sys

class HBNBcommand(cmd.Cmd):

    prompt="(hbnb)"
    
    def do_quit(self,args):
        """Quit command to exit the program"""
        return True
    
    def do_help(self,args):
        """shows a list of usable commands"""

    