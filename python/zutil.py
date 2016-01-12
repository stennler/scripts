import inspect
import pkgutil
import readline
import sys


def h(max_history=0):
    """Prints the history up to a certain max (max is optional)"""
    history_length = readline.get_current_history_length()
    max_length = history_length if max_history == 0 else min(max_history, history_length)  # nopep8
    for i in range(max_length):
        print(readline.get_history_item(i + 1))


def explore(package_name, offset="", show_classes_and_functions=False):
    """Lists modules and functions available for a package"""
    try:
        package = __import__(package_name, fromlist="dummy")
        for importer, mod_name, ispkg in pkgutil.iter_modules(package.__path__):  # nopep8
            full_name = package_name + "." + mod_name
            print(offset + full_name)
            if ispkg:
                explore(full_name, offset + "  ")
            else:
                if show_classes_and_functions:
                    explore_classes(full_name, offset + "  ")
                    explore_functions(full_name, offset + "  ")
    except AttributeError:
        print (package_name)
        if show_classes_and_functions:
            explore_classes(package_name, offset + "  ")
            explore_functions(package_name, offset + "  ")
    except Exception:  # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))  # nopep8


def explore_functions(package_name, offset=""):
    try:
        package = __import__(package_name, fromlist="dummy")
        for name in dir(package):
            obj = getattr(package, name)
            if inspect.isfunction(obj):
                print(offset + "[f] " + obj.__name__)
    except AttributeError:
        explore_classes(package_name, offset + "  ")
        explore_functions(package_name, offset + "  ")
    except Exception:  # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))  # nopep8


def explore_classes(package_name, offset=""):
    try:
        package = __import__(package_name, fromlist="dummy")
        for name in dir(package):
            obj = getattr(package, name)
            if inspect.isclass(obj):
                print(offset + "[c] " + obj.__name__)
    except AttributeError:
        explore_classes(package_name, offset + "  ")
        explore_functions(package_name, offset + "  ")
    except Exception:  # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))  # nopep8
