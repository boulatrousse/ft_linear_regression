# FT_LINEAR_REGRESSION

## Objective

The aim of this project is to introduce you to the basic concept behind machine learning.
For this project, you will have to create a program that predicts the price of a car by
using a linear function train with a gradient descent algorithm.

## Language and librairies used

- Python
- Matplotlib

## Mandatory part

Implementation of linear regression with a single feature : the mileage of the car.

There is two programs :
- The first program will be used to predict the price of a car for a given mileage.
When you launch the program, it should prompt you for a mileage, and then give you back the estimated price for that mileage. The program will use the following hypothesis to predict the price :

$estimatePrice(mileage) = θ_0 + (θ_1 ∗ mileage)$

- The second one will be used to train your model. It will read your dataset file and perform a linear regression on the data. Once the linear regression has completed, you will save the variables theta0 and theta1 for use in the first program. You will be using the following formulas :

$tmpθ_0 = learningRate ∗ $
$\frac{1}{m}$
$\sum_{i=0}^{m-1}$
$(estimateP rice(mileage[i]) − price[i])$

$tmpθ_1 = learningRate ∗ $
$\frac{1}{m}$
$\sum_{i=0}^{m-1}$
$(estimateP rice(mileage[i]) − price[i]) * mileage[i]$

## Bonus part

Here are some bonuses that could be very useful :
- Plotting the data into a graph to see their repartition.
- Plotting the line resulting from the linear regression into the same graph.
- A program that calculates the precision of the algorithm.