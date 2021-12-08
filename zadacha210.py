from abc import ABC, abstractmethod

class fabric_consumption(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @abstractmethod
    def counts(self):
        pass

class coat(fabric_consumption):
    @property
    def counts(self):
        return round((self.parametr / 6.5) + 0.5)

class suit(fabric_consumption):
    @property
    def counts(self):
        return round((2 * self.parametr) + 0.3)

Coat = coat(500)
Suit = suit(1000)
print(Coat.counts + Suit.counts)
