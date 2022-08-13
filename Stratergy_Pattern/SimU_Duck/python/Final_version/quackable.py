from abc import ABC, abstract_method


class Quackable(ABC):
    @abstract_method
    def quack(self):
        pass