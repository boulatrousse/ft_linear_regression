import sys
from statistics import mean
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

        self.km_list = self.get_list(data, args.KM)
        self.price_list = self.get_list(data, args.PR)
        self.normalize_km_list = data_normalization(data, args.KM)
        self.normalize_price_list = data_normalization(data, args.PR)
        
        self.x_mean = mean(self.km_list)
        print(self.x_mean)
        self.y_mean = mean(self.price_list)
        self.get_slope()


    def get_slope(self):
        tmp1 = 1
        tmp2 = 1
        for d in self.data:
            tmp1 += (d.get(args.KM) * d.get(args.PR)) - ((self.data_size) * self.x_mean * self.y_mean)
            tmp2 += (d.get(args.KM) * d.get(args.KM)) - ((self.data_size) * (self.x_mean * self.x_mean))
        print(tmp1/tmp2)

    def get_list(self, data, arg):
        list = []

        for n in data:
            list.append(n.get(arg))
        return list


        
#-----------------------------------------------    
        
def main():
    args = sys.argv

    if len(args) != 2:
        print_error("ERROR: usage: python parsing.py [data.csv].")
        exit(1)
        
    data = get_data(args[1])
    create_json_file()
    
    model = LinearRegression(data, g_learning_rate)

    
if __name__ == "__main__":
    main()
