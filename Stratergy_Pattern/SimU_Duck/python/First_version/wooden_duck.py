from duck import Duck


class WoodenDuck(Duck):
    def __init__(self):
        pass

    def display(self):
        print("WoodenDuck \n")
        self.fly()
        self.quack()
