import pkgutil
def list_mods(package_name, offset=""): 
    try:
        package = __import__(package_name, fromlist="dummy")
        for importer, mod_name, ispkg in pkgutil.iter_modules(package.__path__):
            full_name = package_name + "." + mod_name
            print(offset + full_name)
            if ispkg:
                list_mods(package_name + "." + mod_name, offset + "  ")
    except:
        print (offset + "[Couldn't import module: %s]" % package_name)
