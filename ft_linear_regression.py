from utils.normalization import data_normalization, get_list
from utils.get_data import get_data
from utils.errors import print_error
import sys
import json
import matplotlib.pyplot as plt

g_learning_rate = 20
g_max_iteration = 5000
g_min_slope = 0.0000001

class args:
    KM = 'km'
    PR = 'price'

class LinearRegression:
    
    def __init__(self, data, learning_rate):
        self.data = data
        self.learning_rate = learning_rate

        self.data_size = len(data)
        self.a = 0
        self.b = 0
        self.previous_a = 0
        self.previous_b = 0
        self.previous_cost = 0
        self.theta0 = 0
        self.theta1 = 0

        self.km_list = get_list(data, args.KM)
        self.price_list = get_list(data, args.PR)
        self.normalized_km_list = data_normalization(data, args.KM)
        self.normalized_price_list = data_normalization(data, args.PR)

        plt.ion()
        fig, self.ax = plt.subplots()

    def get_prediction(self, mileage):
        return (self.a + (self.b * mileage))
    
    def get_cost(self):
        cost = 0

        for i in range(0, self.data_size):
            prediction = self.get_prediction(self.normalized_km_list[i])
            try:
                tmp_cost = (prediction - self.normalized_price_list[i]) ** 2
                cost += tmp_cost
            except:
                print_error("Overflow error. You should check if the learning rate is not too high.", True)
        
        return (1 / (2 * self.data_size)) * cost
    
    def get_derivative(self):
        derivative_a = float(0)
        derivative_b = float(0)

        for i in range(0, self.data_size):
            prediction = self.get_prediction(self.normalized_km_list[i])
            derivative_a += (prediction - self.normalized_price_list[i])
            derivative_b += (prediction - self.normalized_price_list[i]) * self.normalized_km_list[i]

        derivative_a = (2 / self.data_size) * derivative_a
        derivative_b = (2 / self.data_size) * derivative_b

        return derivative_a, derivative_b
    
    def gradient_descent(self):
        derivative_a, derivative_b = self.get_derivative()

        self.previous_a = self.a
        self.previous_b = self.b
        self.a = self.previous_a - (self.learning_rate * derivative_a)
        self.b = self.previous_b - (self.learning_rate * derivative_b)

    def print_values(self, tmp_cost):
        print("Cost:", tmp_cost, "a:", self.a, "b:", self.b)

    def get_thetas(self):
        delta_x = max(self.km_list) - min(self.km_list)
        delta_y = max(self.price_list) - min(self.price_list)
        self.theta0 = ((delta_y * self.a) + min(self.price_list) - self.b * (delta_y / delta_x) * min(self.km_list))
        self.theta1 = delta_y * self.b / delta_x

    def write_in_json_file(self):
        dict = {
            'theta0': self.theta0,
            'theta1': self.theta1,
        }
    
        try:
            json_object = json.dumps(dict)
            
            with open("params.json", "w") as outfile:
                outfile.write(json_object)
        except:
            print_error("An error occured while creating the json file.", True)

    def train_model(self):
        for i in range(0, g_max_iteration):
            self.get_thetas()
            self.display()
            tmp_cost = self.get_cost()
            if abs(tmp_cost - self.previous_cost) < g_min_slope:
                print("Cost function converged after", i, "iterations with cost", tmp_cost)
                break
            self.gradient_descent()
            self.print_values(tmp_cost)
            self.previous_cost = tmp_cost
        
        plt.ioff()
        plt.show()
        self.get_thetas()
        self.write_in_json_file()

    def display(self):
        self.ax.clear()
        self.ax.plot(self.km_list, self.price_list, 'co')
        self.ax.set_title('Price of a car for a given mileage')
        self.ax.set_xlabel('Price')
        self.ax.set_ylabel('Mileage')
        self.ax.plot(self.km_list, self.get_line_coord(), 'r')

        plt.draw()
        plt.pause(0.075)

    def get_line_coord(self):
        list = []
        for i in range(0, self.data_size):
            tmp = self.theta0 + (self.theta1 * self.km_list[i])
            list.append(tmp)
        return list
            

def main():
    args = sys.argv

    if len(args) != 2:
        print_error("ERROR: usage: python parsing.py [data.csv].", True)
        
    data = get_data(args[1])
    
    model = LinearRegression(data, g_learning_rate)
    model.train_model()

    
if __name__ == "__main__":
    main()