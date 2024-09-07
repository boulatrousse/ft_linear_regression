import sys

class ParseData:
    def __init__(self, filename):
        self.get_data(filename)
        
    def get_data(self, filename):
        try:
            filename = "../" + filename
            self.data = open(filename, "r")
            print("data was properly open\n")
            print(self.data.read())
        except:
            print("No data.csv file found. Please use a csv file.\n")
            exit(1)


#---------------------------------------------

def main():
    args = sys.argv
    args_len = len(args)

    if (args_len != 2):
        print("Usage: python parsing.py [filename.csv].\n")
        exit(1)
        
    linear_regression = ParseData(args[1])
    
if __name__ == "__main__":
    main()