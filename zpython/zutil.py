import inspect

import zutil

# Importing other python packages to wrap in this script.
import counsyl_utils as zCounsyl_utils
import explore as zExplore
import history as zHistory


def import_all(import_dict):
    """This will add all the functions in zutil to the dictionary arg."""
    for name, func in inspect.getmembers(zutil, inspect.isfunction):
        if name != 'import_all':
            import_dict[name] = func


def loop(iters, f, *args, **kwargs):
    """Execute the passed in function iters times"""
    return [f(*args, **kwargs) for x in range(iters)]


def zlist():
    """Lists all the zutil functions and their docs"""
    members = inspect.getmembers(zutil, inspect.isfunction)
    members.sort()
    for name, func in members:
        if name != 'import_all':
            num_hypens = max(5, 1+len(name))
            print("-"*num_hypens)
            print("%s:" % name)
            print("-"*num_hypens)
            print(func.__doc__)
            print("")


def zls(verbose=None):
    """Lists all the zutil functions (one line each)"""
    if verbose:
        return zlist()
    members = inspect.getmembers(zutil, inspect.isfunction)
    members.sort()
    i = 1
    for name, func in members:
        if name != 'import_all':
            print("{}:\t{}\t\t-{}".format(i, name, func.__doc__.split('\n')[0]))  # nopep8
            i += 1


def h(max_history=25):
    """Prints the history up to a certain max (max is optional)"""
    zHistory.h(max_history)


def explore(package_name, show_classes_and_functions=False, offset=""):
    """Recursively lists modules in a package.

       If True is passed as 2nd arg it will list classes and functions too.
    """
    zExplore.explore(package_name, show_classes_and_functions, offset)


####################################
##### Counsy Related Shortcuts #####
####################################


def sp(cp=None, short=False):
    """Dumps and returns a human readable version of the CustomerProfile object

       No params: Dumps and returns all CustomerProfiles as a QuerySet.
       First Param is integer: Dump and return the 'x'th CustomerProfile.
       First Param is a Customer Profile Object: Dump and return it.
       short kwarg dumps all profiles on one line.
    """
    return zCounsyl_utils.show_profile(cp, short)


def sps(cp=None):
    """Shortcut for sp(short=True)"""
    return sp(cp, True)


def dp(pk):
    """Delete's the CustomerProfile object with the given primary key (or list of keys)"""  # nopep8
    zCounsyl_utils.delete_profile(pk)
    return sps()

