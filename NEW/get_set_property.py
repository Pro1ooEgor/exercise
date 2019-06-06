# two ways to use properties in python


# first, using the built-in decorator property
class Car:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price in range(2000, 2018):
            self.__price = price
        elif price < 2000:
            self.__price = 2000
        elif price > 2018:
            self.__price = 2018

    @price.deleter
    def price(self):
        del self.__price


c = Car(2017)
print(c.price)


# second, using the property function
class Car:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price in range(2000, 2018):
            self.__price = price
        elif price < 2000:
            self.__price = 2000
        elif price > 2018:
            self.__price = 2018

    def del_price(self):
        del self.__price

    price = property(get_price, set_price, del_price)


c = Car(2001)
print(c.price)
