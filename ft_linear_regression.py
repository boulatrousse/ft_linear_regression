import os
import sys

from utils.get_data import get_data
from utils.create_json_file import create_json_file


def main():
    args = sys.argv

    if len(args) != 2:
        print("ERROR: usage: python parsing.py [data.csv].")
        exit(1)
        
    data = get_data(args[1])
    create_json_file()
    
    print("data = ")
    for item in data:
        print(item['km'], "-", item['price'])
    
if __name__ == "__main__":
    main()