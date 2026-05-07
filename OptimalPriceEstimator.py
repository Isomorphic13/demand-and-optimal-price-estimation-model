import scipy as sp
import numpy as np

class OptimalPriceEstimator:

    """
    Estimates the optimal price of the product with given reserve in the inventory and days left before the expiration date.
    the total profit is calculated as price * units_sold - reserve * cost
    """

    def __init__(self, alpha_factor, epsilon):
        """
        :param alpha_factor: alpha factor of the market
        :param epsilon: elasticity of the market
        """
        self.alpha_factor = alpha_factor
        self.epsilon = epsilon

    def _get_current_lambda(self, price, days_left) -> float:
        """
        :param price: current price of the product
        :param days_left: days lest before the expiration date
        :return: mean value of sold product units adjusted for the days lest before the expiration date
        """
        return self.alpha_factor * price ** self.epsilon * (days_left / 365)


    def _expected_profit(self, price, reserve, days_left, cost):
        """

        :param price: current price of the product
        :param reserve: how many units of the product left in the reserve to be sold
        :param days_left: days lest before the expiration date
        :param cost: costs for a single product unit
        :return: expected sold units with the restriction that if the demand higher than reserve, only amount of product in the reserve can be sold
        """
        lambda_value = self._get_current_lambda(price, days_left)

        range_of_steps = np.arange(0, reserve + 1)
        probs = sp.stats.poisson.pmf(mu = lambda_value, k = range_of_steps)
        res = np.dot(range_of_steps, probs)

        expected_units = res + reserve * (1 - sp.stats.poisson.cdf(reserve, mu = lambda_value))

        return price * expected_units - reserve * cost

    def optimal_price(self, lower_bound, upper_bound, reserve, days_left, cost):
        """

        :param lower_bound: lower bound for the price interval, where the optimal price will be searched
        :param upper_bound: upper bound for the price interval, where the optimal price will be searched
        :param reserve: how many units of the product left in the reserve to be sold
        :param days_left: days lest before the expiration date
        :param cost: costs for a single product unit
        :return: gives the optimal price for the product with the given parameter
        """
        optimal_price = sp.optimize.minimize_scalar(
            lambda price: - self._expected_profit(price, reserve, days_left, cost),
             bounds = (lower_bound, upper_bound),
             method = "bounded")
        return optimal_price.x