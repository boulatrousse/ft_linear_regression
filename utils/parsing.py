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
                valid_row = row_is_valid(row)
                if not valid_row:
                    raise
                
                data_line = { 'km': row[0], 'price': row[1] }
                data.append(data_line)
            
    except:
        exit(1)
        
    for item in data:
        print(item['km'], "-", item['price'])
        
    return data

#-------------------------------------------------------------------------
 
def main():
    args = sys.argv
    get_data(args[1])
    
if __name__ == "__main__":
    main()