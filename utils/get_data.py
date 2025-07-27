import os
import csv
from utils.errors import print_error

def get_list(data: list[str], arg: str) -> list[str]:
    list = []

    for n in data:
        list.append(n.get(arg))
    return list


def row_is_valid(row: list[str]) -> bool:
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


def get_data(filename: str) -> list[str]:
    
    if not filename.endswith('.csv'):
        print_error("Wrong extension : file must be a [.csv].", True)
    if os.stat(filename).st_size == 0:
        print_error("Empty file.", True)
        
    data = []
    try:
        cwd = os.getcwd()
        open_filename = os.path.abspath(os.path.join("../", cwd, filename))
        
        with open(open_filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            first_line = next(reader)
            if first_line[0].isdigit():
                print_error("First row of the .csv must be the header.", False)
                raise

            for row in reader:
                if not row_is_valid(row):
                    raise
                
                data_line = { 'km': float(row[0]), 'price': float(row[1]) }
                data.append(data_line)
            
            if not data or len(data) <= 1:
                raise
    except:
        print_error("An error occured while trying to open the .csv.", True)
        
    return data