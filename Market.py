from Customer import Customer
from PriceSimulator import PriceSimulator


class Market:
    """
    Represents a market with a single product. Each price of the product will change under inflation.

    Attributes:
        price: price of the product on the current day
        day: day on the market
        price_simulator: gives new price of the product on the next day
        bought_amount_today: total amount of sold units of the product
    """

    def __init__(self, price,  price_simulator: PriceSimulator):
        """
        :param price: initial price of the product
        :param price_simulator: gives price of the product on the one next day
        """
        self.price = price
        self.day = 0
        self.price_simulator = price_simulator
        self.bought_amount_today = 0

    def update_market_state(self):
        new_price = self.price_simulator.next_day_price()
        self.day += 1
        self.price = new_price
        self.bought_amount_today = 0

    def single_buying_operation(self, customer: Customer, price):
        self.bought_amount_today += customer.consume(price)

    def get_total_bought_amount_today(self):
        return self.bought_amount_today

    def get_price(self):
        return self.price

