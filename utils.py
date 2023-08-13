#!/usr/bin/python3
""" Contains helper functions """
from models import storage, base_model
classes = {"BaseModel": base_model.BaseModel}


def check_cls_exists(cls_name):
    """ checks if a class name exists
        params:
            cls_name (str): class to lookup
        Returns:
            True if exists else false
    """
    if cls_name not in classes:
        print("** class doesn't exist **")
        return False
    return True


def validate_args(args):
    """ validates command arguments and prints Error if any
        params:
            args (str): list of arguments to validate
        Returns:
            a list of arguments if all valid or none and prints error
    """
    if len(args) == 0:
        print("** class name missing **")
        return None
    args = args.split(maxsplit=3)
    if not check_cls_exists(args[0]):
        return None
    elif len(args) < 2:
        print("** instance id missing **")
        return None
    elif not args[0]+"."+args[1] in storage.all().keys():
        print("** no instance found **")
        return None
    return args


def validate_update_args(args):
    """ Validates the arguments passed to the update command
        params:
            args (str): list of arguments passed
    """
    up_args = validate_args(args)
    if not up_args:
        return None
    if len(up_args) < 3:
        print("** attribute name missing **")
        return None
    if len(up_args) < 4:
        print("** value missing **")
        return None

    up_args[3] = up_args[3].lstrip("\"").split("\"")[0]
    return up_args


def cast_to_type(value=""):
    """Cast a string value to its valid type
    params:
        value (str): string value to cast
    Returns:
        casted value or value if cast not possible
    """
    if value.isdigit():
        return int(value)
    if value.isdecimal():
        return float(value)
    if value.startswith("-"):
        if value[1:].isdigit():
            return int(value)
        elif value[1:].isdecimal():
            return float(value)
    return value
