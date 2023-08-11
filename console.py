#!/usr/bin/python3
""" Module for a custom python console """
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Command interpreter class for running commands at a prompt
        Attributes:
            Prompt (str): a default prompt phrase
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        'EOF command to the program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
