import sys

from utils.get_data import get_data
from utils.errors import print_error
from utils.create_json_file import create_json_file
from utils.normalization import data_normalization

g_learning_rate = 0.75

class args:
    KM = 'km'
    PR = 'price'

class LinearRegression:
    
    def __init__(self, data, learning_rate):
        print("Init of LR class")
        self.data = data
        self.data_size = len(data)
        self.theta0 = 0
        self.theta1 = 0
        self.least_sq_sum = 0
        self.learning_rate = learning_rate
        self.normalize_km_list = data_normalization(data, args.KM)
        self.normalize_price_list = data_normalization(data, args.PR)


        
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
