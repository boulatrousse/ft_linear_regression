from utils.errors import print_error
import json

def is_input_valid(input):
    if not input.isdigit():
        print_error("Wrong format, please enter a number equal or greater than 0.")
        return False
    return True

def get_thetas():
    try:
        with open('params.json', 'r') as file:
            data = json.load(file)
    except:
        print_error("An error occured while opening the json file.")
        exit(1)

    try:
        theta0 = data['theta0']
        theta1 = data['theta1']
    except KeyError:
        print_error("An error occured while getting the thetas parameters.")
        exit(1)
    except:
        print_error("An error occured while parsing the json file.")

    return theta0, theta1

def predict_price():
    input_mileage = input("Enter a mileage: ")
    while not is_input_valid(input_mileage):
        input_mileage = input("Enter a mileage: ")

    theta0, theta1 = get_thetas()
    mileage = int(input_mileage)

    price = theta0 + (theta1 * mileage)
    print("Predicted price of the car is: ", str(price))
    

predict_price()