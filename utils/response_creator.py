import time
import hashlib


class ResponseCreator:
    @staticmethod
    def create_response(event, data):
        response = {
            "event": event,
            "timestamp": time.time(),
            "status": "success",
            "data": data,
        }
        checksum = hashlib.md5(str(response).encode()).hexdigest()
        response["checksum"] = checksum
        return response
