from abc import ABC, abstractmethod


class StageScenario(ABC):
    @abstractmethod
    def get_steps(self):
        """
        Zwraca listę kroków do wykonania w scenariuszu.
        Każdy krok to słownik z kluczami: 'handler' i 'delay'.
        """
        pass
