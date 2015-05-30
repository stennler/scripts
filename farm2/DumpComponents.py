#!/usr/bin/python
import json
from pprint import pprint
import os

sourceDir = "/Users/zfleischman/repos/farm2-new"

comps = []
def addCompsFromFile(f):  
    global comps
    try:
        rawJsonFile = open(f)
        rawJsonData = rawJsonFile.read()
        rawJsonFile.close()
        jsonData = json.loads(rawJsonData)
        try:
            listOfUComponents = jsonData["components"].keys()
            comps.extend(listOfUComponents)
            comps = list(set(comps))
            return
        except KeyError:
            return
        except TypeError:
            return
    except ValueError:
        return

for dirname, dirnames, filenames in os.walk(sourceDir):
    # print path to all filenames.
    for filename in filenames:
        fname, fextension = os.path.splitext(filename)
        if fextension == ".json":
            addCompsFromFile(os.path.join(dirname, filename))

    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')

# Print Components
listOfComponents = [x.encode("UTF8") for x in comps]
for component in sorted(listOfComponents):
    print component

