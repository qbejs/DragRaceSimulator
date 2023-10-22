import random


class TimeGenerator:
    TIME_RANGES = {
        "A": {"min": 14.2, "max": 16.0},
        "B": {"min": 10.2, "max": 16.0},
    }

    @staticmethod
    def generate_time(factor):
        time_range = TimeGenerator.TIME_RANGES[factor]
        return random.uniform(time_range["min"], time_range["max"])
