import pkgutil
import importlib
from handlers.BaseHandler import BaseHandler


class StageManager:
    def __init__(self):
        self.handlers = self._load_handlers()

    def _load_handlers(self):
        handlers = []
        package_name = "..handlers"
        package = importlib.import_module(package_name)
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{package_name}.{module_name}")
            for class_name, obj in module.__dict__.items():
                if (
                    isinstance(obj, type)
                    and issubclass(obj, BaseHandler)
                    and obj != BaseHandler
                ):
                    handlers.append(obj())
        return handlers

    def get_handler(self, command_name: str):
        for handler in self.handlers:
            if handler.is_supported(command_name):
                return handler
        return None
