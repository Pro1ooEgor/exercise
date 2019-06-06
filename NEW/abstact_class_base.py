from abc import ABC, abstractmethod


class BaseCar(ABC):
    def __init__(self, car):
        self.car = car

    @abstractmethod
    def move(self):
        pass


class ProductionCar(BaseCar):
    def __init__(self, car, model=''):
        super().__init__(car)
        self.model = model

    def move(self):
        print('Car move')


pc = ProductionCar('Tesla', 'model 3')
pc.move()
