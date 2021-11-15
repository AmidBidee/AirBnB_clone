#!/usr/bin/python3
"""HBNB console module
"""

import cmd
#from models import *


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB backend

    Args:
        cmd ([type]): [description]

    Returns:
        [type]: [description]
    """
    prompt = '(hbnb)'
    #storage.reload()

    valid_classes = ["BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review"]

    def empytline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit interpreter

        Args:
            args ([type]): [description]
        """
        quit()

    def do_EOF(self, args):
        """
        executes EOF(CTRL + D) to exit interpreter
        """
        print("")
        return True


if __name__ == '__main__':
    """
    start cmd loop
    """
    HBNBCommand().cmdloop()
