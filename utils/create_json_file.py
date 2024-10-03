import json
from utils.errors import print_error

def create_json_file(theta0, theta1):
    dict = {
        'theta0': theta0,
        'theta1': theta1,
    }
    
    try:
        json_object = json.dumps(dict)
        
        with open("params.json", "w") as outfile:
            outfile.write(json_object)
    except:
        print_error("An error occured while creating the json file.")
        exit(1)
