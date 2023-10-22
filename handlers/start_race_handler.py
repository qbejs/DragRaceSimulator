from handlers.BaseHandler import BaseHandler


class StartRaceHandler(BaseHandler):
    def is_supported(self, command_name: str) -> bool:
        return command_name == "start_race"

    def get_response(self):
        return {"event": "race_started", "data": "Race has started!"}
