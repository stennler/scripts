#!/usr/bin/python
import json
from pprint import pprint
import os

sourceDir = "/Users/zfleischman/repos/farm2-new"
animalFile = "/Users/zfleischman/repos/farm2-new/data/entity_templates/e_animal_adult_chicken_sultanblack.json"

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
            print parentType
            if parentType in comps:
                comps[parentType] += 1
            else:
                comps[parentType] = 1
            print parentType
            print comps
            return
        except KeyError:
            return
        except TypeError:
            return
    except ValueError:
        return

addCompsFromFile(animalFile)

# Print Components
for item in comps:
    print item + ": " + str(comps[item])
