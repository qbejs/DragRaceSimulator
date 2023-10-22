from abc import ABC, abstractmethod


class BaseHandler(ABC):
    @abstractmethod
    def is_supported(self, command_name: str) -> bool:
        pass

    @abstractmethod
    def get_response(self):
        pass
