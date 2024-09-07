import os
import csv
import sys

# def is_row_valid(row1, row2, row_len):
    
#     if int(row1) < 0 or int(row2) < 0:
#         print("CSV data cannot be negative.")
#         return False
#     if row1.isnumeric() == False or row2.isnumeric() == False:
#         print("CSV file must contain only numbers.")
#         return False
#     if row_len != 2:
#         print("CSV lines must contain only 2 rows.")
#         return False
#     return True

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
                if int(row[0]) < 0 or int(row[1]) < 0:
                    print("CSV data cannot be negative.")
                    raise
                if row[0].isnumeric() == False or row[1].isnumeric() == False:
                    print("CSV file must contain only numbers.")
                    raise
                if len(row) != 2:
                    print("CSV lines must contain only 2 rows.")
                    raise
                
                data_line = { 'km': row[0], 'price': row[1] }
                data.append(data_line)
            
    except:
        print("EXIT")
        exit(1)
        
    for item in data:
        print(item['km'], "-", item['price'])
           
           
#-------------------------------------------------------------------------
 
def main():
    args = sys.argv
    get_data(args[1])
    
if __name__ == "__main__":
    main()