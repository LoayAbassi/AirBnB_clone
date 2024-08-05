#!/usr/bin/python3

import cmd


class command(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):
        print("hello ya weldi")
        print("eb3edni ya khra")

    def do_EOF(self, line):
        print()
        return True
    
    def do_help(self, line):
        print(su)
