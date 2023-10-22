from handlers.BaseHandler import BaseHandler


class CrossFinishHandler(BaseHandler):
    def is_supported(self, command_name: str) -> bool:
        return command_name == "cross_finish"

    def get_response(self):
        return {"event": "crossed_finish", "data": "Car has crossed the finish line!"}
