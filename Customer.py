import random
import numpy as np


class Customer:

    """
    The class represents a customer, who buys a product after his demand.
    A customer buys amount product in a single day after Poisson distribution, where mu = alpha * price ** epsilon /365.
    """

    def __init__(self, id, lower_bound_for_alpha, upper_bound_for_alpha):
        """
        Creates with random alpha and epsilon
        :param id: id of the customer
        """
        self.id = id
        self.alpha = random.uniform(lower_bound_for_alpha, upper_bound_for_alpha)
        self.epsilon = random.uniform(-1.01, -1.99)
        self.bought_today = 0

    def get_mu(self, price):
        return self.alpha * price ** self.epsilon / 365

    def consume(self, price) -> int:
        """
        Method gives random integer from a poisson distribution
        :param price: price of the product on the currrent day
        :return: random integer from poisson distribution
        """

        return np.random.poisson(self.get_mu(price))