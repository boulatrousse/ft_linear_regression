import json

from utils.errors import print_error


def create_json_file():
    dict = {
        'theta0': 0,
        'theta1': 0,
    }
    
    try:
        json_object = json.dumps(dict)
        
        with open("params.json", "w") as outfile:
            outfile.write(json_object)
    except:
        print_error("An error occured while creating the json file.", True)
