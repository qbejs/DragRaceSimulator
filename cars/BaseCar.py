from abc import ABC, abstractmethod
from utils.time_generator import TimeGenerator


class BaseCar(ABC):
    def __init__(self, power_factor, reaction_factor):
        self.power_factor = power_factor
        self.reaction_factor = reaction_factor
        self.disqualified = False

    def get_race_time(self):
        return TimeGenerator.generate_time(self.power_factor)

    def get_reaction_time(self):
        return TimeGenerator.generate_time(self.reaction_factor)

    def disqualify(self):
        self.disqualified = True
