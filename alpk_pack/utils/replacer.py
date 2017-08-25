import re
import json


def getRegexDict(file_name):
    regex_dictionary={}
    with open(file_name) as json_file:
        json_dict=json.load(json_file)
        for key, value in json_dict.items():
            regex=""
            for token in value:
                regex += str(token)
                regex += "|"
            regex = regex[:-1]
            
            regex_dictionary[key]=regex
    return regex_dictionary

def replace(text, regexDict):
    """
    For all keys in regexDict dictionary substitute regexDict key string when its corresponding 
    value(which is regex pattern) is found in the text    
    """
    for key in regexDict:
        if key == "empty":
            print(key,": ", regexDict[key])
            text = re.sub(regexDict[key], "", text)
        else:
            text = re.sub(regexDict[key], key, text)

    return text