import os
import csv
import sys

from create_json_file import create_json_file

def row_is_valid(row):
    row1 = row[0]
    row2 = row[1]
    row_len = len(row)
    if not row1.isnumeric() or not row2.isnumeric():
        print("CSV file must contain only numbers.")
        return False
    if row_len != 2:
        print("CSV lines must contain only 2 rows.")
        return False
    return True

def get_data(filename):
    
    data = []
    try:
        open_filename = os.path.abspath(os.path.join("../", filename))
        
        with open(open_filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            try:
                next(reader)
            except StopIteration:
                pass

            for row in reader:
                if not row_is_valid(row):
                    raise
                
                data_line = { 'km': row[0], 'price': row[1] }
                data.append(data_line)
    except:
        exit(1)
        
    return data
 
def main():
    args = sys.argv

    if len(args) != 2:
        print("ERROR: usage: python parsing.py [data.csv].")
        exit(1)
        
    create_json_file()
    data = get_data(args[1])
    
    print("data = ")
    for item in data:
        print(item['km'], "-", item['price'])
    
if __name__ == "__main__":
    main()