# This is a sample Python script.
import random

from MonteCarloSimulation import MonteCarloSimulation
from OptimalPriceEstimator import OptimalPriceEstimator
import numpy as np
import scipy as sp


'''
Script to play with the simulations. Demand of the market in year is calculated with D = alpha * price ^ epsilon. 
So expected value for units sold for time range will be D' = D * days_left / 365.
Because of how customers are created in a simulation:
Alpha lays in the middle of range [number of customer * lower_bound_for_alph, upper of customer * lower_bound_for_alph]
Epsilon lays around -1.5.
'''

mcs = MonteCarloSimulation(lower_bound_for_alpha = 8000, upper_bound_for_alpha = 11000, number_of_customers = 500)

print("alpha factor of the market: " + str(mcs.alpha_mean))
print("elasticity of the market: " + str(mcs.epsilon_mean))
optimal_price_estimator = OptimalPriceEstimator(alpha_factor = mcs.alpha_mean, epsilon = mcs.epsilon_mean)


# Here you can play with the parameters
price_normal = 18
days_left = 3
cost = 5
reserve =1000

lam_normal = mcs.alpha_mean * price_normal ** mcs.epsilon_mean * days_left / 365
sold_amount = 0


list_of_sold_amount = []


for j in range(2000):
    for i in range(3):
        random_number = random.uniform(0, 1)
        k = sp.stats.poisson.ppf(random_number, lam_normal)
        if k <= reserve:
            sold_amount += k
        else:
            sold_amount += reserve

    list_of_sold_amount.append(sold_amount)
    sold_amount = 0

sold_amount_mean_value = np.array(list_of_sold_amount).sum() / 2000
print(f"profit with the normal price {price_normal}:")
print(price_normal * sold_amount_mean_value - reserve * cost)

price_optimal = optimal_price_estimator.optimal_price(0, 10000, reserve = reserve, days_left = days_left, cost=cost)

lam_optimal = mcs.alpha_mean * price_optimal ** mcs.epsilon_mean * days_left / 365
sold_amount = 0
list_of_sold_amount = []

for j in range(2000):
    for i in range(3):
        random_number = random.uniform(0, 1)
        k = sp.stats.poisson.ppf(random_number, lam_optimal)
        if k <= reserve:
            sold_amount += k
        else:
            sold_amount += reserve
    list_of_sold_amount.append(sold_amount)
    sold_amount = 0

sold_amount_mean_value = np.array(list_of_sold_amount).sum() / 2000

print(f"profit with the optimal price {price_optimal}:")
print(price_optimal * sold_amount_mean_value - reserve * 5)




