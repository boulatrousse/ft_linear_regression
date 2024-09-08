import os
import csv
import sys

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
    
    if not filename.endswith('.csv'):
        print("Wrong extension : file must be a [.csv].")
        
    data = []
    try:
        open_filename = os.path.abspath(os.path.join("../ft_linear_regression", filename))
        
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
        print("An error occured while trying to open the .csv.")
        exit(1)
        
    return data