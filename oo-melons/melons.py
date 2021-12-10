import random
from datetime import datetime

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class TooManyMelonsError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


"""Classes for melon orders."""
class AbstractMelonOrder():
    def __init__(self, species, qty, country_code,order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        if(qty <= 100):
           self.qty = qty
        else:
            raise TooManyMelonsError('qty > 100', "There's too many")
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
        

    def get_base_price(self):
        base_price = random.randint(5,9)
        if datetime.weekday(datetime.now()) < 5 and datetime.weekday(datetime.now()) >= 0 and datetime.timetuple(datetime.now())[3] >= 8 and datetime.timetuple(datetime.now())[3] <= 11:
            base_price = base_price + 4
        return base_price


    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        
        if self.species == "Winter Melon":
            base_price = 5 * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        print(total)
        if self.order_type == "international" and self.qty < 10:
            total = total + 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "USA", "domestic", 0.08)
 


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code, "international", 0.17)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty,"USA","Domestic", 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed