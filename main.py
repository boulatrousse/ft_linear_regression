import sys
from utils.get_data import get_data
from utils.errors import print_error
from utils.create_json_file import create_json_file
from ft_linear_regression import LinearRegression

g_learning_rate = 0.75

def main():
    args = sys.argv

    if len(args) != 2:
        print_error("ERROR: usage: python parsing.py [data.csv].")
        exit(1)
        
    data = get_data(args[1])
    
    model = LinearRegression(data, g_learning_rate)
    model.train_model()

    
if __name__ == "__main__":
    main()