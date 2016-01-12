import inspect

import zutil

# Importing other python packages to wrap in this script.
import explore as zExplore
import history as zHistory


def import_all(import_dict):
    """This will add all the functions in zutil to the dictionary arg."""
    for name, func in inspect.getmembers(zutil, inspect.isfunction):
        if name != 'import_all':
            import_dict[name] = func


def zlist():
    """Lists all the zutil functions"""
    members = inspect.getmembers(zutil, inspect.isfunction)
    members.sort()
    for name, func in members:
        print("-"*(1+len(name)))
        print("%s:" % name)
        print("-"*(1+len(name)))
        print(func.__doc__)
        print("")
        print("")


def h(max_history=25):
    """Prints the history up to a certain max (max is optional)"""
    zHistory.h(max_history)


def explore(package_name, show_classes_and_functions=False, offset=""):
    """Recursively lists modules in a package.

If True is passed as 2nd arg it will list classes and functions too.
"""
    zExplore.explore(package_name, show_classes_and_functions, offset)
