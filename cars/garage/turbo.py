from cars.BaseCar import BaseCar


class Turbo(BaseCar):
    name = "Turbo"

    def __init__(self):
        super().__init__(power_factor="A", reaction_factor="B")

    def get_name(self):
        return self.name
