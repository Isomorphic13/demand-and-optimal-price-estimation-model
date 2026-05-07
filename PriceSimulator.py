import numpy as np

class PriceSimulator:
    """
    An instance of the class simulates growth of price of a product with geometric Brownian motion.

    Attributes:
        current_price: current price of the product
        """
    def __init__(self, s0, mu, sigma, dt = 1/252):
        """
        :param s0: initial price of the product
        :param mu: average proportional growth rate of the price process
        :param sigma: volatility of the price growth
        :param dt: time-step
        """
        self.current_price = s0
        self.mu = mu
        self.sigma = sigma
        self.dt = dt

    def next_day_price(self) -> float:
        """
        Calculates and updates the price for the next time step.
        Returns the new price.
        """

        z = np.random.standard_normal()

        drift = (self.mu - 0.5 * self.sigma ** 2) * self.dt
        diffusion = self.sigma * np.sqrt(self.dt) * z
        growth_factor = np.exp(drift + diffusion)
        self.current_price *= growth_factor

        return self.current_price