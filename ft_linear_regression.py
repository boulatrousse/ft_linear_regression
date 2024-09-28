import sys

from utils.get_data import get_data
from utils.errors import print_error
from utils.create_json_file import create_json_file

g_learning_rate = 0.75

class LinearRegression:
    
    def __init__(self, data, learning_rate):
        print("Init of LR class")
        self.data = data
        self.data_size = len(data)
        self.theta0 = 0
        self.theta1 = 0
        self.least_sq_sum = 0
        self.learning_rate = learning_rate

        
#-----------------------------------------------    
        
def main():
    args = sys.argv

    if len(args) != 2:
        print_error("ERROR: usage: python parsing.py [data.csv].")
        exit(1)
        
    data = get_data(args[1])
    create_json_file()
    
    LinearRegression(data, g_learning_rate)
    
if __name__ == "__main__":
    main()
