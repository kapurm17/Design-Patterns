from abc import ABC, abstract_method


class Flyable(ABC):
    @abstract_method
    def fly(self):
        pass