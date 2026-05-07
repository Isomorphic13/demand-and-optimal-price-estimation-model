from BayesianUpdater import BayesianUpdater

import numpy as np
import matplotlib.pyplot as plt

from Customer import Customer
from Market import Market
from PriceSimulator import PriceSimulator

class MonteCarloSimulation:
    """
    Class that simulates random purchasing from customers and price growth. The simulation allow to check the Bayesian Updater correctness.
    """
    def __init__(self,number_of_customers, lower_bound_for_alpha, upper_bound_for_alpha, initial_price = 10 ):

        """

        :param number_of_customers: initial number of customers
        :param lower_bound_for_alpha: lower bound for the alpha parameter for a single customer
        :param upper_bound_for_alpha: upper bound for the alpha parameter for a single customer
        :param initial_price: initial price of the product
        """

        customers = [Customer(i, lower_bound_for_alpha, upper_bound_for_alpha) for i in range(number_of_customers)]

        price_simulator = PriceSimulator(s0 = initial_price, mu = 0.03, sigma = 1)

        market = Market(price= initial_price, price_simulator = price_simulator)
        epsilons = np.arange(-1, -2, -0.05).tolist()
        alphas = np.arange(number_of_customers * lower_bound_for_alpha, number_of_customers * upper_bound_for_alpha, 1000).tolist()

        bu = BayesianUpdater(alphas = alphas, epsilons = epsilons)

        # The simulation itself. Every customer buys product randomly each day

        for i in range(1000):
            price = market.get_price()
            for customer in customers:
                market.single_buying_operation(customer, price)

            bu.bayesian_update(market.get_total_bought_amount_today(), price)
            market.update_market_state()


        alpha_mean, epsilon_mean = bu.get_weighted_results()

        self.alpha_mean = alpha_mean
        self.epsilon_mean = epsilon_mean
