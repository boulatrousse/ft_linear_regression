import os
import csv
from utils.errors import print_error

def row_is_valid(row):
    row1 = row[0]
    row2 = row[1]
    row_len = len(row)
    
    if not row1.isnumeric() or not row2.isnumeric():
        print_error("CSV file must contain only numbers.", False)
        return False
    if row_len != 2:
        print_error("CSV lines must contain only 2 rows.", False)
        return False
    return True

def get_data(filename):
    
    if not filename.endswith('.csv'):
        print_error("Wrong extension : file must be a [.csv].", True)
    if os.stat(filename).st_size == 0:
        print_error("Empty file.", True)
        
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
                
                data_line = { 'km': float(row[0]), 'price': float(row[1]) }
                data.append(data_line)
    except:
        print_error("An error occured while trying to open the .csv.", True)
        
    return data