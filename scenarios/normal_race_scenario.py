import random

from cars.BaseCar import BaseCar
from handlers.falstart_handler import FalstartHandler
from scenarios.stage_scenario import StageScenario
from handlers.start_race_handler import StartRaceHandler
from handlers.cross_start_handler import CrossStartHandler
from handlers.cross_finish_handler import CrossFinishHandler
from utils.random_falstart import random_false_start


class NormalRaceScenario(StageScenario):
    def __init__(self, track_one_car: BaseCar, track_two_car: BaseCar):
        self.track_one_car = track_one_car
        self.track_two_car = track_two_car

    def get_steps(self):
        steps = [
            {"handler": StartRaceHandler(), "delay": 0},
            {"handler": CrossStartHandler(), "delay": 0},
            {"handler": CrossFinishHandler(), "delay": 0},
        ]

        if random_false_start(probability=0.1):
            car_with_false_start = random.choice(
                [self.track_one_car, self.track_two_car]
            )
            steps.insert(
                1, {"handler": FalstartHandler(car_with_false_start), "delay": 0}
            )

        return steps
