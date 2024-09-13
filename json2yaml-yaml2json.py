#!/usr/bin/env python3

import yaml
import json
import sys
import os


def jsonfile():
    with open(x, "r") as jsonFile:
        data = json.load(jsonFile)
    with open(name + ".yaml", "w") as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)


def yamlfile():
    with open(x, "r") as yamlFile:
        contents = yamlFile.read()
        data = yaml.safe_load(contents)
        out = json.dumps(data, indent=1)
        with open(name + ".json", "w") as outfile:
            outfile.write(out)


def unknownfile():
    isValidJson = True
    isValidYaml = True
    print("\n   I don't recognise the file extension", extension)
    print("   Let's have a look at it's contents...\n")
    with open(x, "r") as file:
        config = file.read()
    try:
        json.loads(config)
    except:
        isValidJson = False
    try:
        yaml.safe_load(config)
    except:
        isValidYaml = False
    if isValidJson:
        print("JSON Detected\n Converting to YAML...")
        try:
            jsonfile()
        except:
            print(errmsg)
            quit()
    if isValidYaml and isValidJson == False:
        print("YAML Detected\n Converting to JSON...")
        try:
            yamlfile()
        except:
            print(errmsg)
            quit()


for i in range(1, len(sys.argv)):
    x = sys.argv[i]
    errmsg = "\n   File \"" + x + "\" is missing or it's content's format does not match it's file extension.\n"
    name, extension = os.path.splitext(x)

    if extension == ".yaml" or extension == ".yml":
        try:
            yamlfile()
        except:
            print(errmsg)
            quit()
    elif extension == ".json":
        try:
            jsonfile()
        except:
            print(errmsg)
            quit()
    else:
        try:
            unknownfile()
        except:
            print(errmsg)
            quit()

print("\n >> It worked! <<\n")
