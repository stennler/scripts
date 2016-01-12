# Importing other python packages to wrap in this script.
import explore as zExplore
import history as zHistory


def import_all(import_dict):
    """This will add all the functions in zutil to the dictionary arg."""
    import_dict['h'] = h
    import_dict['explore'] = explore


def h(max_history=25):
    """Prints the history up to a certain max (max is optional)"""
    zHistory.h(max_history)


def explore(package_name, show_classes_and_functions=False, offset=""):
    """Recursively lists modules in a package.

       If True is passed as 2nd arg it will list classes and functions too.
       """
    zExplore.explore(package_name, show_classes_and_functions, offset)
