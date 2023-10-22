from handlers.BaseHandler import BaseHandler
from cars import BaseCar


class FalstartHandler(BaseHandler):
    def __init__(self, car: BaseCar):
        self.car = car

    def is_supported(self, command_name: str) -> bool:
        return command_name == "falstart"

    def get_response(self):
        return {
            "event": "falstart_detected",
            "data": f"False start detected for car: {self.car.name}!",
        }
