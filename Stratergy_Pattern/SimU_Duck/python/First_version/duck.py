from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self):
        pass

    def quack(self):
        print("The duck quakcs")

    def fly(self):
        print("The duck flies")

    @abstractmethod
    def display(self):
        pass