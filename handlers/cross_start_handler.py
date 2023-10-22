from handlers.BaseHandler import BaseHandler


class CrossStartHandler(BaseHandler):
    def is_supported(self, command_name: str) -> bool:
        return command_name == "cross_start"

    def get_response(self):
        return {"event": "crossed_start", "data": "Car has crossed the start line!"}
