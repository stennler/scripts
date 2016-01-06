import pkgutil
import readline

def h(max_history=0):
    """Prints the history up to a certain max (max is optional)"""
    history_length = readline.get_current_history_length()
    max_length = history_length if max_history==0 else min(max_history, history_length)
    for i in range(max_length):
        print readline.get_history_item(i + 1)

def explore(package_name, offset=""): 
    """Lists modules and functions available for a package"""
    try:
        package = __import__(package_name, fromlist="dummy")
        for importer, mod_name, ispkg in pkgutil.iter_modules(package.__path__):
            full_name = package_name + "." + mod_name
            print(offset + full_name)
            if ispkg:
                explore(full_name, offset + "  ")
    except:
        print (offset + "[Couldn't import module: %s]" % package_name)
