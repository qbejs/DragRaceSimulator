import asyncio

from utils.response_creator import ResponseCreator
from models.race_result import RaceResult
from handlers.falstart_handler import FalstartHandler


class StageScenarioManager:
    def __init__(self, scenario):
        self.scenario = scenario
        self.track_one_car = None
        self.track_two_car = None

    def set_track_one(self, car):
        self.track_one_car = car

    def set_track_two(self, car):
        self.track_two_car = car

    async def exec(self):
        responses = []
        steps = self.scenario.get_steps()
        for step in steps:
            await asyncio.sleep(step["delay"] / 1000)  # delay w ms

            if isinstance(step["handler"], FalstartHandler):
                if self.track_one_car:
                    self.track_one_car.disqualify()
                    event_data = step["handler"].get_response()
                    response = ResponseCreator.create_response(
                        event_data["event"], event_data
                    )
                    responses.append(response)
                if self.track_two_car:
                    self.track_two_car.disqualify()
                    event_data = step["handler"].get_response()
                    response = ResponseCreator.create_response(
                        event_data["event"], event_data
                    )
                    responses.append(response)
                break  # kończymy wyścig po wykryciu fałszywego startu

            if self.track_one_car:
                event_data = step["handler"].get_response()
                event_data["race_time"] = self.track_one_car.get_race_time()
                event_data["reaction_time"] = self.track_one_car.get_reaction_time()
                response = ResponseCreator.create_response(
                    event_data["event"], event_data
                )
                responses.append(response)

            if self.track_two_car:
                event_data = step["handler"].get_response()
                event_data["race_time"] = self.track_two_car.get_race_time()
                event_data["reaction_time"] = self.track_two_car.get_reaction_time()
                response = ResponseCreator.create_response(
                    event_data["event"], event_data
                )
                responses.append(response)

        race_result = RaceResult(self.track_one_car, self.track_two_car)
        responses.append({"event": "race_result", "data": race_result.winner})

        return responses
