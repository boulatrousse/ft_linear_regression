from utils.normalization import data_normalization

#derivative
#gradient_descent

class args:
    KM = 'km'
    PR = 'price'

class LinearRegression:
    
    def __init__(self, data, learning_rate):
        print("Init of LR class")

        self.data = data
        self.learning_rate = learning_rate

        self.data_size = len(data)
        self.a = 0
        self.b = 0
        self.previous_cost = 0
        self.least_sq_sum = 0

        self.km_list = self.get_list(data, args.KM)
        self.price_list = self.get_list(data, args.PR)
        self.normalized_km_list = data_normalization(data, args.KM)
        self.normalized_price_list = data_normalization(data, args.PR)

        self.get_cost()
        self.get_derivative()

    def get_cost(self):
        cost = 0

        for i in range(0, self.data_size):
            prediction = self.get_prediction(self.km_list[i])  #CHANGE TO NORMALIZED
            tmp_cost = (prediction - self.price_list[i]) ** 2  #CHANGE TO NORMALIZED
            cost += tmp_cost
        
        return (1 / (2 * self.data_size)) * cost
    
    def get_derivative(self):
        derivative_a = float(0)
        derivative_b = float(0)

        for i in range(0, self.data_size):
            prediction = self.get_prediction(self.km_list[i])  #CHANGE TO NORMALIZED
            derivative_a += (prediction - self.price_list[i])   #CHANGE TO NORMALIZED
            derivative_b += (prediction - self.price_list[i]) * self.km_list[i]  #CHANGE TO NORMALIZED

        derivative_a = (2 / self.data_size) * derivative_a
        derivative_b = (2 / self.data_size) * derivative_b
        
        return derivative_a, derivative_b


    def get_prediction(self, mileage):
        return (self.a + (self.b * mileage))

    def get_list(self, data, arg):
        list = []

        for n in data:
            list.append(n.get(arg))
        return list