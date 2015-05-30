#!/usr/bin/python
import json
from pprint import pprint
import os
import operator

sourceDir = "/Users/zfleischman/repos/farm2-new"

comps = dict()
def addCompsFromFile(f):  
    global comps
    try:
        rawJsonFile = open(f)
        rawJsonData = rawJsonFile.read()
        rawJsonFile.close()
        jsonData = json.loads(rawJsonData)
        try:
            parentType = jsonData["@type"]
            if parentType in comps:
                comps[parentType] += 1
            else:
                comps[parentType] = 1
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
for item,value in sorted(comps.items(), key=operator.itemgetter(1), reverse=True):
    print item + ": " + str(value)

