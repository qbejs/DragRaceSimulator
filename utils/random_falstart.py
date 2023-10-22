import random


def random_false_start(probability: float = 0.1) -> bool:
    return random.random() < probability
