import sys
import pkgutil
import readline
import inspect

import describe

def h(max_history=0):
    """Prints the history up to a certain max (max is optional)"""
    history_length = readline.get_current_history_length()
    max_length = history_length if max_history==0 else min(max_history, history_length)
    for i in range(max_length):
        print readline.get_history_item(i + 1)

def explore(package_name, offset="", show_classes_and_functions=False): 
    """Lists modules and functions available for a package"""
    try:
        package = __import__(package_name, fromlist="dummy")
        for importer, mod_name, ispkg in pkgutil.iter_modules(package.__path__):
            full_name = package_name + "." + mod_name
            print(offset + full_name)
            # print(offset + full_name + "  \t\t|  import " + full_name)
            if ispkg:
                explore(full_name, offset + "  ")
            else:
                if show_classes_and_functions:
                    # print (offset + "  ---- CLASSES ----")
                    explore_classes(full_name, offset + "  ")
                    # print (offset + "  ---- FUNCTIONS ----")
                    explore_functions(full_name, offset + "  ")
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))

def explore_functions(package_name, offset=""):
    try:
        package = __import__(package_name, fromlist="dummy")
        for name in dir(package):
            obj = getattr(package, name)
            if inspect.isfunction(obj):
                # print(offset + "[func]  " + obj.__name__ + "  \t\t|  from " + package_name + " import " + obj.__name__)
                print(offset + "[f] " + obj.__name__)
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))

def explore_classes(package_name, offset=""):
    try:
        package = __import__(package_name, fromlist="dummy")
        for name in dir(package):
            obj = getattr(package, name)
            if inspect.isclass(obj):
                # print(offset + "[class] " + obj.__name__ + "  \t\t|  from " + package_name + " import " + obj.__name__)
                print(offset + "[c] " + obj.__name__)
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print (offset + "Error: Couldn't import module %s - %s" % (package_name, e))
