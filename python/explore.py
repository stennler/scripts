import inspect
import pkgutil
import sys


def explore(package_name, show_classes_and_functions=False, offset=""):
    """Lists modules and functions available for a package"""
    try:
        package = __import__(package_name, fromlist="dummy")
        for importer, mod_name, ispkg in pkgutil.iter_modules(package.__path__):  # nopep8
            full_name = package_name + "." + mod_name
            print(offset + full_name)
            if ispkg:
                explore(full_name, show_classes_and_functions, offset + "  ")
            else:
                if show_classes_and_functions:
                    explore_classes(full_name, offset + "  ")
                    explore_functions(full_name, offset + "  ")
    except AttributeError:
        print (offset + package_name)
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
                print(offset + "F - " + obj.__name__)
    except Exception:  # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))  # nopep8


def explore_classes(package_name, offset=""):
    try:
        package = __import__(package_name, fromlist="dummy")
        for name in dir(package):
            obj = getattr(package, name)
            if inspect.isclass(obj):
                print(offset + "C - " + obj.__name__)
    except Exception:  # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))  # nopep8
